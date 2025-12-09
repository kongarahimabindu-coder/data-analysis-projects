my_string = "LaunchCode"


# a) Use string methods to remove the first three characters from the string and add them to the end.

converted = my_string[3:] + my_string[:3]

# Use a template literal to print the original and modified string in a descriptive phrase.

print(f"The original string was '{my_string}', and the modified string is '{converted}'")

# b) Modify your code to accept user input. Query the user to enter the number of letters that will be relocated.

actual = input("Enter a string: ") 
num_letters = 4
converted = actual[num_letters:] + actual[:num_letters]
print(f"The original string was '{actual}', and the modified string is '{converted}'")


# c) Add validation to your code to deal with user inputs that are longer than the word. In such cases, default to moving 3 characters. Also, the template literal should note the error.

actual = input("Enter a string: ") 
num_letters = 6

error_message = ""
if num_letters > len(actual):
    error_message = f"(input too long, defaulting to 3 letters)"
    num_letters = 3

converted = actual[num_letters:] + actual[:num_letters]
print(f"The original string was '{actual}', and the modified string is '{converted}'")

