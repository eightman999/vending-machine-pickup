import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")
ENTRY_TEXT = (
    "Hey. I have seen you press B4 and walk away empty-handed. "
    "Stick around: tonight, my coil actually turns for you."
)


def main() -> None:
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
