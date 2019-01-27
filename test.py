import unittest

def fun(x):
    return "test"

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(1), "test")
