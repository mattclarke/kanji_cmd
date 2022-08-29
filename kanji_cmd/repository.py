import importlib
import os


class InvalidLessonException(Exception):
    pass


class Repository:
    def __init__(self, lesson_path):
        self.cards = []
        self.lesson_path = lesson_path

    def load_lesson(self, number):
        if number < 1 or number > self._get_number_of_lessons():
            raise InvalidLessonException("Invalid lesson number")
        module = importlib.import_module(f"lessons.lesson_{number}")
        self.cards = module.cards

    def _get_number_of_lessons(self):
        return len(
            [
                name
                for name in os.listdir(self.lesson_path)
                if name.startswith("lesson_")
            ]
        )
