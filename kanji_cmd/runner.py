import argparse
import random

from kanji_cmd.repository import Repository

WHITE = "\033[0m"
BLUE = "\033[34m"
RED = "\033[31m"


def single_card():
    repo = Repository()
    repo.load_lesson(1)
    card = repo.cards[random.randint(1, len(repo.cards))]
    _show_card(card)


def whole_lesson():
    repo = Repository()
    repo.load_lesson(1)
    cards = list(repo.cards.keys())
    random.shuffle(cards)
    for i in cards:
        card = repo.cards[i]
        _show_card(card)


def _show_card(card):
    print(f"kanji: {card.kanji}")
    input()
    print(f"meaning: {card.meaning}")
    print(f"readings: {card.readings}")
    mnemonic = (
        card.mnemonic.replace("[", BLUE)
        .replace("]", WHITE)
        .replace("`", RED)
        .replace(">", WHITE)
    )
    print(f"mnemonic: {mnemonic}")
    if card.radical:
        print(f"radical: {card.radical}")


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-w",
        "--whole",
        action="store_true",
        help="show the whole lesson in a random order.",
    )
    args = parser.parse_args()
    if args.whole:
        whole_lesson()
    else:
        single_card()
