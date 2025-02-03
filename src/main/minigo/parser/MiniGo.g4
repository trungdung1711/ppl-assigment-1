grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language=Python3;
}


// LEXER RULES

// TOKENS
/* 
    - identifiers, 
    - keywords, 
    - operators, 
    - separators, 
    - literals
*/

/* 
    identifiers:
    - variable names
    - constant names
    - type names
    - function names
    - other user-defined elements
*/
ID                  : [a-zA-Z_] [a-zA-Z0-9_]*;


SINGLE_LINE_COMMENT : '//' ~[\r\n]* -> skip ;

MULTI_LIME_COMMENT  :  '/*' (MULTI_LIME_COMMENT | ~[/*])*  '*/' -> skip;

// blanks, tabs, formfeeds, carriage returns and newlines
WHITESPACE          : [ \t\f\r]+    -> skip ;
NEWLINE             : '\n'          -> skip ;

ERROR_CHAR: .;
ILLEGAL_ESCAPE:.;
UNCLOSE_STRING:.;
// -------------------------------------------


// PARSER RULES
// program             : declaration+ EOF;

// declaration         : constant_declaration
//                     | variable_declaration
//                     | type_declaration      // struct or interface
//                     | function_declaration;

// test only identifiers
program                : ID+ EOF;
// -------------------------------------------