#Password Generator Project
import random
import string

# Create a variable named letters containing both lowercase and uppercase letters
letters = list(string.ascii_lowercase + string.ascii_uppercase)

# Create a variable named numbers containing numbers from 0 to 9
numbers = list(map(str, range(10)))

# Create a variable named symbols containing common symbols
#symbols = list(string.punctuation)
symbols = ['!','@','#','$','%','&','+','*','(',')']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#Eazy Level
# password = ""

# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)

# print(password)

#Hard Level
password_list = []


for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

#print(password_list)
random.shuffle(password_list)
#print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")

# END OF CODE
