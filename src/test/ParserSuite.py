import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: void main() {} """
        input = """func main() {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test_more_complex_program(self):
        """More complex program"""
        input = """func foo () {
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    
    def test_wrong_miss_close(self):
        """Miss ) void main( {}"""
        input = """func main({}"""
        expect = "Error on line 1 col 11: {"
        self.assertTrue(TestParser.checkParser(input,expect,203))

    def test_wrong_variable(self):
        input = """var int\n"""
        expect = "Error on line 1 col 5: int"
        self.assertTrue(TestParser.checkParser(input,expect,204))

    def test_wrong_index(self):
        input = """var i\n"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))
    
    def test_complex_program(self):
        input = """var a int = 12345\n"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))

    def test_wrong_declaration_structure(self):
        input = """vars val int = 100\n"""
        expect = "Error on line 1 col 1: vars"
        self.assertTrue(TestParser.checkParser(input,expect,207))

    def test_unclosed_block_function(self):
        input = """func function() int{"""
        expect = "Error on line 1 col 21: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,208))

    def test_very_complex_program(self):
        input = """func main()   {var a int = 100\na := a * 100 -200 + 4.5 - "string\\n"\n}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,209))

    def test_replacing_semicolon(self):
        input = """func main() {if (a * 100 -200 == b/c){fmt.print(dbv);}}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))

'''
        input = """ """
        expect = ""
        self.assertTrue(TestParser.checkParser(input,expect,211))
'''