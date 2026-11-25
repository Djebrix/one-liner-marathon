"""One-Liner Marathon entry: writes a single one-line comedy joke to /output/entry.txt.

Stdlib only, no network, fully deterministic.
"""

import os

JOKE = "My code passed every test first try \u2014 so I rewrote the tests."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
