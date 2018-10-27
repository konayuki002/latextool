command = "Right: <, Left: >, frac: f, remove: r, number: num, if cursor_ is before other statement and make some statement, update the old statement"
expression = 
print("hello! new expression has just generated!")
print("_=")
expression = Equation()
expression.value[0] = Frac()
expression.value[0].value[0] = "a"
expression.value[0].value[1] = "b"
expression.value[1] = "c"
print(expression.strout())
print(command)
while True:
    strin = input()
    print(strin)

class Frac:
    value = [" ", " "]
    #up and down
    def strout():
        for v in value:
            if type(v) != 'str':
                v = v.strout()
        ans = "\\frac{" + value[0] + "}{" + value[1] + "}"
        return ans

class Equation:
    value = [" ", " "]
    def strout():
        for v in value:
            if type(v) != 'str':
                v = v.strout()
        ans = value[0] + " = " + value[1]
        return ans

class String:
    value = ""
    def strout():
        return value