import tools
tiros=["J2","a","b","c","d","e","f","J1","l","k","j","i","h","g"]
cantidades=["0","4","4","4","4","4","4","0","4","4","4","4","4","4"]
print("\n"+"Bienvenidos, espero que difruten de este juego de Mancala. ")
jugador1=input("Ingrese el apodo del primer jugador:  ")
jugador2=input("Ingrese el apodo del segundo jugador: ")
suma1=24
suma2=24
turno=2
texto=""
puntajes={jugador1:int(cantidades[7]), jugador2:int(cantidades[0])}
print(tools.obtener_tablero(cantidades))
while  cantidades[0]!=25 and cantidades[7]!=25 and suma1!=0 and suma2!=0:
  suma1=0
  suma2=0
  texto,turno=tools.imprimir_turno(turno,jugador1,jugador2)
  print(texto)
  tiro="repetir"
  if turno==1:
    while tiro not in tiros or tiro=="J1"or tiro=="J2" or tiro in tiros[:7] or cantidades[tiros.index(tiro)]=="0":
      tiro=input("Ingrese la literal de la casilla a escoger (g-l): ")
  else:
    while tiro not in tiros or tiro=="J1" or tiro=="J2" or tiro in tiros[7:] or cantidades[tiros.index(tiro)]=="0":
      tiro=input("Ingrese la literal de la casilla a escoger (a-f): ")  
  cantidades,numero=tools.realizar_movimiento(tiro,tiros,turno,cantidades)
  turno=tools.cambiar_turno(numero,turno)
  cantidades=tools.robar_semillas(turno,numero,cantidades)
  suma1,suma2,cantidades=tools.realizar_sumas(suma1,suma2,cantidades)
  print(tools.obtener_tablero(cantidades))
  puntajes={jugador1:int(cantidades[7]), jugador2:int(cantidades[0])}
print(tools.establecer_ganador(puntajes,jugador1,jugador2))
