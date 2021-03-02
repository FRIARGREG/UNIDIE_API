import cards

standard_deck = [
    'JkrB', 'JkrC',
    '2C', '3C', '4C', '5C', '6C', '7C',
    '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AC',
    '2D', '3D', '4D', '5D', '6D', '7D',
    '8D', '9D', '10D', 'JD', 'QD', 'KD', 'AD',
    '2H', '3H', '4H', '5H', '6H', '7H',
    '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AH',
    '2S', '3S', '4S', '5S', '6S', '7S',
    '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AS'
]


def test_deck_build():
    # should always start with a full deck & Jokers (54)
    test_deck = cards.deck()
    assert len(test_deck) == test_deck.cards_remaining == 54


def test_deck_build_order():
    test_deck = cards.deck()
    for l, r in zip(test_deck, standard_deck):
        assert l == r


def test_deck_shuffle_qty():
    test_deck = cards.deck()
    test_deck.shuffle()

    # did the shuffle change the number of cards?
    assert len(test_deck) == test_deck.cards_remaining == 54


def test_deck_shuffle_duplicates():
    test_deck = cards.deck()
    test_deck.shuffle()

    # are there any duplicates?
    for i in standard_deck:
        assert test_deck.count(i) == 1


def test_deck_draw_1():
    test_deck = cards.deck()
    hand = test_deck.draw_card()
    assert len(hand) + len(test_deck) == 54
    assert hand.pop() not in test_deck


def test_deck_draw_5():
    test_deck = cards.deck()
    hand = test_deck.draw_card(5)
    assert len(hand) + test_deck.cards_remaining == 54
    for card in hand:
        assert card not in test_deck


def test_deck_deal_5_1():
    test_deck = cards.deck()
    test_hand = {'Mikey': set()}
    test_deck.deal_cards(test_hand, 5)
    assert len(test_hand['Mikey']) + test_deck.cards_remaining == 54

    for card in test_hand['Mikey']:
        assert card not in test_deck


def test_deck_deal_5_to_5():
    test_deck = cards.deck()
    test_game = {
        "Greg": set(),
        "Theo": set(),
        "Marcus": set(),
        "Jane": set(),
        "Hilda": set()
    }
    test_deck.deal_cards(test_game, 5)

    dealt_sum = 0
    for hand in test_game.values():
        dealt_sum += len(hand)

    assert dealt_sum + test_deck.cards_remaining == 54

    game_copy = test_game.copy()
    for name, hand in test_game.items():
        for k, v in game_copy.items():
            if name != k:
                assert len(hand.intersection(v)) == 0
                assert len(hand.intersection(set(test_deck))) == 0
