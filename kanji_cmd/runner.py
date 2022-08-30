from kanji_cmd.repository import Repository

WHITE = "\033[0m"
BLUE = "\033[34m"
RED = "\033[31m"


def run():
    repo = Repository()
    repo.load_lesson(1)
    card = repo.get_kanji()
    print(f"kanji: {card.kanji}")
    input()
    print(f"meaning: {card.meaning}")
    print(f"readings: {card.readings}")
    mnemonic = (
        card.mnemonic.replace("[", BLUE)
        .replace("]", WHITE)
        .replace("|", RED)
        .replace(">", WHITE)
    )
    print(f"mnemonic: {mnemonic}")
