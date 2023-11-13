import unittest
from math_quiz import function_A, function_B, function_C


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = function_A(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        for _ in range(1000):
             operator= function_B
             self.assertIn(operator,['+','-','*'])
        pass

    def test_function_C(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (2, 3, '+', '2+3',5),
                (4, 1, '-', '4-1',3),
                (8, 5, '*', '8*5',40),
            
            
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                 problem, answer = function_C(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)
            pass

if __name__ == "__main__":
    unittest.main()
