import random
import string

def generate_password(length, num_special_chars):
    # define the set of characters to choose from
    chars = string.ascii_letters + string.digits
    # randomly select characters for the password
    password = ''.join(random.choices(chars, k=length-num_special_chars))
    # add random special characters
    special_chars = random.choices(string.punctuation, k=num_special_chars)
    password += ''.join(special_chars)
    # shuffle the password
    password = ''.join(random.sample(password, len(password)))
    return password

# prompt the user for input
length = int(input("Enter the length of the password: "))
num_special_chars = int(input("Enter the number of special characters: "))

# generate and print the password
password = generate_password(length, num_special_chars)
print("Your password is:")
print(password)
