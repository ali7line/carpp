from pdftables import get_tables
from pprint import pprint
from operator import add
from pyPdf import PdfFileWriter, PdfFileReader

inputpdf = PdfFileReader(open("document.pdf", "rb"))
inputpdf.


for i in xrange(inputpdf.numPages):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
        #with open("document-page%s.pdf" % i, "wb") as outputStream:
            output.write(outputStream)

all_tables = get_tables(open('ss3.pdf', 'rb'))

cars = []
main_found_flag = False
sup_found_flag = False

company = 'Accura'

space = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
car_info = {
        'company': [],
        'year': [],
        'model': [],
        'series/trans': [],
        'engine': [],
        'body': [],
        'color': [],
        'odom': [],
        'price': [],
        'key-options': [],
        'vin': [],
        'sale-type': [],
        'trim': [],
    }

# the lines that are just headers and infos, dates
def is_header(row):
    pass

# the line that includes company name
def is_company(row):
    pass

# a main line with most info
def is_mainrow(row):
    if row[0].isdigit():
        return True
    else:
        return False

# a supplimentary line
def is_suprow(row, main_found_flag, sup_found_flag):
    # check to see if is not empty
    if any(row) and (main_found_flag or sup_found_flag):
        return True
    return False

def merge_sup_to_main(main_dic, sup_dic):
    pass

for page in all_tables:
    print('--------------- AT PAGE')
    for row in page:
        if len(row) != 11:
            print(len(row))
            raise "number of columes does not match"
        if is_mainrow(row):
            print('-------------------------------------')
            main_found_flag = True
            print('main', row)
            #car = dict(car_info)
            #car['company'] = company
            #car['year'] = row[0]
            #car['model'] = row[1]
            #car['series/trans'] = row[2]
            #car['engine'] = row[3]
            #car['body'] = row[4]
            #car['color'] = row[5]
            #car['odom'] = row[6]
            #car['price'] = row[7]
            #car['vin'] = row[8]
            #car['sale-type'] = row[9]
            #car['trim'] = row[10]
            #cars.append(car)
        elif is_suprow(row, main_found_flag, sup_found_flag):
            main_found_flag = False
            sup_found_flag = True
            print('sup', row)
        else:
            main_found_flag = False
            sup_found_flag = False


#pprint(car)
#print(len(cars))
