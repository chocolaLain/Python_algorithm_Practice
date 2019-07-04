# @Time    : 4/22 0022 20:36
# @Author  : Lain
class SweetPotato:
    def __init__(self):
        self.cookedlevel = 0
        self.cookedstring = "生的"


    def __str__(self):
        return "地瓜的生熟程度为：%s\n等级为：%d" % (self.cookedstring, self.cookedlevel)


    #烤地瓜
    def cook(self, times):
        self.cookedlevel += times
        if self.cookedlevel >8:
            self.cookedstring = "焦了"
        elif self.cookedlevel >5:
            self.cookedstring = "熟了"
        elif self.cookedlevel >3:
            self.cookedstring = "半生不熟"
        else:
            self.cookedstring = "生的"


diGua = SweetPotato()
print(diGua)

diGua.cook(1)
print(diGua)
diGua.cook(2)
print(diGua)
diGua.cook(3)
print(diGua)
diGua.cook(4)
print(diGua)
diGua.cook(1)
print(diGua)