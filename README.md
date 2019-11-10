# Vince
Vince is a set of tools useful for preparing manual test cases in Excel to be automated using Selenium with the Python UnitTest framework.
Vince.py will open an Excel file full of test cases and create boilerplate code.

1. Each worksheet of the Excel file will be processed into it's own python output file
2. Vince.py is assuming that the Excel follows this format: Test Name = Col A, Step # = Col B, Action = Col C, and Expected Result = Col D
3. Within each python file that is generated, the following objects are created:
  - Class definition which matches the name of the Excel WorkSheet Name
  - Set up and Tear down functions that launch webdriver
  - 1 function definiton per test case
  - A test suite object consisting of all the test cases imported
4. Within the function definition, comments are created - the comments represent the manual test details
 - This is to help the automation engineer to begin to write his code, without having to reference back to the original file
