# Studying aids module

from typing import List, Dict, Optional
import random
import csv
from time import sleep 

Concordance = Dict[str, List[str]]

class Card:
    def __init__(self, flashes: Concordance):
        self.flashes = flashes

    def items(self):
        return self.flashes.items()
    
class Deck:
    def __init__(self, name: str, cards: List[Card], knowledge: List[float] = []):
        assert (len(cards) == len(knowledge)) or (not knowledge), "There are not same number of knowledge levels as cards. Unable to match."
        self.name = name
        # initialize weights for cards to be uniform
        if not knowledge:
            knowledge = [100.0 for _ in cards]
        self.cards = [[c, k] for (c,k) in zip(cards, knowledge)]
    
    def _update_card_prob(self):
        _all_knowledge = sum([knowledge for card, knowledge in self.cards])
        self._card_probs = [(knowledge / _all_knowledge) for card, knowledge in self.cards]
    
    def change_name(self, new_name: str) -> None:
        self.name = new_name
    
    def change_cards(self) -> None:
        raise NotImplementedError

    def add_cards(self, new_cards: List[Card], new_knowledge: List[int] = []) -> None:
        assert (len(new_cards) == len(new_knowledge)) or (not new_knowledge), "There are not same number of knowledge levels as cards. Unable to match."
        if not new_knowledge:
            new_knowledge = [1 for _ in new_cards]
        self.cards += [[c, k] for (c,k) in zip(new_cards, new_knowledge)]
    
    def flash_a_card(self):
        self._update_card_prob()
        rate = 0.9
        lowest_score = 0.0000001
        card_index: int = random.choices(population=list(enumerate(self.cards)), weights=self._card_probs, k=1)[0][0]
        # show card self.cards[card_index][0]
        question, answer = random.choice(list(self.cards[card_index][0].items()))
        print("\n\nQuestion:\n\n\t" + question + "\n\n")
        quitter = input("[Return to flip card, X for quit]\n\n\n")
        if quitter == 'X':
            clear()
            print("See ya, quitter!")
            return False
        print("\n\nAnswer:\n\n\t" + answer[0]+"\n\n\n")

        while True:
            confidence = input("[Y]: I know this! \n" + \
                "[G]: I got it right, but I need more \n" + \
                "[B]: I did not get it right \n" + \
                "[N]: I really did not get it \n")
            
            if confidence.lower() == 'y':
                print('\nGreat!\n')
                self.cards[card_index][1] *= max((rate)**2, lowest_score)
                break
            elif confidence.lower() == 'g':
                print('\nWill do!\n')
                self.cards[card_index][1] *= max((rate)**1, lowest_score)
                break
            elif confidence.lower() == 'b':
                print('\nKeep trying!\n')
                self.cards[card_index][1] *= (1/rate)**1
                break
            elif confidence.lower() == 'n':
                print('\nIt will happen!\n')
                self.cards[card_index][1] *= (1/rate)**2
                break
            else:
                print('Huh?')
        return True
        

def read_csv_to_deck(filename: str, header=True) -> Deck:
    """
    Imports a csv file into a Deck object.
    This assumes a five column csv with the columns as follows:
    knowledge_level, short_question, detail_answer, detail_question, short_answer
    """

    knowledges: List[float] = []
    cards: List[Card] = []
    with open(filename) as flashcard_file:
        csv_reader = csv.reader(flashcard_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0 and header:
                line_count += 1
            else:
                try:
                    knowledge = float(row[0])
                except:
                    print(f"{row[0]} is not a thing I can make into a float. I'll use 1.0.")
                    knowledge = 100.0
                flashes = {row[1] : [row[2]], row[3] : [row[4]]}
                card = Card(flashes)

                knowledges += [knowledge]
                cards += [card]
                line_count += 1

    assert (line_count - 1.1) < len(knowledges) < (line_count + 0.1), "There do not seem to as many knowledge levels as there are lines in the file."
    assert (len(cards) == len(knowledges)), "There are not same number of knowledge levels as cards."

    print(f'Processed {line_count} lines.\n')

    return Deck(name=filename, cards=cards, knowledge=knowledges)

def write_deck_to_csv(deck: Deck, header=True) -> None:
    """
    Exports a deck to a csv file in the local directory using Deck.name as filename.
    This outpusts a five column csv with the columns as follows:
    knowledge_level, short_question, detail_answer, detail_question, short_answer
    """

    with open(deck.name, mode='w') as flashcard_file:
        csv_writer = csv.writer(flashcard_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        if header:
            csv_writer.writerow(['knowledge_level', 'short_question', 'detail_answer', 'detail_question', 'short_answer'])

        for row in deck.cards:
            
            row_list = [row[1]]
            for question, answer in row[0].items():
                row_list += [question, answer[0]]
            
            csv_writer.writerow(row_list)

    print("Exported: " + deck.name)

    return


from os import system, name 
  
# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
  