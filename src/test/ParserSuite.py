import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: void main() {} """
        input = """func main() {
            for var i int = 0;  i < 100 ; i+=1 {
                scanner.printLn(i)
            };
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))


    def test_more_complex_program(self):
        """More complex program"""
        input = """func foo () {
            for (a[5][2].method() && a) || b {
                var i int = 100.23E+100
                result := s.killTheEarch(i)
                s.print(result)
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    

    def test_wrong_miss_close(self):
        """Miss ) void main( {}"""
        input = """func main({}"""
        expect = "Error on line 1 col 11: {"
        self.assertTrue(TestParser.checkParser(input,expect,203))


    def test_the_fourth_case_of_variable_declaration(self):
        input = """func main() {
            var variable;
            // There is no type or initialisation in this case
        };"""
        expect = "Error on line 2 col 25: ;"
        self.assertTrue(TestParser.checkParser(input,expect,204))


    def test_3_cases_of_variable_declaration(self):
        input = """func main() {
            var a = [3]int{1,2,3}
            var b int;
            var c string = "This is a string \\t"
            return a + b + c
        };"""
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
        input = """func main()   {var a int = 100\na := a * 100 -200 + 4.5 - "string\\n"\n};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,209))


    def test_replacing_semicolon(self):
        input = """func main() {if (a * 100 -200 == b/c){fmt.print(dbv);};};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))


    def test_simple_program_with_newline_replacement(self):
        input = """const PI = 3.1415
const NUM = 10
func add(a, b float) {
    var c float = a + b;
    return c
}
    type Animal interface {
        Eat(food [100]int)
        Attack (a Animal)
    };

    type Dog struct {
        name string
        age int
        leg_number int
        owner int
    }

    func main() {
        var a [2]int = [2]int{1,2}
    }
    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))


    def test_that_i_have_stolen(self):
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for var b [2]ID = (1. + 2.e+100) / 4;  foo().a.b(); i := 1 {
                                            return something(); 
                                        }
                                               var list_2D [2][2]int = [2][2] int{{1,2},{3,4}}
                                    };""","successful",212))
        

    def test_to_check_semi_at_the_end_replacement(self):
        self.assertTrue(TestParser.checkParser("""    
            type Calculator interface {Reset()}
""","Error on line 2 col 47: }", 213))
        

    def test_to_check_declaration_with_var_is_wrong(self):
        self.assertTrue(TestParser.checkParser("""    
            type Calculator struct {
                a int = 2;       
            }
""","Error on line 3 col 23: =", 214))
        

    def test_interface_declaration(self):
        self.assertTrue(TestParser.checkParser("""    
            type Calculator interface {
                Add(x int,c,d ID); Add() int
        }
