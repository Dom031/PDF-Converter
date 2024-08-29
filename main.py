from PyPDF2 import PdfWriter, PdfReader

template = PdfReader(open('Super.pdf', 'rb'))
watermark = PdfReader(open('wtr.pdf', 'rb'))
output = PdfWriter()


for i in range(len(template.pages)):
    page = template.pages[i]
    page.merge_page(watermark.pages[0])
    output.add_page(page)

    with open('watermarked5.pdf', 'wb') as file:
        output.write(file)


