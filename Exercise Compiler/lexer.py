import ply.lex as lex

# List of token names
tokens = (
    'NUMBER', 'KEYWORD', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LPAREN', 'RPAREN', 'ASSIGN', 'NAME', 'EQ', 'NE', 'LT',
    'LE', 'GT', 'GE', 'IF', 'COLON', 'LOOP', 'END', 'SEMICOLON'
)

# Define operator precedence
precedence = (
    ('left', 'PLUS', 'MINUS'),  # + and - have the same precedence
    ('left', 'TIMES', 'DIVIDE'),  # * and / have the same precedence
    ('nonassoc', 'EQ', 'NE', 'LT', 'LE', 'GT', 'GE'),  # Comparison operators
)

# Dictionary mapping reserved words to tokens
reserved = {
    '+': 'PLUS', '-': 'MINUS', '*': 'TIMES', '/': 'DIVIDE',
    '(': 'LPAREN', ')': 'RPAREN', '=': 'ASSIGN', '==': 'EQ',
    '!=': 'NE', '<': 'LT', '<=': 'LE', '>': 'GT', '>=': 'GE',
    'if': 'IF', ':': 'COLON', ';': 'SEMICOLON', 'loop': 'LOOP',
    'end': 'END'
}

# Regular expression rule for numbers
def t_NUMBER(t):
    r'-?\d+'
    t.value = int(t.value)
    return t

# Regular expression rule for keywords and operators
def t_KEYWORD(t):
    r':|\+|-|\*|/|==|!=|<|<=|>|>=|\(|\)|=|loop|end|;'
    t.type = reserved.get(t.value.lower(), 'KEYWORD')
    return t

# Regular expression rule for variable names
def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value.lower(), 'NAME')
    return t

# Ignore whitespace and tabs
t_ignore = ' \t'

# Handle newlines
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignore whitespace (redundant, can be removed)
def t_whitespace(t):
    r'\s+'

# Handle end of file
def t_eof(t):
    return None

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
