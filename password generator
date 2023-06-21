import random
import string

def generate_password(length, include_uppercase=True, include_lowercase=True, include_special=True):
    """Generate a random password of a given length with customizable character sets."""
    characters = ""
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_special:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character set must be included.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def ask_yes_no_question(prompt):
    """Ask a yes or no question and return True for yes, False for no."""
    while True:
        response = input(prompt + " (y/n): ").strip().lower()
        if response in ["y", "yes"]:
            return True
        elif response in ["n", "no"]:
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def main():
    print("Welcome to the Password Generator!")

    while True:
        print("\nPlease answer the following questions:")
        password_length = int(input("Desired password length: "))

        include_uppercase = ask_yes_no_question("Include uppercase letters?")
        include_lowercase = ask_yes_no_question("Include lowercase letters?")
        include_special = ask_yes_no_question("Include special characters?")

        try:
            generated_password = generate_password(password_length, include_uppercase, include_lowercase, include_special)
            print("Generated Password:", generated_password)
        except ValueError as error:
            print("Error:", str(error))

        repeat = ask_yes_no_question("\nGenerate another password?")
        if not repeat:
            break

    print("Thank you for using the Password Generator!")

if __name__ == "__main__":
    main()
