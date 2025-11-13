import pandas as pd
#get the data here from the other file location
data = pd.read_csv("nato_phonetic_alphabet.csv")

#create Dictionary that has a key and value of NATO phonetic alphabet
phonetic_dict = {row.letter:row.code for (index,row) in data.iterrows()}
def converted_to_nato_phonetics():

    word = input("Enter a word: ").upper()
    try:
        converted_word = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        converted_to_nato_phonetics()

    else:
        print(converted_word)

converted_to_nato_phonetics()



