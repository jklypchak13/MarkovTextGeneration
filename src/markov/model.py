from typing import Tuple, List, Dict
from lexer.ngram_generator import NGramGenerator
import random


def select_random(freq_map):
    keys = list(freq_map.keys())
    values = list(freq_map.values())
    values = [value / sum(values) for value in values]
    choice = random.choices(keys, values)[0]
    return choice


class MarkovModel:

    def __init__(self, n, tokenizer):
        self.n = n
        self.data: Dict[Tuple[int], Dict[int, int]] = {}
        self.starting_values: Dict[Tuple[int], int] = {}
        self.tokenizer = tokenizer

    def train(self, file_name):
        ngrams = NGramGenerator(self.n, self.tokenizer(file_name))

        first_ngram = ngrams.first_ngram()
        count = 1
        if first_ngram not in self.starting_values:
            self.starting_values[first_ngram] = 1
        else:
            self.starting_values[first_ngram] += 1

        while not ngrams.finished():
            count += 1
            ngram, next_token = ngrams.get_next_ngram()

            if ngram not in self.data.keys():
                self.data[ngram] = {}

            freq_map = self.data[ngram]

            if next_token not in freq_map.keys():
                freq_map[next_token] = 1
            else:
                freq_map[next_token] += 1
        return count

    def generate(self, n):

        current_ngram = select_random(self.starting_values)
        result = list(current_ngram)
        for i in range(n):
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
