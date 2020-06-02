from lexer.tokenizer import Tokenizer

tokens = Tokenizer('data/sample.txt')

while(not tokens.end()):
    print(tokens.next_token())
