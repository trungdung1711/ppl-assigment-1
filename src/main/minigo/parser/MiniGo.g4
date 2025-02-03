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


// ANTLR prioritizes rules based on order


// LEXER RULES

// TOKENS
/* 
    - keywords, 
    - identifiers, 
    - operators, 
    - separators, 
    - literals
*/

/*
    keywords:
    - reserved words
    - cannot be used as identifiers
*/
INTERFACE           : 'interface' ;
CONTINUE            : 'continue' ;
BOOLEAN             : 'boolean' ;
RETURN              : 'return' ;
STRUCT              : 'struct' ;
STRING              : 'string' ;
FLOAT               : 'float' ;
CONST               : 'const' ;
BREAK               : 'break' ;
RANGE               : 'range' ;
FALSE               : 'false' ;
TRUE                : 'true' ;
FUNC                : 'func' ;
TYPE                : 'type' ;
ELSE                : 'else' ;
FOR                 : 'for' ;
INT                 : 'int' ;
VAR                 : 'var' ;
NIL                 : 'nil' ;
IF                  : 'if' ;

/*
    operators:
    - +, -, *, /, %
    - ==, !=, <, <=, >, >=
    - &&, ||, !
    - =, +=, -=, *=, /=, %=
    - .
 */
// longer rule
AND                     : '&&' ;
OR                      : '||' ;
ADD_ASS                 : '+=' ;
SUB_ASS                 : '-=' ;
MUL_ASS                 : '*=' ;
DIV_ASS                 : '/=' ;
MOD_ASS                 : '%=' ;
EQUALITY                : '==' ;
NOT_EQUAL               : '!=' ;
LESS_THAN_OR_EQUAL      : '<=' ;
GREATER_THAN_OR_EQUAL   : '>=' ;
// shorter rule
ADD                     : '+' ;
SUB                     : '-' ;
MUL                     : '*' ;
DIV                     : '/' ;
MOD                     : '%' ;
ASSIGNMENT              : '=' ;
LESS_THAN               : '<' ;
GREATER_THAN            : '>' ;
DOT                     : '.' ;
NOT                     : '!' ;

/*
    separators:
    - (, )
    - {, }
    - [, ]
    - ,
    - ;
 */
LP                      : '(' ;
RP                      : ')' ;
LB                      : '[' ;
RB                      : ']' ;
LCB                     : '{' ;
RCB                     : '}' ;
COMMA                   : ',' ;
SEMICOLON               : ';' ;

/*
    literals:
    - integer literal
        + decimal
        + binary
        + octal
        + hexa
    - floating-point literal
    - string literal
    - boolean literal
    - nil literal
*/
DECIMAL_INTEGER         : '0' | [1-9] [0-9]* ;
BINARY_INTEGER          : '0' [bB] [0-1]+ ;
OCTAL_INTEGER           : '0' [oO] [0-7]+ ;
HEXA_INTEGER            : '0' [xX] [0-9a-fA-F]+ ;
FLOATING_POINT          : INTEGER DOT FRACTION? EXPONENT? ;
    fragment INTEGER        : DIGIT+ ;
    fragment FRACTION       : DIGIT+ ;
    fragment EXPONENT       : [eE] [+-]? DIGIT+ ;

/* 
    identifiers:
    - variable names
    - constant names
    - type names
    - function names
    - other user-defined elements
*/
ID                     : (LETTER | UNDERSCORE) (LETTER | DIGIT | UNDERSCORE)*;
    fragment LETTER         : [a-zA-Z] ;
    fragment DIGIT          : [0-9] ;
    fragment UNDERSCORE     : '_' ;

// Comments
SINGLE_LINE_COMMENT : '//' ~[\r\n]* -> skip ;
MULTI_LIME_COMMENT  :  '/*' (MULTI_LIME_COMMENT | ~[/*])*  '*/' -> skip;

// blanks, tabs, formfeeds, carriage returns and newlines
WHITESPACE          : [ \t\f\r]+    -> skip ;
NEWLINE             : '\n'          -> skip ;

// Handling errors
ERROR_CHAR: .;
ILLEGAL_ESCAPE:.;
UNCLOSE_STRING:.;
// -------------------------------------------


// PARSER RULES
program             : declaration+ EOF;

declaration         : constant_declaration
                    | variable_declaration
                    | type_declaration      // struct or interface
                    | function_declaration;
// -------------------------------------------