################################################
#Test scripts
#German Torre - 
################################################
#INIT Import related modules
import paramiko
import time
import math
import xlrd

#START VARIABLES

row = 2
column = 4
row_x = 0
column_x = 4

#FUNCTION DEFINITION
def get_ns_vip(row_x,column_x):

    #READ LIST OF NETWORK SEGMENTS
    #Read Excel table with NS VLAN 18 tables

    #Location of Scripts/Support files "C:\CODE\NS.xls"
    #NOTE: 
    loc = ('C:\\CODE\\NS.xls')
    
    # To open Workbook
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    
    # For row 0 and column 0
    print(sheet.cell_value(row_x, column_x))

#MAIN LOOP5

NS = int(input("ENTER NETWORK SEGMENT: "))
print("SELECTED NETWORK SEGMENT IS ",NS)
#calculate NS ROWS and COLUMNS by adding NS to start variables "row" and "column" and storing the result on variables "row_x" and "column_x"
row_x = row + NS

#CALL get_ns_vip() with calculated rows and columns
get_ns_vip(row_x,column_x)





