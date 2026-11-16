---
generated_by: "OpenAI Codex (GPT-6; exact variant not exposed)"
timestamp: "2026-11-06T11:11:30-06:00"
---
# Native drawing finding

Near-midnight native screenshots exposed contracted narrow hands when using gpath_rotate_to in the related Triangle/Lume implementations. Direct fixed-point vertex transforms preserve intended widths; Railway now uses the same verified method. Native 31-case matrix passed after change. Exact SDK internals were not diagnosed.

Initial live-seconds probes can race app startup after install. Wait for the app, resend the setting, then poll up to several seconds for visible movement. This does not relax static seconds-off checks.

## 2026-11-06 — Store changes rare PNG colors
Error: four uploaded Railway round PNGs failed native pixel comparison, despite correct dimensions and visible composition. One gray channel shifted170→171; rare tinted edge colors merged into a dominant color.
Cause observed: the public PNG bytes decoded differently from the uploaded native PNGs. Other faces were unaffected; do not weaken the exact pixel assertion to accept this loss.
Fix: losslessly re-encode the same native pixels as single-frame GIFs, replace only the four affected round stills through the listing editor, and verify the new publicGIFpixels. Preserve the PBW and original Emery animated GIF. All four corrected public assets now match exactly.
Graduated-to: procedural/publish_round_update.md.
