import string
import argparse
import random

parser = argparse.ArgumentParser(description = "Create strong passwords using a simple string builder")
parser.add_argument("-l", help="Set length of generated passwords", type=int)
parser.add_argument("-g", help="Set number of generated passwords", type=int)
parser.add_argument("-s", help="Set use of symbols in generated passwords", action="store_true")
parser.add_argument("-n", help="Set use of numbers in generated passwords", action="store_true")

args = parser.parse_args()

password_length = args.l or 8
number_of_passwords = args.g or 1
include_symbols = args.s
include_numbers = args.n



def generate_password(length, include_symbols, include_numbers):
    characters = string.ascii_letters
	
    if include_symbols:
       characters += string.punctuation
		
    if include_numbers:
        characters += string.digits

    password = ''.join(random.choice(characters) for _ in range (length))
    return password


passwords = '\n'.join(generate_password(password_length, include_symbols, include_numbers) for _ in range(number_of_passwords))


print(passwords)
