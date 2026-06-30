import os
print("Python Calculator")

def get_numbers():
    a = float(input("a: "))
    b = float(input("b: "))
    return a, b

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def add():
    a,b=get_numbers()
    return a+b

def subtrat():
    a,b=get_numbers()
    return a-b

def multiply():
    a,b=get_numbers()
    return a*b

def divide():
    a,b=get_numbers()
    if b==0:
        return "Cannot divide by Zero"
    return a/b

def power():
    a,b=get_numbers()
    return a**b

def modulus():
    a,b=get_numbers()
    if b==0:
        return "Cannot divide by Zero"
    return a%b 

def main():
    while True :
        clear_screen()

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
            print(f"Result: {add()}")
            input("\nPress Enter to continue...")
        elif choice == 2:
            print(f"Result: {subtrat()}")
            input("\nPress Enter to continue...")
        elif choice == 3:
            print(f"Result: {multiply()}")
            input("\nPress Enter to continue...")
        elif choice == 4:
            print(f"Result: {divide()}")
            input("\nPress Enter to continue...")
        elif choice == 5:
            print(f"Result: {power()}")
            input("\nPress Enter to continue...")
        elif choice == 6:
            print(f"Result: {modulus()}")
            input("\nPress Enter to continue...")
        elif choice == 7:
            print("Goodbye!")
            input("\nPress Enter to continue...")
            break
        else:
            print("Invalid Choice!")



main ()    