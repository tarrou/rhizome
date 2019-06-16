import sys
import pandas as pd

def main():
    _ = sys.argv[0]
    flashcards_file = sys.argv[1]
    # What is file doesn't exist?
    if not flashcards_file:
        "Using default flashcards"
        flashcards_file = "flashcards.csv"

def flash(filename):
    cards = pd.read_csv(filename)
    #pick number according to prob



if __name__ == '__main__':
   main()