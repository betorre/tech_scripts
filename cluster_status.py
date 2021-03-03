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
column_dps = 12
column_hsp = 13
column_mcr100 = 14
column_mcr101 = 15
column_mcr102 = 16
column_mcr103 = 17
column_ipm = 18

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
    #NOTE: double backslash is needed for unicode/utf8 interaction
    loc = ('C:\\CODE\\NS.xls')
    
    # To open Workbook
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    
    # For row 0 and column 0
    print(sheet.cell_value(row_nsid, column_h2))
###
###GET DPS IP based on User Input of NSID
def get_ns_dps(row_nsid,column_dps):

    #READ LIST OF NETWORK SEGMENTS
    #Read Excel table with NS VLAN 18 tables

    #Location of Scripts/Support files "C:\CODE\NS.xls"
    #NOTE: double backslash is needed for unicode/utf8 interaction
    loc = ('C:\\CODE\\NS.xls')
    
    # To open Workbook
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    
    # For row 0 and column 0
    print(sheet.cell_value(row_nsid, column_dps))
###
###GET HSP IP based on User Input of NSID
def get_ns_hsp(row_nsid,column_hsp):

    #READ LIST OF NETWORK SEGMENTS
    #Read Excel table with NS VLAN 18 tables

    #Location of Scripts/Support files "C:\CODE\NS.xls"
    #NOTE: double backslash is needed for unicode/utf8 interaction
    loc = ('C:\\CODE\\NS.xls')
    
    # To open Workbook
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    
    # For row 0 and column 0
    print(sheet.cell_value(row_nsid, column_hsp))
###
###GET MCR100 IP based on User Input of NSID
def get_ns_mcr100(row_nsid,column_mcr100):

    #READ LIST OF NETWORK SEGMENTS
    #Read Excel table with NS VLAN 18 tables

    #Location of Scripts/Support files "C:\CODE\NS.xls"
    #NOTE: double backslash is needed for unicode/utf8 interaction
    loc = ('C:\\CODE\\NS.xls')
    
    # To open Workbook
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    
    # For row 0 and column 0
    print(sheet.cell_value(row_nsid, column_mcr100))
###
###GET MCR101 IP based on User Input of NSID
def get_ns_mcr101(row_nsid,column_mcr101):

    #READ LIST OF NETWORK SEGMENTS
    #Read Excel table with NS VLAN 18 tables

    #Location of Scripts/Support files "C:\CODE\NS.xls"
    #NOTE: double backslash is needed for unicode/utf8 interaction
    loc = ('C:\\CODE\\NS.xls')
    
    # To open Workbook
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    
    # For row 0 and column 0
    print(sheet.cell_value(row_nsid, column_mcr101))
###
###GET MCR102 IP based on User Input of NSID
def get_ns_mcr102(row_nsid,column_mcr102):

    #READ LIST OF NETWORK SEGMENTS
    #Read Excel table with NS VLAN 18 tables

    #Location of Scripts/Support files "C:\CODE\NS.xls"
    #NOTE: double backslash is needed for unicode/utf8 interaction
    loc = ('C:\\CODE\\NS.xls')
    
    # To open Workbook
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    
    # For row 0 and column 0
    print(sheet.cell_value(row_nsid, column_mcr102))
###
###GET MCR103 IP based on User Input of NSID
def get_ns_mcr103(row_nsid,column_mcr103):

    #READ LIST OF NETWORK SEGMENTS
    #Read Excel table with NS VLAN 18 tables

    #Location of Scripts/Support files "C:\CODE\NS.xls"
    #NOTE: double backslash is needed for unicode/utf8 interaction
    loc = ('C:\\CODE\\NS.xls')
    
    # To open Workbook
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    
    # For row 0 and column 0
    print(sheet.cell_value(row_nsid, column_mcr103))
###
###GET IPM IP based on User Input of NSID
def get_ns_ipm(row_nsid,column_ipm):

    #READ LIST OF NETWORK SEGMENTS
    #Read Excel table with NS VLAN 18 tables

    #Location of Scripts/Support files "C:\CODE\NS.xls"
    #NOTE: double backslash is needed for unicode/utf8 interaction
    loc = ('C:\\CODE\\NS.xls')
    
    # To open Workbook
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    
    # For row 0 and column 0
    print(sheet.cell_value(row_nsid, column_ipm))
###
#MAIN LOOP

NS = int(input("ENTER NETWORK SEGMENT: "))
print("SELECTED NETWORK SEGMENT IS ",NS)
#calculate NS ROWS and COLUMNS by adding NS to start variables "row" and "column" and storing the result on variables "row_x" and "column_x"
row_nsid = row + NS

#CALL get_ns_vip() with calculated rows and columns
get_ns_vip(row_nsid,column_vip)
get_ns_h1(row_nsid,column_h1)
get_ns_h2(row_nsid,column_h2)
get_ns_dps(row_nsid,column_dps)
get_ns_hsp(row_nsid,column_hsp)
get_ns_mcr100(row_nsid,column_mcr100)
get_ns_mcr101(row_nsid,column_mcr101)
get_ns_mcr102(row_nsid,column_mcr102)
get_ns_mcr103(row_nsid,column_mcr103)
get_ns_ipm(row_nsid,column_ipm)






