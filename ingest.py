import fitz
from pathlib import Path

PDF_FOLDER = "data"

def extract_pdf(pdf_path):
    doc = fitz.open(pdf_path)

    pages = []

    for page_num, page in enumerate(doc):
        text = page.get_text()

        pages.append({
            "page": page_num + 1,
            "text": text
        })

    return pages

if __name__ == "__main__":

    pdfs = Path(PDF_FOLDER).glob("*.pdf")

    for pdf in pdfs:

        print(f"\nProcessing: {pdf.name}")

        pages = extract_pdf(pdf)

        print(f"Pages: {len(pages)}")

        print("\nPreview:")

        print(pages[0]["text"][:500])