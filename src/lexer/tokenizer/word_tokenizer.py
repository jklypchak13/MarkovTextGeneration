from lexer.tokenizer.base import Tokenizer


class WordTokenizer(Tokenizer):
    """a tokenizer breaking down a file by the different words it has.
    """
    separators = '.?\n\t ,![]()'
    token_map = {}

    def __init__(self, file_path: str):
        self.separators: str = self.__class__.get_separators()
        super().__init__(file_path)

    def valid(self):
        """Determine if the tokenizer is still processing a single token, or if a new token has been identified.

        Returns:
            [bool] -- If a new token has been identified.
        """
        return self.current_char != '' and (self.next_char in self.separators) == (self.current_char in self.separators)

    @classmethod
    def get_separators(cls) -> str:
        """retrieve the list of the current separators

        Returns:
            str -- the single character separators
        """
        return cls.separators
