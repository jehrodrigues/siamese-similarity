# -*- coding: utf-8 -*-

from nltk import TreebankWordTokenizer

class Tokenizer:
    
    def __init__(self):
        self.tokenizer = TreebankWordTokenizer()
        
    def tokenize(self, sentence):
        tokens = self.tokenizer.tokenize(sentence)
        return tokens
    
    
if __name__ == '__main__':
    sentence = 'What percentage did bacon sales climb in 2013 in the U.S.?'
    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize(sentence)
    print(tokens)