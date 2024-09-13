import ply.yacc as yacc
from lexer import tokens

# Grammar rule for multiple statements
def p_statements(p):
    '''statements : statements statement
                  | statement'''
    p[0] = p[1] + [p[2]] if len(p) == 3 else [p[1]]

# Grammar rule for assignment statements
def p_statement(p):
    '''statement : NAME ASSIGN expression
                 | expression
                 | IF expression COLON statements END
                 | LOOP expression COLON statements END'''
    if len(p) == 4:
        p[0] = ('assign', p[1], p[3])
    elif len(p) == 2:
        p[0] = ('expr', p[1])
    elif len(p) == 6:
        p[0] = (p[1].lower(), p[2], p[4])

# Grammar rule for binary operations
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression EQ expression
                  | expression NE expression
                  | expression LT expression
                  | expression LE expression
                  | expression GT expression
                  | expression GE expression'''
    p[0] = ('binop', p[2], p[1], p[3])

# Grammar rule for parentheses
def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

# Grammar rule for numbers
def p_expression_number(p):
    'expression : NUMBER'
    p[0] = ('number', p[1])

# Grammar rule for variable names
def p_expression_name(p):
    'expression : NAME'
    p[0] = ('name', p[1])

# Error handling rule
def p_error(p):
    print("Syntax error in input!", p.value)

# Build the parser
parser = yacc.yacc()
