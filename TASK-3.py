import secrets
import string

def create_secure_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def get_user_input_and_generate_password():
    try:
        length = int(input("Enter the desired password length: "))
        if length < 8:
        
            print("Password length should be at least 8 characters for security.")
        else:
            password = create_secure_password(length)
            print("Generated Password: ", password)
    except ValueError:
        print("Invalid input. Please enter a valid number for password length.")

if __name__ == "__main__":
    get_user_input_and_generate_password()
