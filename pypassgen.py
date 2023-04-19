import generator

# prompt the user for input
length = int(input("Enter the length of the password: "))
num_special_chars = int(input("Enter the number of special characters: "))

# generate and print the password
password = generator.generate_password(length, num_special_chars, '')
print("Your password is:")
print(password)
