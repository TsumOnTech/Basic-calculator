print("\tBasic Calculator")

while True:
    try:
        op = input("Enter operator (+, -, *, /, q): ")
        if op == 'q':
            break
        elif op in ('+', '-', '*', '/'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                if num2 == 0:
                    print("Error: Cannot divide by zero!")
                    continue
                result = num1 / num2

            print(f"Result: {result}")
        else:
            print("Invalid operator. Please use +, -, *, / or q to quit")

    except ValueError:
        print("Invalid number input! Please try again.")