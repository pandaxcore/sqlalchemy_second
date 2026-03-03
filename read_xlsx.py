from openpyxl import load_workbook
from engine import engine
from model import Base


Base.metadata.create_all(engine)

wb = load_workbook('file_example_XLS_10.xlsx')
print(wb.sheetnames)

sheet = wb['Sheet1']
print(sheet['d10'].value)

for row in sheet.iter_rows(values_only=True):
    print(row[0])
