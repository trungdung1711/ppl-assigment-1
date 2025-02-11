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
ASS                     : ':=' ;
DOUBLE_EQUAL            : '==' ;
NOT_EQUAL               : '!=' ;
LESS_THAN_OR_EQUAL      : '<=' ;
GREATER_THAN_OR_EQUAL   : '>=' ;
// shorter rule
ADD                     : '+' ;
SUB                     : '-' ;
MUL                     : '*' ;
DIV                     : '/' ;
MOD                     : '%' ;
EQUAL                   : '=' ;
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
COLON                   : ':' ;
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
    fragment INTEGER            : DIGIT+ ;
    fragment FRACTION           : DIGIT+ ;
    fragment EXPONENT           : [eE] [+-]? DIGIT+ ;
STRING_LITERAL          : '"' (~["\\] | ESCAPE_SEQUENCE)* '"';
    fragment ESCAPE_SEQUENCE    : '\\' [ntr"\\];
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
// Write the grammar using BNF not EBNF
program             : declaration+ EOF
                    ;

declaration         : constant_declaration
                    | variable_declaration
                    | type_declaration      // struct or interface
                    | function_declaration
                    ;
    type_declaration    : struct_declaration
                        | interface_declaration
                        ;
        struct_declaration  : TYPE struct_name STRUCT LCB property_declaration_list RCB statement_end
                            ;
            struct_name             : ID
                                    ;
            property_declaration_list   : property_declaration property_declaration_list
                                        | property_declaration
                                        ;
                property_declaration        : property_name type statement_end
                                            ;
                    property_name               : ID
                                                ;
        interface_declaration   : TYPE interface_name INTERFACE LCB method_declaration_list RCB statement_end
                                ;
            interface_name          : ID
                                    ;
            // can it be empty list ???
            method_declaration_list : method_declaration method_declaration_list
                                    | method_declaration
                                    ;
                method_declaration      : function_name LP parameter_list RP type statement_end
                                        | function_name LP parameter_list RP statement_end
                                        ;

    // not the same as C/C++ when the declaration can be separated from function definition
    function_declaration: function_definition
                        ;
        function_definition : normal_function_definition
                            | method_definition
                            ;
            normal_function_definition  : function_header function_body 
                                        ;
                function_header             : FUNC function_name LP parameter_list RP type
                                            | FUNC function_name LP parameter_list RP
                                            ;
                    function_name               : ID
                                                ;
                    parameter_list              : parameter_prime
                                                | ;
                        parameter_prime             : parameter COMMA parameter_prime
                                                    | parameter
                                                    ;
                            // cause ambiguity, but solved based on ANTLR ordering rule
                            parameter                   : name_type
                                                        | same_type_list
                                                        ;
                                same_type_list          : name_list type
                                                        ;
                                    name_list               : name COMMA name_list
                                                            | name
                                                            ;
                                        name                    : ID
                                                                ;
                                name_type                   : name type
                                                                ;
                function_body                   : block
                                                ;
            method_definition           : method_header function_body
                                        ;
                method_header               : FUNC LP receiver RP function_name LP parameter_list RP type
                                            | FUNC LP receiver RP function_name LP parameter_list RP
                                            ;
                    receiver                    : name type
                                                ; 

// it doesn't contain function_declaration, thus a block should have multiple statements
statement           : variable_declaration
                    | constant_declaration
                    | assignment_statement
                    | if_statement
                    | for_statement
                    | break_statement
                    | continue_statement
                    | call_statement
                    | return_statement
                    ;
    // variable_declaration    : VAR variable_name type? initialisation? statement_end;
    variable_declaration    : VAR variable_name type initialisation statement_end
                            | VAR variable_name type                statement_end
                            | VAR variable_name      initialisation statement_end
                            | VAR variable_name                     statement_end
                            ;
        variable_name           : ID
                                ;
        type                    : primitive_type     // representing type of variable
                                | composite_type     // can be type of Struct or Interface (user defined)
                                | array_type
                                ;
            primitive_type          : INT
                                    | FLOAT
                                    | BOOLEAN
                                    | STRING
                                    ;
            // parser would allow wrong type, but not the case of semantic analysis
            composite_type          : ID
                                    ;
            // array_type              : dimension_list (primitive_type | composit_type);
            // should be the expression while the semantic analysis would reject the incorrect one
            // based on the MiniGo specification:
            // - only allow integer_literal and constant only
            // - different from array indexing in expression actually
            array_type              : dimension_list primitive_type 
                                    | dimension_list composite_type
                                    ;
                dimension_list          : dimension dimension_list 
                                        | dimension
                                        ;
                    dimension               : LB integer_literal RB
                                            | LB constant        RB
                                            ;
                        // the parser cannot determine 
                        // whether an identifier actually refers to a constant
                        constant                : ID 
                                                ;
        // value must be computable at compile time
        initialisation          : EQUAL expression
                                ;
            expression              : expression OR ex1
                                    | ex1
                                    ;
                ex1                     : ex1 AND ex2
                                        | ex2 
                                        ;
                    ex2                     : ex2 relational_operator ex3
                                            | ex3
                                            ;
                        relational_operator     : DOUBLE_EQUAL
                                                | NOT_EQUAL
                                                | LESS_THAN
                                                | LESS_THAN_OR_EQUAL
                                                | GREATER_THAN
                                                | GREATER_THAN_OR_EQUAL
                                                ;
                        ex3                     : ex3 binary_add_sub ex4
                                                | ex4
                                                ;
                            binary_add_sub          : ADD
                                                    | SUB
                                                    ;
                            ex4                     : ex4 mul_div_mod ex5
                                                    | ex5
                                                    ;
                                mul_div_mod             : MUL
                                                        | DIV
                                                        | MOD
                                                        ;
                                ex5                     : unary_not_sub ex5
                                                        | ex6
                                                        ;
                                    unary_not_sub           : NOT
                                                            | SUB
                                                            ;
                                    // get the element in the array (expression)
                                    // get the element of the struct type
                                    // call the method of the struct type
                                    ex6                     : ex6 LB expression RB
                                                            | ex6 DOT function_call     // with the receiver before the DOT operator
                                                            | ex6 DOT field_name
                                                            | ex7
                                                            ;
                                        ex7                     : literal
                                                                | variable_name         // can be merged and let semantic analysis to handle??
                                                                | call
                                                                | LP expression RP      // result from other operator
                                                                ;
                                            call                    : function_call
                                                                    // | method_call - already represented by DOT operator
                                                                    ;
                                                function_call           : function_name LP argument_list RP
                                                                        ;
                                                    argument_list           : argument_prime
                                                                            | 
                                                                            ;
                                                        argument_prime          : argument COMMA argument_prime
                                                                                | argument
                                                                                ;
                                                            argument                : expression
                                                                                    ;
                                            literal                 : integer_literal
                                                                    | FLOATING_POINT
                                                                    | STRING_LITERAL
                                                                    | boolean_literal
                                                                    | NIL
                                                                    | array_literal
                                                                    | struct_literal
                                                                    ;
                                                integer_literal         : DECIMAL_INTEGER
                                                                        | BINARY_INTEGER
                                                                        | OCTAL_INTEGER
                                                                        | HEXA_INTEGER
                                                                        ;
                                                boolean_literal         : TRUE
                                                                        | FALSE;
                                                // must always have the [array_type] part
                                                // but inside, it can be 
                                                    // expression (in the case of multiple array): allow array_type
                                                    // not the expression but in the type of LCB
                                                array_literal           : array_type LCB array_element_list RCB
                                                                        ;
                                                    array_element_list      : array_element_prime
                                                                            |
                                                                            ;
                                                        array_element_prime     : array_element COMMA array_element_prime
                                                                                | array_element
                                                                                ;
                                                            // allowing type deduction
                                                            // Take one part of the array_literal
                                                            // array_literal           : [array_type] (LCB element_array_list RCB)
                                                            array_element           : expression                    // which can allow typed array literal
                                                                                    | LCB array_element_list RCB    // allow type deduction
                                                                                    ;
                                                struct_literal          : struct_name LCB struct_element_list RCB
                                                                        ;
                                                    struct_element_list     : struct_element_prime
                                                                            |
                                                                            ;
                                                        struct_element_prime    : struct_element COMMA struct_element_prime
                                                                                | struct_element
                                                                                ;
                                                            struct_element          : field_name COLON expression
                                                                                    ;
                                                                field_name              : ID
                                                                                        ;
        statement_end       : SEMICOLON 
                            | NEWLINE
                            ;
    // different between Go and C/C++
    // In Go, const means "absolutely immutable and evaluable at compile time."
    // Go doesn't allow 
    // var z = 100
	// const m = z + 100
    // -----
    // In C/C++, const only means "this value cannot be changed after initialization," 
    // but it does not have to be evaluable at compile time.
    // In C++, const int y = x + 10; is allowed, but x might change later, causing confusion.
    // note about constexpr
    constant_declaration    : CONST const_name EQUAL value statement_end;
        const_name              : ID;
        // should be a general expression (no need to separate them)
        // Go does not allow const for array, struct, slice, or map types.
        // Valid constant types: int, float, bool, string, complex.
        value                   : expression
                                // | literal_constant-redundant, as expression can be resolve to literal actually
                                ;
            // literal_constant        : integer_literal
            //                         | FLOATING_POINT
            //                         | STRING_LITERAL
            //                         | boolean_literal
            //                         ;
    assignment_statement    : lhs assignment_operator rhs statement_end
                            ;
        // note, we must allow them to be chained together
        // allow expression in []
        // the left hand side is separately defined from the expression
        // only ASS can be changed to declaration if the expression in the right hand side
        // does contain the value
        // the other operator will be rejected by semantic analysis

        // Here, both foo().bar()[1].baz(); and myArray[2][3] use chaining, 
        // but they are not part of expressions. 
        // This means the parser must recognize them without relying on 
        // the normal expression grammar.

        // parse the same as the expression actually
        // lhs                     : lhs DOT field_name
        //                         | lhs LB expression RB
        //                         | scalar_variable
        //                         ;
        lhs                     : expression DOT field_name
                                | expression LB expression RB
                                | scalar_variable
                                ;
            scalar_variable         : ID
                                    ;
        assignment_operator     : ASS       
                                // the only operator, that can be changed from assignment to declaration
                                | ADD_ASS
                                | SUB_ASS
                                | MUL_ASS
                                | DIV_ASS
                                | MOD_ASS
                                ;
        rhs                     : expression
                                ;   // value must be compatible with the type of lhs
    // How about the statement_end which enforces the ending of the statement ???
    // must be check again for correct AST generation
    // may not explicitly represented in AST
    if_statement            : IF LP boolean_expression RP block
                            | IF LP boolean_expression RP block              else 
                            | IF LP boolean_expression RP block else_if_list
                            | IF LP boolean_expression RP block else_if_list else
                            ;
        boolean_expression      : expression
                                ;
        else_if_list            : else_if else_if_list | else_if 
                                ;
            else_if                 : ELSE IF LP boolean_expression RP block
                                    ;
        else                    : ELSE block
                                ;
    /*
        for statement: 
            - basic form
            - form with initialization
            - form for iterating over an array
     */
    for_statement           : basic_for_statement
                            | ini_for_statement
                            | range_for_statement;
        basic_for_statement     : FOR boolean_expression block
                                ;
        ini_for_statement       : FOR ini SEMICOLON condition SEMICOLON update block
                                ;
            // there can be mistake at that point, but I choose to risk
            ini                     : init_assignment
                                    | init_declaration
                                    ;
                init_assignment         : for_lhs assignment_operator rhs
                                        ;
                    for_lhs                 : scalar_variable
                                            ;
                init_declaration        : VAR variable_name type initialisation
                                        | VAR variable_name      initialisation
                                        ;
            condition               : boolean_expression
                                    ;
            update                  : for_lhs assignment_operator rhs
                                    ;
        range_for_statement     : FOR index COMMA value_array ASS RANGE array block
                                ;
            index                   : ID
                                    ;   // if it is an UNDERSCORE character -> may be handled in semantic analysis
            value_array             : ID
                                    ;
            // should be defined as expression
            // element access
            // return from function
            array                   : expression
                                    ;
                                // inside the for_statement handled by semantic analysis (context stack)
    break_statement             : BREAK statement_end
                                ;
    continue_statement          : CONTINUE statement_end
                                ;
    // Here, both foo().bar()[1].baz(); and myArray[2][3] use chaining, 
    // but they are not part of expressions. 
    // This means the parser must recognize them without relying on 
    // the normal expression grammar.
    call_statement              : function_call_statement
                                | method_call_statement
                                ;
        function_call_statement     : function_call statement_end
                                    ;
        // problematic
        method_call_statement       : expression DOT function_call statement_end
                                    ;
    return_statement            : RETURN expression statement_end
                                | RETURN            statement_end
                                ;
/*
    what semantic analysis (semantic checking) do, not the parser's job: 
        - scope
        - type compatible
        - operation is allowed for a type
        - assignment but not declaration -> add to the symbol table
        - scope hierarchy
 */
// -------------------------------------------