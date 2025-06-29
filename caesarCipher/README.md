# 🛡️ Caesar Cipher - Python Implementation

This is a simple **Caesar Cipher** implementation in Python. The Caesar Cipher is one of the oldest encryption techniques. It works by shifting each letter in the plaintext by a fixed number of positions down the alphabet.

## 📜 What This Project Does

This Python script:

- Takes a message input from the user.
- Takes an offset value (shift number).
- Encrypts the message using the Caesar Cipher method.
- Displays the encrypted text.


3. **Enter your message** when prompted.

4. **Enter an offset value** (e.g., 3).

5. The program will display the **encrypted message** using Caesar Cipher logic.

### Example

```
Enter a message : hello world
Enter the offset value : 3

Encrypted Text : khoor zruog
```

## 🧠 How It Works

- Only lowercase alphabet characters are shifted.
- Non-letter characters (like spaces or punctuation) are left unchanged.
- Shifting wraps around the alphabet using `%` to stay within bounds.
