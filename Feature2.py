import unittest
from selenium import webdriver

class Feature2(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome()

	def tearDown(self):
		self.driver.close()

	def test_Feature2_Test1(self):
		#Step: 1.0
		#Action: feature2 test 1 action 1
		#Expected Result: feature2 test 1 res 1

		#Step: 2.0
		#Action: feature2 test 1 action 2
		#Expected Result: feature2 test 1 res 2

		pass

	def test_Feature2_Test2(self):
		#Step: 1.0
		#Action: feature2 test 2 action 1
		#Expected Result: feature2 test 2 res 1

		#Step: 2.0
		#Action: feature2 test 2 action 2
		#Expected Result: feature2 test 2 res 2

		pass

def Feature2_suite():
	suite = unittest.TestSuite()
	suite.addTest(Feature2('test_Feature2_Test1'))
	suite.addTest(Feature2('test_Feature2_Test2'))
	return suite

mySuite = Feature2_suite()
runner = unittest.TextTestRunner()
runner.run(mySuite)


