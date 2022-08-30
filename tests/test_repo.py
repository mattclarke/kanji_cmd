import pytest

from kanji_cmd.kanji import Kanji
from kanji_cmd.repository import InvalidLessonException, Repository


def test_repository_can_load_lesson_1():
    repo = Repository()

    repo.load_lesson(1)

    assert len(repo.cards) > 0
    assert isinstance(repo.cards[1], Kanji)


def test_repository_throws_on_lesson_number_less_than_1():
    repo = Repository()

    with pytest.raises(InvalidLessonException):
        repo.load_lesson(0)


def test_repository_throws_on_lesson_number_greater_than_max():
    repo = Repository()

    with pytest.raises(InvalidLessonException):
        repo.load_lesson(10000000)
