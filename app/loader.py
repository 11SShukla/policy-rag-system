import os
from pdf2image import convert_from_path
import pdfplumber

from app.ocr_utils import extract_text_from_image
from app.text_cleaner import clean_text


def load_documents(data_path):

    documents = []

    for file in os.listdir(data_path):

        if not file.endswith(".pdf"):
            continue

        file_path = os.path.join(data_path, file)

        text = ""

        print(f"Processing {file}")

        # Try normal PDF extraction
        try:
            with pdfplumber.open(file_path) as pdf:

                for page in pdf.pages:

                    page_text = page.extract_text()

                    if page_text:
                        text += page_text + "\n"

        except:
            pass

        # Trigger OCR if little text found
        if len(text.strip()) < 200:

            print(f"OCR used for {file}")

            images = convert_from_path(file_path)

            for img in images:

                ocr_text = extract_text_from_image(img)

                text += ocr_text + "\n"

        text = clean_text(text)

        documents.append({
            "doc_id": file,
            "text": text
        })

    return documents