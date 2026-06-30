print("Python Calculator")

def Add():
    a=float(input("a:"))
    b=float(input("b:"))
    return a+b

def Subtrat():
    a=float(input("a:"))
    b=float(input("b:"))
    return a-b

def Multiply():
    a=float(input("a:"))
    b=float(input("b:"))
    return a*b

def Divide():
    a=float(input("a:"))
    b=float(input("b:"))
    return a/b

def Power():
    a=float(input("a:"))
    b=float(input("b:"))
    return a**b

def Modulus():
    a=float(input("a:"))
    b=float(input("b:"))
    return a%b 

def main():
    while True :
        print("""1. Add
2. Subtract
3. Multiply
4. Divide
5. Power
6. Modulus
7. Exit
""")
        choice = input("Choice: ")


        