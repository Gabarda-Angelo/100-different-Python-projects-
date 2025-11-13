#TODO: Create a letter using starting_letter.txt
#format letters for everyone
with open("../Mail Merge Project Start/Input/Letters/starting_letter.txt") as file:
    format_letter = file.read()


with open("../Mail Merge Project Start/Input/Names/invited_names.txt", "r") as name_file:
    for name in name_file:
        invited_name = name.strip()
        with open(f"letter_for_{invited_name}.txt", mode="w") as file:
            txt = format_letter
            new_letter = txt.replace("[name]", f"{invited_name}")
            file.write(new_letter)

    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp