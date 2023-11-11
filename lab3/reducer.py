#!/usr/bin/python3
import sys
def main(argv):

    # Initialize the current word and the count
    current_word = None
    count = 0

    # Read each line
    for line in sys.stdin:

        # Split the line the other way round (strip and split)
        # Get the word and the count

        ### STRIP_START ###
        word, n = line.strip().split("\t",1)
        n = int(n)
        ### STRIP END ###

        # Don't forget that Hadoop sorted the sequences for us
        # We need to check the new word we received is still the same than the "current_word"
        # If it's the case, update the count

        ### STRIP_START ###
        if current_word == word:
            count += n
        ### STRIP END ###

        # Otherwise, we must:
        # print the current word an its count
        # update the count to the one of the new word
        # update the current word

        ### STRIP_START ###
        else:
            if current_word:
                print(current_word+"\t"+str(count))
            count = n
            current_word = word
        ### STRIP_END ###

    # Don't forget to display the last word once we exit the loop
    if current_word == word:
        print(current_word+"\t"+str(count))

if __name__ == "__main__":
    main(sys.argv)
