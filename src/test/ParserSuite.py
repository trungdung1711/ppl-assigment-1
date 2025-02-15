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
                                        for var b [2]ID = (1. + 2.) / 4;  foo().a.b(); i := 1 {
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
                } else {
                    var z ID;
                }
            }
        ""","successful", 216))


    def test_interface_that_contains_nothing(self):
        self.assertTrue(TestParser.checkParser("""
            type Calculator interface {
                                        
                Add(x, y, z int, a float) int;
                Add(x, y int, a, b, c, d string) int;
                Reset(a,b  ,c,d int, m int, n float, x,y,z,t string)
                                        
                Hello(name string);
                                        
            }
            type Weapon interface {}                                                                       
        ""","Error on line 11 col 36: }", 217))


    def test_statements_inside_block_at_the_end_of_the_function_there_must_be_a_semi(self):
        self.assertTrue(TestParser.checkParser("""
                                    func something() {
                                        ab += "string\\\\";
                                        ab -= a[2].b().c().d().e();
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
    util.list(ARR)
};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,225))


    def test_full_executable_program(self):
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
    name string;
    age int;
    HBKK [8]Money
    ID string;
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



















    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))


    # def test_(self):
    #     input = """ """
    #     expect = ""
    #     self.assertTrue(TestParser.checkParser(input,expect,2))

'''
        input = """ """
        expect = ""
        self.assertTrue(TestParser.checkParser(input,expect,211))
'''