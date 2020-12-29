#Is that the monkey and the banana have high similarities compared to the the cat and the monkey, it because a monkey favourite fruit is a banana.
import spacy
nlp = spacy.load("en_core_web_md")
tokens = nlp ('mouse cat dog snake ')
for token1 in tokens:
    for token2 in tokens:
        print (token1.text, token2.text, token1.similarity(token2))

word1 = nlp ("mouse")
word2= nlp ("cat")
word3= nlp ("dog")
word4= nlp ("snake")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
print(word4.similarity(word2))
print(word4.similarity(word1))
print(word3.similarity(word4))

