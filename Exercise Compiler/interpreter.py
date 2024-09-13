class Interpreter:
    def __init__(self):
        self.variables = {}

    def evaluate(self, node):
        if isinstance(node, list):
            last_result = None
            for stmt in node:
                last_result = self.evaluate(stmt)
            return last_result
        elif node[0] == 'number':
            return node[1]
        elif node[0] == 'name':
            return self.variables.get(node[1], 0)
        elif node[0] == 'binop':
            left = self.evaluate(node[2])
            right = self.evaluate(node[3])
            if node[1] == '+':
                pass #TODO: Implement addition
            elif node[1] == '-':
                return left - right
            elif node[1] == '*':
                pass #TODO: Implement multiplication
            elif node[1] == '/':
                return left / right
            elif node[1] == '==':
                return left == right
            elif node[1] == '!=':
                return left != right
            elif node[1] == '<':
                pass #TODO: Implement less than
            elif node[1] == '<=':
                return left <= right
            elif node[1] == '>':
                return left > right
            elif node[1] == '>=':
                return left >= right
        elif node[0] == 'assign':
            pass #TODO: Implement assignment
        elif node[0] == 'expr':
            return self.evaluate(node[1])
        elif node[0] == 'if':
            condition = self.evaluate(node[1])
            if condition:
                return self.evaluate(node[2])
        elif node[0] == 'loop':
            count = self.evaluate(node[1])
            for _ in range(count):
                self.evaluate(node[2])
