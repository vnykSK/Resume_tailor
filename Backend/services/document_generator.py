from docx import Document



def create_docx(content, filename):

    doc = Document()

    for line in content.split("\n"):
        doc.add_paragraph(line)

    doc.save(filename)