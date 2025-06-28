# PDF Merger Script

This is a simple Python script to merge multiple PDF files into a single PDF file using the PyPDF2 library.

## Features

- Prompts the user to enter the number of PDF files to merge.
- Takes the filenames of the PDFs to merge as input.
- Merges the specified PDF files into one output file named `merged-pdf.pdf`.

## Requirements

- Python 3.x
- PyPDF2 library

## Installation

Install the PyPDF2 library using pip if you don't have it already:

```bash
pip install PyPDF2
```

## Usage

Run the script and follow the prompts:

```bash
python mergepdf.py
```

You will be asked to enter the number of PDF files you want to merge, then enter each PDF filename one by one.

The merged PDF will be saved as `merged-pdf.pdf` in the current directory.

## License

This project is licensed under the MIT License.
