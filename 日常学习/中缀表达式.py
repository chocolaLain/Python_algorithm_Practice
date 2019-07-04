# @Time    : 4/22 0022 17:33
# @Author  : Lain


from SStack import *
from 课堂练习_逆波兰表达式 import suf_exp_evaluator

priority = {'(':1, '+':3, '-':3, '*':5, '/':5}
infix_opeators = "+-*/()"

def trans_infix_suffix(line):
    if x not in infix_opeators:
        exp.append(x)
    elif st.is_empty()