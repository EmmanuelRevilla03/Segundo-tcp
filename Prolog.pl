
ave(canario).
ave(paloma).
mamifero(perro).
mamifero(gato).


es_ave(X) :- ave(X), tiene_plumas(X), pone_huevos(X).
es_mamifero(X) :- mamifero(X), da_leche(X).


tiene_plumas(canario).
tiene_plumas(paloma).
pone_huevos(canario).
pone_huevos(paloma).
da_leche(perro).
da_leche(gato).
