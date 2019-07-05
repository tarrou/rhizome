import sys
#import streakers.studying as studying
import studying


# flashcard csv file contains 5 columns
# Knowledge: positive float, short Q, long A, long Q, short A
# ex.: 10.5, "What is the studying modue?", "The studying module contians the tools for displaying flashcards.", "What is the module needed for a tool that displays flashcards?", "studying"

def main():

    # Load flashcards
    flashcards_file = sys.argv[1]
    # What is file doesn't exist?
    if not flashcards_file:
        print("Using default flashcards file 'flashcards.cvs'")
        flashcards_file = "flashcards.csv"
    deck = studying.read_csv_to_deck(flashcards_file)

    input("Press return to start flashcards")
    keep_going: bool = True

    while keep_going:
        keep_going = deck.flash_a_card()
        print(keep_going)
    
    while True:
        record_it = input("Would you like to record progress to file? (This will modify the flashcards file you were using.) y/n \n")
        if record_it.lower() == 'y':
            studying.write_deck_to_csv(deck)
            break
        elif record_it.lower() == 'n':
            print("Not recorded.")
            break
        else:
            print("Let us try again.\n")
    
if __name__ == '__main__':
   main()