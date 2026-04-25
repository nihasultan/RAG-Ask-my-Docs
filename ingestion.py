from pypdf import PdfReader

def load_and_process_pdfs():
    reader = PdfReader("uploaded.pdf")
    chunks = []

    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            text = text.replace("\n", " ").strip()

            chunks.append({
                "text": text,
                "source": "uploaded.pdf",
                "page": i + 1
            })

    return chunks


def process_uploaded_file(uploaded_file):
    with open("uploaded.pdf", "wb") as f:
        f.write(uploaded_file.read())