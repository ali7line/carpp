import io
from carpp import parse_pdf
from pyPdf import PdfFileReader, PdfFileWriter


if __name__ == '__main__':
    tables = []
    with open('tests/sample_1_page.pdf', 'rb') as f:
        main_pdf = PdfFileReader(f)
        for i in range(main_pdf.numPages):
            tmp_pdf = io.BytesIO()
            output = PdfFileWriter()
            output.addPage(main_pdf.getPage(i))
            output.write(tmp_pdf)
            print('========== PROCESSING page: %d ==============' % i)
            table = parse_pdf.columize_pdf(tmp_pdf)
            tables.append(table)

        print('--------------')
        print parse_pdf.print_tables(tables)
