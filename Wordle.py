import random
from termcolor import colored

# Change the number of letters if you wish longer words
n_letters = 5

file_dict = open("/home/davood/Downloads/sowpods.txt")
wordle_dict = file_dict.read().split('\n')
wordle = [w for w in wordle_dict if len(w) == n_letters and len(set(w))>(n_letters-2)] 

Word_of_the_day = wordle[random.randint(0, len(wordle)-1)]

n_guess = n_letters
counter = 0

while counter < n_guess:
    correct = 0
    guess = input(f"Guess a {n_letters} letter word: ").upper()
    if len(guess) != n_letters:
        print("Wrong SIZE!")
        continue
    
    colors = ['white']*n_letters
    for g in guess:
        if(g in Word_of_the_day):
            indexes = []
            indexes.append(guess.find(g))
            for ii in indexes:
                if(ii >= 0):
                    colors[ii] = 'red'
    for ii in range(len(guess)):
        if guess[ii] == Word_of_the_day[ii]:
            colors[ii] = 'green'
            correct = correct + 1
    
    for ii in range(len(guess)):
        print(colored(guess[ii], colors[ii]), sep=' ', end='', flush=True)
    
    counter = counter + 1
    
    if correct == n_guess:
        print("\nCongrats the word was:", Word_of_the_day)
        break

if correct < n_guess:
    print("\nSorry! The word was:", Word_of_the_day)
