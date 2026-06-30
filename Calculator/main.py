print("Python Calculator")

def get_numbers():
    a = float(input("a: "))
    b = float(input("b: "))
    return a, b

def Add():
    a,b=get_numbers()
    return a+b

def Subtrat():
    a,b=get_numbers()
    return a-b

def Multiply():
    a,b=get_numbers()
    return a*b

def Divide():
    a,b=get_numbers()
    return a/b

def Power():
    a,b=get_numbers()
    return a**b

def Modulus():
    a,b=get_numbers()
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


        