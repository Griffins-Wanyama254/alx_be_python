def perform_operation(num1: float, num2: float, operation: str):
    """
    Perform basic arithmetic operations.

    Parameters:
        num1 (float): first number
        num2 (float): second number
        operation (str): 'add', 'subtract', 'multiply', or 'divide'

    Returns:
        float | str: numeric result or an error message
    """
    op = operation.strip().lower()

    if op == "add":
        return num1 + num2
    elif op == "subtract":
        return num1 - num2
    elif op == "multiply":
        return num1 * num2
    elif op == "divide":
        if num2 == 0:
            return "Error: Division by zero is not allowed"
        return num1 / num2
    else:
        return "Error: Invalid operation"
