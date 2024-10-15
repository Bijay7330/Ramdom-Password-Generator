#Password Generator - Hard
import random
letters = ['a' , 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

numbers = ['0', '1','2','3','4','5','6','7','8','9']

symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcome to password generator !")

number_of_letters = int(input("How many letters would you like in your password ? \n"))

number_of_numbers = int(input("How many numbers would you like in your password ? \n"))

number_of_symbols = int(input("How many symbols would you like in your password ? \n"))

password_list= []

for char in range(1,number_of_letters+1):
  random_char = random.choice(letters)
  password_list += random_char


for num in range(1,number_of_numbers+1):
  random_number = random.choice(numbers)
  password_list += random_number

for sign in range(1,number_of_symbols + 1):
  random_sign = random.choice(symbols)
  password_list += random_sign


random.shuffle(password_list)

password=""

for char in password_list:
  password += char

print(password)