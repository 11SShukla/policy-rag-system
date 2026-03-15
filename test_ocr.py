import os
from app.ingest import extract_text_from_pdf

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

pdf_path = os.path.join(BASE_DIR, "data_RBI", "KYC1.pdf")

text = extract_text_from_pdf(pdf_path)

print(text[:1000])