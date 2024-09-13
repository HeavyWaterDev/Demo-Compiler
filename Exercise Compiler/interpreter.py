class Interpreter:
    def __init__(self):
        self.variables = {}
        # Dictionary of binary operations
        self.operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
            '==': lambda x, y: x == y,
            '!=': lambda x, y: x != y,
            '<': lambda x, y: x < y,
            '<=': lambda x, y: x <= y,
            '>': lambda x, y: x > y,
            '>=': lambda x, y: x >= y,
        }

    def evaluate(self, node):
        # Handle list of statements
        if isinstance(node, list):
            return [self.evaluate(stmt) for stmt in node][-1]
        
        node_type = node[0]
        
        # Handle different node types
        if node_type == 'number':
            return node[1]
        elif node_type == 'name':
            return self.variables.get(node[1], 0)
        elif node_type == 'binop':
            op, left, right = node[1], self.evaluate(node[2]), self.evaluate(node[3])
            return self.operations[op](left, right)
        elif node_type == 'assign':
            self.variables[node[1]] = self.evaluate(node[2])
        elif node_type == 'expr':
            return self.evaluate(node[1])
        elif node_type == 'if':
            if self.evaluate(node[1]):
                return self.evaluate(node[2])
        elif node_type == 'loop':
            count = self.evaluate(node[1])
            for _ in range(count):
                self.evaluate(node[2])
