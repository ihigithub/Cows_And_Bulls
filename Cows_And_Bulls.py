# Cows And Bulls game
from random import randint
from list_overlap.list_overlap import commonlist

keynumber = randint(100,999)
keynumber_splt = [int(digit) for digit in str(keynumber)]
print keynumber_splt
guesses = 0
while True:
    guess = eval(raw_input())
    guesses += 1
    guess_splt = [int(digit) for digit in str(guess)]
    count_matches = 0
    for digit, index_kn_s in enumerate(keynumber_splt):
        if index_kn_s == guess_splt[digit]:
            count_matches +=1
    #TODO: wrong printed numbers
    print len(list(set(sorted(keynumber_splt,key=int)) & set(sorted(guess_splt,key=int))))
    print count_matches
    if guess == keynumber:
        print "you win!"
        break
