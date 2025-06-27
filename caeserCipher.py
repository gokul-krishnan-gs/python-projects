def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if char in alphabet:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
        else:
            encrypted_text += char
            
    print(f"\nEncrypted Text : {encrypted_text}\n")

text = input("\nEnter a message : ")
shift = int(input("Enter the offset value : "))
caesar(text, shift)
