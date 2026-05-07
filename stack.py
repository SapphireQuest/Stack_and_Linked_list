MAX_STACK_SIZE = 100

class Stack:
    def __init__(self, data_type):
        self.items = []
        self.data_type = data_type
    def push(self, item):
        if len(self.items) >= MAX_STACK_SIZE:
            raise Exception("Stack overflow") 
        if not isinstance(item, self.data_type):
            raise Exception("Type error")
        self.items.append(item)
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items.pop()
    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items[-1]
    def is_empty(self):
        return len(self.items) == 0

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



def calculateAnswer(expression):
    ans = Stack(int)
    for token in expression.split():
        if token.isdigit():
            ans.push(int(token))
        else:
            b = ans.pop()
            a = ans.pop()
            if token == '+':
                ans.push(a + b)
            elif token == '-':
                ans.push(a - b)
            elif token == '*':
                ans.push(a * b)
            elif token == '/':
                ans.push(a / b)
    print("Result: ",ans.pop())  

def changeToPostfix(infix):
    output = Stack(str)
    operators = Stack(str) 
    operators_num = {'+': 2, '-': 2, '*': 1, '/': 1}
    for token in infix.split():
        if token.isdigit():
           output.push(token)
        elif token in operators_num:
            while (not operators.is_empty() and operators.top() in operators_num and operators_num[operators.top()] >= operators_num[token]):
                output.push(operators.pop())
            operators.push(token)
        elif token == '(':
            operators.push(token)
        elif token == ')':
            while not operators.is_empty() and operators.top() != '(':
                output.push(operators.pop())
            if not operators.is_empty():
                operators.pop()
    while not operators.is_empty():
        output.push(operators.pop())
    final_postfix = " ".join(output.items)
    return final_postfix
         
        
def main():
    print("Provide expression: ")
    user_input = input()
    expression = changeToPostfix(user_input)
    calculateAnswer(expression) 

main()