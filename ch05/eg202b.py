import nltk

text = nltk.corpus.brown.words(categories="learned")
print(sorted(set(b for (a, b) in nltk.bigrams(text) if a == "often")))

ttext = text = nltk.corpus.brown.tagged_words(categories="learned")
tags = [b[1] for (a, b) in nltk.bigrams(ttext) if a[0] == "often"]
dist = nltk.FreqDist(tags)
dist.tabulate()

