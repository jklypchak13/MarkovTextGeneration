
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

    def next_token(self) -> str:
        """retrieve the next token in the file

        Returns:
            str -- the next token
        """
        token: str = self.current_char

        while self.valid():
            token += self.next_char
            self._next()

        self._next()

        if '  ' in token:
            token.replace('  ', ' ')
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
        raise NotImplementedError

    @classmethod
    def get_id(cls, token):
        return cls.token_map[token]

    @classmethod
    def get_token(cls, token_id):
        for token in cls.token_map:
            if cls.token_map[token] == token_id:
                return token_id
        return None
