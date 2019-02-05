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

    def testNotaTriangles(self):
        self.assertEqual(classifyTriangle(11,3,5),"Not a Triangle","11,3,5 is not a triangle")
    
    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(15,11,9),"Scalene","15,11,9 is a scalene triangle")
    
    def testIsocelesTriangles(self):
        self.assertEqual(classifyTriangle(9,11,9),"Isoceles","9,11,9 is an Isoceles triangle")
         
    def test_triangles2(self):
        self.assertNotEqual(classifyTriangle(10,10,10),"Isoceles","10,10,10 should be equilateral")

if __name__ == '__main__':
    print("Running unittest cases")
    unittest.main(exit=False, verbosity=2)

