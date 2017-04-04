#!/usr/bin/env python3
'''
To run
	1] chmod a+x grading_module_tests.py
	2] ./grading_module_tests.py
'''

from grading_module import GradingAPI
import unittest

class_A_grades = [99, 92, 91, 91, 89, 85, 83, 82, 80, 79, 78, 78, 77, 76, 75, 74, 62, 55, 43, 20]
class_B_grades = [56,36,66,88,90,99,100,43,76,76,76,76,44] 
class_C_grades = [66,78,65,90]
class_D_grades = [90,85,75,65,50] 
class_7_grades = [55,66,77,88,99,22,11] 
class_cheaters = [77,77,77,77,77,77]


class GradingTest(unittest.TestCase):

    def testCalculation(self):
        self.assertEqual(GradingAPI(class_A_grades, {99: 'A', 92: 'A', 91: 'A', 89: 'B', 85: 'B',
         83: 'B', 82: 'B', 80: 'C', 79: 'C', 78: 'C', 77: 'D', 76: 'D', 75: 'D', 74: 'D', 62: 'F', 55: 'F', 43: 'F', 20: 'F'})
        self.assertEqual(GradingAPI(class_B_grades, {100: 'A', 99: 'A', 90: 'B', 88: 'B', 76: 'C', 66: 'C', 56: 'D', 44: 'D', 43: 'F', 36: 'F'})
        self.assertEqual(GradingAPI(class_C_grades, "Class size is too small to apply this calculation correctly. Requires a minimum of 5 grades")
        self.assertEqual(GradingAPI(class_D_grades, {90: 'A', 85: 'B', 75: 'C', 65: 'D', 50: 'F'} )
        self.assertEqual(GradingAPI(class_7_grades, {99: 'A', 88: 'B', 77: 'C', 66: 'C', 55: 'D', 22: 'F', 11: 'F'})
        self.assertEqual(GradingAPI(class_cheaters), {"77":F})

if __name__ == "__main__": 
    unittest.main()


 # Test for sample B is working and I dont know why this test isnt being passed.