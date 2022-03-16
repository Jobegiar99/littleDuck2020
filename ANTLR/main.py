from antlr4 import *
from littleDuckLexer import littleDuckLexer
from littleDuckListener import littleDuckListener
from littleDuckParser import littleDuckParser

class LittleDuckPrintListener(littleDuckListener):
    def enterEnd0(self,ctx):
        print("No errors 👍")

test_valid_1 = """
program test1;
{
	v1 = 12;
}
"""

test_valid_2 = """
			program 
			test2
			;
		
			var 
					v1: int; 
					v2: float;
					v3: int;
					v4: float;
					v5,v6,v7,v8,v9: int;
{
	v1 = 23;
	print("HOLA","MUNDO");
	if( 4 < 5){
		v2 = 12.23;
		if( 
			4 < 5
		)
		{
			v2
						 = 
						123;
			if( 
					-9 < 5
				)
			{
				v2 = -123.234234;
			};
		};
	}
	
								else{
												v1 = 4;
	};
}
"""

test_valid_3 = """
program a5;
var a5: int;
{

}
"""

test_invalid_1 = """
pro gr am 1;
v a r xD: int;{
	$
}
"""

test_invalid_2 = """
p
r
o
g
r
@
m
"""

tests = [test_valid_1,test_valid_2,test_valid_3,test_invalid_1,test_invalid_2]

for test in tests:
    print("--------------")
    print("Test: ", tests.index(test) + 1)
    lexer = littleDuckLexer(InputStream(test))
    stream = CommonTokenStream(lexer)
    parser = littleDuckParser(stream)
    tree = parser.program0()
    printer = LittleDuckPrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer,tree)
