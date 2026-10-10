sentence = input("Ведіть речення: ")

words = sentence.split()

print("Слова з літерою 'о':")

for word in words:
    if "о" in word.lower():
        print(word)