PLACEHOLDER = "[name]"

with open("day_23_invited_names.txt") as names_file:
    names = names_file.readlines()
    # print(names)
    
with open("./day_23/day_23_starting_letter.docx") as letter_file:
    letter_contents = letter_file.read()
    
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        
        with open(f"./day_23_letters/day_23_letter_for_{stripped_name}.docx", mode="w") as completed_letter:
            completed_letter.write(new_letter)
