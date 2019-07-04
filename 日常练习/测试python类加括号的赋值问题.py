class ClassName(object):
    """docstring for ClassName"""
    def __init__(self, arg02 = None):
        self.arg = 3
        self.arg02 = arg02


c = ClassName
print(c)
print(c == ClassName)
c.arg02 = 1
print(ClassName.arg02)
print(c.arg02)

print("----------分割线----------")

b = ClassName(4)
print(b)
print(b == ClassName)
print(ClassName.arg02)
print(b.arg02)
b.arg02 = 3
print(ClassName.arg02)
print(b.arg02)

        