class Frac:
    value = [" ", " "]
    #up and down
    def strout():
        for v in value:
            if type(v) != 'str':
                v = v.strout()
        ans = "\\frac{" + value[0] + "}{" + value[1] + "}"
        return ans
    def setup(arg):
        value[0] = arg
    def setdown(arg):
        value[1] = arg
    def getup():
        return value[0]
    def getdown():
        return value[1]


class Equation:
    value = [" ", " "]
    def strout():
        for v in value:
            if type(v) != 'str':
                v = v.strout()
        ans = value[0] + " = " + value[1]
        return ans
    def setleft(arg):
        value[0] = arg
    def setright(arg):
        value[1] = arg
    def getleft():
        return value[0]
    def getright():
        return value[1]

class String:
    value = ""
    def strout():
        return value

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