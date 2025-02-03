import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):


    def test_decimal_integer(self):
        self.assertTrue(TestLexer.checkLexeme("1", "1,<EOF>", 101))
        self.assertTrue(TestLexer.checkLexeme("42", "42,<EOF>", 102))
        self.assertTrue(TestLexer.checkLexeme("12345", "12345,<EOF>", 103))
        self.assertTrue(TestLexer.checkLexeme("0", "0,<EOF>", 104))
        self.assertTrue(TestLexer.checkLexeme("99999999", "99999999,<EOF>", 105))


    def test_binary_integer(self):
        self.assertTrue(TestLexer.checkLexeme("0b0", "0b0,<EOF>", 106))
        self.assertTrue(TestLexer.checkLexeme("0b1", "0b1,<EOF>", 107))
        self.assertTrue(TestLexer.checkLexeme("0b101010", "0b101010,<EOF>", 108))
        self.assertTrue(TestLexer.checkLexeme("0b111111", "0b111111,<EOF>", 109))
        self.assertTrue(TestLexer.checkLexeme("0b11110000", "0b11110000,<EOF>", 110))
        self.assertTrue(TestLexer.checkLexeme("0B1010101010101010", "0B1010101010101010,<EOF>", 111))
        self.assertTrue(TestLexer.checkLexeme("0B1", "0B1,<EOF>", 112))


    def test_octal_integer(self):
        self.assertTrue(TestLexer.checkLexeme("0o0", "0o0,<EOF>", 113))
        self.assertTrue(TestLexer.checkLexeme("0o1", "0o1,<EOF>", 114))
        self.assertTrue(TestLexer.checkLexeme("0o1234567", "0o1234567,<EOF>", 115))
        self.assertTrue(TestLexer.checkLexeme("0o7654321", "0o7654321,<EOF>", 116))
        self.assertTrue(TestLexer.checkLexeme("0O1234567", "0O1234567,<EOF>", 117))
        self.assertTrue(TestLexer.checkLexeme("0O7654321", "0O7654321,<EOF>", 118))
        self.assertTrue(TestLexer.checkLexeme("0o12", "0o12,<EOF>", 119))
        self.assertTrue(TestLexer.checkLexeme("0O77", "0O77,<EOF>", 120))

    
    def test_hex_integer(self):
        self.assertTrue(TestLexer.checkLexeme("0x0", "0x0,<EOF>", 121))
        self.assertTrue(TestLexer.checkLexeme("0x1", "0x1,<EOF>", 122))
        self.assertTrue(TestLexer.checkLexeme("0x1234567890abcdef", "0x1234567890abcdef,<EOF>", 123))
        self.assertTrue(TestLexer.checkLexeme("0x1234567890ABCDEF", "0x1234567890ABCDEF,<EOF>", 124))
        self.assertTrue(TestLexer.checkLexeme("0X1234567890abcdef", "0X1234567890abcdef,<EOF>", 125))
        self.assertTrue(TestLexer.checkLexeme("0X1234567890ABCDEF", "0X1234567890ABCDEF,<EOF>", 126))
        self.assertTrue(TestLexer.checkLexeme("0x12", "0x12,<EOF>", 127))
        self.assertTrue(TestLexer.checkLexeme("0X77", "0X77,<EOF>", 128))
        self.assertTrue(TestLexer.checkLexeme("0x1234567890abcdefABCDEF", "0x1234567890abcdefABCDEF,<EOF>", 129))
        self.assertTrue(TestLexer.checkLexeme("0x1A", "0x1A,<EOF>", 130))
        self.assertTrue(TestLexer.checkLexeme("0XFF", "0XFF,<EOF>", 131))


    def test_floating_point_literal(self):
        self.assertTrue(TestLexer.checkLexeme("0.0", "0.0,<EOF>", 132))
        self.assertTrue(TestLexer.checkLexeme("0.1", "0.1,<EOF>", 133))
        self.assertTrue(TestLexer.checkLexeme("0.1234567890", "0.1234567890,<EOF>", 134))
        self.assertTrue(TestLexer.checkLexeme("0.1234567890e-123", "0.1234567890e-123,<EOF>", 135))
        self.assertTrue(TestLexer.checkLexeme("0.1234567890e+123", "0.1234567890e+123,<EOF>", 136))
        self.assertTrue(TestLexer.checkLexeme("0.1234567890e123", "0.1234567890e123,<EOF>", 137))
        self.assertTrue(TestLexer.checkLexeme("0.1234567890E-123", "0.1234567890E-123,<EOF>", 138))
        self.assertTrue(TestLexer.checkLexeme("0.1234567890E+123", "0.1234567890E+123,<EOF>", 139))
        self.assertTrue(TestLexer.checkLexeme("0.1234567890E123", "0.1234567890E123,<EOF>", 140))
        self.assertTrue(TestLexer.checkLexeme("0.1234567890e-123", "0.1234567890e-123,<EOF>", 141))
        self.assertTrue(TestLexer.checkLexeme("0.1234567890e+123", "0.1234567890e+123,<EOF>", 142))
        self.assertTrue(TestLexer.checkLexeme("0.1234567890e123", "0.1234567890e123,<EOF>", 143))
        self.assertTrue(TestLexer.checkLexeme("0.1234567890E-123", "0.1234567890E-123,<EOF>", 144))
        self.assertTrue(TestLexer.checkLexeme("0.1234567890E+123", "0.1234567890E+123,<EOF>", 145))
        self.assertTrue(TestLexer.checkLexeme("0.1234567890E123", "0.1234567890E123,<EOF>", 146))
        self.assertTrue(TestLexer.checkLexeme("0.1234567890e-123", "0.1234567890e-123,<EOF>", 147))
        self.assertTrue(TestLexer.checkLexeme("3.14", "3.14,<EOF>", 148))
        self.assertTrue(TestLexer.checkLexeme("3.14e-123", "3.14e-123,<EOF>", 149))
        self.assertTrue(TestLexer.checkLexeme("0.", "0.,<EOF>", 150))
        self.assertTrue(TestLexer.checkLexeme("2.", "2.,<EOF>", 151))
        '''Allowing leading zeros in the INTEGER and FRACTION and EXPONENT part''' 
        self.assertTrue(TestLexer.checkLexeme("000123.000230045E0001", "000123.000230045E0001,<EOF>", 152))
        self.assertTrue(TestLexer.checkLexeme("012.e+012", "012.e+012,<EOF>", 153))
        self.assertTrue(TestLexer.checkLexeme("000.", "000.,<EOF>", 154))
        '''Full leading zeros'''
        self.assertTrue(TestLexer.checkLexeme("000.000E+000", "000.000E+000,<EOF>", 155))


    def test_string_literal(self):
        self.assertTrue(TestLexer.checkLexeme("\"\"", "\"\",<EOF>", 156))
        self.assertTrue(TestLexer.checkLexeme("\"a\"", "\"a\",<EOF>", 157))
        self.assertTrue(TestLexer.checkLexeme("\"abc\"", "\"abc\",<EOF>", 158))
        self.assertTrue(TestLexer.checkLexeme("\"abc def\"", "\"abc def\",<EOF>", 159))
        self.assertTrue(TestLexer.checkLexeme("\"abc def 123\"", "\"abc def 123\",<EOF>", 160))
        self.assertTrue(TestLexer.checkLexeme("\"abc def 123 xyz\"", "\"abc def 123 xyz\",<EOF>", 161))
        self.assertTrue(TestLexer.checkLexeme("\"abc def 123 xyz 456\"", "\"abc def 123 xyz 456\",<EOF>", 162))
        '''with escape characters'''
        self.assertTrue(TestLexer.checkLexeme("\"\\n\"", "\"\\n\",<EOF>", 163))
        self.assertTrue(TestLexer.checkLexeme("\"\\t\"", "\"\\t\",<EOF>", 164))
        self.assertTrue(TestLexer.checkLexeme("\"\\r\"", "\"\\r\",<EOF>", 165))
        self.assertTrue(TestLexer.checkLexeme("\"\\\\\"", "\"\\\\\",<EOF>", 166))
        '''with actual new line and actual tab'''
        self.assertTrue(TestLexer.checkLexeme("\"abcdef\nabcdef\"", "\"abcdef\nabcdef\",<EOF>", 167))
        self.assertTrue(TestLexer.checkLexeme("\"abcdef\tabcdef\"", "\"abcdef\tabcdef\",<EOF>", 168))
        self.assertTrue(TestLexer.checkLexeme("\"123\"", "\"123\",<EOF>", 169))
        '''with escape sequences + characters'''
        self.assertTrue(TestLexer.checkLexeme("\"Hello World!\"", "\"Hello World!\",<EOF>", 170))
        self.assertTrue(TestLexer.checkLexeme("\"A string with a new line\\n\"", "\"A string with a new line\\n\",<EOF>", 171))
        
        