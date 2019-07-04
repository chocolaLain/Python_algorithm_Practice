class ClassName(object):
    ins = 0
    """测试方法"""
    def __init__(self):
        ClassName.ins += 1
    
    @classmethod
    def rate():
        return classmethod.ins


fr = ClassName()
print(fr.ins)

sc = ClassName()
print(sc.ins)
