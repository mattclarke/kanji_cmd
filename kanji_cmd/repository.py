import importlib
import os


class InvalidLessonException(Exception):
    pass


class Repository:
    def __init__(self):
        self.cards = []

    def load_lesson(self, number):
        if number < 1 or number > self._get_number_of_lessons():
            raise InvalidLessonException("Invalid lesson number")
        module = importlib.import_module(f".lessons.lesson_{number}", "kanji_cmd")
        self.cards = module.cards

    def _get_number_of_lessons(self):
        path = os.path.dirname(os.path.realpath(__file__))
        return len(
            [
                name
                for name in os.listdir(os.path.join(path, "lessons"))
                if name.startswith("lesson_")
            ]
        )
