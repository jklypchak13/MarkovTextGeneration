from lexer.tokenizer.base import Tokenizer


class CharTokenizer(Tokenizer):
    """A tokenizer that just breaks a file down by it's individual characters
    """

    token_map = {}

    def __init__(self, file_path: str):
        super().__init__(file_path)

    def valid(self) -> bool:
        """Determine if the tokenizer is still processing a single token, or if a new token has been identified.

        Returns:
            [bool] -- If a new token has been identified.
        """

        # Just check if we have large gaps of spaces, combine those into one token.
        return self.current_char == ' ' and self.next_char == ' '
