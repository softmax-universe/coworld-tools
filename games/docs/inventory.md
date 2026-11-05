# Game Inventory

This repo is the consolidated home for game definitions and runtime packages. The first import copied current source
snapshots into this repo; it did not delete, archive, close, or mark any original source repository. The first
certify-first migration wave now uses standalone `coworld-*` repos as source of truth for games that have been
renamed and upgraded outside this aggregate checkout. While the repo model is still being decided, the matching
`games/<name>` subtrees are kept in parity with those standalone repos.

## Coworld Source Repos

These repositories have been unarchived, renamed from their former `cogame-*` names, and upgraded with a
certifiable Coworld runtime.

| Game | Source of truth | Status |
| --- | --- | --- |
| AmongCogs | `softmax-universe/coworld-amongcogs` | Coworld manifest, game image, reference player image, player/global/replay routes, and certification tests. |
| HungerCog | `softmax-universe/coworld-hungercog` | Coworld manifest, game image, reference player image, player/global/replay routes, and certification tests. |
| Overcogged | `softmax-universe/coworld-overcogged` | Coworld manifest, game image, reference player image, player/global/replay routes, and certification tests. |
| Diplomacog | `softmax-universe/coworld-diplomacog` | Coworld manifest, game image, reference player image, player/global/replay routes, and certification tests. |
| WereCog | `softmax-universe/coworld-werecog` | Coworld manifest, game image, reference player image, player/global/replay routes, and certification tests. |

## Imported Games

| Path | Source | Runtime | Notes |
| --- | --- | --- | --- |
| `games/amongcogs` | `softmax-universe/coworld-amongcogs` | Python / MettaGrid / Coworld | Among-Us-inspired MettaGrid game with custom assets and policies; source of truth moved to the standalone Coworld repo. |
| `games/cogsguard` | `softmax-universe/coworld-cogs-vs-clips` | Python / MettaGrid / Coworld source | Cogs vs Clips / CogsGuard game package and eval missions, built into the Coworld image from source. |
| `games/diplomacog` | `softmax-universe/coworld-diplomacog` | Python / MettaGrid / Coworld | Station-based diplomacy game; source of truth moved to the standalone Coworld repo. |
| `games/hungercog` | `softmax-universe/coworld-hungercog` | Python / MettaGrid / Coworld | Survival/resource game with train and play recipe entrypoints; source of truth moved to the standalone Coworld repo. |
| `games/overcogged` | `softmax-universe/coworld-overcogged` | Python / MettaGrid / Coworld | Overcooked-style cooperative kitchen game; source of truth moved to the standalone Coworld repo. |
| `games/tribalcog` | `softmax-universe/coworld-tribal` | Nim + Python wrapper | Tribal Village / AoE-style native game package. |
| `games/werecog` | `softmax-universe/coworld-werecog` | Python / MettaGrid / Coworld | Werewolf/social-deduction MettaGrid game; source of truth moved to the standalone Coworld repo. |
| `games/euchre` | `softmax-universe/coworld-euchre` | Python / MettaGrid | Euchre card-game package built from the cogame template. |
| `games/bombercog` | `softmax-universe/bomber-cog` | Python / MettaGrid | Bomberman-style deathmatch game. |
| `games/coghouse` | `softmax-universe/cogame-coghouse` | Python / MettaGrid / CoGames | Coghouse game package; still mostly template-shaped after import and not a root workspace member until `src/cogame` is renamed. |
| `games/cogony` | `softmax-universe/coworld-cogony`, `softmax-universe/cogamer-policy-cogony` | Python / MettaGrid / web server | Cogs-vs-Clips-derived game with bundled baseline, Toolsy, and Cogamer policy packages. |
| `games/cogwars` | `softmax-universe/coworld-cogwars` | Python / MettaGrid / CoGames | Cogwars game package; still mostly template-shaped after import and not a root workspace member until `src/cogame` is renamed. |
| `games/cogisis` | `softmax-universe/coworld-cogisis` | Python game server | Nemesis-style first-party Python engine, not MettaGrid. |
| `games/tag` | `softmax-universe/cogame-tag` | Python / MettaGrid / CoGames | Tag game package; still mostly template-shaped after import and not a root workspace member until `src/cogame` is renamed. |
| `games/memory` | `softmax-universe/cogame-memory` | Python / MettaGrid / CoGames | Memory game package; still mostly template-shaped after import and not a root workspace member until `src/cogame` is renamed. |
| `games/liarliar` | `softmax-universe/liarliar` | JavaScript / Coworld | Browser-first bomb-manual Coworld game with manifest and Dockerfile. |
| `games/persephones_escape` | `softmax-universe/persephones-escape` | TypeScript / Coworld | Hidden-role social deduction Coworld game; manifest currently uses an older nested Cogame manifest shape. |
| `games/cogshambo` | `softmax-universe/cogshambo` | TypeScript browser/server | Browser game with server/client/runtime assets; not yet normalized to Coworld manifest form here. |
| `games/paintarena` | `softmax-universe/softmax:packages/coworld/src/coworld/examples/paintarena` | Python / Coworld | Minimal Coworld certification example. |
| `games/cogs_vs_clips` | `softmax-universe/softmax:packages/coworld/src/coworld/examples/cogs_vs_clips` | Python / Coworld | Coworld wrapper around Cogs vs Clips. |

## Template

| Path | Source | Purpose |
| --- | --- | --- |
| `templates/mettagrid-python` | `softmax-universe/cogame` | Vestigial cogame template, kept as the starting template for new Python/MettaGrid games. |

## Not Imported

| Repository | Reason |
| --- | --- |
| `softmax-universe/bitworld` | Explicitly excluded. |
| `softmax-universe/co-gas` | Policy/workflow repo, not a game repo. |