""","successful", 215))
        

    def test_if_else_statement(self):
        self.assertTrue(TestParser.checkParser("""    
            func test_if_else() {
                if (x > 101) {return; } 
                if (x > 102.) {
                  return; 
                } else if (x == 10) {
                    var z str;
                } else if (x == 123){
                    var z ID;
                }
            }
        ""","successful", 216))


    def test_interface_that_contains_nothing(self):
        self.assertTrue(TestParser.checkParser("""
            type Calculator interface {
                                        
                AddMany(x, y, z int, a float) int;
                AddAll(x, y int, a, b, c, d string) int;
                Sub(a,b  ,c,d int, m int, n float, x,y,z,t string)
                                        
                Hello_world(name string,a,b,c,d,e float);
                                        
            }
            type Weapon interface {}                                                                       
        ""","Error on line 11 col 36: }", 217))


    def test_statements_inside_block_at_the_end_of_the_function_there_must_be_a_semi(self):
        self.assertTrue(TestParser.checkParser("""
                                    func something() {
                                        ab += "string\\\\";
                                        ab -= a[2].b().c().d().e().f(----e).method(a[1])[1][1][1][1];
                                        ab /= 2.0e34
                                        ab *= 2.
                                        ab %= 0.2E89;       
                                    };""","successful", 218))
        

    def test_function_and_the_left_hand_side(self):
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        a.c[2].e[3].m.foo().arr[2][3] += 2;       
                                    };""","successful", 219))


    def test_left_hand_side_cant_be_a_function_call(self):
        self.assertTrue(TestParser.checkParser("""
                                    func doo() {
                                        a.mov() += 2;       
                                    };""","Error on line 3 col 49: +=", 220))
        

    def test_inside_a_block_there_are_statements_not_a_nested_block_because_semi_replacement_could_fail(self):
        input = """func main() {
            for _ , arr := range a.foo().boo().too().a[1].list {
                arr.getName();
                {
                    // This is a nested block -> it is not allowed
                }
            }
            return;
        };"""
        expect = """Error on line 4 col 17: {"""
        self.assertTrue(TestParser.checkParser(input,expect,221))


    def test_array_literal_fixing(self):
        self.assertTrue(TestParser.checkParser("""
                                            const a = [sometjomg][2][C]int{{{1.,2.,3.}}, 0x1234a, 364.23, nil, false,nil, 0O1273645, 34.e+2345}                              
                                        ""","successful", 222))
        

    def test_array_literal(self):
        input = """
const NAME = [2]Name{A,B,C,{1,2,3,0b001},Student{name: "Trung Dung", ID: "2210573"},"string"};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,223))


    def test_variable_declaration_expression(self):
        self.assertTrue(TestParser.checkParser("""    
            var z Type = a.a.m.m.d.a.a.b.c.array[2][2][3][4].c[2].foo(1,);                         
        ""","Error on line 2 col 73: )", 224))


    def test_literal_1(self):
        input = """
