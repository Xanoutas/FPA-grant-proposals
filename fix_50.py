# path/to/existing/tutorial_generator.py

import os
import subprocess
from scribus import *

def convert_odt_to_pdf(odt_path, pdf_path):
    try:
        # Check if Scribus is available
        if not haveDoc():
            raise Exception("Scribus is not available or no document is open.")
        
        # Open the ODT file in Scribus
        openDoc(odt_path)
        
        # Save the document as PDF
        saveDoc(pdf_path)
        
        # Close the document without saving
        closeDoc()
        
        print(f"Successfully converted {odt_path} to {pdf_path}")
    except Exception as e:
        print(f"Error converting {odt_path} to {pdf_path}: {e}")

def main():
    # Example paths
    odt_path = "path/to/tutorial.odt"
    pdf_path = "path/to/tutorial.pdf"
    
    # Convert ODT to PDF
    convert_odt_to_pdf(odt_path, pdf_path)

if __name__ == "__main__":
    main()