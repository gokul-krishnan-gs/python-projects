def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    # Raise an error if the input is negative (square root of negative number is not real)
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers.')

    # Handle special case when input is 0
    if square_target == 0:
        print(f"Square root of {square_target} is 0")
        return 0

    # Handle special case when input is 1
    if square_target == 1:
        print(f"Square root of {square_target} is 1")
        return 1

    # Initialize the range for bisection
    low = 0
    high = max(1, square_target)  # For numbers < 1, we set high to 1
    root = None  # Will store the final result once found

    # Loop to apply bisection up to max_iterations times
    for iteration in range(1, max_iterations + 1):
        mid = (low + high) / 2           # Midpoint of the current interval
        square_mid = mid ** 2            # Square of the midpoint

        # Check if the result is close enough to the target
        if abs(square_mid - square_target) < tolerance:
            root = mid                   # Found a sufficiently accurate result
            break                        # Exit the loop

        # If mid squared is less than target, move to the right half
        elif square_mid < square_target:
            low = mid
        # If mid squared is greater than target, move to the left half
        else:
            high = mid

    # After looping, check if a result was found
    if root is None:
        print(f"Failed to converge within {max_iterations} iterations.")
        return None
    else:
        print(f"\nThe square root of {square_target} is approximately {root:.10f}")
        return root


def main():
    try:
        # Take input from the user
        x = int(input("Enter the number to find square root: "))
        # Call the square root bisection function
        square_root_bisection(x)
    except ValueError:
        # Handle non-integer or invalid inputs
        print("Please enter a valid non-negative number.")

# Start the program
main()
