import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):


    def test_decimal_integer(self):
        self.assertTrue(TestLexer.test("1", "1,<EOF>", 101))
        self.assertTrue(TestLexer.test("42", "42,<EOF>", 102))
        self.assertTrue(TestLexer.test("12345", "12345,<EOF>", 103))
        self.assertTrue(TestLexer.test("0", "0,<EOF>", 104))