#! python3
# Chapter3.py

from Stack import Stack
from Queue import Queue
from Deque import Deque
import random

def rev_str(string):
    '''Reverses the given string and returns the output.'''
    letters = Stack()
    for letter in string:
        letters.push(letter)
    rev_string = str()
    while letters.size() > 0:
        rev_string += letters.pop()
    return rev_string

def par_checker(symbol_string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]

        if symbol in '([{':
            s.push(symbol)
        if symbol in ')]}':
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index += 1
    return balanced and s.is_empty()

def matches(opening, closing):
    a = '([{'
    b = ')]}'
    return a.index(opening) == b.index(closing)

def base_converter(dec_number, base = 2):
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    rem_stack = Stack()

    while dec_number > 0:
        rem = dec_number % base
        rem_stack.push(rem)
        dec_number = dec_number // base


    new_string = ''
    while not rem_stack.is_empty():
        new_string += digits[rem_stack.pop()]

    return new_string

def is_valid(expr):
    if not par_checker(expr):
        
        return False
    expr_list = expr.split()
    a = Stack()
    for var in expr_list:
        if var not in '+-/*^()':
            a.push(var)
        elif var in '()':
            pass
        else:
            if a.is_empty():
                return False
            else:
                a.pop()
    return True
            
    


def infix_to_postfix(infix_expr):
    '''Converts an infix expression like A + B * C to postfix expression like ABC*+'''
    if not is_valid(infix_expr):
        print('Invalid Expression')
        return None

    prec = dict() # A dictionary to define the precedence of operators
    prec['^'] = 4
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    op_stack = Stack() # Stack to store and retrive the operators encountered
    postfix_list = list()
    token_list = infix_expr.split()
    

    for token in token_list:
        if token not in ''.join(prec.keys())+')':
            postfix_list.append(token)
        elif token == '(':
            op_stack.push(token)
        elif token == ')':
            top_token = op_stack.pop()
            while top_token != '(':
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while (not op_stack.is_empty()) and (prec[op_stack.peek()] >= prec[token]):
                postfix_list.append(op_stack.pop())
                
            op_stack.push(token)
            
    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())
            
    return ' '.join(postfix_list)

def infix_to_prefix(infix_expr):
    '''Converts an infix expression like A + B * C to prefix expression like +A*BC'''

    prec = dict() # A dictionary to define the precedence of operators
    prec['^'] = 4
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    prefix_list = list()
    operand_stack = Stack() # Stack to store and retrive the operands encountered
    op_stack = Stack()  # Stack to store and retrive the operators encountered
    token_list = infix_expr.split()
    for token in token_list:
        if token not in ''.join(prec.keys()) + ')':
            operand_stack.push(token)
        elif token == '(':
            while operand_stack.size() > 0:
                prefix_list.append(operand_stack.pop())
            prefix_list.append(token)
    
        elif token == ')':
            print(') found')
            temp = prefix_list.pop()
            while temp != '(':
                operand_stack.push(temp)
                print(operand_stack)
                temp = prefix_list.pop()
            
        else:
            prefix_list.append(token)
        
    while operand_stack.size() > 0:
        prefix_list.append(operand_stack.pop())
    return ' '.join(prefix_list)
            
        
    
        
def postfix_eval(postfix_expr):
    operand_stack = Stack()
    token_list = postfix_expr.split()

    for token in token_list:
        if token not in '+-*/':
            operand_stack.push(int(token))
        else:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = do_math(token, operand1, operand2)
            operand_stack.push(result)
    return operand_stack.pop()

def do_math(operator, op1, op2):
    if operator == '*':
        return op1 * op2
    if operator == '/':
        return op1 / op2
    if operator == '+':
        return op1 + op2
    if operator == '-':
        return op1 - op2
    
def postfix_to_infix(postfix_expr):
    operand_stack = Stack()
    token_list = postfix_expr.split()

    for token in token_list:
        if token not in '+-*/^':
            operand_stack.push(token)

        else:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = '(' + operand1 + token + operand2 + ')'
            operand_stack.push(result)
    return operand_stack.pop()

    
def hot_potato(name_list, num = 2):
    sim_queue = Queue()

    for name in name_list:
        sim_queue.enqueue(name)

    turn = 0
    while sim_queue.size() > 1:
        if turn % (num + 1) == 0 :
            if turn == 0:
                pass
            else:
                sim_queue.dequeue() # Removes the member from the queue permanently
        else:
            sim_queue.enqueue(sim_queue.dequeue()) #Removes the first member from the queue and puts them again at the begging of the queue
        turn += 1
    return sim_queue.dequeue()

def hot_potato2(name_list, num = 2):
    sim_queue = Queue()

    for name in name_list:
        sim_queue.enqueue(name)

    while sim_queue.size() > 1:
        for i in range(num):
            sim_queue.enqueue(sim_queue.dequeue())

        sim_queue.dequeue()
    return sim_queue.dequeue()

def random_hot_potato(name_list):
    sim_queue = Queue()

    for name in name_list:
        sim_queue.enqueue(name)

    turn = 0
    while sim_queue.size() > 1:
        num = random.randrange(1, 20)
        if turn % (num + 1) == 0 :
            if turn == 0:
                pass
            else:
                sim_queue.dequeue() # Removes the member from the queue permanently
        else:
            sim_queue.enqueue(sim_queue.dequeue()) #Removes the first member from the queue and puts them again at the begging of the queue
        turn += 1
    return sim_queue.dequeue()

def pal_check(a_string):
    char_deque = Deque()

    for ch in a_string:
        char_deque.add_rear(ch)

    still_equal = True

    while char_deque.size() > 1 and still_equal:
        if char_deque.remove_front() != char_deque.remove_rear():
            still_equal = False

    return still_equal

def infix_eval(expr):
    prec = dict() # A dictionary to define the precedence of operators
    prec['^'] = 4
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    token_list = expr.split()
    operand_stack = Stack()
    operator_stack = Stack()
    for token in token_list:
        if token not in list(prec.keys()) + [')']:
            operand_stack.push(int(token))
        elif token == '(':
            operator_stack.push(token)
        elif token == ')':
            operator = operator_stack.pop()
            print(operator_stack, operand_stack)
            while operator != '(':
                operand2 = operand_stack.pop()
                operand1 = operand_stack.pop()
                result = do_math(operator, operand1, operand2)
                operand_stack.push(result)
                operator = operator_stack.pop()
            
        else:
            if not operator_stack.is_empty():
                if prec[operator_stack.peek()] > prec[token]:
                    operator = operator_stack.pop()
                    op2 = operand_stack.pop()
                    op1 = operand_stack.pop()
                    operand_stack.push(do_math(operator, op1, op2))
            operator_stack.push(token)
    while operator_stack.size() > 0 or operand_stack.size() > 1:
        operand2 = operand_stack.pop()
        operand1 = operand_stack.pop()
        operator = operator_stack.pop()
        result = do_math(operator, operand1, operand2)
        operand_stack.push(result)
    return operand_stack.pop()
        
def calculator():
    
    while True:
        a = input('Enter an expression:(Enter q to break) \n')
        if a == 'q':
            break
        print(infix_eval(a))
    


if __name__ == '__main__':
    names = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
