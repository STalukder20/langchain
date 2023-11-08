from imdb import Cinemagoer

ia = Cinemagoer()

movies = ia.search_movie('minions')

minions = ia.get_movie(movies[0].movieID)

print(minions['plot'])

# res = ia.search_person('Liam Neeson')

# print(res)

# print('Directors:')
# for director in movie['directors']:
#     print(director['name'])

# print('Genres:')
# for genre in movie['genres']:
#     print(genre)

# people = ia.search_person('Mel Gibson')

# for person in people:
#     print(person.personID, person['name'])
