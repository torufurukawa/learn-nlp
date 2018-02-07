import nltk
from nltk.corpus import brown
brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.tagged_sents(categories='news')

# default tagger from 5.4.1
tags = [tag for (word, tag) in brown.tagged_words(categories='news')]
default_tag = nltk.FreqDist(tags).max()
print("default tag:", default_tag)

raw = "I do not like green eggs and ham, I do not like them Sam I am!"
tokens = nltk.word_tokenize(raw)
default_tagger = nltk.DefaultTagger(default_tag)
tagged_tokens = default_tagger.tag(tokens)
print("Tagged tokens:", tagged_tokens)
print("Evaluated:", default_tagger.evaluate(brown_tagged_sents))
