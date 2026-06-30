print("Python Calculator")

def add_fun():
    a=float(input("a:"))
    b=float(input("b:"))
    return a+b

def sub_fun():
    a=float(input("a:"))
    b=float(input("b:"))
    return a-b

def mul_fun():
    a=float(input("a:"))
    b=float(input("b:"))
    return a*b

def div_fun():
    a=float(input("a:"))
    b=float(input("b:"))
    return a/b

def pow_fun():
    a=float(input("a:"))
    b=float(input("b:"))
    return a**b

def mod_fun():
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


        