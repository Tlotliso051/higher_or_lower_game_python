import random

suit_tuples = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
rank_tuples = ['Ace', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

Ncards = 8




def get_the_card():
    """
    Pass in a deck and this function returns a random card from the deck
    """
    the_card = suit_tuples.pop()
    return the_card


def shuffle_cards(list_in_deck_cards):
    """
    function returns the copy of shuffled deck
    """
    list_out_deck = list_in_deck_cards.copy()
    random.shuffle(list_out_deck)
    return list_out_deck



print('Welcome to Higher or Lower Game.')
print('you have to show if the next card is higher or lower than the present card value')
print('guessing it right adds 50 points; wrong guess subtract 25 points')
print('you have 300 points to start.')
print()

start_deck_list = []
for suit in suit_tuples:
    for the_value, rank in enumerate(rank_tuples):
        cards_to_dict = {'rank': 'rank', 'suit': 'suit', 'value': the_value + 1}
        start_deck_list.append(cards_to_dict) 


score = 300

while True: 
    print()
    print(start_deck_list)
    gameDeckList = random.shuffle(start_deck_list)
    print(gameDeckList)
    currentCardDict = get_the_card(gameDeckList)
    print(currentCardDict)
    currentCardRank = currentCardDict['rank']
    currentCardValue = currentCardDict['value']
    currentCardsuit = currentCardDict['suit']
    print(f'starting card is: {currentCardRank} of {currentCardsuit}')
    print()

    for cardnumber in range(Ncards):
        print('is not case-sensitive')
        answer = input(f'Will the next card be higher or lower than the {currentCardRank} of {currentCardsuit} ? (Enter h or l)').lower()
        nextCardDict = get_the_card(gameDeckList)
        nextCardRank = nextCardDict['rank']
        nextCardSuit = nextCardDict['suit']
        nextCardValue = nextCardDict['vavue']
        print(f'Next card is : {nextCardRank} of {nextCardSuit}')

    if answer == 'h':
        if nextCardValue > currentCardValue:
            print('Yougot it rright, It was higher')
            score += 50

        else:
            print('Sorry, It was lower')
            score -= 25

    elif answer == 'l':
        if nextCardValue < currentCardValue:
            print('You got it right, it was lower')
            score += 50

        else:
            print('Sorry, it was not lower')
            score -= 25

    print(f'your score is : {score}')
    print()
    currentCardRank = nextCardRank
    currentCardValue = currentCardValue

    tryAgain = input('To play again, press ENTER or "q" to quit:')
    tryAgain.casefold()
    if tryAgain == 'q':
        break

print('OK bye')

def main():
    deck_list_in = get_the_card()
    shuffle_cards(deck_list_in)


if __name__ == '__main__':
    main()
    



            
            





