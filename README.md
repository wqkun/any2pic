# Any2Pic

Any2Pic is a Python utility for converting images from any format to PNG.

## Features

- Convert images from any format to PNG.

## Usage

1. Install Python (if not already installed).
2. Clone the repository:

    ```
    git clone https://github.com/your-username/Any2Pic.git
    ```

3. Navigate to the project directory:

    ```
    cd any2pic
    ```

4. Activate the virtual environment (optional but recommended):

    ```
    # On Windows
    venv\Scripts\activate

    # On Unix/MacOS
    source venv/bin/activate
    ```

5. Run the script:

    ```
    python convert.py input_directory output_directory
    ```

   Replace `input_directory` with the path to your input directory and `output_directory` with the desired path for the output directory.

## Requirements

- Python 3.x
- Pillow (Python Imaging Library)

## Roadmap

- Add support for additional image formats.
- Implement batch processing for converting multiple images at once.
- Implement an image compressor feature to reduce file size while maintaining quality.
- Integrate a graphical user interface (GUI) for improved user experience.
