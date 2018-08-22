import xlrd
# Открываем workbook
wb = xlrd.open_workbook('excel-sample.xls')
# Пишем имена табличек
print(wb.sheet_names())
# Получаем первую таблицу по имени или индексу
sh = wb.sheet_by_index(0)
# Перебираем строки, возвращая их как список, который я могу индексировать
for rownum in range(sh.nrows):
    print(sh.row_values(rownum))
# Если хочу только первую колонку
first_column = sh.col_values(0)
print(first_column)
# Индекс отдельных ячеек
cell_c4 = sh.cell(3, 2).value
print(cell_c4)
# Let's say you want the same cell from x identical sheets in a workbook:
x = 2
while x >= 0:
    sh = wb.sheet_by_index(x)
    cell_x = sh.cell(2, 3).value
    print(cell_x)
    x = x - 1