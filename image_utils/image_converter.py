# image_converter.py

import os
from PIL import Image

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

def batch_convert(input_dir, output_dir) -> None:
    """
    Batch convert images within a directory to PNG format.

    :param input_dir: Directory containing input images.
    :type input_dir: str

    :param output_dir: Directory where the PNG images will be saved.
    :type output_dir: str

    :return: None
    :rtype: None
    """
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Loop through all files in the input directory
    for filename in os.listdir(input_dir):
        input_path = os.path.join(input_dir, filename)
        if os.path.isfile(input_path):
            # Generate output file path by replacing the extension with .png
            output_filename = os.path.splitext(filename)[0] + ".png"
            output_path = os.path.join(output_dir, output_filename)
            # Convert the image to PNG
            image_to_png(input_path, output_path)
