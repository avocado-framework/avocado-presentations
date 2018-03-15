from avocado import Test

def triangle_check(a, b, c):
    unique_sides = set([a, b, c])
    if len(unique_sides) == 1:
        return "equilateral"
    elif len(unique_sides) == 2:
        return "isosceles"
    else:
        return "scalene"

class Triangle(Test):

    def test_equilateral(self):
        self.assertEqual(triangle_check(1, 1, 1), "equilateral")

    def test_isosceles(self):
        self.assertEqual(triangle_check(2, 2, 3), "isosceles")
        self.assertEqual(triangle_check(3, 2, 3), "isosceles")

    def test_scalene(self):
        self.assertEqual(triangle_check(3, 4, 5), "scalene")
