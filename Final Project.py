import random

f = open("log.txt", "a")
f.write("\n\n**NEW GAME**\n")

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']


class Card:
    rank = ''
    suit = ''

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return self.rank + ' of ' + self.suit

    def showrank(self):
        return self.rank


class Deck:
    deck = []
    total = 0

    def __init__(self):

        count = 0
        while count < 52:
            for x in range(len(suits)):
                for y in range(len(ranks)):
                    c = Card(ranks[y], suits[x])
                    self.deck.append(c)
                    count += 1
        random.shuffle(self.deck)

    def __str__(self):
        s = ''
        for x in self.deck:
            s += '\n' + x.__str__()
        return '\nDeck total:' + s

    def deal(self):
        c = str(self.deck[len(self.deck) - 1])

        if c[:1] in ('J', 'Q', 'K', '1'):
            self.total += 10
        elif c[:1] in ('2', '3', '4', '5', '6', '7', '8', '9'):
            self.total += int(c[:1])
        elif c[:1] == 'A':
            if self.total <= 10:
                self.total += 11
            else:
                self.total += 1

        popped = self.deck.pop()
        print(str(popped))
        f.write("\n" + str(popped))

    def printtotal(self):
        print("\nYour total is " + str(self.total))
        f.write("\nYour total is " + str(self.total))


print("\nTry to get to 21. Good luck!")

play = ''
while play != 'e':

    d = Deck()
    print()
    f.write('\n')
    d.deal()
    d.deal()
    d.printtotal()
    total = d.total

    if total == 21:
        print("Lucky WIN!")
        f.write("\nLucky WIN!")
        play = input("\nPlay again? Or type 'e' to exit.\n")

    else:
        while total < 21:
            hit = input("\nWould you like another card? Or type 'e' to exit.\n")
            if hit.lower() != 'e':
                print()
                f.write('\n')
                d.deal()
                d.printtotal()
                total = d.total
                if total > 21:
                    print("You LOSE!")
                    f.write('\nYou LOSE!')
                    play = input("\nPlay again? Or type 'e' to exit.\n")
                elif total == 21:
                    print("You WIN!")
                    f.write('\nYou WIN!')
                    play = input("\nPlay again? Or type 'e' to exit.\n")
                else:
                    continue
            else:
                play = input("\nPlay again? Or type 'e' to exit.\n")
                break
f.close()