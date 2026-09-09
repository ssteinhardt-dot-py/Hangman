#Simple word guessing game to practice core coding concepts
import random
def getword():
    with open('word_list.txt', 'r') as f:
        #create an empty array to fill with words from word list file
        word_list = []
        for line in f.readlines():
            #This part is done because without it word_list will get a bunch of random \n strings
            word_list.append(line.strip())
        #picks a random word from the list that we just created
        word = word_list[random.randint(0, len(word_list))]
        return word
#Compares guessed word to the word we are trying to our word from word list.
def guess_word(guess):
    if guess in word:
        #Enumerate is used here to find the index and the letter in word
        for i, j in enumerate(word):
            #If the guess matches a letter in word then assign that letter to the same place in guessed_word
            if guess == j:
                guessed_word[i] = word[i]
def unpack_hangman():
    hangman = []
    #Fetch the ascii art from the hangman.txt file
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
