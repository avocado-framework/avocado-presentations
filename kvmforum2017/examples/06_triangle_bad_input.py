# -*- coding: utf-8 -*-

from avocado import Test

def triangle_check(a, b, c):
    try:
        a = int(a)
    except ValueError:
        return "error"
    try:
        b = int(b)
    except ValueError:
        return "error"
    try:
        c = int(c)
    except ValueError:
        return "error"
    
    if min([a, b, c]) <= 0:
        return "error"

    for (x, y, z) in [(a, b, c),   # covers (b, a, c)
                      (a, c, b),   # covers (c, a, b)
                      (b, c, a)]:  # covers (c, b, a)
        if ((x + y) <= z):
            return "error"

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

    def test_no_length(self):
        self.assertEqual(triangle_check(0, 1, 1), "error")
        self.assertEqual(triangle_check(-1, 1, 1), "error")

    def test_sum_2_sides_larger_3rd(self):
        self.assertEqual(triangle_check(1, 1, 2), "error")
        self.assertEqual(triangle_check(1, 2, 3), "error")
        self.assertEqual(triangle_check(3, 2, 1), "error")

    def test_bad_input(self):
        self.assertEqual(triangle_check("π", 4, 5), "error")
