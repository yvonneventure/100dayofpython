#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
import pandas
nato=pandas.read_csv("nato_phonetic_alphabet.csv")
rows=nato.iterrows()
#print(nato)
list={row.letter: row.code for (index,row) in rows}
print(list)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user=input("Enter a word: ").upper()
result=[code for (letter,code) in list.items() if letter in user]
print(result)

