build:
	python3 execution/build.py
verify:
	python3 execution/verify.py
test:
	python3 -m pytest tests/test_policy.py
	node watchface/settings.test.js
