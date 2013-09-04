'''
Created on 4 Sep 2013

@author: brian
'''
class Stack(object):
    def __init__(self):
        self.__storage = []

    def isEmpty(self):
        return len(self.__storage) == 0

    def push(self, p):
        self.__storage.append(p)

    def pop(self):
        if self.isEmpty():
            raise IndexError("Empty stack!")
        return self.__storage.pop()
    
    def peek(self):
        if self.isEmpty():
            raise IndexError("Empty stack!")
        return self.__storage[-1]
    
    def __repr__(self):
        return str(self.__storage)

class Operator(object):
    operators = {'(' : 0, ')': 0, '+': 1, '-': 1, '*': 2, '/': 2}
        
    def __init__(self, token):
        if not token in Operator.operators:
            raise ValueError("Not an operator! " + token)
        self.op = token
    
    def __lt__(self, other):
        return Operator.operators[self.op] < Operator.operators[other.op]
    
    def __eq__(self, other):
        return self.op == other.op
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __repr__(self):
        return self.op
    
Operator.Multiply = Operator('*')
Operator.Divide = Operator('/')
Operator.Add = Operator('+')
Operator.Subtract = Operator('-')
Operator.Arithmetic = [Operator.Multiply, Operator.Divide, Operator.Add, Operator.Subtract]
Operator.Lparen = Operator('(')
Operator.Rparen = Operator(')')
    
class Calculator(object):
    def __init__(self, expr = ""):
        self.__infix = expr.split();
        self.__postfix = []
    
    def evaluate(self):
        stack = Stack()
        stack.push(None)
        for token in self.__postfix:
            try:
                # By trying to create an operator we can tell if the token
                # is an operator or a token
                operator = Operator(token)
                if operator == Operator.Multiply:
                    stack.push(stack.pop() * stack.pop())
                elif operator == Operator.Divide:
                    op2 = stack.pop()
                    stack.push(stack.pop() / op2)
                elif operator == Operator.Add:
                    stack.push(stack.pop() + stack.pop())
                elif operator == Operator.Subtract:
                    op2 = stack.pop()
                    stack.push(stack.pop() - op2)
            except ValueError:
                # Assume it's an operand so we push it
                stack.push(float(token))
        return stack.pop()
    
    def asPostfix(self):
        stack = Stack() 
        for token in self.__infix:
            try:
                # By trying to create an operator we can tell if the token
                # is an operator or a token
                operator = Operator(token)
                if operator in Operator.Arithmetic:
                    while not stack.isEmpty() and operator < stack.peek():
                        if stack.peek() != Operator.Lparen:
                            self.__postfix.append(stack.pop().op)
                elif operator == Operator.Rparen:
                    while stack.peek() != Operator.Lparen:
                        self.__postfix.append(stack.pop().op)
                    stack.pop()                        
                if operator != Operator.Rparen:
                    stack.push(operator)
            except ValueError:
                # It's an operand
                self.__postfix.append(token)
        while not stack.isEmpty():
            self.__postfix.append(stack.pop().op)
        return self
    
    def __repr__(self):
        return "Infix: " + str(self.__infix) +  "\nPostfix: " + str(self.__postfix)
            
if __name__ == "__main__":
    calc = Calculator("1 + 2 * 6 - ( 1 + 2 ) * 6")
    print calc.asPostfix()
    print calc.evaluate()

