import baraja

ordenada = baraja.creaBaraja()
print("Esta es la primera baraja: ",ordenada)

otraBaraja = baraja.creaBaraja()
print("Esta es la segunda baraja: ", otraBaraja)
baraja.barajar(otraBaraja)
print("Y ahora la he barajado: ",otraBaraja)
