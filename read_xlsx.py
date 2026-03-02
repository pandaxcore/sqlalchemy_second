import openpyxl
from engine import engine
from model import Base


Base.metadata.create_all(engine)

workbook = openpyxl.load_workbook('file_example_XLS_10.xlsx')
sheet = workbook.active

cell_value = sheet['A1'].value

for row in sheet.iter_rows():
    for cell in row:
        if cell.value:
            print(cell.value)
