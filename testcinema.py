from imdb import Cinemagoer

ia = Cinemagoer()

movie = ia.get_movie('0133093')

res = ia.search_person('Liam Neeson')

print(res)

print('Directors:')
for director in movie['directors']:
    print(director['name'])

print('Genres:')
for genre in movie['genres']:
    print(genre)

people = ia.search_person('Mel Gibson')

for person in people:
    print(person.personID, person['name'])
