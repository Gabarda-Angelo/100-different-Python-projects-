import pandas as pd


#get the data here from the other file location
data = pd.read_csv("nato_phonetic_alphabet.csv")




#create Dictionary that has a key and value of NATO phonetic alphabet
phonetic_dict = {row.letter:row.code for (index,row) in data.iterrows()}

print(phonetic_dict)

#Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()

converted_word = [phonetic_dict[letter] for letter in word]

print(converted_word)