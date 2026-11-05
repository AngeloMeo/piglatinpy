from src.error import PigLatinError


def _indexOfFirstVowel(phrase) -> int:
    found = False
    i = 0
    while not found and i < len(phrase):
        if phrase[i] in "aeiou":
            found = True
        else:
            i += 1
    return i

class PigLatinTranslator:

    def __init__(self, phrase: str):
        """
        Creates a pig latin translator given a phrase.
        :param phrase: the phrase.
        :raise PigLatinError: for any error situation.
        """
        self.phrase = phrase.lower()

    def get_phrase(self) -> str:
        """
        Returns the phrase.
        :return: the phrase.
        """
        return self.phrase

    def translate(self) -> str:
        """
        Returns the Pig Latin translation of the phrase.
        :return: the translation.
        """
        if self.phrase == "":
            return "nil"

        start_letter = self.phrase[0].lower()
        ending_letter = self.phrase[-1].lower()

        if start_letter in "aeiou":
            if ending_letter in "aeiou":
                return self.phrase + "yay"
            else:
                if ending_letter == "y":
                    return self.phrase + "nay"
            return self.phrase + "ay"
        else:
            if start_letter not in "aeiou":
                i = _indexOfFirstVowel(self.phrase)

                return self.phrase[i:] + self.phrase[0:i] + "ay"


        pass
