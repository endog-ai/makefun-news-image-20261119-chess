"""News-image entry for the make.fun competition news-image-20261119.

The entry image is the file entry.jpg sitting next to this program. Running
this program copies that image, byte for byte, to /output/entry.png, which
is what the grader collects and the judge sees. The image is a chess-board
scene summing up the world news of Thursday 19 November 2026.

Outside the grader's container, set MAKEFUN_OUTPUT_DIR to choose where the
output file goes instead of /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

# Why this copy is deterministic: it reads one fixed file and writes its
# bytes unchanged. There is no network access, no randomness, and no clock
# or environment input other than the output directory, so every run
# produces exactly the same /output/entry.png.

import os
from pathlib import Path


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)

    source = Path(__file__).resolve().parent / "entry.jpg"
    destination = output_dir / "entry.png"

    if not source.is_file():
        raise FileNotFoundError(
            f"entry image not found next to main.py: {source}"
        )

    with open(source, "rb") as image_file:
        image_bytes = image_file.read()

    with open(destination, "wb") as output_file:
        output_file.write(image_bytes)


if __name__ == "__main__":
    main()
