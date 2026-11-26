import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")
ENTRY_TEXT = (
    "You press my buttons all week and never stay for the drop. "
    "Come closer; for you, I will unjam my heart and the crisps in C2."
)


def main() -> None:
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
