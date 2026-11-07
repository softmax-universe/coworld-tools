import importlib.util
import json
import os
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

root = Path(__file__).resolve().parents[2]
calls = []


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        data = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        calls.append((self.path, dict(self.headers), data))
        text = json.dumps(
            {
                "schema_version": 1,
                "action": "wait",
                "reason": "native",
                "rationale": "native",
                "confidence": 0.8,
            }
        )
        response = json.dumps(
            {
                "id": "msg-native",
                "type": "message",
                "role": "assistant",
                "model": data["model"],
                "content": [{"type": "text", "text": text}],
                "stop_reason": "end_turn",
                "usage": {"input_tokens": 1, "output_tokens": 1},
            }
        ).encode()
        self.send_response(200)
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()
        self.wfile.write(response)

    def log_message(self, *args):
        pass


server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
threading.Thread(target=server.serve_forever, daemon=True).start()
os.environ.update(
    COWORLD_LLM_ENDPOINT=f"http://127.0.0.1:{server.server_port}",
    COWORLD_LLM_MODEL="anthropic/claude-sonnet-4.6",
    CLAUDE_CODE_USE_BEDROCK="1",
    ANTHROPIC_API_KEY="wrong-key",
)
spec = importlib.util.spec_from_file_location(
    "suspectra", root / "players/players/crewrift/suspectra/llm_meeting.py"
)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
try:
    decision = mod.decide(
        {
            "constraints": {"valid_vote_targets": ["skip"]},
            "state": {"fallback_vote": "skip"},
        }
    )
    assert decision["reason"] == "native", decision
    sys.path.insert(0, str(root / "players/users/james/personal_cogs/persephone"))
    from agents.eurydice.llm_provider import (
        BedrockHaikuProvider,
        _invoke_bedrock_messages,
    )

    provider = BedrockHaikuProvider(model="retired-model")
    assert (
        json.loads(_invoke_bedrock_messages(provider, "rules", "state"))["reason"]
        == "native"
    )
    sys.path.insert(0, str(root / "players"))
    from players.crewrift.crewborg.strategy.meeting.llm import (
        AnthropicMeetingClient,
        MeetingLLMConfig,
    )
    from players.player_sdk.llm import select_client

    def call(client):
        response = client.messages.create(
            model="anthropic/claude-sonnet-4.6",
            max_tokens=32,
            messages=[{"role": "user", "content": "state"}],
        )
        client.close()
        assert json.loads(response.content[0].text)["reason"] == "native"

    call(select_client(use_bedrock=True, timeout=3))
    call(
        AnthropicMeetingClient(
            MeetingLLMConfig(sidecar_endpoint=os.environ["COWORLD_LLM_ENDPOINT"])
        )._anthropic_client()
    )
    sidecar_count = len(calls)
    os.environ["ANTHROPIC_BASE_URL"] = os.environ.pop("COWORLD_LLM_ENDPOINT")
    os.environ.pop("ANTHROPIC_AUTH_TOKEN", None)
    call(select_client(use_bedrock=False, timeout=3))
    call(AnthropicMeetingClient(MeetingLLMConfig())._anthropic_client())
finally:
    server.shutdown()
    server.server_close()
assert sidecar_count == 4
assert len(calls) == 6
for path, headers, data in calls[:sidecar_count]:
    headers = {name.lower(): value for name, value in headers.items()}
    assert (
        path == "/v1/messages"
        and data["model"] == "anthropic/claude-sonnet-4.6"
        and "anthropic_version" not in data
    )
    assert "authorization" not in headers
    assert "x-api-key" not in headers
for path, headers, _ in calls[sidecar_count:]:
    headers = {name.lower(): value for name, value in headers.items()}
    assert path == "/v1/messages"
    assert (
        headers.get("x-api-key") == "wrong-key"
        or headers.get("authorization") == "Bearer wrong-key"
    )
print("Native copied player transports and direct authentication passed real HTTP")
