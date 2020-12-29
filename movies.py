import spacy
nlp = spacy.load("en_core_web_md")
sentences_to_compare = 'which movie to watch next'
f = open('movies.txt', 'r')
Hacker = 'Trying to save the world through tech' 'Will they succed without the authorities deeming it unlawful?' 'Will people see it as ground breaking'
'What about the people who will be affected by the hacker?' ' Who deems it right what they are doing?' 'Will they die or live to tell the tail'
model_Hacker = nlp(Hacker)
movies = []
def similarity_movie (test_string):
    for movie in ofile:
        movies.append(movie)
    sim_value = 0
    similarity_results = ""

    for mov in movies:
        similarity = nlp(mov).similarity(model_Hacker)
        print(str(similarity +"-"+ mov)
        if similarity > sim_value:
            sim_value = similarity
            similarity_results = mov
    print (f'Next movie, you would probally like {similarity_results[0:8]} the most from the list given')
    similarity_movie(movies)
    ofile.close()



