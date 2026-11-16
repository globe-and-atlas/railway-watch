---
generated_by: "OpenAI Codex (GPT-6; exact variant not exposed)"
timestamp: "2026-11-06T11:15:00-06:00"
---
# Railway

Native Pebble Time 2 watchface inspired by the clarity of railway clocks: bold black batons, flat hands, and a red lollipop seconds hand. Original graphics; no manufacturer logo.

- Six palettes: Classic, Night, Cream, Navy, Mint, Blue.
- Custom background, hand, and seconds colors.
- Optional digital footer with watch default, 12-hour, or 24-hour time.
- Date off, weekday/day, ISO, US, or European order.
- Battery percentage from Pebble's battery service.
- Seconds hand on/off; off subscribes only to minute ticks.

```sh
npm install --prefix watchface
node watchface/settings.test.js
python3 -m pytest tests/test_policy.py
python3 execution/build.py
python3 execution/verify.py
```

Builds target Emery200×228, Chalk180×180, and Gabbro260×260. Native fixture captures are under media/. Fixture flags RAIL_* are stripped by the production build. Published version0.1.1: https://apps.repebble.com/b882652051884d01bfcabfdf.


## Round-compatible release — 0.1.1

Railway includes native layouts for Pebble Time2 (Emery200×228), original Time Round (Chalk180×180), and Round2 (Gabbro260×260). The rectangular layout and existing settings identities are preserved.

Build: `python3 execution/build.py`, then `python3 execution/verify.py`. Local bundle: `dist/Railway-0.1.1.pbw`. Native round previews: `media/round/`. Repeatable fixture/capture instructions: [round compatibility QA](knowledge/procedural/round_compatibility.md).

This update is [publicly available](https://apps.repebble.com/b882652051884d01bfcabfdf) with round screenshots. Public PBW bytes and screenshot pixels verify; physical-watch validation remains separate.
