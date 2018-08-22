import xlrd
from collections import OrderedDict
import simplejson as json
# открываю воркбук и выбираю первый лист
wb = xlrd.open_workbook('excel-sample.xls')
sh = wb.sheet_by_index(0)
# список для хранения словарей
elements_list = []
# итерации по каждой строке в листе и выбор значений в словаре
for rownum in range(1, sh.nrows):
    elements = OrderedDict()
    row_values = sh.row_values(rownum)
    elements['elem-id'] = row_values[0]
    elements['name'] = row_values[1]
    elements['formula'] = row_values[2]
    elements['mass'] = row_values[3]
    elements_list.append(elements)
# Пихаем списки словарей в json
j = json.dumps(elements_list)
# Записываем в файл
with open('data.json', 'w') as f:
    f.write(j)