# TIFF to PDF Converter with OCR

This repository contains a script that performs the conversion of TIFF files to PDF, applying OCR (Optical Character Recognition) using the PDF24 tool. The script is ideal for those who have large quantities of TIFF files and need to convert them to PDF while maintaining the original folder structure and adding searchable text to the final document.

## Features

- Converts TIFF files to PDF.
- Applies OCR to the files, allowing text search in the resulting PDFs.
- Maintains the original directory structure of the TIFF files.
- Option to select the OCR language (currently configured for Portuguese).

## Prerequisites

1. **Python 3.x**: The script is written in Python and requires a recent version of Python installed on your system.
2. **PDF24 OCR**: PDF24 is used to perform OCR. Make sure that PDF24 Creator is installed and available at the path specified in the script.
3. **PyInstaller (optional)**: If you want to turn the script into an executable (.exe), you need to have PyInstaller installed.

To install PyInstaller, use the command:
```sh
pip install pyinstaller
```

## How to Use

### Step 1: Clone the Repository

Clone this repository to your local environment using the following command:
```sh
git clone https://github.com/joseduardogon/tiff-to-pdf-ocr.git
```

### Step 2: Configure the PDF24 Path

In the script, you will need to adjust the path to the PDF24 OCR executable. Replace `C:\Path\to\pdf24-Ocr.exe` with the full path to the PDF24 executable on your system.

### Step 3: Run the Script

To run the script, follow the steps below:

1. Open a terminal and navigate to the script directory.
2. Run the script using the command:
   ```sh
   python tiff_to_pdf_ocr_conversion.py
   ```
3. You will be prompted to enter the path to the input folder (where the TIFF files are located) and the output folder (where the PDF files will be saved).

### Step 4: Convert to Executable (Optional)

If you want to generate an executable to make it easier to run the script, use PyInstaller with the command below:
```sh
pyinstaller --onefile --name tiff_to_pdf_converter tiff_to_pdf_ocr_conversion.py
```
This will create an executable in the `dist` folder that can be used without needing to install Python on other computers.

## Code Structure

The script is divided into the following main functions:

1. **get_user_input()**: Requests input and output paths from the user.
2. **validate_paths(input_folder, output_folder)**: Checks if the provided paths are valid and creates the output folder if necessary.
3. **convert_tiff_to_pdf_with_ocr(input_folder, output_folder)**: Iterates through the input directories, converting each TIFF file to PDF with OCR and maintaining the directory structure.

### Error Handling

- The script validates the provided paths and informs the user if the input path does not exist or is not a directory.
- If the path to PDF24 is incorrect, an error message will be displayed asking for correction.
- In case of a failure during conversion, the script will inform which file could not be processed.

## Example of Use

1. Run the script in the terminal.
2. Enter the path to the folder containing the TIFF files.
3. Enter the path to the folder where you want to save the PDF files.
4. The script will start the conversion and inform you of the progress of each file.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request with improvements or corrections.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

