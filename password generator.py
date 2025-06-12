import random
import string

def generate_password(length):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")

    # Character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure one character from each category
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Remaining characters
    all_chars = lowercase + uppercase + digits + symbols
    password += random.choices(all_chars, k=length - 4)

    # Shuffle to avoid predictable order
    random.shuffle(password)

    return ''.join(password)

# Get input from user
try:
    user_length = int(input("Enter the desired password length (minimum 4): "))
    password = generate_password(user_length)
    print("Generated Password:", password)
except ValueError as e:
    print("Error:", e)
