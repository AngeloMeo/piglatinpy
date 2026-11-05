from src.error import PigLatinError


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
        if ((self.phrase.lower().startswith("a")) or (self.phrase.lower().startswith("e")) or
                (self.phrase.lower().startswith("i")) or (self.phrase.lower().startswith("o")) or
        (self.phrase.lower().startswith("u"))):

            if ((self.phrase.lower().endswith("a")) or (self.phrase.lower().endswith("e")) or
            (self.phrase.lower().endswith("i")) or (self.phrase.lower().endswith("o")) or
            (self.phrase.lower().endswith("u"))):
                return self.phrase + "yay"

            return self.phrase + "nay"

        pass
