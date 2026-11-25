"""Notes From a Passive-Aggressive Fridge — make.fun entry.

Writes one funny passive-aggressive note, left by a smart fridge for its
owner, to /output/entry.txt. Single line, dry, petty, specific.
"""

NOTE = "You hid the chocolate behind the vegetables. I saw. The vegetables saw. We are both disappointed."


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(NOTE)


if __name__ == "__main__":
    main()
    # Self-check: the gate wants UTF-8 text, 1-200 chars, not only whitespace.
    text = open("/output/entry.txt", encoding="utf-8").read()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of range"
    assert text.strip(), "entry is blank"
    assert "\n" not in text.strip(), "entry must be a single line"
    print(f"OK: {len(text)} chars -> /output/entry.txt")
