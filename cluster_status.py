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
row_nsid = 0
column_vip = 4
column_h1 = 5
column_h2 = 6

#FUNCTION DEFINITION
###GET NS VIP based on user input of NS ID
def get_ns_vip(row_nsid,column_vip):

    #READ LIST OF NETWORK SEGMENTS
    #Read Excel table with NS VLAN 18 tables

    #Location of Scripts/Support files "C:\CODE\NS.xls"
    #NOTE: 
    loc = ('C:\\CODE\\NS.xls')
    
    # To open Workbook
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    
    # For row 0 and column 0
    print(sheet.cell_value(row_nsid,column_vip))
###
###GET H1-NSCX IP based on User Input of NSID
def get_ns_h1(row_nsid,column_h1):

    #READ LIST OF NETWORK SEGMENTS
    #Read Excel table with NS VLAN 18 tables

    #Location of Scripts/Support files "C:\CODE\NS.xls"
    #NOTE: 
    loc = ('C:\\CODE\\NS.xls')
    
    # To open Workbook
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    
    # For row 0 and column 0
    print(sheet.cell_value(row_nsid, column_h1))
###
###GET H2-NSCX IP based on User Input of NSID
def get_ns_h2(row_nsid,column_h2):

    #READ LIST OF NETWORK SEGMENTS
    #Read Excel table with NS VLAN 18 tables

    #Location of Scripts/Support files "C:\CODE\NS.xls"
    #NOTE: 
    loc = ('C:\\CODE\\NS.xls')
    
    # To open Workbook
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    
    # For row 0 and column 0
    print(sheet.cell_value(row_nsid, column_h2))
###
#MAIN LOOP5

NS = int(input("ENTER NETWORK SEGMENT: "))
print("SELECTED NETWORK SEGMENT IS ",NS)
#calculate NS ROWS and COLUMNS by adding NS to start variables "row" and "column" and storing the result on variables "row_x" and "column_x"
row_nsid = row + NS

#CALL get_ns_vip() with calculated rows and columns
get_ns_vip(row_nsid,column_vip)





