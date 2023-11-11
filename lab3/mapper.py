#!/usr/bin/python3
import sys
def main(argv):
    for line in sys.stdin:
        # Line is the input line that comes in (e.g `Some content`)
        # You must remove cases with too many spaces, start space and end space (Strip) and split the sequence
        # The for each word in the list, print it with a 1 next to 1 (this will be read by the reducer)
        # Separate the word and the 1 by a tab
        ### STRIP START ###
        wordlist = line.strip().split()
        for word in wordlist:
            print(word+"\t"+"1")
        ### STRIP END ###

if __name__ == "__main__":
    main(sys.argv)
