from avocado import Test

def triangle_check(a, b, c):
    if a == b == c:
        return "equilateral"
    elif a != b != c:
        return "scalene"
    else:
        return "isosceles"

class Triangle(Test):

    def test_equilateral(self):
        self.assertEqual(triangle_check(1, 1, 1), "equilateral")

    def test_isosceles(self):
        self.assertEqual(triangle_check(2, 2, 3), "isosceles")
        self.assertEqual(triangle_check(3, 2, 3), "isosceles")

    def test_scalene(self):
        self.assertEqual(triangle_check(3, 4, 5), "scalene")
