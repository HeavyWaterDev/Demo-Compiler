import unittest
import ply.lex as lex
import ply.yacc as yacc
from lexer import lexer
from parser import parser
from interpreter import  Interpreter

class TestSimpleInterp(unittest.TestCase):

    def setUp(self):
        # Reset the variables dictionary before each test
        global interpreter
        interpreter = Interpreter()

    def test_assignment(self):
        s = 'x = 10'
        parsed_program = parser.parse(s, lexer=lexer)
        interpreter.evaluate(parsed_program)
        self.assertEqual(interpreter.variables['x'], 10)

    def test_expression(self):
        s = 'x = 10 + 5'
        parsed_program = parser.parse(s, lexer=lexer)
        interpreter.evaluate(parsed_program)
        self.assertEqual(interpreter.variables['x'], 15)

    def test_conditional_true(self):
        s = '''
        if 1 == 1:
            x = 10
        end
        '''
        parsed_program = parser.parse(s, lexer=lexer)
        interpreter.evaluate(parsed_program)
        self.assertEqual(interpreter.variables['x'], 10)

    def test_conditional_false(self):
        s = '''
        if 1 == 2:
            x = 10
        end
        '''
        parsed_program = parser.parse(s, lexer=lexer)
        interpreter.evaluate(parsed_program)
        self.assertNotIn('x', interpreter.variables)

    def test_loop(self):
        s = '''
        x = 0
        loop 3:
            x = x + 1
        end
        '''
        parsed_program = parser.parse(s, lexer=lexer)
        interpreter.evaluate(parsed_program)
        self.assertEqual(interpreter.variables['x'], 3)

    def test_nested_loop(self):
        s = '''
        x = 0
        loop 2:
            loop 2:
                x = x + 1
            end
        end
        '''
        parsed_program = parser.parse(s, lexer=lexer)
        interpreter.evaluate(parsed_program)
        self.assertEqual(interpreter.variables['x'], 4)

    def test_complex_expression(self):
        s = 'x = (10 + 5) * 2'
        parsed_program = parser.parse(s, lexer=lexer)
        interpreter.evaluate(parsed_program)
        self.assertEqual(interpreter.variables['x'], 30)

    def test_variable_reference(self):
        s = '''
        x = 10
        y = x + 5
        '''
        parsed_program = parser.parse(s, lexer=lexer)
        interpreter.evaluate(parsed_program)
        self.assertEqual(interpreter.variables['y'], 15)

    def test_loop_variable_reference(self):
        s = '''
        x = 10
        y = x + 5
        z = 0
        loop x:
            loop y:
                z = z + 1
            end
        end

        '''
        parsed_program = parser.parse(s, lexer=lexer)
        interpreter.evaluate(parsed_program)
        self.assertEqual(interpreter.variables['z'], 150)

    def test_If_loop(self):
        s = '''
        x = 10
        y = x + 5
        z = 0

        if 1 == 2:
            loop x:
                loop y:
                    z = z + 1
                end
            end
            z = 1
        end
        
        '''
        parsed_program = parser.parse(s, lexer=lexer)
        interpreter.evaluate(parsed_program)
        self.assertEqual(interpreter.variables['z'], 0)

if __name__ == '__main__':
    unittest.main()