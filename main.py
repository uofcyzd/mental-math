import random, sys, xlsxwriter

def add(x,y):
    return(x+y)

def subtract(x,y):
    return(x-y)

def multiply(x,y):
    return(x*y)

def divide(x,y):
    return(x/y)

def rng(o):

    if o == "a":
        x = random.randint(10,99)
        y = random.randint(10,99)
        return([x,y])
    elif o == "b":
        x = random.randint(100,999)
        y = random.randint(10,99)
        return([x,y])
    elif o == "c":
        x = random.randint(100,999)
        y = random.randint(100,999)
        return([x,y])
    elif o == "d":
        x = random.randint(1000,9999)
        y = random.randint(100,999)
        return([x,y])


def game(x,y):

    while True:
        values = rng(y)
        while True:
            try:
                print(values)
                guess = int(input("{} {}".format(name(x), "the 2 numbers (enter 0 to quit): ")))
                break
            except ValueError:
                print("Invalid selection detected")

        if (guess == 0 and options(x, values) != 0): #Unfortunately, the terrible workaround for when 0 is the answer
            break
        elif guess == options(x,values):
            print("Correct")
        else:
            print("Incorrect")



def options(x, terms):
    if x == "a":
        return(add(terms[0], terms[1]))
    elif x == "b":
        return(subtract(terms[0],terms[1]))
    elif x == "c":
        return(multiply(terms[0],terms[1]))
    else:
        return(math.floor(divide(terms[0],terms[1]))) #so far inputs only looks at integer inputs; change later


def name(x):
    if x == "a":
        return("sum")
    elif x == "b":
        return("difference")
    elif x == "c":
        return("multiply")
    else:
        return("divide")

def optionSelect():
    while True:
        try:
            select = input("(a) 2 by 2, (b) 3 by 2, (c) 3 b 3, (d) 4 by 3, (q) quit: ")
            options = {"a","b","c","d","q"}
            if select not in options:
                print("Incorrect selection, please try again.")

            elif select == "q":
                sys.exit(0)
            elif select == "a":
                return("a")
            elif select == "b":
                return("b")
            elif select == "c":
                return("c")
            else:
                return("d")
        except ValueError:
            print("Incorrect selection, please try again.")





def gameSelect():
    while True:
        try:
            test = input("(a) addition, (b) subtraction, (c) multiplication, (d) division, (q) quit: ")
            options = {"a","b","c","d","q"}
            if test not in options:
                print("Incorrect selection, please try again.")
            elif test == "q":
                sys.exit(0)
            elif test == "a":
                return("a")
            elif test == "b":
                return("b")
            elif test == "c":
                return("c")
            else:
                return("d")

        except ValueError:
            print("Incorrect selection, please try again.")


game(gameSelect(),optionSelect())

'''
workbook = xw.WorkBook('Demo.xlsx')
wsHello = workbook.add_worksheet(name = 'Hello')
ws2 = workbook.add_worksheet()

wsHello.write('A1','Hello')
wsHello.write(1,0,'Goodbye')

workbook.close()
'''
