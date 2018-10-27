class Equation:
    left = " "
    right = " "
    def strout(self):
        strleft, strright = "", ""
        if type(self.left) != type(''):
            strleft = self.left.strout()
        else:
            strleft = self.left
        if type(self.right) != type(''):
            strright = self.right.strout()
        else:
            strright = self.right
        ans = strleft + "=" + strright
        return ans
    def setleft(self, arg):
        self.left = arg
    def setright(self, arg):
        self.right = arg
    def getleft(self):
        return self.left
    def getright(self):
        return self.right

class Statement:
    def strout(self):
        strvalue = []
        for v in self.value:
            if type(v) == type(''):
                strvalue.push(v)
            else:
                strvalue.push(v.strout())
        return 
        tempformat = self.strformat
        for i in range(len(strvalue)):
            tempformat = tempformat.replace('#' + i, strvalue[i])
        return tempformat
    def setvalue(self, index, value):
        self.value[index] = value
    def getvalue(self, index):
        return self.value[index]

class Equation(Statement):
    strformat = "#0=#1"
    value = [" ", " "]
class Frac(Statement):
    strformat = "\\frac{#0}{#1}"
    value = [" ", " "]

command = "Right: <, Left: >, frac: f, remove: r, number: num, if cursor_ is before other statement and make some statement, update the old statement"
print("hello! new expression has just generated!")
print("_=")
print(Frac())
frac = Frac()
frac.setvalue(0,"a")
frac.setvalue(1,"b")
expression = Equation()
expression.setvalue(0,frac)
expression.setvalue(1,"c")
print(expression.strout())
print(command)
while True:
    strin = input()
    print(strin)