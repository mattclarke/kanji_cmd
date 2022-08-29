import pytest

from kanji_cmd.repository import InvalidLessonException, Repository


def test_repository_can_load_lesson_1():
    repo = Repository()

    repo.load_lesson(1)

    assert len(repo.cards) > 0
    assert repo.cards[1] == (
        "一",
        "ONE",
        "イツ, ひと-つ",
        "If you hold ONE finger horizontally for too long [it will start to ITCH (イチ)].",
        True,
    )


def test_repository_throws_on_lesson_number_less_than_1():
    repo = Repository()

    with pytest.raises(InvalidLessonException):
        repo.load_lesson(0)


def test_repository_throws_on_lesson_number_greater_than_max():
    repo = Repository()

    with pytest.raises(InvalidLessonException):
        repo.load_lesson(10000000)
