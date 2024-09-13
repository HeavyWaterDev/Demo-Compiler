import ply.yacc as yacc
from lexer import tokens

# Parsing rules
def p_statements(p):
    '''statements : statements statement 
                  | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_statement_assign(p):
    #TODO: Implement assignment statement
    p[0] = ('assign', p[1], p[3])

def p_statement_expr(p):
    'statement : expression'
    #TODO: Implement expression statement

def p_statement_if(p):
    pass #TODO: Implement if statement

def p_statement_loop(p):
    '''statement : LOOP expression COLON statements END'''
    p[0] = ('loop', p[2], p[4])

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

def p_expression_group(p):
    '''expression : LPAREN expression RPAREN'''
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = ('number', p[1])

def p_expression_name(p):
    'expression : NAME'
    p[0] = ('name', p[1])

def p_error(p):
    print("Syntax error in input!", p.value)

parser = yacc.yacc()
