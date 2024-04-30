filmes = {
'avatar':2009,
'titanic':1997,
'starwars':2015,
'harry-potter':2011,
'avengers':2012
}

filmes_novachave = filmes.fromkeys(filmes)
filmes_novachave = filmes.fromkeys(filmes, 'bilionário')
print(filmes.get('frozen'))
print(filmes.get('frozen', 2013))
print(filmes.get('avatar'))
filmes.items()
filmes.keys()
filmes.values()
filmes.update({"frozen":2013})
filmes