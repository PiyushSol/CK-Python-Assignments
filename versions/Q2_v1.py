import random
import string
import re

uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
numbers = string.digits
special = "!@#$%&*"


def generate_password():

    password_chars = []

    password_chars.append(random.choice(uppercase))
    password_chars.append(random.choice(lowercase))
    password_chars.append(random.choice(numbers))
    password_chars.append(random.choice(numbers))
    password_chars.append(random.choice(special))

    
    all_chars = uppercase + lowercase + numbers + special

    while len(password_chars) < 16:
        char = random.choice(all_chars)

        if char not in password_chars:
            password_chars.append(char)

    random.shuffle(password_chars)

    return "".join(password_chars)


def validate_password_regex(password):

    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=(?:.*\d){2,})(?=.*[!@#$%&*])[A-Za-z\d!@#$%&*]{16}$'

    if not re.match(pattern, password):
        print("Regex Validation: Password format requirements not satisfied")
        return

    if len(set(password)) != len(password):
        print("Regex Validation: Password contains repeating characters")
        return

    print("Regex Validation: Password is valid")


def validate_password_no_regex(password):

    if len(password) != 16:
        print("Manual Validation: Password must be 16 characters")
        return

    if len(set(password)) != 16:
        print("Manual Validation: Password contains repeating characters")
        return

    upper = lower = digits = special_count = 0

    for ch in password:

        if ch.isupper():
            upper += 1

        elif ch.islower():
            lower += 1

        elif ch.isdigit():
            digits += 1

        elif ch in "!@#$%&*":
            special_count += 1

        else:
            print("Manual Validation: Invalid character found")
            return

    if upper < 1:
        print("Manual Validation: Must contain at least one uppercase letter")
        return

    if lower < 1:
        print("Manual Validation: Must contain at least one lowercase letter")
        return

    if digits < 2:
        print("Manual Validation: Must contain at least two numbers")
        return

    if special_count < 1:
        print("Manual Validation: Must contain at least one special character")
        return

    print("Manual Validation: Password is valid")



password = generate_password()

print("Generated Password:", password)

print()

validate_password_regex(password)
validate_password_no_regex(password)