import unittest
import math
def classify_triangle(a,b,c):
    if a+b <= c or a+c<=b or b+c<= a:
        return 'Not a triange'
    
    isRight = False
    if (a**2+b**2)==c**2 or (a**2+c**2)==b**2 or (b**2+c**2)==a**2:
        isRight = True

    if a==b==c:
        return 'Equilateral, isRight: ' + str(isRight)
    elif a==b or a==c or b==c:
        return 'Isosceles, isRight: ' + str(isRight)
    else:
        return 'Scalene, isRight: ' + str(isRight)

def runClassifyTriangle(a, b, c):
    print('classify_triangle(',a, ',', b, ',', c, ')=',classify_triangle(a,b,c),sep="")

class TestTriangles(unittest.TestCase):
    def testInvalidInputs(self):
        self.assertEqual(classify_triangle(1,1,9),'Not a triange','1,1,9 is not a triangle')

    def testValidInputs(self):
        self.assertEqual(classify_triangle(5,6,8),'Scalene, isRight: False','5,6,8 is a Scalene triangle')
        self.assertEqual(classify_triangle(3,4,5),'Scalene, isRight: True','3,4,5 is a Scalene, Right triangle')
        self.assertEqual(classify_triangle(2,2,3),'Isosceles, isRight: False','2,2,3 is an Isosceles triangle')
        self.assertEqual(classify_triangle(1,1,1),'Equilateral, isRight: False','1,1,1 is an Equilateral triangle')
    
    def testInvalidTests(self): 
        self.assertNotEqual(classify_triangle(1,1,1),'Isosceles, isRight: False','1,1,1 should be equilateral')
        self.assertEqual(classify_triangle(10,15,30),'Scalene, isRight: False','Should be not a triangle')
    

if __name__ == '__main__':
    # examples of running the code
    runClassifyTriangle(1,2,3)
    runClassifyTriangle(1,1,1)
    runClassifyTriangle(7,8,10)
    runClassifyTriangle(5,5,6)
    runClassifyTriangle(3,4,5)

    unittest.main(exit=True)