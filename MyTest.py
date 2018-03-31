import unittest
from PolynomialWork import Polynomial

class MyTest(unittest.TestCase):
    
    def testIntInit(self):
        p = Polynomial([2, 1, 3])
        self.assertEqual(p.coeffs, [2, 1, 3])
        self.assertEqual(p.degree, 2)

    def testFloatInit(self):
        p = Polynomial([-1.0, 0.0, -4.5, 4.0, 7.1])
        self.assertEqual(p.coeffs, [-1.0, 0.0, -4.5, 4.0, 7.1])
        self.assertEqual(p.degree, 4)

    def testEmptyList(self):
        self.assertRaises(TypeError, Polynomial, [])

    def testNullList(self):
        self.assertRaises(TypeError, Polynomial, "3")

    def testWrongList(self):
        self.assertRaises(TypeError, Polynomial, ["dfgh", 1])

    def testFirstNullCoeffs(self):
        p = Polynomial([0, 0, 1, 2])
        self.assertEqual(p.coeffs, [1, 2])
        self.assertEqual(p.degree, 1)

    def testFirstNullCoeffsWithZeroDegree(self):
        p = Polynomial([0, 0, 1])
        self.assertEqual(p.coeffs, [1])
        self.assertEqual(p.degree, 0)

    def testEqual(self):
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial([1, 2, 3])
        self.assertTrue(p1 == p2)

    def testNotEqual(self):
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial([1, 3])
        self.assertFalse(p1 == p2)

    def testConstEqual(self):
        p1 = Polynomial([5])
        p2 = 5
        self.assertTrue(p1 == p2)

    def testStringEquals(self):
        p1 = Polynomial([2, 0, 0])
        self.assertFalse(p1 == "2")

    def testMul1(self):
        p1 = Polynomial([1, 1])
        p2 = Polynomial([1, 1])
        p3 = p1 * p2
        self.assertEqual(p3.coeffs, [1, 2, 1])
        self.assertEqual(p3.degree, 2)

    def testMul2(self):
        p1 = Polynomial([1, 1])
        p2 = Polynomial([1, 1, 1])
        p3 = p1 * p2
        self.assertEqual(p3.coeffs, [1, 2, 2, 1])
        self.assertEqual(p3.degree, 3)

    def testMul3(self):
        p1 = Polynomial([1, 1, 0])
        p2 = Polynomial([0, 0])
        p3 = p1 * p2
        self.assertEqual(p3.coeffs, [0])
        self.assertEqual(p3.degree, 0)

    def testMul4(self):
        p1 = Polynomial([1, 2])
        p2 = 1.4
        p3 = p1 * p2
        self.assertEqual(p3.coeffs, [1.4, 2.8])
        self.assertEqual(p3.degree, 1)

    def testMul5(self):
        p1 = Polynomial([1, 2])
        p2 = 4
        p3 = p1 * p2
        self.assertEqual(p3.coeffs, [4, 8])
        self.assertEqual(p3.degree, 1)

    def testMul5(self):
        p1 = Polynomial([1, 2])
        self.assertRaises(TypeError, p1.__mul__, "5")

    def testTypeCoeff(self):
        self.assertRaises(TypeError, Polynomial, ["sdfg", "ggg"])

    def testStr(self):
        p1 = Polynomial([0, -2])
        self.assertEqual(str(p1), '-2')

    def testStr0(self):
        p1 = Polynomial([0, 0, 0])
        self.assertEqual(str(p1), '0')

    def testStr1(self):
        p1 = Polynomial([3, 4, 5, 1])
        self.assertEqual(str(p1), '3x^3+4x^2+5x+1')

    def testStr2(self):
        p1 = Polynomial([-1,0, 1])
        self.assertEqual(str(p1), '-x^2+1')

    def testStr3(self):
        p1 = Polynomial([0, -1, -1])
        self.assertEqual(str(p1), '-x-1')

if __name__ == "__main__":
    unittest.main()
    
