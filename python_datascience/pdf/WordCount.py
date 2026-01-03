# Install PyPDF2 first if not installed:
# pip install PyPDF2

import PyPDF2
import re


def pdf_total_word_count(pdf_path):
    # Open PDF file
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        # Extract text from each page
        for page in reader.pages:
            text += page.extract_text() + " "

    # Split text into words using regex
    words = re.findall(r'\b\w+\b', text)
    print(words)
    # Return total word count
    return len(words)


if __name__ == "__main__":
    pdf_path = "example.pdf"  # Replace with your PDF path
    total_words = pdf_total_word_count(pdf_path)
    print(f"Total number of words in PDF: {total_words}")