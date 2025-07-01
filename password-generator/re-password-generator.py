# Import required modules
import re            # For regex-based pattern matching
import secrets       # For secure random generation (better than random for passwords)
import string        # Provides pre-made strings like ascii_letters, digits, punctuation

# Function to generate the password based on user-defined constraints
def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    # Validate if total required characters exceed the specified password length
    if nums + special_chars + uppercase + lowercase > length:
        raise ValueError("Total required characters exceed the password length")

    # Define character sets
    letters = string.ascii_letters        # a-z and A-Z
    digits = string.digits                # 0-9
    symbols = string.punctuation          # Special characters like !@#$%^&*

    # Combine all characters into one pool to randomly pick from
    all_characters = letters + digits + symbols

    # Keep trying until we generate a password that satisfies all constraints
    while True:
        # Randomly generate a password of the specified length
        password = ''.join(secrets.choice(all_characters) for _ in range(length))

        # Define constraints with corresponding regex patterns
        constraints = [
            (nums, r'\d'),                                  # Digits: 0–9
            (special_chars, fr'[{re.escape(symbols)}]'),    # Special characters
            (uppercase, r'[A-Z]'),                          # Uppercase letters
            (lowercase, r'[a-z]')                           # Lowercase letters
        ]

        # Check if the password meets all the constraints using regex pattern matching
        if all(
            required <= len(re.findall(pattern, password))  # Count matches and compare
            for required, pattern in constraints
        ):
            return password  # Valid password found, return it

# Main program to interact with the user
def main():
    try:
        print("\nPASSWORD GENERATOR!\n")

        # Get inputs from the user
        length = int(input("Enter the password length: "))
        nums = int(input("Enter the minimum number of digits: "))
        special = int(input("Enter the minimum number of special characters: "))
        uppercase = int(input("Enter the minimum number of uppercase letters: "))
        lowercase = int(input("Enter the minimum number of lowercase letters: "))

        # Call the function to generate the password
        new_password = generate_password(length, nums, special, uppercase, lowercase)

        # Display the generated password
        print("\nGenerated Password:", new_password)

    # Handle non-integer input errors
    except ValueError:
        print("Please enter valid integer numbers.")
    # Handle any other unexpected errors
    except Exception as e:
        print("Error:", e)

# Start the program
main()
