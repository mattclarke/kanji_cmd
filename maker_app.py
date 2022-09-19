import argparse

from kanji_cmd.repository import Repository
from kanji_cmd.runner import BLUE, RED, WHITE

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    required_args = parser.add_argument_group("required arguments")
    required_args.add_argument(
        "-l", "--lesson", type=int, help="the lesson number", required=True
    )

    args = parser.parse_args()

    repo = Repository()
    repo.load_lesson(args.lesson)

    for n, card in repo.cards.items():
        print(f"{n}")
        print(f"kanji: {card.kanji}")
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
        print("")
