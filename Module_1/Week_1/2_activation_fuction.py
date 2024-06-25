import math


def is_number(n):
    try:
        float(n)
        return True
    except ValueError:
        return False


def activation_function(x, function_name):
    # Check if x is a number
    if not is_number(x):
        print("x must be a number")
        return

    # Convert x to float
    x = float(x)

    # Validate the activation function name
    if function_name not in ['sigmoid', 'relu', 'elu']:
        print(f"{function_name} is not supported")
        return

    # Compute the activation function
    if function_name == 'sigmoid':
        result = 1 / (1 + math.exp(-x))
    elif function_name == 'relu':
        result = max(0, x)
    elif function_name == 'elu':
        alpha = 0.01
        result = x if x > 0 else alpha * (math.exp(x) - 1)

    # Print the result
    print(f"{function_name}: f({x}) = {result}")


# Example usage
activation_function(1.5, 'sigmoid')
activation_function('thinh', 'relu')
activation_function(100, 'belu')
