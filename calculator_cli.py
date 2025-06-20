import os
import subprocess

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    

def precedance(a):
    precedance = {"+": 1, "-": 1, "*": 2, "/": 2}
    return precedance[a]

def infix_to_postfix(a):
    infix = a
    postfix = []
    stack = []

    for i in infix:
        # if operand
        if i.isalnum():
            # push to postfix
            postfix.append(i)
        # if stack is empty
        elif len(stack) == 0: 
            # push to stack
            stack.append(i)
        # if current operator is of lower precendence than stack top operator
        elif not len(stack) == 0 and precedance(i) < precedance(stack[-1]):
            # push all to stack until stack is empty
            while not len(stack) == 0 and precedance(i) < precedance(stack[-1]):
                postfix.append(stack.pop())
            stack.append(i)
        elif precedance(i) >= precedance(stack[-1]): # if current operator is of higher precendece than stack top operator
            stack.append(i) # push to stack
        else:
            continue

    print(f"Infix: {infix}")
    print(f"Postfix: {postfix}")
    print(f"Stack: {stack}")

    while stack:
        postfix.append(stack.pop())

    print(f"Infix: {infix}")
    print(f"Postfix: {postfix}")
    print(f"Stack: {stack}")

    postfix_to_infix(postfix)


def postfix_to_infix(a):
    postfix = a
    infix = []
    stack = []

    for i in postfix:
        # if operand
        if i.isalnum():
            # push to stack
            stack.append(i)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            print(f"({op2} {i} {op1})")


def clear():
    if os.name == "nt":
        subprocess.run("cls", shell=True)
    else:
        subprocess.run("clear", shell=True)


def memory():
    global history
    history = []


def add_to_memory(a, b):
    entry = {"operation": a, "result": b}
    history.append(entry)
    print(f"Memory saved: {a} = {b}")


def display_memory():
    if not history:
        print("Memory is empty")
    else:
        print("Memory\n")
        for index in range(len(history)):
            entry = history[index]
            print(f"{index + 1}. {entry['operation']} = {entry['result']}")
    print("\n")


def get_previous_result():
    if not history:
        print("Memory is empty")
    else:
        prev_result = history[-1]['result']
        print(f"Previous result: {prev_result}\n")
        return prev_result


def clear_memory():
    history.clear()
    print("Memory cleared\n")


def get_input():
    try:
        print("First: ", end = ' ')
        num1 = int(input())
        print("Second: ", end = ' ')
        num2 = int(input())
        return num1, num2
    except ValueError:
        print("Numeric values only")
        print("Try again")
        return get_input()
    

def display_choice():
    # print("1. Basic arithmetic operations")
    print("1. BODMAS operations")
    print("2. Percentage operations")
    print("3. Show Memory")
    print("4. Clear memory")
    print("5. Clear CLI")
    print("6. Exit\n")

    print("Enter choice: ", end=' ')


def select(choice):
    if choice == 1:
        # basic_arithmetic_operations()
        bodmas_operations()
    elif choice == 2:
        percentage_operations()
    elif choice == 3:
        display_memory()
    elif choice == 4:
        clear_memory()
    else:
        print("Invalid choice")
        print("Try again")


def bodmas_operations():
    print("Enter expression: ", end=' ')
    expression = input()
    infix_to_postfix(expression)

def basic_arithmetic_operations():
    current_result = None

    while True:
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Show Memory")
        print("6. Clear Memory")
        print("7. Get Previous Result")
        print("8. Reset Current Calculation")
        print("9. Back")
        print("10. Exit\n")

        print("Enter choice: ", end=' ')

        choice = int(input())

        if choice == 5:
            display_memory()
            continue
        elif choice == 6:
            clear_memory()
            continue
        elif choice == 7:
            current_result = get_previous_result()
            continue
        elif choice == 8:
            current_result = None
            print("Current calculation reset\n")
            continue
        elif choice == 9:
            break
        elif choice == 10:
            exit()
        else:
            if current_result is not None:
                print(f"Current result: {current_result}\n")
                num1 = current_result
                print("Enter second number: ", end=' ')
                num2 = int(input())
            else:
                print("Enter 2 numbers")
                num1, num2 = get_input()
            
            if choice == 1:
                result = add(num1, num2)
                print(f"output ({num1} + {num2}): {result}\n")
                add_to_memory(str(f"{num1} + {num2}"), result)
            elif choice == 2:
                result = subtract(num1, num2)
                print(f"output ({num1} - {num2}): {result}\n")
                add_to_memory(f"{num1} - {num2}", result)
            elif choice == 3:
                result = multiply(num1, num2)
                print(f"output ({num1} * {num2}): {result}\n")
                add_to_memory(f"{num1} * {num2}", result)
            elif choice == 4:
                result = divide(num1, num2)
                print(f"output ({num1} / {num2}): {result}\n")
                add_to_memory(f"{num1} / {num2}", result)
            else:
                print("Invalid choice")
                print("Try again")

            current_result = result


