
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGN COLON DIVIDE END EQ GE GT IF KEYWORD LE LOOP LPAREN LT MINUS NAME NE NUMBER PLUS RPAREN SEMICOLON TIMESstatements : statements statement \n                  | statementstatement : expressionstatement : LOOP expression COLON statements ENDexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression DIVIDE expression\n                  | expression EQ expression\n                  | expression NE expression\n                  | expression LT expression\n                  | expression LE expression\n                  | expression GT expression\n                  | expression GE expressionexpression : LPAREN expression RPARENexpression : NUMBERexpression : NAME'
    
_lr_action_items = {'LOOP':([0,1,2,3,6,7,8,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[4,4,-2,-3,-16,-17,-1,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,4,-15,4,-4,]),'LPAREN':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[5,5,-2,-3,5,5,-16,-17,-1,5,5,5,5,5,5,5,5,5,5,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,5,-15,5,-4,]),'NUMBER':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[6,6,-2,-3,6,6,-16,-17,-1,6,6,6,6,6,6,6,6,6,6,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,6,-15,6,-4,]),'NAME':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[7,7,-2,-3,7,7,-16,-17,-1,7,7,7,7,7,7,7,7,7,7,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,7,-15,7,-4,]),'$end':([1,2,3,6,7,8,21,22,23,24,25,26,27,28,29,30,32,34,],[0,-2,-3,-16,-17,-1,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-4,]),'END':([2,3,6,7,8,21,22,23,24,25,26,27,28,29,30,32,33,34,],[-2,-3,-16,-17,-1,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,34,-4,]),'PLUS':([3,6,7,19,20,21,22,23,24,25,26,27,28,29,30,32,],[9,-16,-17,9,9,9,9,9,9,9,9,9,9,9,9,-15,]),'MINUS':([3,6,7,19,20,21,22,23,24,25,26,27,28,29,30,32,],[10,-16,-17,10,10,10,10,10,10,10,10,10,10,10,10,-15,]),'TIMES':([3,6,7,19,20,21,22,23,24,25,26,27,28,29,30,32,],[11,-16,-17,11,11,11,11,11,11,11,11,11,11,11,11,-15,]),'DIVIDE':([3,6,7,19,20,21,22,23,24,25,26,27,28,29,30,32,],[12,-16,-17,12,12,12,12,12,12,12,12,12,12,12,12,-15,]),'EQ':([3,6,7,19,20,21,22,23,24,25,26,27,28,29,30,32,],[13,-16,-17,13,13,13,13,13,13,13,13,13,13,13,13,-15,]),'NE':([3,6,7,19,20,21,22,23,24,25,26,27,28,29,30,32,],[14,-16,-17,14,14,14,14,14,14,14,14,14,14,14,14,-15,]),'LT':([3,6,7,19,20,21,22,23,24,25,26,27,28,29,30,32,],[15,-16,-17,15,15,15,15,15,15,15,15,15,15,15,15,-15,]),'LE':([3,6,7,19,20,21,22,23,24,25,26,27,28,29,30,32,],[16,-16,-17,16,16,16,16,16,16,16,16,16,16,16,16,-15,]),'GT':([3,6,7,19,20,21,22,23,24,25,26,27,28,29,30,32,],[17,-16,-17,17,17,17,17,17,17,17,17,17,17,17,17,-15,]),'GE':([3,6,7,19,20,21,22,23,24,25,26,27,28,29,30,32,],[18,-16,-17,18,18,18,18,18,18,18,18,18,18,18,18,-15,]),'COLON':([6,7,19,21,22,23,24,25,26,27,28,29,30,32,],[-16,-17,31,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,]),'RPAREN':([6,7,20,21,22,23,24,25,26,27,28,29,30,32,],[-16,-17,32,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statements':([0,31,],[1,33,]),'statement':([0,1,31,33,],[2,8,2,8,]),'expression':([0,1,4,5,9,10,11,12,13,14,15,16,17,18,31,33,],[3,3,19,20,21,22,23,24,25,26,27,28,29,30,3,3,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statements","S'",1,None,None,None),
  ('statements -> statements statement','statements',2,'p_statements','parser.py',6),
  ('statements -> statement','statements',1,'p_statements','parser.py',7),
  ('statement -> expression','statement',1,'p_statement_expr','parser.py',18),
  ('statement -> LOOP expression COLON statements END','statement',5,'p_statement_loop','parser.py',25),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','parser.py',29),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','parser.py',30),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','parser.py',31),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','parser.py',32),
  ('expression -> expression EQ expression','expression',3,'p_expression_binop','parser.py',33),
  ('expression -> expression NE expression','expression',3,'p_expression_binop','parser.py',34),
  ('expression -> expression LT expression','expression',3,'p_expression_binop','parser.py',35),
  ('expression -> expression LE expression','expression',3,'p_expression_binop','parser.py',36),
  ('expression -> expression GT expression','expression',3,'p_expression_binop','parser.py',37),
  ('expression -> expression GE expression','expression',3,'p_expression_binop','parser.py',38),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','parser.py',42),
  ('expression -> NUMBER','expression',1,'p_expression_number','parser.py',46),
  ('expression -> NAME','expression',1,'p_expression_name','parser.py',50),
]
