# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    
    def testScaleneTriangleA(self):
        self.assertEqual(classifyTriangle(5,7,9),'Scalene','5,7,9 is a Scalene triangle')

    def testScaleneTriangleB(self):
        self.assertEqual(classifyTriangle(9,7,5),'Scalene','9,7,5 is a Scalene triangle')

    def testIsoscelesTriangleA(self):
        self.assertEqual(classifyTriangle(6,6,8),'Isosceles','6,6,8 is an Isosceles triangle')

    def testIsoscelesTriangleB(self):
        self.assertEqual(classifyTriangle(8,6,6),'Isosceles','8,6,6 is an Isosceles triangle')

    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(3,4,8),'NotATriangle','3,4,8 is not a triangle')

    def testInvalidInputA(self):
        self.assertEqual(classifyTriangle(0,0,0),'InvalidInput','0,0,0 is not a valid input')

    def testInvalidTriangleB(self):
        self.assertEqual(classifyTriangle(201,201,201),'InvalidInput','201,201,201 is not a valid input')

    def testInvalidTriangleC(self):
        self.assertEqual(classifyTriangle('201','201','201'),'InvalidInput',"'201','201','201' is not a valid input")    

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

