import os

history = []

def get_numbers():
    a = float(input("a: "))
    b = float(input("b: "))
    return a, b

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def view_history():
    if len(history) == 0:
        print ("No history available.")
    else:
        for element in history:
            print(element)

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b==0:
        return "Cannot divide by Zero"
    return a/b

def power(a,b):
    return a**b

def modulus(a,b):
    if b==0:
        return "Cannot divide by Zero"
    return a%b 

def main():
    while True :
        clear_screen()
        print("===Python Calculator===\n\n")
        print("""1. Add
2. Subtract
3. Multiply
4. Divide
5. Power
6. Modulus
7. View History
8. Exit
""")
        choice = int(input("Choice: "))

        if choice == 8:
            print("Goodbye!")
            input("\nPress Enter to exit...")
            break
        elif choice == 7:
            print("Previous operations:  ")
            view_history()
            input("\nPress Enter to continue...")
            continue
        elif choice < 1 or choice > 8:
            print("Invalid Choice!")
            input("\nPress Enter to continue...")
            continue
        

        a,b=get_numbers()

        result=0
        operator=""

        if choice == 1:
            result=add(a,b)
            operator="+"
        elif choice == 2:
            result=subtract(a,b)
            operator="-"
        elif choice == 3:
            result=multiply(a,b)
            operator="*"
        elif choice == 4:
            result=divide(a,b)
            operator="/"
        elif choice == 5:
            result=power(a,b)
            operator="**"
        elif choice == 6:
            result=modulus(a,b)
            operator="%"
        
        
        
        print(f"Result: {result}")
        history.append(f"{a} {operator} {b} = {result}")
        input("\nPress Enter to continue...")





main()    