from lexer.ngram_generator import NGramGenerator
from lexer import CharTokenizer

tokenizer = CharTokenizer('data/sample.txt')
ngrams = NGramGenerator(2, tokenizer)

while not ngrams.finished():
    print(ngrams.get_next_ngram())
