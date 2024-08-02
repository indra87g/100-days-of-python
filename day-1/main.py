"""
Day 1 - Simple Calculator
"""

num1 = int(input("Enter the first number:"))
operator = str(input("Enter the operator:"))
num2 = int(input("Enter the second number:"))


def main():
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        print("Invalid operators!")
        main()

    print(
        f"""
          ====== RESULT ======
          {num1} {operator} {num2} = {result}
          Thanks for using this app.
          ====================
          """
    )


if __name__ == "__main__":
    main()
