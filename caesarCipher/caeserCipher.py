# Define the Caesar cipher encryption function
def caesar(message, offset):
    # Define the alphabet to be used for shifting
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    # Initialize the encrypted text as an empty string
    encrypted_text = ''
    
    # Loop through each character in the input message (converted to lowercase)
    for char in message.lower():
        # If the character is a letter in the alphabet
        if char in alphabet:
            # Find the index of the character in the alphabet
            index = alphabet.find(char)
            # Calculate the new index after applying the offset (with wrap-around using %)
            new_index = (index + offset) % len(alphabet)
            # Append the encrypted character to the result
            encrypted_text += alphabet[new_index]
        else:
            # If the character is not a letter (like space or punctuation), add it as-is
            encrypted_text += char

    # Display the encrypted result
    print(f"\nEncrypted Text : {encrypted_text}\n")


# Prompt the user to enter a message
text = input("\nEnter a message : ")

# Prompt the user to enter the offset value for encryption
shift = int(input("Enter the offset value : "))

# Call the Caesar function with the user-provided message and offset
caesar(text, shift)
