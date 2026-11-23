import unittest

from app import greet


class TestGreet(unittest.TestCase):
    def test_greet_default(self):
        result = greet()
        print("Default greeting:", result)
        expected = "Hello, Jenkins!"
        self.assertEqual(result, expected)

    def test_greet_with_name(self):
        name = "BCIT"
        result = greet(name)
        print("Greeting with name:", result)
        expected = "Hello, BCIT!"
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
