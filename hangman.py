#Simple word guessing game to practice core coding concepts
import random
def getword():
    with open('word_list.txt', 'r') as f:
        word_list = []
        for line in f.readlines():
            word_list.append(line.strip())
        word = word_list[random.randint(0, len(word_list))]
        return word
#Compares guessed word to the word we are trying to our word from word list.
def guess_word(guess):
    if guess in word:
        for i, j in enumerate(word):
            if guess == j:
                guessed_word[i] = word[i]
def unpack_hangman():
    hangman = []
    with open("hangman.txt", "r") as f:
        for line in f.readlines():
            hangman.append(line.strip('\n'))
    return hangman


word = getword()
guessed_word = ['*'] * len(word)
hangman = unpack_hangman()
hangman_line = 0
while ''.join(guessed_word) != word:
    guess = input("Guess a letter in the word: ")
    guess_word(guess)
    if guess not in word:
        for i in hangman[0:hangman_line]:
            print(i)
        hangman_line += 1
        if hangman_line >= len(hangman):
            print("Oh no! You lost!")
            print(f"The word was {word}.")
            break
    print(''.join(guessed_word))
    if ''.join(guessed_word) == word:
        print("Congradulations! You guessed the word!")
