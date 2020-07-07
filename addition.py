import random

def sum(a,b):
    return(a+b)

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


def gameState(s):
    i = 0
    while i == 0:
        while True:
            x = rng(s)
            try:
                print(x)
                val = int(input("enter sum of the 2 numbers (enter 0 to quit): "))
                if val == sum(x[0],x[1]):
                    print("Correct")
                elif val == 0:
                    i = 1
                    break
                else:
                    print("Incorrect")
                break

            except ValueError:
                print("invalid selection detected; please input an integer")

def main():

    print("Welcome to mental arithmetic - addition!")

    while True:
        try:
            val  = input("select option of practice: (a) 2 by 2, (b) 3 by 2, (c) 3 by 3, (d) 4 by 3, (q) quit: ")
            options = {"a","b","c","d","q"}
            if val not in options:
                print("invalid selection detected; please input the letter inside () for choice")
                main()
            elif val == 'q':
                break
            else:
                gameState(val)
            break
        except ValueError:
            print("invalid selection detected; please input the letter inside () for choice")







main()
