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
        print(self.strformat)
        for i in range(len(strvalue)):
            print(tempformat)
            tempformat = tempformat.replace('#' + str(i), strvalue[i])
            print(tempformat)
        print(tempformat)
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

command = "Right: <, Left: >, frac: f, remove: r, number: num, if cursor_ is before other statement and make some statement, update the old statement"
print("hello! new expression has just generated!")
frac = Frac()
print(frac.strformat)
frac.setvalue(0,"a")
frac.setvalue(1,"b")
print(frac.strformat)
print(frac.strout())
expression = Equation()
expression.setvalue(0,frac)
expression.setvalue(1,"c")
print(expression.strout())
print(command)
while True:
    strin = input()
    print(strin)