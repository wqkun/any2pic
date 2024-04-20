# app.py

import sys
from image_utils.image_converter import batch_convert

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python app.py input_directory output_directory")
    else:
        input_dir = sys.argv[1]
        output_dir = sys.argv[2]
        batch_convert(input_dir, output_dir)
