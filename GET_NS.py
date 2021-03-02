#Read Excel table with NS VLAN 18 tables
import xlrd

#Location of Scripts/Support files "C:\CODE"
loc = ('C:\\CODE\\NS.xls')
 
# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
 
# For row 0 and column 0
print(sheet.cell_value(3, 4))