from PyPDF2 import PdfReader

def check_metadata(pdf_path):
    reader = PdfReader(pdf_path)
    metadata = reader.metadata
    print("Metadata dalam PDF:")
    for key, value in metadata.items():
        print(f"{key}: {value}")

check_metadata("cv.pdf")