import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_lower_identifier(self):
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))
    

    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.checkLexeme("Variable","Variable,<EOF>",102))

    
    def test_valid_identifiers(self):
        self.assertTrue(TestLexer.checkLexeme("x", "x,<EOF>", 103))
        self.assertTrue(TestLexer.checkLexeme("userName", "userName,<EOF>", 104))
        self.assertTrue(TestLexer.checkLexeme("tempVar", "tempVar,<EOF>", 105))
        self.assertTrue(TestLexer.checkLexeme("count123", "count123,<EOF>", 106))
        self.assertTrue(TestLexer.checkLexeme("_myVariable", "_myVariable,<EOF>", 107))
        self.assertTrue(TestLexer.checkLexeme("A_Var_Name", "A_Var_Name,<EOF>", 108))
        self.assertTrue(TestLexer.checkLexeme("longIdentifierName123", "longIdentifierName123,<EOF>", 109))


    def test_identifiers_with_underscores(self):
        self.assertTrue(TestLexer.checkLexeme("_", "_,<EOF>", 110))  # Single underscore (should be valid)
        self.assertTrue(TestLexer.checkLexeme("_leadingUnderscore", "_leadingUnderscore,<EOF>", 111))  # Starts with _
        self.assertTrue(TestLexer.checkLexeme("trailingUnderscore_", "trailingUnderscore_,<EOF>", 112))  # Ends with _
        self.assertTrue(TestLexer.checkLexeme("multiple___underscores", "multiple___underscores,<EOF>", 113))  # Multiple underscores in middle


    def test_mixed_case_identifiers(self):
        self.assertTrue(TestLexer.checkLexeme("camelCase", "camelCase,<EOF>", 114))  # Camel case
        self.assertTrue(TestLexer.checkLexeme("PascalCase", "PascalCase,<EOF>", 115))  # Pascal case
        self.assertTrue(TestLexer.checkLexeme("snake_case", "snake_case,<EOF>", 116))  # Snake case
        self.assertTrue(TestLexer.checkLexeme("MIXED_Case123", "MIXED_Case123,<EOF>", 117))  # Upper + lower + digits


    def test_long_identifiers(self):
        self.assertTrue(TestLexer.checkLexeme("averyveryverylongidentifiername", "averyveryverylongidentifiername,<EOF>", 131))  # Very long name
        self.assertTrue(TestLexer.checkLexeme("a" * 255, "a" * 255 + ",<EOF>", 118))  # 255-character identifier (assuming no limit)


    def test_identifiers_with_numbers(self):
        self.assertTrue(TestLexer.checkLexeme("var123", "var123,<EOF>", 119))  # Ends with number
        self.assertTrue(TestLexer.checkLexeme("id_42_name", "id_42_name,<EOF>", 120))  # Contains number
        self.assertTrue(TestLexer.checkLexeme("_123abc", "_123abc,<EOF>", 121))  # Starts with _ then number


    def test_only_one_char_identifiers(self):
        self.assertTrue(TestLexer.checkLexeme("a", "a,<EOF>", 122))
        self.assertTrue(TestLexer.checkLexeme("b", "b,<EOF>", 123))
        self.assertTrue(TestLexer.checkLexeme("c", "c,<EOF>", 124))
        self.assertTrue(TestLexer.checkLexeme("A", "A,<EOF>", 125))
        self.assertTrue(TestLexer.checkLexeme("_", "_,<EOF>", 126))