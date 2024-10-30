import random
import string

def generate_password(length):
    alphabets = string.ascii_letters  # All letters
    numbers = string.digits             # All digits
    symbols = string.punctuation         # All symbols

    all_characters = alphabets + numbers + symbols

    # Ensure the password contains at least one of each type
    password = [
        random.choice(alphabets),
        random.choice(numbers),
        random.choice(symbols)
    ]

    # Fill the rest of the password length with random choices
    password += random.choices(all_characters, k=length - 3)

    # Shuffle the password list to randomize character order
    random.shuffle(password)

    # Join the list into a single string
    result = "".join(password)
    return result

length = int(input("Enter the length of password: "))
print("Generated password:", generate_password(length))
