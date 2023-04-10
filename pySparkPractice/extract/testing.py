from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTLine, LTRect, LTImage
from pdfminer.pdfpage import PDFPage
import io

def extract_lines_images(page):
    # Create a PDF resource manager and a PDF device object
    rsrcmgr = PDFResourceManager()
    laparams = LAParams()
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    # Create a layout analyzer object
    layout = device.get_result()

    # Iterate over the elements in the layout and extract the lines and images
    lines = []
    images = []
    for element in layout:
        if isinstance(element, LTTextBox):
            for line in element:
                if isinstance(line, LTTextLine):
                    lines.append(line.get_text())
        elif isinstance(element, (LTLine, LTRect)):
            # This is a line or rectangle
            lines.append(element)
        elif isinstance(element, LTImage):
            # This is an image
            images.append(element)

    return lines, images
file_name = r'C:\Users\GokulReddy\PycharmProjects\pySparkPractice\data\sample_new.pdf'
# Open the PDF file and get the first page
with open(file_name, 'rb') as fp:
    stream = io.BytesIO(fp.read())
with pdf.PdfFileReader(stream) as reader:
    page = reader.getPage(0)

# Extract the lines and images from the page
lines, images = extract_lines_images(page)
