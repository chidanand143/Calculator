def calculator():
    """
    A simple command-line calculator app.
    """
    print("🚀 Simple Command-Line Calculator")
    print("--------------------------------")
    print("Operations: +, -, *, /")
    print("Enter 'quit' to exit.")

    while True:
        # Get user input for the calculation
        user_input = input("Enter a calculation (e.g., 5 + 3): ")

        # Check for the exit command
        if user_input.lower() == 'quit':
            print("Exiting calculator. Goodbye!")
            break

        try:
            # Use eval() to parse and evaluate the user input string as a Python expression
            result = eval(user_input)
            print("Result:", result)
        except (NameError, TypeError, SyntaxError, ZeroDivisionError) as e:
            # Handle various potential errors gracefully
            if isinstance(e, ZeroDivisionError):
                print("Error: Cannot divide by zero.")
            else:
                print("Invalid input. Please enter a valid calculation.")
                print("Example: 5 * 2")

if __name__== "__main__":
    calculator()