# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Letters/starting_letter.txt", "r") as letter_file:
    letter = letter_file.read()

# print(letter)
with open("./Input/Names/invited_names.txt", "r") as list_file:
    name_list = list_file.readlines()
    name_list = [x.strip("\n") for x in name_list]

# print(name_list)
for name in name_list:
    with open(f"./Output/ReadyToSend/Letter_for_{name}.txt", "w") as letter_content:
        letter_content.write(letter.replace("[name]", name))
