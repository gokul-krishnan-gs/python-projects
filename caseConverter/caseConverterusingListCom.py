# Function to convert a camelCase or PascalCase string to snake_case
def convert_to_snake_case(pascal_or_camel_cased_string):
    # Create a list using list comprehension:
    # If the character is uppercase, convert it to lowercase and prefix it with '_'
    # Otherwise, keep the character as-is
    snake_cased_character_list = [
        '_' + char.lower() if char.isupper() else char
        for char in pascal_or_camel_cased_string
    ]

    # Join the list into a single string and remove any leading underscore
    # (in case the original string started with a capital letter)
    return ''.join(snake_cased_character_list).strip('_')

# Main function to interact with the user
def main():
    # Ask the user to input a camelCase or PascalCase string
    word = input("Enter camelCase/PascalCase string: ")

    # Convert the input string to snake_case and print the result
    print(convert_to_snake_case(word))

# Run the main function
main()
