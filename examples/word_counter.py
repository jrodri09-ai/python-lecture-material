user_string = input("Please type your sentence here.")

spaces_and_letters = ""

# this for loop is used to reduce the string to letters, numbers, and spaces.

for char in user_string:
    if char.isalnum() or char.isspace() or char == "-" or char == "'":
        spaces_and_letters += char

string_list = spaces_and_letters.split()

print(string_list)

num_words_in_string = len(string_list)

print(num_words_in_string)

