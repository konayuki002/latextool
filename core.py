class Frac:
    value = [" ", " "]
    #up and down
    def strout(self):
        for v in self.value:
            if type(v) != type(''):
                v = v.strout()
        ans = "\\frac{" + self.value[0] + "}{" + self.value[1] + "}"
        return ans
    def setup(self, arg):
        self.value[0] = arg
    def setdown(self, arg):
        self.value[1] = arg
    def getup(self):
        return self.value[0]
    def getdown(self):
        return self.value[1]


class Equation:
    value = [" ", " "]
    def strout(self):
        for v in self.value:
            if type(v) != type(''):
                v = v.strout()
        ans = value[0] + " = " + value[1]
        return ans
    def setleft(self, arg):
        self.value[0] = arg
    def setright(self, arg):
        self.value[1] = arg
    def getleft(self):
        return self.value[0]
    def getright(self):
        return self.value[1]

class String:
    value = ""
    def strout(self):
        return self.value

command = "Right: <, Left: >, frac: f, remove: r, number: num, if cursor_ is before other statement and make some statement, update the old statement"
print("hello! new expression has just generated!")
print("_=")
print(Frac())
frac = Frac()
frac.setup("a")
frac.setdown("b")
expression = Equation()
expression.setleft(frac)
expression.setright("c")
print(expression.strout())
print(command)
while True:
    strin = input()
    print(strin)