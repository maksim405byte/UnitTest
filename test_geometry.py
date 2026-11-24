import math
import unittest

import circle
import rectangle
import square
import triangle


class RectangleTestCase(unittest.TestCase):
    # 1
    def test_rectangle_area_normal(self):
        self.assertEqual(rectangle.area(5, 10), 50)

    # 2
    def test_rectangle_area_zero(self):
        self.assertEqual(rectangle.area(10, 0), 0)

    # 3
    def test_rectangle_perimeter_normal(self):
        self.assertEqual(rectangle.perimeter(5, 10), 30)

    # 4
    def test_rectangle_perimeter_square_case(self):
        self.assertEqual(rectangle.perimeter(7, 7), 28)


class SquareTestCase(unittest.TestCase):
    # 5
    def test_square_area_normal(self):
        self.assertEqual(square.area(6), 36)

    # 6
    def test_square_area_zero(self):
        self.assertEqual(square.area(0), 0)

    # 7
    def test_square_perimeter_normal(self):
        self.assertEqual(square.perimeter(6), 24)


class CircleTestCase(unittest.TestCase):
    # 8
    def test_circle_area_normal(self):
        self.assertAlmostEqual(circle.area(3), math.pi * 9)

    # 9
    def test_circle_area_zero(self):
        self.assertEqual(circle.area(0), 0)

    # 10
    def test_circle_perimeter_normal(self):
        self.assertAlmostEqual(circle.perimeter(5), 10 * math.pi)


class TriangleTestCase(unittest.TestCase):
    # 11
    def test_triangle_area_normal(self):
        self.assertEqual(triangle.area(10, 4), 20)

    # 12
    def test_triangle_area_zero_height(self):
        self.assertEqual(triangle.area(10, 0), 0)

    # 13
    def test_triangle_perimeter_normal(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)


if __name__ == "__main__":
    unittest.main()