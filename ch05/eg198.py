import nltk
tagged_words = nltk.corpus.brown.tagged_words(categories="news")
dist = nltk.FreqDist(tag.replace("$", r"\$") for (word, tag) in tagged_words)
dist.plot()
