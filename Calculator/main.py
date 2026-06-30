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
        choice = int(input("Choice: "))

        if choice == 1:
            print(f"Result: {Add()}")
        elif choice == 2:
            print(f"Result: {Subtrat()}")
        elif choice == 3:
            print(f"Result: {Multiply()}")
        elif choice == 4:
            print(f"Result: {Divide()}")
        elif choice == 5:
            print(f"Result: {Power()}")
        elif choice == 6:
            print(f"Result: {Modulus()}")
        elif choice == 7:
            print("Goodbye!")
            break
        else:
            print("Invalid Choice!")



main ()    