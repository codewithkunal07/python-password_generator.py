import string
import random

def generate_password(length):
    """Generates a random password using letters, digits, and punctuation."""
    if length < 4:
        return "Password length must be at least 4 characters."

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 Welcome to SecurePasswordGen")
    try:
        length = int(input("Enter desired password length (min 4): "))
        password = generate_password(length)
        print("Generated Password:", password)
    except ValueError:
        print("❗ Please enter a valid number.")

if __name__ == "__main__":
    main()