// comment
/* comment */
const NUM = 1;
const ARR = [2]int{1,2}
func main() {
    // utility is a type used for different uses in 
    // a program, like getting the size of the array
    // or list all element of the array
    var util Utility = Utility{}
    var i int = 0
    for i < util.size(ARR) {
        ARR[i] += NUM;
    }
    util.list(ARR);
};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,225))


    def test_full_executable_program_including_decl_stmt_and_more(self):
        input = """// constant declaration
const NAME = \"HCMUT\"
const ID = \"2210573\"
const MASK = 0B1111111111111111;

// variable declaration
var a Student = Student{name : "Dung", age : 18}
var b string;
var c = [4][4]int{{1,2,3,4},{5,6,7,8},{9,10,11,12},{13,14,15,15}}
// var d;

//type declaration
//struct
type Student struct {
    name string
    age int
    HBKK [8]Money
    ID string
    friends [N]Student
}


//interface
type Human interface {
    eat(food Food);
    walk();
    attack(human Human)
    giveBirth() Human
    makeCraft(things [10]Wood, e Axe, a,b,c,d string);
};


// function declaration
// normal
func add (a int, b int) int {
    return a + b;
}

func getRandomInt(seed int) int {
    return (7564+8474-(seed%273)*(seed+123-34))/(seed%(seed*100))
}
// method
func (s Student) doExercise(e Exercise) {
    return e.done()
}

func (s Student) getId() {
    return s.ID;
}

func (s Student) getName() string {
    return s.name;
}

//main
func main() {
    // inside the block, there are statements
    // variable declaration
    var i int = 1;
    // constant declaration
    const PI = 3.1415
    // assignment statement, RHS is expression
    i := 2
    // if statement
    // else_if_list and else_block is optional
    if (i > 100) {
        var s Student = Student{name: "Dung", age : 20};
    } else if (i < 1) {
        // let the student do the homework
        var e Exercise = Exercise{q1:"1+1",q2:"2*2"}
        s.doExercise(e)
    } else {
        // return the student's name
        return s.getName();
    }
    // for statement
    //basic, ini, range
    // struct literal -> forget type -> 
    // parser would think that is a array interal
    // list of element -> : which is error
    class := [35]Student{Student{name: "Dung", ID: "2210573"}}
    for i:=0;i<10;i+=1 {
        // print the name of the class
        class[i].getName();
        // use of break
        if (class[i].getId() == "2210573") {
            // if the student have ID as 2210573
            break;
        }
    }

    //call statement
    // argument list is not parameter list
    // function call
    number1 := 100
    number2 := 200
    add (number1 + add(number1, number2), number2+number1)
    sub (number1, number2+number2)

    /*method call*/
    a.b[10].foo().field[number1 + number2][number1 - number2].foo()

    //return 
    return (1 + 1)-(2+2)/78%12 - a.b.c.d.e.foo();
    return 
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,226))


    def test_nested_struct(self):
        input = """type Address struct {
        city string;
        postalCode int;
    }

    type Person struct {
        name string;
        age int;
        address Address;
    }
    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 227))


    def test_complex_interface(self):
        input = """type Animal interface {
        eat(food string);
        sleep(hours int);
        run(speed float);
        sound() string;
    }
    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 228))


    def test_function_multiple_parameters(self):
        input = """func calculate(a int, b float, c string, x,y,z,t,m,p,q boolean) float {
        return a + b * 2.5;
    };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 229))



    def test_recursive_function_false_expression(self):
        input = """func factorial(n int) int {
        if (n = 0) {
            return 1;
        }
        return n * factorial(n - 1);
    }
    """
        expect = "Error on line 2 col 15: ="
        self.assertTrue(TestParser.checkParser(input, expect, 230))


    def test_method_returning_struct(self):
        input = """func (p Person) getAddress() Address {
        return p.address;
    }
    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 231))


    def test_for_loop_nested_condition_but_outside_function(self):
        input = """for i := 0; i < 10; i += 1 {
        if (i % 2 == 0) {
            print("Even");
        } else {
            print("Odd");
        }
    }
    """
        expect = "Error on line 1 col 1: for"
        self.assertTrue(TestParser.checkParser(input, expect, 232))


    def test_array_struct_elements(self):
        input = """var students [3]Student = [3]Student{Student{name: "Alice", age: 20}, Student{name: "Bob", age: 21}, Student{name: "Charlie", age: 22} };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 233))


    def test_nested_function_calls_and_expression(self):
        input = """func add(a int, b int) int {
        return a + b;
    }

    func main() {
        var full_expression int = (((-100) + ((-b) - (!true))) && ((a+c-b*d%e/d-100+90/23) > ((a[1][2][3][4].foo().foo()[1][2][3].field.call(a,c,d,f)) >= (0X123abc)))) || (((a - 100) <= (banana())) == (((34.43 - 90.45) * ((123- 90 * 45/ 0x0001)/(a % r ))) < (true && false)))
        result := add(add(1, 2), add(3, 4)) + full_expression;
        return
    };
    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 234))


    def test_array_literal_complex_case(self):
        self.assertTrue(TestParser.checkParser("""const a = [1][A][C][D][_]int{{1, 0x1, 0b0011, 0o234, 0XABCFF}, id{name : "This is a string\\n\\t\\\\"}, {{ID{something: "sonething"}}}}                    
""","successful", 235))
        
        
    def test_array_literal_complex_case_2(self):
        self.assertTrue(TestParser.checkParser("""const a = [1]int{{1, 0x1}, ID{a : 100}, 1.2, "s"} + nil - nil
