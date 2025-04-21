from docxtpl import DocxTemplate
import os

def generate_cover_letter(context, template_path="templates/cover_letter_template.docx", output_dir="output/tailored_docs"):
    doc = DocxTemplate(template_path)
    doc.render(context)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    file_path = os.path.join(output_dir, f"{context['company']}_cover_letter.docx")
    doc.save(file_path)
    return file_path
