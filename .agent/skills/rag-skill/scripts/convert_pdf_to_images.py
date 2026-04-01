import os
import sys
from pathlib import Path

from pdf2image import convert_from_path


def convert(pdf_path: str, output_dir: str, max_dim: int = 1000) -> bool:
    """Converts each page of a PDF to a PNG image.

    Args:
        pdf_path: Path to the PDF file.
        output_dir: Directory to save the PNG images.
        max_dim: Maximum width or height for output images.

    Returns:
        True if conversion succeeded, False otherwise.
    """
    pdf_file = Path(pdf_path)

    if not pdf_file.exists():
        print(f"Error: PDF file not found: {pdf_path}")
        return False

    if not pdf_file.is_file():
        print(f"Error: Path is not a file: {pdf_path}")
        return False

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    try:
        images = convert_from_path(str(pdf_file), dpi=200)
    except Exception as e:
        print(f"Error converting PDF: {e}")
        return False

    for i, image in enumerate(images):
        width, height = image.size
        if width > max_dim or height > max_dim:
            scale_factor = min(max_dim / width, max_dim / height)
            new_width = int(width * scale_factor)
            new_height = int(height * scale_factor)
            image = image.resize((new_width, new_height))

        image_path = output_path / f"page_{i + 1}.png"
        image.save(image_path)
        print(f"Saved page {i + 1} as {image_path} (size: {image.size})")

    print(f"Converted {len(images)} pages to PNG images")
    return True


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: convert_pdf_to_images.py [input pdf] [output directory]")
        sys.exit(1)

    success = convert(sys.argv[1], sys.argv[2])
    sys.exit(0 if success else 1)
