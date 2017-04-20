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

def print_tables(tables):
    for table in tables:
        for row in table:
            print row


def columize_pdf(pdf_page, column_goal=12):
    sug_calibrations = range(3,8)
    best_calibration = 1
    max_column = 1

    best_table = []
    for cal in sug_calibrations:
        print '- Checking calibration: %d' % (cal,)
        table = get_tables(pdf_page, calibrate=cal)
        print table
        print table[0]
        table = table[0]
        first_row = table[0]

        # checking is row has correct number of columns of pick best so far
        if len(first_row) == column_goal:
            print '    number of columns: %d' % len(first_row)
            print '    PERFECT MATCH FOUND'
            best_calibration = cal
            max_col = len(first_row)
            best_table = table
            break
        else:
            print '     number of columns: %d' % len(first_row)
            if max_column < len(first_row):
                print '     a better calibration found'
                best_calibration = cal
                max_column = len(first_row)
                best_table = table
            continue

    return table



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
            table = columize_pdf(tmp_pdf)
            tables.append(table)

        print('--------------')
        print print_tables(tables)
