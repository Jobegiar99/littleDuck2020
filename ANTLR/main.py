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
	if( 
        5 < 4
        )
        {
        print("HOLA");
    };
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
		if( 4 < 5){
			v2 = 123;
			if(-9 > 5)
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
program a1;
{
    print("HOLA ","MUNDO ");
}

"""

test_invalid_1 = """
progr am 1;
v a r xD: int;{
	DX
}

"""

lexer = littleDuckLexer(InputStream(test_valid_1))
stream = CommonTokenStream(lexer)
parser = littleDuckParser(stream)
tree = parser.program0()
printer = LittleDuckPrintListener()
walker = ParseTreeWalker()
walker.walk(printer,tree)
