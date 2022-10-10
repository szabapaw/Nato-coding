import pandas

data=pandas.read_csv('nato_phonetic_alphabet.csv')

word=input('Type the word: ').upper()
dict_={row.letter:row.code for(index,row) in data.iterrows()}
code=[dict_[letter] for letter in word]
print(code)


# for i in word:
#     for (index, row) in data.iterrows():
#         if row.letter in i:
#             print(row.code)











