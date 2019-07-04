class Person:
    def __init__(self, name):
        self._name = name


per = Person('zyf2')
print(per._name)        # 输出zyf2 但是无法直接访问__name

