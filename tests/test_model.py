import pytest


class Model:
    def get_card(self):
        return '月'


def test_model_supplies_kanji_from_selection():
    model = Model()

    assert model.get_card() in ['月', '田']
