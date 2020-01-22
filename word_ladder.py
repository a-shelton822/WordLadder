import sys
import time

## Global variables used by all methods to hold words
used_words = []
dictionary = []
word_list = []
source_file = "words_alpha.txt"




## If no arguments are passed by the command line, prompt the user for input
if len(sys.argv) == 3:
    start_word = sys.argv[1].lower()
    end_word = sys.argv[2].lower()
else:
    start_word = input("Enter start word: ").lower()
    end_word = input("Enter end word: ").lower()




## Checks that both words are the same length and found in the dictionary
def check_words():
    global start_word, end_word

    while start_word not in dictionary:
        print("%s is not in the dictionary." % start_word)
        start_word = input("Please enter another start word: ").lower()
    while end_word not in dictionary:
        print("%s is not in the dictionary." % end_word)
        end_word = input("Please enter another end word: ").lower()

    while len(start_word) != len(end_word):
        print("Both words are not the same length.")
        start_word = input("Enter a new start word: ")
        end_word = input("Enter a new end word: ")

        while start_word not in dictionary:
            print("%s is not in the dictionary." % start_word)
            start_word = input("Please enter another start word: ").lower()
        while end_word not in dictionary:
            print("%s is not in the dictionary." % end_word)
            end_word = input("Please enter another end word: ").lower()




## Creates a list of all words found in the provided text file
def build_dictionary():
    with open(source_file) as f:
        for line in f:
            dictionary.append(line.strip().replace("\n",""))




## Builds a list of all words with the same length as the starting word
def build_word_list():
    for word in dictionary:
        if len(word) == len(start_word):
            word_list.append(word)




## Returns a list of words one letter different than the passed word
def get_words_one_letter_away(base_word):
    one_letter_away = []

    for word in word_list:
        letters_different = 0
        for i in range(0,len(word)):
            if word[i] != base_word[i]:
                letters_different += 1
        if letters_different == 1:
            one_letter_away.append(word)
    return one_letter_away




## Returns a list of words one letter away from their neighors that link the
## starting word and the ending word
def build_ladder(start, end):
    ladder = []
    list_of_ladders = []
    one_away = get_words_one_letter_away(end)

    ladder.append(end)
    used_words.append(end)
    list_of_ladders.append(ladder)

    while list_of_ladders:

        ## Retrieve the top ladder on the list
        ladder = list_of_ladders.pop(0)
        one_away = get_words_one_letter_away(ladder[-1])

        ## For every word one letter away from the ladder's top,
        ## Clone the ladder and append the new word onto it
        for word in one_away:
            if word not in ladder and word not in used_words:
                ladder.append(word)

                ## If the top of the ladder is the start word, return it
                if ladder[-1] == start:
                    return ladder

                used_words.extend(ladder)

                new_ladder = []
                new_ladder.extend(ladder)

                list_of_ladders.append(new_ladder)
                ladder.remove(word)




## Program logic
def main():
    build_dictionary()
    check_words()
    build_word_list()

    print("Attempting to find a ladder between %s and %s"\
            % (start_word, end_word))
    start_time = time.time()
    ladder = build_ladder(start_word, end_word)
    end_time = round(time.time() - start_time, 3)

    print("After " + str(end_time) + " seconds", end = ", ")
    if ladder:
        print("a ladder was found.")
        for word in ladder:
            print(word)
    else:
        print("no ladder found.")




## Program execution
main()
