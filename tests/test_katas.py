import unittest
import katas
import math


class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertEqual(katas.add(15, 5), 20)
        self.assertEqual(katas.add(-5, 5), 0)
        self.assertEqual(katas.add(-15, 5), -10)

    def test_multiply(self):
        self.assertEqual(katas.multiply(2, 30), 60)
        self.assertEqual(katas.multiply(-2, 30), -60)
        self.assertEqual(katas.multiply(-2, -2), 4)

    def test_power(self):
        self.assertEqual(katas.power(4, 4), 256)
        self.assertRaises(ValueError, katas.power, -1, 0.5)

    def test_factorial(self):
        for i in range(14):
            self.assertEqual(katas.factorial(i), math.factorial(i))

    def test_fibonacci(self):
        fib_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
                    144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946,
                    17711, 28657, 46368, 75025, 121393, 196418, 317811,
                    514229
                    ]
        for index, value in enumerate(fib_list):
            self.assertEqual(katas.fibonacci(index), value)
            self.assertRaises(ValueError, katas.fibonacci, -1)


if __name__ == '__main__':
    unittest.main()
