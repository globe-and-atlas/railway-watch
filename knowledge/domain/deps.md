---
generated_by: "OpenAI Codex (GPT-6; exact variant not exposed)"
timestamp: "2026-11-06T11:15:00-06:00"
---
# Dependencies

Native Pebble SDK 4.33.1 / tool 5.0.40. Clay 1.1.0 is locked in watchface/package-lock.json. Python Pillow handles native screenshot boards. System Gothic font requires no external font license.

## Round native QA — 2026-11-06
Pillow12.3.0 is pinned for deterministic screenshot decoding, palette normalization, and contact sheets. This is development tooling only; Pebble runtime dependencies are unchanged. It provides `Image.get_flattened_data()` used by the capture audit. No SDK upgrade was installed.

## 2026-11-06 — Round SDK targets
Installed SDK4.33.1/tool5.0.40 built Emery, Chalk, and Gabbro without an SDK upgrade. Clay1.1.0 recognizes both round platforms. Pillow12.3.0 is native QA tooling only.
