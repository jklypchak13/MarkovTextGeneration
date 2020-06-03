from .tokenizer import Tokenizer
from typing import Tuple


class NGramGenerator:

    def __init__(self, n: int, file_path: str):
        self.tokenizer = Tokenizer(file_path)
        self.n: int = n
        self.current_ngram = tuple(
            [self.tokenizer.next_token() for i in range(n)])
        self.first = self.current_ngram

    def get_next_ngram(self):
        result = self.current_ngram
        token = self.tokenizer.next_token()

        self.current_ngram = list(self.current_ngram)[1:]
        self.current_ngram.append(token)
        self.current_ngram = tuple(self.current_ngram)
        return result, token

    def finished(self):
        return self.tokenizer.end()

    def first_ngram(self):
        return self.first
