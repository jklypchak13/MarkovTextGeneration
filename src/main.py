from markov.model import MarkovModel
from lexer.tokenizer import CharTokenizer as Tokenizer
import os
import sys
ngrams = MarkovModel(7, Tokenizer)

token_counts = []
for root, dirs, files in os.walk("office_scripts\\", topdown=False):
    for name in files:
        token_counts.append(ngrams.train(os.path.join(root, name)))


for i in range(12, 20):

    length = int(sum(token_counts) / len(token_counts))
    result = ngrams.generate(length)
    sentence = Tokenizer.translate(result)
    with open(f'data/episode{i}.txt', 'w') as fp:
        fp.write(sentence)
    print(len(result))
