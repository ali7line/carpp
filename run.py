import io
import pickle
from carpp import parse_pdf
from pyPdf import PdfFileReader, PdfFileWriter


def get_pages(filename):
    with open(filename, 'rb') as f:
        main_pdf = PdfFileReader(f)
        for i in range(main_pdf.numPages):
            tmp_pdf = io.BytesIO()
            output = PdfFileWriter()
            output.addPage(main_pdf.getPage(i))
            output.write(tmp_pdf)
            print('========== PROCESSING page: %d ==============' % i)
            yield tmp_pdf


def save_list(tables, filename):
    with open(filename, 'wb') as f:
        pickle.dump(table, f)


if __name__ == '__main__':
    tables = []
    for page in get_pages('tests/sample_full_page.pdf'):
        table = parse_pdf.columize_pdf(page)
        tables.append(table)

        print('--------------')
        print parse_pdf.print_tables(tables, with_type=True)

    save_list(tables, 'sample_full.pkl')
