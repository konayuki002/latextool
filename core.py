class Frac:
    up = " "
    down = " "
    #up and down
    def strout(self):
        strup, strdown = "", ""
        if type(up) != type(''):
            strup = self.up.strout()
        if type(down) != type(''):
            strdown = self.down.strout()
        ans = "\\frac{" + strup + "}{" + down + "}"
        return ans
    def setup(self, arg):
        self.up = arg
    def setdown(self, arg):
        self.down = arg
    def getup(self):
        return self.up
    def getdown(self):
        return self.down


class Equation:
    left = " "
    right = " "
    def strout(self):
        strleft, strright = "", ""
        if type(left) != type(''):
            strleft = self.left.strout()
        if type(right) != type(''):
            strright = self.right.strout()
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