""","successful", 236))
        

    def test_for_loop_with_declaration_but_there_is_no_ini(self):
        # the update only accepts simple variable
        self.assertTrue(TestParser.checkParser("""
                                    func doo() {
                                        for var i [2] int = 0; foo().a.b() > 5; i[a + b] := 1 {
                                            return; 
                                        }
                                    };""","Error on line 3 col 82: [", 237))
        

    def test_unary_literals(self):
        input = """var x int = -100;
    var y bool = !true;
    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 238))


    def test_unary_variables(self):
        input = """var a int;
    var b int = -a;
    var c bool = !b;
    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 239))


    def test_expression_with_parentheses(self):
        input = """var result int = ((((((a + b) - (c * d)) % e) / f)))/90.;
    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 240))


    def test_complex_logical_expression(self):
        input = """var logic bool = (a && b) || (!(c || de) && e)
    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 241))


    def test_comparison_with_arithmetic(self):
        input = """var compare bool = ((_a + _b * _c * _*_-909.) >= ((d - e / f)));
    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 242))


    def test_function_calls_in_expression(self):
        input = """var result bool = (banana() == 100) || (foo(a, b) < 20);
    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 243))


    def test_nested_array_access(self):
        input = """var element int = a[1][2][3][4];
    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 244))


    def test_method_chaining(self):
        input = """var obj int = a[1][2][3][4].foo().foo()[1][2][3].field.call(a, c, d, f);
    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 245))


    def test_hex_literals(self):
        input = """var a bool = (0X123abc >= 0x0001);
    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 246))


    def test_floating_point_arithmetic(self):
        input = """var result float = (34.43 - 90.45) * ((123 - 90 * 45 / 0x0001) / (a % r));
    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 247))


    def test_invalid_operator(self):
        input = """func main() {
            var x int = (10 - 5)-5-5--5----5----5-----5-----5-----5----5---5*4*4*4*4*4*4*2*(2)/2/2/2/2/2/2;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 248))


    def test_continue_statement(self):
        input = """func main() {
            if (x > 0) {
                var y int = 20;
                continue;
            };
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 249))


    def test_unmatched_parentheses(self):
        input = """func main() {
            print("Hello";
        };"""
        expect = "Error on line 2 col 26: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 250))


    def test_assignment_lhs_rhs(self):
        input = """func main() {
            var a = 100 * 200 - 300
            a.field := 200
            a[a.field] := 300
            a := 900
            a[a[a[a[a[a[a[100]]]]]]] += 800
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 251))


    def test_reserved_keyword_as_identifier(self):
        input = """func main() {
            var return int = 10;
        }"""
        expect = "Error on line 2 col 17: return"
        self.assertTrue(TestParser.checkParser(input, expect, 252))


    def test_mismatched_braces_function(self):
        input = """func main() {
            var x int = 10;"""
        expect = "Error on line 2 col 28: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 253))


    def test_wrong_array_declaration_expression(self):
        input = """
            var arr [2+3]int = nil;
"""
        expect = "Error on line 2 col 23: +"
        self.assertTrue(TestParser.checkParser(input, expect, 254))


    def test_array_declaration_magic_with_integer_literal(self):
        input = """
            var arr [0b1001][0o12723][0XFF]int = nil + nil - true + false
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 255))


    def test_multiple_line_if_statement_auto_insert_SEMI(self):
        input = """func main() Something {
            var a int = util.getInput()
            if (a < 100) {
                    break;
                }// done if statement
                else if (a == 100) {
                    return Something{a : "string_a", b : "string_b", c : "string_c"}
                }
        };"""
        expect = "Error on line 6 col 17: else"
        self.assertTrue(TestParser.checkParser(input,expect,256))


    def test_multiple_if_else_auto_semi_insert_make_wrong(self):
        input = """/* this is method declaration*/
        func (p Person) Greet() string {
                if (!true) {return;}
                else if (true)
                {
                    break;
                }
            };  
        """
        expect = """Error on line 4 col 17: else"""
        self.assertTrue(TestParser.checkParser(input,expect,257))


    def test_for_loop_ini_the_lhs_can_be_only_scalar_variable(self):
        ''' left hand side of for init is not scalar'''
        input = """func listArray(arr [10]int) {
            for arr[i] := 0 ; i < 10 ; object.i+=1 {
                util.printLn(arr[i])
            }
        };"""
        expect = "Error on line 2 col 24: :="
        self.assertTrue(TestParser.checkParser(input,expect,258))


    def test_struct_declaration_does_not_contain_method_declaration(self):
        input = """type Weapon struct {
            weaponType string;
            damage int;
            flexible int
            canThrow boolean

            func (w Weapon) shoot(e Student) float {
                return ((w.damage % 100)*w.flexible);
            }
        };"""
        expect = "Error on line 7 col 13: func"
        self.assertTrue(TestParser.checkParser(input,expect,259))


    def test_valid_basic_for_loop(self):
        input = """func main() {
            var i int = 0
            for i < 10 {
                var util Util = Util{basic : true}
                util.print(i);
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 260))


    def test_valid_for_loop_more_complex(self):
        input = """func main() {
            var arr [10]int = [10]int{1,2,3,4,5,6,7,8,9,10}
            a := 0
            b := 10
            for a != b {
                a+=1
                b-=1
                if (a == b) {
                    break;
                }
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 261))


    def test_basic_for_missing_curly_braces(self):
        input = """func main() {
            var x int = 10
            for x > 0
                print(x);
        };"""
        expect = "Error on line 3 col 22: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 262))


    def test_basic_for_missing_condition(self):
        input = """func main() {
            for {
                print("Hello");
            }// insert ;
        };"""
        expect = "Error on line 2 col 17: {"
        self.assertTrue(TestParser.checkParser(input, expect, 263))


    def test_complex_condition_for_loop(self):
        input = """func main() {
            var x boolean = true;
            var y boolean = false;
            z := true;
            for (x > 0 && y < 100) || z == 10 && (x && y && z) {
                print("Complex condition");
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 264))


    def test_assignment_in_condition_not_a_valid_expression_operator(self):
        input = """func main() {
            for x = 10 {
                print("Wrong condition");
            }
        };"""
        expect = "Error on line 2 col 19: ="
        self.assertTrue(TestParser.checkParser(input, expect, 265))


    def test_nested_for_loops(self):
        input = """func main() {
            var i = 0;
            var j int = 0;
            var util Util = Util{advanced : true};
            for i < 10 {
                for j < 5 {
                    util.print(i, j);
                }
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 266))


    def test_nested_3_types_of_for(self):
        input = """const L1 = 10;
        const L2 = 10;
        const L3 = 10;

        var util Util = Util {advanced : true}
        
        func loop(arr [10][10][10]int, util Util) {
            var i int = 0
            for i < L1 {
                for var j int = 0;j < L2; j+=1 {
                    for index, e := range arr[i][j] {
                        util.printLn(e);
                    }
                }
                i += 1
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,267))


    def test_for_range_statement(self):
        input = """func main() {
        var util Util = Util{basic : true};
        arr := [3]int{10, 20, 30}
        for index, value := range arr {
        util.print("Index: ", index)
        util.print("Value: ", value)
        }

        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,268))


    def test_for_range_and_if_statement(self):
        input = """//method definition for a type struct
        func (c Customer) buyTicket() Ticket {
            var list_tickets [N]Ticket = getTicket();
            for _, ticket := range list_tickets {
                if (c.agree(ticket) == true) {
                    return ticket
                }
            }
            return nil;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,269))


    def test_in_range_for_not_assignment_operator(self):
        input = """func main() {
    arr := [3]int{10, 20, 30};
    for index, value = range a.b.c.d.e.f.foo()[1] {
        print(index, value);
    }
}
"""
        expect = "Error on line 3 col 22: ="
        self.assertTrue(TestParser.checkParser(input,expect,270))


    def test_function_call_statement(self):
        input = """func main() {
            add(subtract(10, 5), multiply(2, 3));
            foo()
            loo()
            lot_of_args(a,b, 0x123AF, "String")
            foo(loo(), foo(), another(), "string1" + "string2", foo())
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,271))


    def test_method_call_statement(self):
        input = """func method_call() string {
            calculator.add(3, 4);
            calculator.reset();
            obj.first().second().third();
            a.b.foo()
            a[a(b())][b(c())][c(d())][d(e(a && b, b && c, a.c.field * 67, [1] boolean{1,2,3}))].foo()
            process((a + b) * c, (x + y) / (z - w));
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,272))


    def test_function_call_with_parenthesis(self):
        input = """func main() {
            add
        };"""
        expect = "Error on line 2 col 16: ;"
        self.assertTrue(TestParser.checkParser(input,expect,273))


    def test_function_call_statement_with_extra_comma(self):
        input = """func (c Calculator) cal() int{
                    add(3,, 4);
        }
        """
        expect = "Error on line 2 col 27: ,"
        self.assertTrue(TestParser.checkParser(input,expect,274))


    def test_function_call_missing_parenthesis(self):
        input = """type Laptop struct {
            ID string
            lap_type string
            OS string
            Ram float
        };
        
        func (l Laptop) on() {
            l.OS.load();
        }
        
        func main() {
            add(3, 4
        };"""
        expect = "Error on line 13 col 21: ;"
        self.assertTrue(TestParser.checkParser(input,expect,275))


    def test_method_call_without_parenthesis_not_statement_at_all(self):
        input = """const STR = "This is a string\\t\\n"
                    func main() int {
                    calculator.add 
                    };"""
        expect = "Error on line 3 col 36: ;"
        self.assertTrue(TestParser.checkParser(input,expect,276))


    def test_function_call_invalid_argument(self):
        input = """const STR = add(3, 4,);"""
        expect = "Error on line 1 col 22: )"
        self.assertTrue(TestParser.checkParser(input,expect,277))


    def test_function_call_with_unmatched_parenthesis(self):
        '''Because , is not in a valid expression (argument)'''
        input = """func main() {
                add((3, 4)
            };"""
        expect = "Error on line 2 col 23: ,"
        self.assertTrue(TestParser.checkParser(input,expect,278))


    def test_chained_method_call_in_expression_and_lhs(self):
        input = """func main() {
            // expression
            var i int = a.field.foo().getField().abc[1][2].foo().f()
            // left hand side
            a.foo().a.b.c[gh.foo().doo()].noo().soo().low().too()._somefunction()[1].field += a.c.v.d.f.foo(a,  c,v,  b,d,g,  h,j,[3]int{1,2,3})
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,279))


    def test_statements_all_in_place(self):
        input = """var global_variable int = ((100%200)/(200))%(123*a)/-12/--34/--23/--45 + (!(!(a != b)) && !true)
                    const ARR = [1][2][3][4][5][global_variable]Struct{12,23,0B010101,{1,2,3,4}, {{1,2},{1,2,3}}}
                    func main() {
                    if (a == b) {
                        getInt()
                        } else if (a == 4) {
                            return 100;
                        } else if (a == 100) {
                            continue;
                        } else if ( 1 == 00.00) {
                            foo()
                        } else {
                            a[1][2][3][4] := 4
                        }
                    
                          };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,280))


    def test_dimension_in_array_type_can_not_be_expression_but_literal_or_constant(self):
        input = """    
            var z [1]int = [true]int{1};                         
        """
        expect = "Error on line 2 col 29: true"
        self.assertTrue(TestParser.checkParser(input,expect,281))


    def test_full_assignment_statements_all_in_one(self):
        input = """func test_all_assignment_statement() boolean{
            x := 5;
            x += 10
            y := x + 3 * 2;
            arr[2] *= 3;
            person.age := 25
            x := 10;
            y := x + 5;
            z := y * 2
            a := 5;
            b -= 2
            c /= 4
            d %= 3;
            x := (a + b) * c;
            arr[x + 1] := 42
            car.speed := car.speed + 10

        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,282))


    def test_very_complex_expression(self):
        input = """type Testing struct {
            test_type string;
        }
            func (t Testing) expression_test(a int, a,b,c float, a string, a,b,c,d,t boolean) bool{
            x := 5 + 3 * 2 - 4 / 2;
            x := (a + b) * (c - d) / (e % f);
            x := arr[3] + arr[foo[1]];
            y := add(10, subtract(20, 5));
            result := calculator.add(3, 4) * calculator.multiply(2, 5);
            finalResult := obj.first().second().third();
            complex := ((a + 5) * b.method()) / arr[4] % (funcCall() - x);
            matrix[2][3] := getValue(foo(1, 2)) + arr[bar(4)];
            flag := (a > b) && (x <= y) || (!isValid);
            value_very_complex := person.friends[3].getName().length() + foo().bar() * (x - y);
            matrix[a + b][foo(4)] := bar(5 * x) + arr[arr2[1]];
            car.speed := getCar().computeSpeed(50);
            x := arr[foo().bar()].method() * (calculate(a, b) - obj.field);
            result := obj.foo(obj.bar(obj.baz(10)));
            x := arr[1].get()[2].next().field * (foo() + bar);
            output := obj.transform(a + b).adjust(x * y).finalize();
            };
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,283))


    def test_assignment_missing_assignment_operator(self):
        input = """func main () {
            x 5 + 3;
        };"""
        expect = "Error on line 2 col 15: 5"
        self.assertTrue(TestParser.checkParser(input,expect,284))


    def test_expression_dont_terminate_correctly(self):
        input = """func main() {
            if (!!!!!true) {
                x := arr[2 + (3 * 4;
            }
        };"""
        expect = "Error on line 3 col 36: ;"
        self.assertTrue(TestParser.checkParser(input,expect,285))


    def test_expression_unclosed_parenthesis(self):
        input = """func (c Calculator) cal(a int, b string, c, d int) boolean {
            for i := 0 ; i < 100 ; i := i + 1 {
                x := (a + b * (c - d;
            }
        };"""
        expect = "Error on line 3 col 37: ;"
        self.assertTrue(TestParser.checkParser(input,expect,286))


    def test_using_assignment_in_rhs_which_is_expression(self):
        input = """type House interface {
            bulid() House;
            corrupt() boolean;
            upgrade() House;
            destroy(w Weapon);
        };
            type MyHouse struct {
                width int;
                length int;
            }

            func (h MyHouse) build() House {
            x := (y := 5) + 10;
            return true;
            if (a == b) {
                a := 4
            }
            }
        """
        expect = "Error on line 13 col 21: :="
        self.assertTrue(TestParser.checkParser(input,expect,287))


    def test_empty_right_hand_side(self):
        input = """func (c Calculator) foo() string {
            x %=;
        }
        """
        expect = "Error on line 2 col 17: ;"
        self.assertTrue(TestParser.checkParser(input,expect,288))


    def test_left_hand_side_is_not_lvalue_or_is_expression(self):
        input = """var u = [1][2]int{1,2,3,4,0xFF}
        func main() {
            (a + b) := 42
        };"""
        expect = "Error on line 3 col 21: :="
        self.assertTrue(TestParser.checkParser(input,expect,289))


    def test_left_hand_side_which_is_a_method_call_not_lvalue(self):
        input = """type Machine interface {
            turnOn() bool ;
            tornOff() bool;
            fix() bool;
            turnAiOn() bool;
        }
        
            type PuzzlePile struct{
                program Program
            };
            
            func (p PuzzlePipe) solve() bool {
                obj.foo() := 42;
            };"""
        expect = "Error on line 13 col 27: :="
        self.assertTrue(TestParser.checkParser(input,expect,290))


    def test_correct_array_literal(self):
        input = """var arr [2][2]Something = [2][2]Something{{Something{a : 10}, Something{a : 20}}, {Something{a:30}, Something{a:40}}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,291))


    def test_array_literal_contains_another_array_literal_but_not_in_the_type_infer_case(self):
        input = """func (c Calculator) array() boolean {
            const arr = [2][2]int{[2]int{1,2},[2]int{3,4}}
            return arr;
        };"""
        expect = "Error on line 2 col 35: ["
        self.assertTrue(TestParser.checkParser(input,expect,292))


    def test_array_literal_contain_only_literal(self):
        input = """const a = 10
        const b = 20
        const c = 30
        func add (a,b,c int, d,e string) {
            var array = [5]string{"string", "abcd", "efd", "\\t\\n\\r\\\\\\""}
            return printArray(array);
            if (a == b) {
            a := 5
            } else if (a == 4) {
            a := 8
            } else if (a == 10) {
            a := 2837
            };

            if (a == 8) {
                print(a);

            } else {
                a[1][2][3][4] += 9
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,293))


    def test_struct_literal_which_can_be_empty(self):
        input = """func main() {
            var b1 Book = Book {n : 1000, a : "JK"}
            var b2 Book = Book {n : 2000, a : "Dung"}
            var b3      = Book {}
            foo()[2] := 2;
            a.b.d.c.d.d.d.f.d.e.r.f.g.foo(a,c,d,v,g)[1][2][3] := 10283 * 283745 /78474 % 234
            return b1.getPage() + b2.getPage() + b3.getPage()
        }
        
        type Book struct {
            n int;
            a string;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,294))


    def test_interface_with_method_declaration_return_type(self):
        input = """type AI interface {
            SolveProblem(p Problem) boolean;
            TalkAboutLife(topic string) string
            SearchInfor(search string) [10]string;
            DoCommand(command string) boolean;
            AutoDestroy(on boolean) boolean 
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,295))


    def test_case_sentisive_for_if_else(self):
        input = """func doing(If int) int{
            if (If == 1) {
                return If
            } else {
                var Else int = 2 * If
                return doing(Else);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,296))


    def test_chained_if_else_statement(self):
        input = """const PI = 3.1415;
            func main() {
                var i int = getInt();

                if (i < 0) {
                    for i := 0 ; i < 100 ; i += 1 {
                        var util Util = Util{advanced : true};
                        util.print(i)

                        if (i == 20) {
                            break;
                        } else if (i == 40) {
                        continue;
                        } else if (i == 80) {
                            return 100 % 34 * i
                        }
                    }
                } else {
                    continue;
                }

                return 100;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,297))


    def test_built_in_function_usage(self):
        input = """type BuiltIn struct {
            dump int
        }
        
        func (b BuiltIn) calling() bool {
            var Int int = 100;
            var Float float = 0.01E-34
            getInt();
            putInt(Int)
            putIntLn(Int);
            getFloat()
            putFloat(Float);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,298))


    def test_for_statement_in_all_statements(self):
        input = """func main() bool {
            for _, arr := range a.b.c.d.f.g.e.r[1].foo().coo().a {
                if (arr != arr.parent()) {
                    break;
                }
                
                if (arr == arr.children()) {
                    continue;
                }

                a();
                b.a();
                a[3].foo()[1] := arr
                return;
            }
        }
        func add(a,b float) {
            return a + b
            var humanName string = Person{name:"Dung"}.getName();
        };"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,299))


    def test_final_test_case_for_variable_declaration_in_for_loop_init(self):
        input = """func Add() int {
                for var i [13]int = 0; foo().a.b(); i[3] += 1 {
                    break;
                }

                /*they are literal, which is part of 
                the expression, thus, it's oke to do so*/
                var value int = [5]int{1,2,3,4,5}[0];
                return true;
                    };"""
        expect = "Error on line 2 col 54: ["
        self.assertTrue(TestParser.checkParser(input,expect,300))