import fitz
from docx import Document
3
def extract_pdf_text(path):
doc = fitz.open(path)
text = ""
for page in doc:
text += page.get_text()
return text
def extract_docx_text(path):
doc = Document(path)
text = "\n".join([
para.text for para in doc.paragraphs
])
return text
def extract_resume_text(path):
if path.endswith(".pdf"):
return extract_pdf_text(path)
elif path.endswith(".docx"):
return extract_docx_text(path)
else:
raise Exception("Unsupported file format")