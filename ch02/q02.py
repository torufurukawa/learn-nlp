from nltk.corpus import gutenberg
FILE_ID = "austen-persuasion.txt"

words = gutenberg.words(FILE_ID)
print("Words:", len(words))
print("Vocabulary:", len(set([w.lower() for w in words])))
