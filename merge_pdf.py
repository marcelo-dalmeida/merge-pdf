import os
import glob
import PyPDF2


def merge_pdfs(pdf_list, output):
    pdf_writer = PyPDF2.PdfFileWriter()

    for pdf in pdf_list:
        pdf_reader = PyPDF2.PdfFileReader(pdf)
        for page_num in range(pdf_reader.getNumPages()):
            page = pdf_reader.getPage(page_num)
            pdf_writer.addPage(page)

    with open(output, 'wb') as out:
        pdf_writer.write(out)

def fetch_pdfs(directory):
    os.chdir(directory)
    pdfs = glob.glob('*.pdf')
    pdfs.sort()  # Sort the list in place
    return pdfs

# Directory to fetch PDFs from
directory = '.'

pdfs = fetch_pdfs(directory)

# Output PDF
output_pdf = './output/merged.pdf'

merge_pdfs(pdfs, output_pdf)
