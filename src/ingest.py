import fitz
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

PDF_FOLDER = BASE_DIR / "data" / "pdfs"


def extract_pdf(pdf_path):
    doc = fitz.open(pdf_path)

    pages = []

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)

        pages.append({
            "page": page_num + 1,
            "text": page.get_text()
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