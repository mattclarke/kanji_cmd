from kanji_cmd.repository import Repository

if __name__ == "__main__":
    repo = Repository()
    repo.load_lesson(1)
    print(repo.cards[1])
