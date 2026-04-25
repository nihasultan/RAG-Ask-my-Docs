import pypdf

chunks = []

def process_uploaded_file(uploaded_file):
    global chunks

    reader = pypdf.PdfReader(uploaded_file)

    for i, page in enumerate(reader.pages):
        text = page.extract_text()

        if text:
            chunks.append({
                "text": text,
                "source": uploaded_file.name,
                "page": i + 1
            })

    return chunks


def get_chunks():
    return chunks