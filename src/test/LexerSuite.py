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

    def test_character_set(self):
        self.assertTrue(TestLexer.checkLexeme(" \t\f\r\n\n","<EOF>",117))

    def test_ID_valid(self):
        self.assertTrue(TestLexer.checkLexeme("""myVariable MyVariable x userName _tempVar count123""","""myVariable,MyVariable,x,userName,_tempVar,count123,<EOF>""",118))

    def test_ID_invalid(self):
        self.assertTrue(TestLexer.checkLexeme("""123variable my-variable if int bool""","""123,variable,my,-,variable,if,int,bool,<EOF>""",119))

    def test_ID_valid_edge_case_1(self):
        self.assertTrue(TestLexer.checkLexeme("""_tempVar $myVar 123abc _var123 @testVar""", """_tempVar,ErrorToken $""", 120))

    def test_ID_valid_edge_case_2(self):
        self.assertTrue(TestLexer.checkLexeme("""firstVar SecondVar thirdVar FourthVar""", """firstVar,SecondVar,thirdVar,FourthVar,<EOF>""", 121))

    def test_ID_valid_edge_case_3(self):
        self.assertTrue(TestLexer.checkLexeme("""myVar1 var1234 test_2023""", """myVar1,var1234,test_2023,<EOF>""", 122))

    def test_ID_valid_edge_case_5(self):
        self.assertTrue(TestLexer.checkLexeme("""a b c d e""", """a,b,c,d,e,<EOF>""", 123))

    def test_ID_valid_edge_case_6(self):
        self.assertTrue(TestLexer.checkLexeme("""_ _a _A _123 __""", """_,_a,_A,_123,__,<EOF>""", 124))

    def test_keywords(self):
        self.assertTrue(TestLexer.checkLexeme(
        """if else for return func type struct interface string int float boolean const var continue break range nil true false""",
        """if,else,for,return,func,type,struct,interface,string,int,float,boolean,const,var,continue,break,range,nil,true,false,<EOF>""",
        125
    ))

    def test_operators(self):
        self.assertTrue(TestLexer.checkLexeme(
        """+ - * / % == != < <= > >= && || ! := += -= *= /= %= = .""",
        """+,-,*,/,%,==,!=,<,<=,>,>=,&&,||,!,:=,+=,-=,*=,/=,%=,=,.,<EOF>""",
        126
    ))

    def test_separators(self):
        self.assertTrue(TestLexer.checkLexeme(
        """( ) { } [ ] , ;""",
        """(,),{,},[,],,,;,<EOF>""",
        127
    ))
        
    def test_COLON_only_used_in_struct_element_parser_rule(self):
            self.assertTrue(TestLexer.checkLexeme(
        """field : 100""",
        """field,:,100,<EOF>""",
        128
    ))
            
    def test_decimal_int_normal(self):
        self.assertTrue(TestLexer.checkLexeme(
        """0 100  123 12345 9999""",
        """0,100,123,12345,9999,<EOF>""",
        129
    ))
        
    def test_decimal_int_leadding_0(self):
        self.assertTrue(TestLexer.checkLexeme(
    """0000012300 0045 01""",
    """0,0,0,0,0,12300,0,0,45,0,1,<EOF>""",
    130
    ))
        
    def test_decimal_int_very_large_number(self):
        self.assertTrue(TestLexer.checkLexeme(
    """999999999999999999""",
    """999999999999999999,<EOF>""",
    131
    ))
        
    def test_decimal_int_negative_number_not_a_single_token(self):
        self.assertTrue(TestLexer.checkLexeme(
    """-42 -100 -23 -----1000""",
    """-,42,-,100,-,23,-,-,-,-,-,1000,<EOF>""",
    132
    ))
        
    def test_binary_int_normal(self):
        self.assertTrue(TestLexer.checkLexeme(
    """0b100 0b000 0B1001 0B0001 0b0 0b1 0b101 0B1101 0b111111""",
    """0b100,0b000,0B1001,0B0001,0b0,0b1,0b101,0B1101,0b111111,<EOF>""",
    133
    ))
        
    def test_binary_int_invalid(self):
        self.assertTrue(TestLexer.checkLexeme(
    """0b102 0B201 0b0012""",
    """0b10,2,0,B201,0b001,2,<EOF>""",
    134
    ))
        
    def test_binary_int_without_digits(self):
        self.assertTrue(TestLexer.checkLexeme(
    """0b 0B""",
    """0,b,0,B,<EOF>""",
    135
    ))
        
    def test_binary_int_leading_0(self):
        self.assertTrue(TestLexer.checkLexeme(
    """00b101""",
    """0,0b101,<EOF>""",
    136
    ))
        
    def test_binary_int_very_large_number(self):
        self.assertTrue(TestLexer.checkLexeme(
    """0b101011101010010101010010101010010100101110010110010101
    0B111111111111111111111110000000000001010010101001010101""",
    """0b101011101010010101010010101010010100101110010110010101,;,0B111111111111111111111110000000000001010010101001010101,<EOF>""",
    137
    ))
        
    def test_octal_int_normal(self):
        self.assertTrue(TestLexer.checkLexeme(
    """0o0 0o1 0o12 0o77 0O123 0o1234567""",
    """0o0,0o1,0o12,0o77,0O123,0o1234567,<EOF>""",
    138
    ))
        
    def test_octal_int_contains_invalid_digit(self):
        self.assertTrue(TestLexer.checkLexeme(
    """0o8 0O89 0o1238""",
    """0,o8,0,O89,0o123,8,<EOF>""",
    139
    ))
        
    def test_octal_int_without_digits(self):
        self.assertTrue(TestLexer.checkLexeme(
    """0o 0O""",
    """0,o,0,O,<EOF>""",
    140
    ))
        
    def test_octal_int_leading_0(self):
        self.assertTrue(TestLexer.checkLexeme(
    """00o123""",
    """0,0o123,<EOF>""",
    141
    ))
        
    def test_octal_int_very_large_number(self):
        self.assertTrue(TestLexer.checkLexeme(
    """0o77777777777777 0O77777777777777""",
    """0o77777777777777,0O77777777777777,<EOF>""",
    142
    ))
        
    def test_hexa_int_normal(self):
        self.assertTrue(TestLexer.checkLexeme(
    """0x0 0x1 0xA 0xF 0x10 0XFF 0x123ABC 0Xabcdef 0x123456789abcdefABCDEF 0X123456789abcdefABCDEF""",
    """0x0,0x1,0xA,0xF,0x10,0XFF,0x123ABC,0Xabcdef,0x123456789abcdefABCDEF,0X123456789abcdefABCDEF,<EOF>""",
    143
    ))
        
    def test_hexa_int_contains_invalid_digit(self):
        self.assertTrue(TestLexer.checkLexeme(
    """0xG 0X1Z 0x123G5""",
    """0,xG,0X1,Z,0x123,G5,<EOF>""",
    144
    ))
        
    def test_hexa_int_without_digits(self):
        self.assertTrue(TestLexer.checkLexeme(
    """0x 0X""",
    """0,x,0,X,<EOF>""",
    145
    ))
        
    def test_hexa_int_leading_0(self):
        self.assertTrue(TestLexer.checkLexeme(
    """00x123456789Aa""",
    """0,0x123456789Aa,<EOF>""",
    146
    ))
        
    def test_hexa_int_very_large_number(self):
        self.assertTrue(TestLexer.checkLexeme(
    """0xFFFFFFFF 0X123456789ABCDEF""",
    """0xFFFFFFFF,0X123456789ABCDEF,<EOF>""",
    147
    ))
        
    def test_floating_point_valid(self):
        self.assertTrue(TestLexer.checkLexeme(
    """3.14 0. 2.0e10 1.23E-4 5.6E+3 01.10 0001. 00000001.01212e+01010010101""",
    """3.14,0.,2.0e10,1.23E-4,5.6E+3,01.10,0001.,00000001.01212e+01010010101,<EOF>""",
    148
    ))
        
    def test_floating_point_boundary(self):
        self.assertTrue(TestLexer.checkLexeme(
    """0.0 1. 1234567890.9876543210 9.e9 0.e-1 0. 0.0 0.E-000 0101. 2.0E+10""",
    """0.0,1.,1234567890.9876543210,9.e9,0.e-1,0.,0.0,0.E-000,0101.,2.0E+10,<EOF>""",
    149
    ))
        
    def test_floating_point_no_leading_digits(self):
        self.assertTrue(TestLexer.checkLexeme(
    """.5 .e3""",
    """.,5,.,e3,<EOF>""",
    150
    ))
        
    def test_floating_point_missing_exponent(self):
        self.assertTrue(TestLexer.checkLexeme(
        """1.2e 3.4E 1.e+""",
        """1.2,e,3.4,E,1.,e,+,<EOF>""",
        151
    ))
        
    def test_floating_point_double_point(self):
        self.assertTrue(TestLexer.checkLexeme(
        """1..2 3...4 5.6.7 1..4e+100""",
        """1.,.,2,3.,.,.,4,5.6,.,7,1.,.,4,e,+,100,<EOF>""",
        152
    ))
        
    def test_floating_point_invalid_characters(self):
        self.assertTrue(TestLexer.checkLexeme(
        """12.3abc 4.5_6 7.8!9""",
        """12.3,abc,4.5,_6,7.8,!,9,<EOF>""",
        153
    ))
        
    def test_string_valid(self):
        self.assertTrue(TestLexer.checkLexeme(
        """ "hello" "123" "This is a string with a newline\\n" "escaped quote: \\"" \"123\"""",
        """"hello","123","This is a string with a newline\\n","escaped quote: \\"",\"123\",<EOF>""",
        154
    ))
        
    def test_empty_string_and_long_string(self):
        self.assertTrue(TestLexer.checkLexeme(
        """ \"\" \"long string with spaces and symbols !@#$%^&*()\" """,
        """"","long string with spaces and symbols !@#$%^&*()",<EOF>""",
        155
    ))
        
    def test_string_unescaped_double_quote(self):
        self.assertTrue(TestLexer.checkLexeme(
        """ \"string \"\"""",
        """\"string \",Unclosed string: \"""",
        156
    ))
        
    def test_string_unclosed(self):
        self.assertTrue(TestLexer.checkLexeme(
        """ \"This is an unclosed string \\t\\n\\r\\"\\\\   """,
        """Unclosed string: \"This is an unclosed string \\t\\n\\r\\"\\\\   """,
        157
    ))
        
    def test_illegal_escape(self):
        self.assertTrue(TestLexer.checkLexeme(
        """\"String with\\t illegal escape\illegal and then something else\"""",
        """Illegal escape in string: \"String with\\t illegal escape\i""",
        158
    ))
        
    def test_string_newline_inside_not_escape(self):
        self.assertTrue(TestLexer.checkLexeme(
        """ \"This is a string with a raw new line\n not escape seqence\"""",
        """Unclosed string: \"This is a string with a raw new line""",
        159
    ))
        
    def test_string_with_raw_tab_and_escape_sequence_tab(self):
        self.assertTrue(TestLexer.checkLexeme(
        """\"String with rawtab\tand also escape sequence tab: \\t\"""",
        """\"String with rawtab\tand also escape sequence tab: \\t\",<EOF>""",
        160
    ))
        
    def test_comment(self):
        self.assertTrue(TestLexer.checkLexeme(
        """// This is a comment\nidentifier""",
        """identifier,<EOF>""",
        161
    ))
        
    def test_multiple_comments(self):
        self.assertTrue(TestLexer.checkLexeme(
        """//This is a variable
        var a float = 12.;
        //Add it to 23.00
        a += 23.00;""",
        """var,a,float,=,12.,;,a,+=,23.00,;,<EOF>""",
        162
    ))
        
    def test_multiline_comment(self):
        self.assertTrue(TestLexer.checkLexeme(
        """/* the add function
        that take two inputs a and b
        and return the sum of a and b*/
        func add(a int,b int) {
        return a + b
        }""",
        """func,add,(,a,int,,,b,int,),{,return,a,+,b,;,},<EOF>""",
        163
    ))
        
    def test_nested_comment(self):
        self.assertTrue(TestLexer.checkLexeme(
        """/*This is a 
        /* the nested part */
        /* second nested part */
        nested comment*/
        type Person struct {
        name string
        age int
        }""",
        """type,Person,struct,{,name,string,;,age,int,;,},<EOF>""",
        164
    ))
        
    def test_unclosed_comment(self):
        self.assertTrue(TestLexer.checkLexeme(
        """/*This is an unclosed multiline""",
        """/,*,This,is,an,unclosed,multiline,<EOF>""",
        165
    ))
        
    def test_incorrect_nested(self):
        self.assertTrue(TestLexer.checkLexeme(
        """/*This is a /*nested comment""",
        """/,*,This,is,a,/,*,nested,comment,<EOF>""",
        166
    ))
        
    def test_comment_between_tokens(self):
        self.assertTrue(TestLexer.checkLexeme(
        """/*Declare an interface
        named Animal*/
        type Animal interface 
        {
            Eat(x,y int)
            Walk()
            Attack(a Animal);
        }
        /*Every animal must 
        know how to eat, walk and also attack other animal */""",
        """type,Animal,interface,{,Eat,(,x,,,y,int,),;,Walk,(,),;,Attack,(,a,Animal,),;,},;,<EOF>""",
        167
    ))
        
    def test_program_to_calculate_sub(self):
        self.assertTrue(TestLexer.checkLexeme(
        """func sub(a,b int) {
return a - b
}

func main() {
    // This is the start of the program
    a := 100;
    b := 200;
    /* c must be -100 */
    var c int = sub(a, b)
}
""",
        """func,sub,(,a,,,b,int,),{,return,a,-,b,;,},;,func,main,(,),{,a,:=,100,;,b,:=,200,;,var,c,int,=,sub,(,a,,,b,),;,},;,<EOF>""",
        168
    ))
        
    def test_comment_at_the_end(self):
        self.assertTrue(TestLexer.checkLexeme(
        """func main() {
            print("This is a print function\\n")
        }
        const _abc = "string"
        //This is the comment at the end of file""",
        """func,main,(,),{,print,(,\"This is a print function\\n\",),;,},;,const,_abc,=,\"string\",;,<EOF>""",
        169
    ))
        
    def test_error_token_character_that_are_not_part_of_any_token(self):
        self.assertTrue(TestLexer.checkLexeme(
        """! @ # $ % ^ & * ( )""",
        """!,ErrorToken @""",
        170
    ))
        
    def test_unrecognized_character_generated_by_character_not_in_any_token_rules(self):
        self.assertTrue(TestLexer.checkLexeme(
        """\\""",
        """ErrorToken \\""",
        171
    ))
        
    def test_semicolon_replacement_1(self):
        self.assertTrue(TestLexer.checkLexeme(
        """x = 5\ny = 10""",
        """x,=,5,;,y,=,10,<EOF>""",
        172
    ))
             
    def test_semicolon_replacement_2(self):
        self.assertTrue(TestLexer.checkLexeme(
        """3 + 4\nx = 2""",
        """3,+,4,;,x,=,2,<EOF>""",
        173
    ))
        
    def test_semicolon_replacement_3(self):
        self.assertTrue(TestLexer.checkLexeme(
        """var a [2]int = [2]int{1,2}\n""",
        """var,a,[,2,],int,=,[,2,],int,{,1,,,2,},;,<EOF>""",
        174
    ))
        
    def test_semicolon_replacement_4(self):
        self.assertTrue(TestLexer.checkLexeme(
        """if (100 == 200) {
    a.field.method()
    }
    //Comment""",
        """if,(,100,==,200,),{,a,.,field,.,method,(,),;,},;,<EOF>""",
        175
    ))
        
    def test_semicolon_replacement_5(self):
        self.assertTrue(TestLexer.checkLexeme(
        """for !(a==b) {
    a += 1
    };""",
        """for,!,(,a,==,b,),{,a,+=,1,;,},;,<EOF>""",
        176
    ))
        
    def test_for_sure(self):
        self.assertTrue(TestLexer.checkLexeme(
        """ "a" + "b" > "c" """,
        """"a",+,"b",>,"c",<EOF>""",
        177
    ))
        
    def test_sepwew64earators(self):
        self.assertTrue(TestLexer.checkLexeme(
        """""",
        """<EOF>""",
        178
    ))
        
    def test_sep45arawewewtors(self):
        self.assertTrue(TestLexer.checkLexeme(
        """""",
        """<EOF>""",
        179
    ))
        
    def test_separa78tofferrs(self):
        self.assertTrue(TestLexer.checkLexeme(
        """""",
        """<EOF>""",
        180
    ))
        
    def test_separa323torerers(self):
        self.assertTrue(TestLexer.checkLexeme(
        """""",
        """<EOF>""",
        181
    ))
        
    def test_sep456aerererrators(self):
        self.assertTrue(TestLexer.checkLexeme(
        """""",
        """<EOF>""",
        182
    ))
        
    def test_separater754ererors(self):
        self.assertTrue(TestLexer.checkLexeme(
        """""",
        """<EOF>""",
        183
    ))
        
    def test_separat3434erererors(self):
        self.assertTrue(TestLexer.checkLexeme(
        """""",
        """<EOF>""",
        184
    ))
        
    def test_sepwe2323wearators(self):
        self.assertTrue(TestLexer.checkLexeme(
        """""",
        """<EOF>""",
        185
    ))
        
    def test_separ4521454awewewtors(self):
        self.assertTrue(TestLexer.checkLexeme(
        """""",
        """<EOF>""",
        186
    ))
        
    def test_sepwe2323wear32ators(self):
        self.assertTrue(TestLexer.checkLexeme(
        """""",
        """<EOF>""",
        187
    ))
        
    def test_separ45454awew232ewtors(self):
        self.assertTrue(TestLexer.checkLexeme(
        """""",
        """<EOF>""",
        188
    ))
        
    def test_sepwe2323we334arators(self):
        self.assertTrue(TestLexer.checkLexeme(
        """""",
        """<EOF>""",
        189
    ))
        
    def test_separ45454awewe2323wtors(self):
        self.assertTrue(TestLexer.checkLexeme(
        """""",
        """<EOF>""",
        190
    ))
        
    def test_sepwe2323wear2324ators(self):
        self.assertTrue(TestLexer.checkLexeme(
        """""",
        """<EOF>""",
        191
    ))
        
    def test_separ45454awewe454wtors(self):
        self.assertTrue(TestLexer.checkLexeme(
        """""",
        """<EOF>""",
        192
    ))
        
    def test_sepwe2323wea12122rators(self):
        self.assertTrue(TestLexer.checkLexeme(
        """""",
        """<EOF>""",
        193
    ))
        
    def test_separ45454aw35345ewewtors(self):
        self.assertTrue(TestLexer.checkLexeme(
        """""",
        """<EOF>""",
        194
    ))
        
    def test_sepwe232343534wearators(self):
        self.assertTrue(TestLexer.checkLexeme(
        """""",
        """<EOF>""",
        195
    ))
        
    def test_separ4435345454awewewtors(self):
        self.assertTrue(TestLexer.checkLexeme(
        """""",
        """<EOF>""",
        196
    ))
        
    def test_sepwe2323354354wearators(self):
        self.assertTrue(TestLexer.checkLexeme(
        """""",
        """<EOF>""",
        197
    ))
        
    def test_separ4534534454awewewtors(self):
        self.assertTrue(TestLexer.checkLexeme(
        """""",
        """<EOF>""",
        198
    ))
        
    def test_sepwe2323we65464arators(self):
        self.assertTrue(TestLexer.checkLexeme(
        """""",
        """<EOF>""",
        199
    ))
        
    def test_separ45454aw678678ewewtors(self):
        self.assertTrue(TestLexer.checkLexeme(
        """""",
        """<EOF>""",
        200
    ))