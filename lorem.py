from random import randint

anime_word = [
     'Naruto','Ajin','Erased','DBZ','One punch Man','Noragami','Tokyo Ghuol',
     'Attack on titan','Boku no hero academia','kuroko no Basket ball','Haikyuu',
     'Death Note','Mirai Nikki','Boruto'
  ]

def animerize(word):
    random_pos = randint(0,len(anime_word)-1)
    return '{0}{1}'.format(word,anime_word[random_pos])

paragraphs = int(input('How many paragraphs of anime ipsum you want to create:'))

with open('ipsum.txt') as ipsum_original:
    items = ipsum_original.read().split()

for n in range(paragraphs):
    anime_text = list(map(animerize,items))
    with open('anime_ipsum.txt','a') as ipsum_anime:
        ipsum_anime.write(''.join(anime_text)+'\n\n')
