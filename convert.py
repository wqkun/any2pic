from PIL import Image
import sys

def image_to_png(input_path, output_path) -> None:
    """
    Convert an image to PNG format.

    This function takes an input_path pointing to the image
    and an output_path where the PNG image will be saved after conversion.

    :param input_path: Path to the image file.
    :type input_path: str

    :param output_path: Path where the PNG image will be saved.
    :type output_path: str

    :return: None
    :rtype: None
    """
    try:
        # Open the image
        with Image.open(input_path) as img:
            # Convert to RGB if necessary
            if img.mode != "RGB":
                img = img.convert("RGB")
            # Save as PNG
            img.save(output_path, "PNG")
        print(f"Conversion successful: {input_path} converted to {output_path}")
    except Exception as e:
        print(f"Error converting {input_path} to PNG: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert.py input_file.[webp|jpg|...] output_file.png")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        image_to_png(input_file, output_file)
