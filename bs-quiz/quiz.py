def ask3(qs, a1, a2, a3, c, cc):
    print(qs)
    print("A - " + a1)
    print("B - " + a2)
    print("C - " + a3)
    while True:
        a = input("->")
        if a == c or a == cc:
            print("Correct!")
            break
        else:
            print("Wrong!")
def ask4(qs, a1, a2, a3, a4, c, cc):
    print(qs)
    print("A - " + a1)
    print("B - " + a2)
    print("C - " + a3)
    print("D - " + a4)
    while True:
        a = input("->")
        if a == c or a == cc:
            print("Correct!")
            break
        else:
            print("Wrong!")
def ask5(qs, a1, a2, a3, a4, a5, c, cc):
    print(qs)
    print("A - " + a1)
    print("B - " + a2)
    print("C - " + a3)
    print("D - " + a4)
    print("E - " + a5)
    while True:
        a = input("->")
        if a == c or a == cc:
            print("Correct!")
            break
        else:
            print("Wrong!")
def ask6(qs, a1, a2, a3, a4, a5, a6, c, cc):
    print(qs)
    print("A - " + a1)
    print("B - " + a2)
    print("C - " + a3)
    print("D - " + a4)
    print("E - " + a5)
    print("F - " + a6)
    while True:
        a = input("->")
        if a == c or a == cc:
            print("Correct!")
            break
        else:
            print("Wrong!")

def ask(qs, c):
    print(qs)

    while True:
        a = input("->")
        if a == c:
            print("Correct!")
            break
        else:
            print("Wrong!")
