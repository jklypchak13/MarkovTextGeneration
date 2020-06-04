from lexer.tokenizer import Tokenizer
from typing import Tuple


class NGramGenerator:

    def __init__(self, n: int, tokenizer: Tokenizer):
        self.tokenizer = tokenizer
        self.n: int = n
        self.current_ngram: Tuple[int] = tuple(
            [self.tokenizer.next_token() for i in range(n)])
        self.first: Tuple[int] = self.current_ngram

    def get_next_ngram(self) -> Tuple[Tuple[int], int]:
        """generate the next ngram given by the current tokenizer

        Returns:
            Tuple[Tuple[int], int] -- A tuple of length 2 such that
            return[0] = the next NGram
            return[1] = the next token after the NGram
        """
        result: Tuple[int] = self.current_ngram
        token: int = self.tokenizer.next_token()

        previous_ngram: List[int] = list(self.current_ngram)[1:]
        previous_ngram.append(token)
        self.current_ngram = tuple(previous_ngram)

        return result, token

    def finished(self) -> bool:
        """Determine if this file is out of Ngrams

        Returns:
            bool -- whether this generator is done
        """
        return self.tokenizer.end()

    def first_ngram(self) -> Tuple[int]:
        """return the first ngram encountered by this

        Returns:
            Tuple[int] -- the first ngram
        """
        return self.first