def percentage_operations():
    current_result = None
    while True:
        print("1. Percentage of a number")
        print("2. Percentage increase/decrease")
        print("3. Percentage of total of a number")
        print("4. Percentage change between 2 numbers")
        print("5. Show Memory")
        print("6. Clear Memory")
        print("7. Get previous result")
        print("8. Reset Current Calculation")
        print("9. Back")
        print("10. Exit\n")

        print("Enter choice: ", end=' ')

        choice = int(input())

        if choice == 5:
            display_memory()
            continue
        elif choice == 6:
            clear_memory()
            continue
        elif choice == 7:
            current_result = get_previous_result()
            continue
        elif choice == 8:
            current_result = None
            print("Current calculation reset\n")
            continue
        elif choice == 9:
            break
        elif choice == 10:
            exit()
        else:
            if current_result is not None:
                print(f"Current result: {current_result}\n")
                num1 = current_result
                print("Enter second number: ", end=' ')
                num2 = int(input())
            else:
                print("Enter 2 numbers")
                num1, num2 = get_input()
            
            print("\n")

            if choice == 1:
                print(f"Number: {num1}\n")
                print(f"Percentage: {num2}%\n")
                print("Calculation: ({num1} / 100) * {num2}\n")
                result = percentage_calculation(num1, num2)
                print(f"Output {num2}% of {num1}: {result}")
                add_to_memory(f"{num2}% of {num1}", result)
            elif choice == 2:
                print(f"Number: {num1}\n")
                print(f"Percentage: {num2}%\n")
                print("1. Increase")
                print("2. Decrease")

                print("Enter choice: ", end=' ')
                if int(input()) == 1:
                    result = percentage_inc(num1, num2)
                    print(f"Calculation: {num1} + ({num2}% of {num1})\n")
                    print(f"Output: {result} (Increased by {num2}%)\n")
                    add_to_memory(f"{num1} + {num2}% of {num1}", result)
                else:
                    result = percentage_dec(num1, num2)
                    print(f"Calculation: {num1} - ({num2}% of {num1})\n")
                    print(f"Output: {result} (Decrease by {num2}%)\n")
                    add_to_memory(f"{num1} - {num2}% of {num1}", result)
            elif choice == 3:
                result = percentage_total(num1, num2)
                print(f"Total: {num1}\n")
                print(f"Number: {num2}\n")
                print(f"Calculation: {num1} / {num2} * 100\n")
                print(f"Output: {result}")
                add_to_memory(f"{num1} / {num2} * 100", result)
            elif choice == 4:
                print(f"Final number: {num1}\n")
                print(f"Initial number: {num2}\n")
                print("1. Increase")
                print("2. Decrease")

                print("Enter choice: ", end=' ')
                if int(input()) == 1:
                    result = percentage_change_inc(num1, num2)
                    print(f"Calculation: ({num1} - {num2}) / {num2} * 100")
                    print(f"Output: {percentage_change_inc(num1, num2)}%")
                    add_to_memory(f"({num1} - {num2}) / {num2} * 100", result)
                else:
                    result = percentage_change_dec(num1, num2)
                    print(f"Calculation: ({num2} - {num1}) / {num2} * 100")
                    print(f"Output: {percentage_change_dec(num1, num2)}%")
                    add_to_memory(f"({num2} - {num1}) / {num2} * 100", result)
            else:
                print("Invalid choice")
                print("Try again")

            current_result = result


def percentage_calculation(a, b):
    return (a / 100) * b


def percentage_inc(a, b):
    return a + ((b / 100) * a)


def percentage_dec(a, b):
    return a - ((b / 100) * a)


def percentage_total(a, b):
    return (a / b) * 100


def percentage_change_inc(a, b):
    return abs((a - b) / a * 100)


def percentage_change_dec(a, b):
    return abs((b - a) / a * 100)


def main():
    # Initialize memory
    memory()

    while True:
        display_choice()

        choice = int(input())

        if choice == 5:
            clear()
            continue

        if choice == 6:
            break
        
        select(choice)


if __name__ == '__main__':
    main()