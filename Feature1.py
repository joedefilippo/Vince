import unittest
from selenium import webdriver

class Feature1(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome()

	def tearDown(self):
		self.driver.close()

	def test_Verify_Google_Search_Testing(self):
		#Step: 1.0
		#Action: Open Google.com
		#Expected Result: Google appears in the page title

		#Step: 2.0
		#Action: Enter testing in the search bar and press enter
		#Expected Result: Some search results are displayed

		pass

	def test_Verify_Google_Search_Python(self):
		#Step: 1.0
		#Action: Open Google.com
		#Expected Result: Google appears in the page title

		#Step: 2.0
		#Action: Enter python in the search bar and press enter
		#Expected Result: Some search results are displayed

		pass

	def test_Verify_Something_Else(self):
		#Step: 1.0
		#Action: Do something
		#Expected Result: Something happens

		#Step: 2.0
		#Action: Try this next
		#Expected Result: This thing should happen

		#Step: 3.0
		#Action: Input this information and Press Submit
		#Expected Result: Page X appears

		#Step: 4.0
		#Action: Check if the information is correct
		#Expected Result: Info appears as expected

		pass

def Feature1_suite():
	suite = unittest.TestSuite()
	suite.addTest(Feature1('test_Verify_Google_Search_Testing'))
	suite.addTest(Feature1('test_Verify_Google_Search_Python'))
	suite.addTest(Feature1('test_Verify_Something_Else'))
	return suite

mySuite = Feature1_suite()
runner = unittest.TextTestRunner()
runner.run(mySuite)


