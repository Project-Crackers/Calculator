def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):


    return a / b

print("\n CALCULATOR")
print("\n Operations:")
print("     1. ADDITION")
print("     2. SUBTRACTION")
print("     3. MULTIPLICATION")
print("     4. DIVISION")

while True:
    choice = input("\n Enter your choice of operation (1 / 2 / 3 / 4): ")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("\n    Enter the FIRST number: "))  
            num2 = float(input("    Enter the SECOND number: "))  
        except ValueError:
            print("\n Invalid input. Please enter a valid number...")
            continue

        if choice == '1':
            print(f"\n        {num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"\n        {num1} - {num2} = {sub(num1, num2)}")
        elif choice == '3':
            print(f"\n        {num1} * {num2} = {mul(num1, num2)}")
        elif choice == '4':
            if num2 == 0 :
                print("\n  --- Cannot be divide by 'zero' ---")
            else :
                print(f"\n        {num1} / {num2} = {div(num1, num2)}")
            

    else:
        print("\n Invalid choice, please select a valid operational choice.")

    nxt_cal = input("\n Do you want to continue with the next calculation? (yes / no): ").lower()
    if nxt_cal == 'no':
        break
