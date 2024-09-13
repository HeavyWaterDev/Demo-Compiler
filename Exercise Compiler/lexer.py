import ply.lex as lex

# List of token names
tokens = (
    'NUMBER', 'KEYWORD', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LPAREN', 'RPAREN', 'ASSIGN', 'NAME', 'EQ', 'NE', 'LT',
    'LE', 'GT', 'GE', 'IF', 'COLON', 'LOOP', 'END', 'SEMICOLON'
)

precedence = (
    ('left', 'PLUS', 'MINUS'),  # + and - have the same precedence
    ('left', 'TIMES', 'DIVIDE'),  # * and / have the same precedence
    ('nonassoc', 'EQ', 'NE', 'LT', 'LE', 'GT', 'GE'),  # Comparison operators
)

# Regular expression rules for simple tokens
reserved = {
    '+': 'PLUS', '-': 'MINUS', '*': 'TIMES', '/': 'DIVIDE',
    '(': 'LPAREN', ')': 'RPAREN', '=': 'ASSIGN', '==': 'EQ',
    '!=': 'NE', '<': 'LT', '<=': 'LE', '>': 'GT', '>=': 'GE',
    'if': 'IF', ':': 'COLON', ';': 'SEMICOLON', 'loop': 'LOOP',
    'end': 'END'
}

def t_NUMBER(t):
    r'-?\d+'
    t.value = int(t.value)
    return t

def t_KEYWORD(t):
    r':|\+|-|\*|/|==|!=|<|<=|>|>=|\(|\)|=|loop|end|;'
    t.type = reserved.get(t.value.lower(), 'KEYWORD')
    return t

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value.lower(), 'NAME')
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_whitespace(t):
    r'\s+'

def t_eof(t):
    return None

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
