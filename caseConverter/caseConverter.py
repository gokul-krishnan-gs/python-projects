# Function to convert a PascalCase or camelCase string into snake_case
def convert_to_snake_case(pascal_or_camel_cased_string):
    # Create an empty list to store parts of the snake_case string
    snake_cased_character_list = []

    # Loop through each character in the input string
    for char in pascal_or_camel_cased_string:
        # If the character is uppercase, it's likely the start of a new word
        if char.isupper():
            # Convert it to lowercase and prefix with an underscore
            converted_character = '_' + char.lower()
            # Add it to the list
            snake_cased_character_list.append(converted_character)
        else:
            # If it's lowercase, just add it as-is
            snake_cased_character_list.append(char)

    # Join the list into a single string
    snake_cased_string = "".join(snake_cased_character_list)

    # Remove any leading underscore (in case the string starts with uppercase)
    clean_snake_cased_string = snake_cased_string.strip('_')

    # Return the final snake_case result
    return clean_snake_cased_string


# Main function to take user input and show the converted result
def main():
    # Prompt user for camelCase or PascalCase input
    word = input("Enter camelCase/PascalCase string: ")
    
    # Convert the input and print the snake_case version
    print(convert_to_snake_case(word))


# Run the program
main()
