from spellchecker import SpellChecker
import re

text_area = None

# Spelling stuff
class Spelling:
    languages = {
        "english": "en",
        "russian": "ru",
        "spanish": "es",
        "portuguese": "pt",
        "italian": "it",
        "french": "fr",
        "german": "de",
        "arabic": "ar",
        "persian": "fa",
        "dutch": "nl",
        "latvian": "lv",
        "basque": "eu",
    }

    spellcheckers = {
        name: SpellChecker(language=code)
        for name, code in languages.items()
    }

    def tokenize(text):
        TOKEN_PATTERN = re.compile(r"\w+|\W+")
        return TOKEN_PATTERN.findall(text)
    def check_spelling(lang='none', text=""):
        if lang == 'none':
            return text
        checker = Spelling.spellcheckers.get(lang)
    