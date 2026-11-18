import unittest
from student import calculate_total, calculate_average, get_grade

class TestStudent(unittest.TestCase):

    def test_total(self):
        self.assertEqual(calculate_total(80, 75, 90), 245)

    def test_average(self):
        self.assertAlmostEqual(calculate_average(80, 75, 90), 81.6666667)

    def test_grade(self):
        self.assertEqual(get_grade(90), "A")

if _name_ == "_main_":
    unittest.main()