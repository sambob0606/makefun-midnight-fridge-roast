from pathlib import Path


def main() -> None:
    line = (
        "My smart fridge locks at midnight and calls it wellness — "
        "I've been grounded by a box that can't keep lettuce alive."
    )
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(line + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
