
class Tokenizer:
    """a tokenizer, breaking down a file by words/separators
    """
    separators = '.?\n\t ,![]()'
    token_map = {}

    def __init__(self, file_path: str):
        self.fp: File = open(file_path, 'r')
        self.separators: str = Tokenizer.get_separators()
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

        while self.current_char != '' and (self.next_char in self.separators) == (self.current_char in self.separators):
            token += self.next_char
            self._next()
        self._next()
        if '  ' in token:
            token.replace('  ', ' ')
        if token not in Tokenizer.token_map:
            Tokenizer.token_map[token] = len(Tokenizer.token_map)
        return Tokenizer.token_map[token]

    def end(self) -> bool:
        """determine if the tokenizer is at the end of the file

        Returns:
            bool -- if the tokenize is at the end of the file
        """
        return self.current_char == ''

    @classmethod
    def get_separators(cls) -> str:
        """retrieve the list of the current separators

        Returns:
            str -- the single character separators
        """
        return cls.separators

    @classmethod
    def get_id(cls, token):
        return cls.token_map[token]

    @classmethod
    def get_token(cls, token_id):
        for token in cls.token_map:
            if cls.token_map[token] == token_id:
                return token
        return None

    @classmethod
    def translate(cls, token_ids):
        result = ''
        for token in token_ids:
            result += cls.get_token(token)

        return result
