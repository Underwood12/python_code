from datetime import date, time, datetime
from decimal import Decimal
from xlwt import Workbook

wb = Workbook()
ws = wb.add_sheet("Type examples")
ws.col(0).width = 5000
ws.write(0, 0, '第一列为数字数据')
ws.write(1, 0, 3.145)
ws.write(2, 0, 2 << 40)
ws.write(3, 0, Decimal('3.65'))
ws.write(4, 0, date(2019, 1, 8))
ws.write(5, 0, datetime(2019, 1, 8, 14, 1, 32))
ws.write(6, 0, time(17, 1))

ws.write(0, 1, 'Text')
ws.write(1, 1, 5 > 9)
ws.write(2, 1, True)
wb.save('types.xls')