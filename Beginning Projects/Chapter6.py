#! python3
# Chapter6

from Stack import Stack
from binary_tree_data_structure import BinaryTree
import operator

def build_parse_tree(fp_exp):
    fp_list = true_split(fp_exp)
    p_stack = Stack()
    e_tree = BinaryTree('')
    p_stack.push(e_tree)
    current_tree = e_tree
    for i in fp_list:
        if i == '(':
            current_tree.insert_left('')
            p_stack.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif i not in '+-*/)':
            current_tree.set_root_val(int(i))
            parent = p_stack.pop()
            current_tree = parent
        elif i in '+-*/':
            current_tree.set_root_val(i)
            current_tree.insert_right('')
            p_stack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif i == ')':
            current_tree = p_stack.pop()
        else:
            raise ValueError
    return e_tree

def build_parse_tree2(fp_exp):
    fp_list = true_split(fp_exp)
    p_stack = Stack()
    e_tree = BinaryTree('')
    p_stack.push(e_tree)
    current_tree = e_tree
    prec = dict()
    prec['/'] = 3
    prec['*'] = 2
    prec['+'] = 1
    prec['-'] = 1
    prec['('] = 0
    for i in fp_list:
        if i == '(':
            if current_tree.get_root_val() == '':
                current_tree.insert_left('')
                p_stack.push(current_tree)
                current_tree = current_tree.left_child
            else:
                current_tree.insert_right('')
                p_stack.push(current_tree)
                current_tree = current_tree.right_child
        elif i not in '+-*/()':
            if current_tree.get_root_val() == '':
                current_tree.insert_left(int(i))
            else:
                current_tree.insert_right(int(i))
        elif i in '+-*/':
            if current_tree.get_root_val() == '':
                current_tree.set_root_val(i)
            elif prec[i] < prec[current_tree.get_root_val()]:
                parent = p_stack.pop()
                parent.insert_left(i)
                current_tree = parent.left_child
                p_stack.push(parent)
            else:
                current_tree.insert_right(i)
                p_stack.push(current_tree)
                current_tree = current_tree.right_child
                current_tree.left_child, current_tree.right_child = current_tree.right_child, current_tree.left_child
        elif i == ')':
            current_tree = p_stack.pop()
        else:
            print(i)
            raise ValueError
    return e_tree
            
    

def evaluate(parse_tree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

    left = parse_tree.get_left_child()
    right = parse_tree.get_right_child()

    if left and right:
        fn = opers[parse_tree.get_root_val()]
        return fn(evaluate(left), evaluate(right))
    else:
        return parse_tree.get_root_val()

def postorder_eval(tree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
    res1 = None
    res2 = None
    if tree:
        res1 = postorder_eval(tree.get_left_child())
        res2 = postorder_eval(tree.get_right_child())
        if res1 and res2:
            return opers[tree.get_root_val()](res1, res2)
        else:
            return tree.get_root_val()

def print_exp(tree):
    str_val = ''
    if tree and tree.right_child and tree.left_child:
        str_val += '(' + print_exp(tree.get_left_child())
        str_val += str(tree.get_root_val())
        str_val += print_exp(tree.get_right_child()) + ')'
    elif tree:
        str_val += ' ' + str(tree.get_root_val()) + ' '
    return str_val

def true_split(exp):
    current = ''
    r_list = list()
    for i in exp:
        if i == ' ':
            pass
        elif i not in '+-/*()':
            current += i
        else:
            if current != '':
                r_list.append(current)
            r_list.append(i)
            current = ''
    if current != '':
        r_list.append(current)
    return r_list

def calc():
    print('Enter q to quit.')
    user_input = input()
    while user_input != 'q':
        print(evaluate(build_parse_tree(user_input)))
        print('Enter q to quit.')
        user_input = input()
        

def preorder(tree):
    if tree:
        print(tree.get_root_val())
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())

def postorder(tree):
    if tree != None:
        postorder(tree.get_left_child())
        postorder(tree.get_right_child())
        print(tree.get_root_val())

def inorder(tree):
    if tree != None:
        inorder(tree.get_left_child())
        print(tree.get_root_val())
        inorder(tree.get_right_child())



