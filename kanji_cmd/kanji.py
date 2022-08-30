from dataclasses import dataclass


@dataclass
class Kanji:
    kanji: str
    meaning: str
    readings: str
    mnemonic: str
    is_radical: bool
