import random
from warnings import filters
class poker_game:
#デッキ作成、配布
    MARK = "♤♧♡♢"
    NUMBER = range(1, 14)

    def make_deck(self):
        deck = [f'{mark}{number}'
                for mark in MARK
                for number in NUMBER]
        random.shuffle(deck)
        return deck

    def draw_card(self,deck, n=1):
        card = deck[:n]
        del deck[:n]
        return card

    card_deck = make_deck()
    player_card = draw_card(card_deck, 5)
    cpu_card = draw_card(card_deck, 5)

    #役の判定
    def poker_judgement(self):
        