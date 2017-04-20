import io
from operator import add
from pyPdf import PdfFileReader, PdfFileWriter
from pdftables import get_tables



def type_row(row):
    if not row[0]:
        return 'dont know yet'
    elif row[0] == u'Yr':
        return 'header'
    elif row[0].isdigit():
        return 'main'
    else:
        return 'company'


def merge_rows(rows):
    if len(rows) < 2:
        return None
    else:
        return [' '.join(i).strip() for i in zip(*rows)]

def process_tables(tables):
    # flags=[False, False, False]
    for table in tables:
        for row in table[1]:
            print(type_row(row), row)


def columize_pdf(pdf_page, page_num, good_pages, bad_pages):
    found_correct_col = False

    for cal in [5, 6, 7, 8, 4, 3]:
        table = get_tables(pdf_page, calibrate=cal)[0]
        # if page_num == 0:
        #     head = table[:8]
        #     table = table[8:]
        print('Table on page %d has %d rows' % (page_num, len(table)))
        if len(table[0]) != 12:
            print(len(table[0]), table[0])
            print('changing cal %d' % (cal,))
            continue
        else:
            found_correct_col = True
            good_pages.append((page_num, table))
            for row in table:
                print(len(row), row)
            break

    if not found_correct_col:
        bad_pages.append((page_num, table))


if __name__ == '__main__':
    with open('ss3.pdf', 'rb') as f:
        good = []
        bad = []
        main_pdf = PdfFileReader(f)
        for i in range(main_pdf.numPages):
            tmp_pdf = io.BytesIO()
            output = PdfFileWriter()
            output.addPage(main_pdf.getPage(i))
            output.write(tmp_pdf)
            print('= PROCESSING page: %d' % i)
            columize_pdf(tmp_pdf, page_num=i, good_pages=good, bad_pages=bad)

        print('--------------')
        print('good ones %d:' % len(good))
        print('bad ones %d:' % len(bad))

        cars = process_tables(good)
