from spellchecker import SpellChecker
import re
from tkinter import messagebox

# Spelling stuff
class Spelling:
    def __init__(self, text_widget=None):
        self.text_area = text_widget
        self.languages = {
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

        self.spellcheckers = {
            name: SpellChecker(language=code)
            for name, code in self.languages.items()
        }

    def tokenize(self, text):
        TOKEN_PATTERN = re.compile(r"\w+|\W+")
        return TOKEN_PATTERN.findall(text)
    
    def preserve_case(self, original, corrected):
        if original.isupper():
            return corrected.upper()
        if original[0].isupper():
            return corrected.capitalize()
        return corrected

    def check_spelling(self, lang='none', text=""):
        if lang == 'none':
            return text
        checker = self.spellcheckers.get(lang)
        if not checker:
            return text
        tokens = self.tokenize(text)
        corrected_tokens = []
        for token in tokens:
            if token.isalpha():
                corrected = checker.correction(token)
                corrected = self.preserve_case(token, corrected)
                corrected_tokens.append(corrected)
            else:
                corrected_tokens.append(token)
        return ''.join(corrected_tokens)
    
    def spellcheck_selected(self, language_mode=None):
        try:
            selected_text = self.text_area.get("sel.first", "sel.last")
            corrected_text = self.check_spelling(language_mode, selected_text)
            self.text_area.delete("sel.first", "sel.last")
            self.text_area.insert("insert", corrected_text)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during spellcheck: {str(e)}")
