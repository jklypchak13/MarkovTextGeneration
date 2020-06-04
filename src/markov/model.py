from typing import Tuple, List, Dict
from lexer.ngram_generator import NGramGenerator
import random


def select_random(freq_map: Dict[int, int]) -> int:
    """select a random element proportionally to the given frequency map

    Arguments:
        freq_map {Dict[int, int]} -- the frequency map to select an element from

    Returns:
        int -- the selected element
    """
    keys: List[int] = list(freq_map.keys())
    values: List[int] = list(freq_map.values())
    values: list[int] = [value / sum(values) for value in values]
    choice: int = random.choices(keys, values)[0]
    return choice


class MarkovModel:

    def __init__(self, n: int, tokenizer):
        """[summary]

        Arguments:
            n {int} -- the number of tokens to utilize in one n-gram
            tokenizer {class} -- the class of the tokenizer to use.
        """
        self.n: int = n
        self.data: Dict[Tuple[int], Dict[int, int]] = {}
        self.starting_values: Dict[Tuple[int], int] = {}
        self.tokenizer = tokenizer

    def train(self, file_name: str) -> int:
        """train this model with a file of text

        Arguments:
            file_name {str} -- the name of the file to train this model with

        Returns:
            int -- the number of n grams in this file
        """
        ngrams: NGramGenerator = NGramGenerator(
            self.n, self.tokenizer(file_name))

        first_ngram: Tuple[int] = ngrams.first_ngram()
        count: int = 1

        # Account for the first ngram as a starting point.
        if first_ngram not in self.starting_values:
            self.starting_values[first_ngram] = 1
        else:
            self.starting_values[first_ngram] += 1

        while not ngrams.finished():
            count += 1

            # Add the next NGram and it's corresponding token to our frequency map
            ngram, next_token = ngrams.get_next_ngram()

            if ngram not in self.data.keys():
                self.data[ngram] = {}

            freq_map = self.data[ngram]

            if next_token not in freq_map.keys():
                freq_map[next_token] = 1
            else:
                freq_map[next_token] += 1
        return count

    def generate(self, seq_length: int) -> List[int]:
        """generate a random sequence of tokens based on our training data.

        Arguments:
            seq_length {int} -- the length of the sequence to generate

        Returns:
            List[int] -- the generated sequence of token ids
        """

        current_ngram: Tuple[int] = select_random(self.starting_values)
        result: List[int] = list(current_ngram)

        for i in range(seq_length):
            if current_ngram not in self.data.keys():
                print('ERROR')
                break
            else:
                next_token = select_random(self.data[current_ngram])
            result.append(next_token)
            current_ngram = list(current_ngram)[1:]
            current_ngram.append(next_token)
            current_ngram = tuple(current_ngram)
        return result
