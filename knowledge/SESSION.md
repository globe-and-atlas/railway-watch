---
generated_by: "OpenAI Codex (GPT-6; exact variant not exposed)"
timestamp: "2026-11-06T21:20:26-06:00"
---
# Railway — published round update

Goal: publish the verified multi-platform release with round screenshots.
Agent: OpenAI Codex
Handoff-from: OpenAI Codex
Handoff-type: continuation
Status: published and public assets independently verified

## Result
- Version0.1.1 is public: [Railway](https://apps.repebble.com/b882652051884d01bfcabfdf).
- Native binaries cover Emery200×228, Chalk180×180, and Gabbro260×260. Original UUID/settings mappings preserved.
- Two native screenshots appear under each round watch selection.
- First public release; native six-palette GIF leads the Time2 gallery.
- User explicitly excluded T9; its public release/gallery remain unchanged.

Railway round stills use single-frame GIF encoding: store PNG processing merged rare colors. Corrected public GIF pixels exactly match the original native PNGs; the Emery animated GIF is untouched.

## Evidence
- Public PBW SHA-256 matches the reviewed production artifact: `c90852aecbc38b9084600d86db40f4d7ae5189100a220dba57390b739f7f32ea`.
- Four public round images decode to exact native source pixels. Both watch selections were checked in the public UI.
- Fresh independent verifier accepted all15PBWs,60round images, sixnewGIFs, existing9galleries, and unchangedT9.
- Upload guards/read-retry/failure-path tests:5passed. No repeated release uploads were used for screenshot correction.
- No Git commits or pushes were performed. Physical-device testing remains separate.

## Artifacts and continuation
- `release/store-release.json`: current verified receipt.
- `release/round-update/0.1.1/public-proof.json`: public asset URLs and assertions.
- `media/store/round-update/`: native round listing assets and release plan.
- [Round store workflow](procedural/publish_round_update.md); [local validation archive](sessions/2026-11-06-round-local-validation.md).

S.D.G.: Lets owners of either round Pebble install Railway from the public store with accurate native previews.
Feynman gap: Public bytes and preview pixels are verified; physical-watch readability and endurance remain device checks.
