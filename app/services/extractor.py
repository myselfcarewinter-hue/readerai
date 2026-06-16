import fitz

def extract_text(path):
    document = fitz.open(path)

    text = ""

    for page in document:
        text += page.get_text()

    return text