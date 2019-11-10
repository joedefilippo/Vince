'''
@author: Joe DeFilippo
@date: November 2019
@license: GNU General Public License v3.0
@version: 1.0
@summary: "Vince" is a set of tools useful for preparing manual test cases in Excel to be automated using Selenium with the Python UnitTest Framework.   
'''

import xlrd
import unittest

# Excel field mapping constants
# Excel Column A = 0, B = 1, C = 2, D = 3
TEST_NAME_COLUMN_INDEX = 0
STEP_NUMBER_COLUMN_INDEX = 1
ACTION_COLUMN_INDEX = 2
EXPECTED_RESULT_COLUMN_INDEX = 3

# Open the Excel file with the manual test cases
manual_tests_excel_file ="Manual Tests Sample File.xlsx"
excel_workbook = xlrd.open_workbook(manual_tests_excel_file) 

# Get the names of all sheets stored in the workbook
sheet_names = excel_workbook.sheet_names()

# For each sheet in the workbook...    
for sheet_index in range(0,sheet_names.__len__()):
    workbook_sheet = excel_workbook.sheet_by_index(sheet_index)

    # Create a dictionary that will keep track of how many steps are in each test case
    test_step_count = {}  

    # Iterate each row in the Excel file - each row represents a test step
    # Change the test case name to something more friendly to the Python UnitTest framework
    # Keep a running tally of the number of steps for each test case
    for a_row in range(1,workbook_sheet.nrows):
        manual_test_case_name = workbook_sheet.cell_value(a_row,TEST_NAME_COLUMN_INDEX)
    
        automated_test_case_name = "test_"+manual_test_case_name.replace(" ","_")
    
        if not automated_test_case_name in test_step_count:
            test_step_count[automated_test_case_name] = 1
        else:
            test_step_count[automated_test_case_name] += 1
    
    # Start to output to the file boilerplate code
    # Header/Imports
    vince_output_file = open(sheet_names[sheet_index]+".py","w")
    vince_output_file.write("import unittest\n")
    vince_output_file.write("from selenium import webdriver\n\n")        

    # Create the class definition - each sheet in the workbook will be its own class
    # Recommendation is to separate test cases into different sheets based on feature or module within the application
    # Create the setup (launch chrome) and teardown (close chrome) functions 
    vince_output_file.write("class "+sheet_names[sheet_index]+"(unittest.TestCase):\n\n")
    vince_output_file.write("\tdef setUp(self):\n")
    vince_output_file.write("\t\tself.driver = webdriver.Chrome()\n\n")
    vince_output_file.write("\tdef tearDown(self):\n")
    vince_output_file.write("\t\tself.driver.close()\n\n")        

    # Iterate through all the tests and create the function definitions
    # Pull the Step Numbers, Actions, and Expected Results in from the current Excel sheet
    # Output those values as comments in the function definition
    # Increment the counter that keeps track of the test case row number (step number)         
    test_case_step_number = 1
    for test in test_step_count:
        vince_output_file.write("\tdef " + test + "(self):\n")
        for step in range(1,test_step_count[test]+1):
            vince_output_file.write("\t\t#Step: "+ str(workbook_sheet.cell_value(test_case_step_number,STEP_NUMBER_COLUMN_INDEX))+"\n")
            vince_output_file.write("\t\t#Action: "+ workbook_sheet.cell_value(test_case_step_number,ACTION_COLUMN_INDEX)+"\n")
            vince_output_file.write("\t\t#Expected Result: "+ workbook_sheet.cell_value(test_case_step_number,EXPECTED_RESULT_COLUMN_INDEX)+"\n\n")
            test_case_step_number += 1
        vince_output_file.write("\t\tpass\n\n")
    
    # Define a Python Unit Test Test Suite and add all the test cases to it
    # Output the code to create the suite object and run the test suite
    vince_output_file.write("def "+sheet_names[sheet_index]+"_suite():\n")    
    vince_output_file.write("\tsuite = unittest.TestSuite()\n")
    
    for test in test_step_count:
        vince_output_file.write("\tsuite.addTest("+sheet_names[sheet_index]+"('"+test+"'))\n")    
    vince_output_file.write("\treturn suite\n\n")
    
    vince_output_file.write("mySuite = "+sheet_names[sheet_index]+"_suite()\n")    
    vince_output_file.write("runner = unittest.TextTestRunner()\n")  
    vince_output_file.write("runner.run(mySuite)\n\n\n")  

vince_output_file.close()