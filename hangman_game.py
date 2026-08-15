#hangman game
import random

Listofwords = ["chair", "football", "sailor", "watermelon", "moon"]
word = random.choice(Listofwords)

N = 6
found_letters = []  # letters confirmed so far, across turns

while N > 0:
    guess = input("guess the word: ")
    a = 0

    if word == guess:
        print("correct!")
        break
    else:
        for letter in guess:
            if letter in word and letter not in found_letters:
                found_letters.append(letter)
                a += 1
                # show every position this letter appears at
                positions = []
                i = 0
                while i < len(word):
                    if word[i] == letter:
                        positions.append(i + 1)
                    i += 1
                print("the word contains the letter", letter, "at position(s):", positions)

        if a == 0:
            N -= 1
            print(N, "attempts left.")

        print("Letters found so far:", found_letters)

print("The correct word is:", word)