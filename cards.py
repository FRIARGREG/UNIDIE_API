from random import choice, shuffle


class deck(list):
    """ Standard deck of cards. Some game systems use playing cards """

    def __init__(self):
        self.rebuild_deck()

    @property
    def cards_remaining(self):
        return len(self)

    def rebuild_deck(self):
        self.clear()

        suites = ["C", "D", "H", "S"]  # index doubles as heirarchy
        values = [str(x) for x in range(2, 10+1)] + ["J", "Q", "K", "A"]
        jokers = ["JkrB", "JkrC"]

        self.extend(jokers)

        for x in suites:
            for y in values:
                self.append(f"{y}{x}")

    def draw_card(self, count=1):
        draw = []
        while count > 0:
            draw.append(self.pop())
            count -= 1
        return draw

    def deal_cards(self, players, cards=0):
        for x in range(cards):
            for player in players:
                players[player].update(self.draw_card())
        return players

    def shuffle(self):
        shuffle(self)

    def show_deck(self):
        print(self)
