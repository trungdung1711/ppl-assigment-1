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

    def test_white_space_being_skipped(self):
        self.assertTrue(TestLexer.checkLexeme(""" \t\f\r\n \t\f\r\n""","""<EOF>""",111))

    def test_single_line_comment_2(self):
        self.assertTrue(TestLexer.checkLexeme("""// \"This is\\ the\\ comment **537%$3^%%$#$^%\nfor""","""for,<EOF>""",112))

    def test_simple_multipline_comment(self):
        self.assertTrue(TestLexer.checkLexeme("""/*This is a\n multiple\n comment*/float""","""float,<EOF>""",113))

    def test_nested_multi_line_comment(self):
        self.assertTrue(TestLexer.checkLexeme("""/*/*nested*/comment/*nested/*nested*/*/*/if""","""if,<EOF>""",114))

    def test_nested_multi_line_comment_with_open_comment(self):
        self.assertTrue(TestLexer.checkLexeme("""/*com/*ment/*ne/*sted*/*/boolean""","""boolean,<EOF>""",115))

    def test_very_complex_comment_and_multi_line_comment(self):
        self.assertTrue(TestLexer.checkLexeme("""
        /*/*comment*/com/*comment*//*comment*//*comment*/ment/*comment*/*/
        /*/*comment*/co/*comment*//*comment*//*comment*/mment/*comment*/*/
        /*comment*//*comment*//*comment*/
        /*comment*//*comment*//*comment*/
        // comment// comment// comment// 
        // comment
        // comment
        // comment
        // comment
        func""","""func,<EOF>""",116))

    def test_(self):
        self.assertTrue(TestLexer.checkLexeme(""" """,""" """,117))

    def test_(self):
        self.assertTrue(TestLexer.checkLexeme(""" """,""" """,118))

    def test_(self):
        self.assertTrue(TestLexer.checkLexeme(""" """,""" """,119))

    def test_(self):
        self.assertTrue(TestLexer.checkLexeme(""" """,""" """,120))

    def test_(self):
        self.assertTrue(TestLexer.checkLexeme(""" """,""" """,121))

    def test_(self):
        self.assertTrue(TestLexer.checkLexeme(""" """,""" """,122))

    def test_(self):
        self.assertTrue(TestLexer.checkLexeme(""" """,""" """,123))

    def test_(self):
        self.assertTrue(TestLexer.checkLexeme(""" """,""" """,124))

    def test_(self):
        self.assertTrue(TestLexer.checkLexeme(""" """,""" """,125))

    def test_(self):
        self.assertTrue(TestLexer.checkLexeme(""" """,""" """,126))

    def test_(self):
        self.assertTrue(TestLexer.checkLexeme(""" """,""" """,127))

    def test_(self):
        self.assertTrue(TestLexer.checkLexeme(""" """,""" """,128))
