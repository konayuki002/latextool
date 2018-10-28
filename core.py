class Statement:
    def __init__(self):
        self.strformat = ""
        self.value = []
    def strout(self):
        strvalue = []
        for v in self.value:
            if type(v) == type(''):
                strvalue.append(v)
            else:
                strvalue.append(v.strout())
        tempformat = self.strformat
        for i in range(len(strvalue)):
            tempformat = tempformat.replace('#' + str(i), strvalue[i])
        return tempformat
    def setvalue(self, index, value):
        self.value[index] = value
    def getvalue(self, index):
        return self.value[index]

class Equation(Statement):
    def __init__(self):
        super().__init__()
        self.strformat = "#0 = #1"
        self.value = [" ", " "]
class Frac(Statement):
    def __init__(self):
        super().__init__()
        self.strformat = "\\frac{#0}{#1}"
        self.value = [" ", " "]

command = "Right: ri, Left: l, frac: f, remove: r, number: each number"
print("hello! new expression has just generated!")
expression = Equation()
expression.setvalue(0,Frac())
expression.getvalue(0).setvalue(0,"a")
expression.getvalue(0).setvalue(1,"b")
expression.setvalue(1,"c")
print(expression.strout())
print(command)
while True:
    strin = input()
    print(strin)