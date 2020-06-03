from lexer.ngram_generator import NGramGenerator


ngrams = NGramGenerator(2, 'data/sample.txt')

while not ngrams.finished():
    print(ngrams.get_next_ngram())
