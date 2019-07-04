# @Time    : 4/22 0022 16:42
# @Author  : Lain


from SStack import *

class ESStack(SStack):
    def depth(self):
        return len(self._elems)

def suffix_exp_evaluator(line):
    return suf_exp_evaluator(line.split())

def suf_exp_evaluator(exp):
    operators = "+-*/"
    st = ESStack()


    for x in exp:
        if x not in operators:
            st.push(float(x))
            continue

        if st.depth() < 2:
            raise SyntaxError("short of operand(s).")
        a = st.pop()
        b = st.pop()

        if x == "+":
            c = b + a
        elif x == "-":
            c = b - a
        elif x == "*":
            c = b * a
        elif x == "/":
            c = b / a
        else:
            break
        # else分支不可能出现，写在这里是为了清晰
        st.push(c)

    if st.depth() == 1:
        return st.pop()
    raise SyntaxError("Extra operand(s).")


def suffix_exp_caculator():
    while True:
        try:
            line = input("Suffix Expression:")
            if line == "end":
                return
            res = suf_exp_evaluator(line)
            print(res)
        except Exception as ex:
            print("Error:", type(ex), ex.args)


def demo_suffix():
    print(suffix_exp_evaluator("1"))
    print(suffix_exp_evaluator("1 2 +"))
    print(suffix_exp_evaluator("1 3 + 2"))
    print(suffix_exp_evaluator("1 3 + 2 5 - *"))


if __name__ == "__main__":
    demo_suffix()
