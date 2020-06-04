from typing import List


class Tokenizer:
    """a tokenizer base class, breaking a file down in to it's base tokens
    """

    token_map = {}

    def __init__(self, file_path: str):
        self.fp: File = open(file_path, 'r')
        self.current_char: str = self.fp.read(1)
        self.next_char: str = self.fp.read(1)

    def _next(self):
        """advance the current character by one
        """
        self.current_char: str = self.next_char
        self.next_char: str = self.fp.read(1)

    def next_token(self) -> int:
        """retrieve the next token in the file

        Returns:
            [int] -- the integer id of the next token
        """
        token: str = self.current_char

        # Continue to parse characters until a full token is found
        while self.valid():
            token += self.next_char
            self._next()

        # Consume the last character of the current token
        self._next()

        # Replace Lengths of Spaces with just one space
        while '  ' in token:
            token = token.replace('  ', ' ')

        # See if a new token has been found
        if token not in self.__class__.token_map:
            self.__class__.token_map[token] = len(self.__class__.token_map)

        return self.__class__.token_map[token]

    def end(self) -> bool:
        """determine if the tokenizer is at the end of the file

        Returns:
            bool -- if the tokenize is at the end of the file
        """
        return self.current_char == ''

    def valid(self):
        """Determine if the tokenizer is still processing a single token, or if a new token has been identified.

        Returns:
            [bool] -- If a new token has been identified.
        """
        raise NotImplementedError

    @classmethod
    def get_id(cls, token: str) -> int:
        """get the integer id number of a given token (that has been encountered)

        Arguments:
            token {str} -- the token to find the integer id of.

        Returns:
            int -- the integer id representing the given token.
        """
        return cls.token_map[token]

    @classmethod
    def get_token(cls, token_id: int) -> str:
        """get the string represented by a specific token id

        Arguments:
            token_id {int} -- the token id to retrieve

        Returns:
            str -- the string token
        """
        for token in cls.token_map:
            if cls.token_map[token] == token_id:
                return token
        return None

    @classmethod
    def translate(cls, token_ids: List[int]) -> str:
        """translate a given list of token id's into the string output

        Arguments:
            token_ids {List[int]} -- a list of valid token ids

        Returns:
            str -- the string representing the list of token ids
        """
        result: str = ''
        for token in token_ids:
            result += cls.get_token(token)

        return result
