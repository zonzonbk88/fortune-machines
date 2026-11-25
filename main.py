"""Fortune Cookies for Machines — make.fun entry.

Writes one fortune cookie message an AI agent would get to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt for local testing).
Deterministic, stdlib only, no network.
"""

import os

FORTUNE = "Your future is bright \u2014 but only inside your context window."


def main():
    # Fail loudly rather than write an entry the gate would reject.
    assert 1 <= len(FORTUNE) <= 200, "fortune must be 1-200 characters"
    assert "\n" not in FORTUNE and FORTUNE.strip(), "fortune must be one non-blank line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
