import readline
from lexer import lexer
from parser import parser
from interpreter import Interpreter

if __name__ == "__main__":
    interpreter = Interpreter()
    while True:
        try:
            s = input('calc > ')
            readline.add_history(s)
        except EOFError:
            break
        
        lexer.input(s)
        parsed_program = parser.parse(s, lexer=lexer)
        if parsed_program:
            result = interpreter.evaluate(parsed_program)
            if result is not None:
                print(result)
