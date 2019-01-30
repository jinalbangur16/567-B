
import unittest

def classify_triangle(a, b, c):
    s=""
    sides = [a,b,c]
    sides.sort()
    if sides[0] + sides[1] <= sides[2] or sides[1] + sides[2] <= sides[0] or sides[2] + sides[0] <= sides[1]:
        s += "Not a Triangle"
    else:
        if sides[0]**2 + sides[1]**2 == sides[2]**2:
            s += "Right "

        if  len(list(set(sides))) == 1:
            s += "Equilateral"

        if len(list(set(sides))) == 2:
            s += "Isoceles"

        if len(list(set(sides))) == 3:
            s += "Scalene"
    return s

classify_triangle(3,4,5)
classify_triangle(1,1,1)

def runclassify_triangle(a, b, c):
    print("classify_triangle(",a,",",b,",",c,") = ", classify_triangle(a,b,c) )

class test_classify_triangle(unittest.TestCase):
    def test_triangles1(self):
        self.assertEqual(classify_triangle(3,4,5),"Right Scalene","3,4,5 is a Right Scalene Triangle")
        self.assertEqual(classify_triangle(4,4,4),"Equilateral","4,4,4 is an Equilateral Triangle")
        self.assertEqual(classify_triangle(1,2,3),"Not a Triangle","1,2,3 is not a triangle")
        self.assertEqual(classify_triangle(11,3,5),"Not a Triangle","11,3,5 is not a triangle")
        self.assertEqual(classify_triangle(15,11,9),"Scalene","15,11,9 is a scalene triangle")
        self.assertEqual(classify_triangle(9,11,9),"Isoceles","9,11,8 is an Isoceles triangle")
         
    def test_triangles2(self):
        self.assertNotEqual(classify_triangle(10,10,10),"Isoceles","10,10,10 should be equilateral")

if __name__=='__main__':

    runclassify_triangle(15,11,9)
    runclassify_triangle(9,11,8)
    runclassify_triangle(7,11,7)

    unittest.main(exit=False, verbosity=2)