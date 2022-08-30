from dataclasses import dataclass


@dataclass
class Kanji:
    kanji: str
    english: str
    readings: str
    mnemonics: str
    is_radical: bool
