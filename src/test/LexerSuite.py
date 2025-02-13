import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    def test_lower_identifier(self):
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))
    
    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab?sVN","ab,ErrorToken ?",102))
    
    def test_keyword_var(self):
        self.assertTrue(TestLexer.checkLexeme("var abc int ;","var,abc,int,;,<EOF>",103))
    
    def test_keyword_func(self):
        self.assertTrue(TestLexer.checkLexeme("""func abc ( ) ""","""func,abc,(,),<EOF>""",104))
    
    def test_single_line_comment(self):
        self.assertTrue(TestLexer.checkLexeme("""//comment""","""<EOF>""",105))

    def test_unrecognized_character(self):
        self.assertTrue(TestLexer.checkLexeme("""$value""","""ErrorToken $""",106))
    
    def test_unclosed_string(self):
        self.assertTrue(TestLexer.checkLexeme(""""this is a string""","""Unclosed string: \"this is a string""",107))

    def test_double_quote_in_string_token(self):
        self.assertTrue(TestLexer.checkLexeme("""\"this string contains \" \"""","""\"this string contains \",Unclosed string: \"""",108))

    def test_replacing_semicolon_1(self):
        self.assertTrue(TestLexer.checkLexeme("""var abc int = 100\n""","""var,abc,int,=,100,;,<EOF>""",109))

    def test_replacing_semicolon_2(self):
        self.assertTrue(TestLexer.checkLexeme("""a := 100-200+500/2.3e12\n""","""a,:=,100,-,200,+,500,/,2.3e12,;,<EOF>""",110))

#       self.assertTrue(TestLexer.checkLexeme(""" """,""" """,110))
