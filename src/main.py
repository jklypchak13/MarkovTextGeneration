from markov.model import MarkovModel
from lexer.tokenizer import CharTokenizer as Tokenizer
from typing import List
import os
import sys
ngrams: MarkovModel = MarkovModel(7, Tokenizer)

token_counts = []

# Train the Data on all of the data in the office scripts file
for root, dirs, files in os.walk("office_scripts\\", topdown=False):

    # TODO - Add a % based output so that we are aware how far through the training we are. JSK
    for name in files:
        token_counts.append(ngrams.train(os.path.join(root, name)))

# Calculate the average length of a training sample
length: int = int(sum(token_counts) / len(token_counts))

# Generate a sequence
result = ngrams.generate(length)

# Translate the sequence from token IDs to it's token form.
sentence = Tokenizer.translate(result)

# See if an output directory exists
if not os.path.exists('output'):
    os.mkdir('output')

# Output the result
with open(f'output/episode.txt', 'w') as fp:
    fp.write(sentence)
