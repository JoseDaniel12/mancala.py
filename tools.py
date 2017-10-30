def obtener_tablero(cantidades):
	cantidades2=cantidades[:]
	impresion=""
	for i in cantidades2:
  		if len(i)<2:
  			cantidades2[cantidades2.index(i)]="0"+cantidades2[cantidades2.index(i)]
	fila00=""
	fila01="       *********************************************************************************************************************************************"
	fila02="       *                                                                                                                                           *"
	fila03="       *                            a               b               c                 d               e               f                            *"
	fila04="       *         J2                                                                                                                     J1         *"
	fila05="       *   **************     *************   *************   *************     *************   *************   *************     **************   *"
	fila06="       *   *            *     *           *   *           *   *           *     *           *   *           *   *           *     *            *   *"
	fila07="       *   *            *     *           *   *           *   *           *     *           *   *           *   *           *     *            *   *"
	fila08="       *   *            *     *           *   *           *   *           *     *           *   *           *   *           *     *            *   *"
	fila09="       *   *            *     *           *   *           *   *           *     *           *   *           *   *           *     *            *   *"
	fila10="       *   *            *     *           *   *           *   *           *     *           *   *           *   *           *     *            *   *"
	fila11="       *   *            *     *    "+cantidades2[1]+"     *   *    "+cantidades2[2]+"     *   *    "+cantidades2[3]+"     *     *     "+cantidades2[4]+"    *   *     "+cantidades2[5]+"    *   *     "+cantidades2[6]+"    *     *            *   *"
	fila12="       *   *            *     *           *   *           *   *           *     *           *   *           *   *           *     *            *   *"
	fila13="       *   *            *     *           *   *           *   *           *     *           *   *           *   *           *     *            *   *"
	fila14="       *   *            *     *           *   *           *   *           *     *           *   *           *   *           *     *            *   *"
	fila15="       *   *            *     *           *   *           *   *           *     *           *   *           *   *           *     *            *   *"
	fila16="       *   *            *     *           *   *           *   *           *     *           *   *           *   *           *     *            *   *"
	fila17="       *   *            *     *************   *************   *************     *************   *************   *************     *            *   *"
	fila18="       *   *            *                                                                                                         *            *   *"
	fila19="       *   *            *                                                                                                         *            *   *"
	fila20="       *   *            *                                                                                                         *            *   *"
	fila21="       *   *     "+cantidades2[0]+"     *           g               h                i                j               k              l            *     "+cantidades2[7]+"     *   *"
	fila22="       *   *            *                                                                                                         *            *   *"
	fila23="       *   *            *     *************   *************   *************     *************   *************   *************     *            *   *"
	fila24="       *   *            *     *           *   *           *   *           *     *           *   *           *   *           *     *            *   *"
	fila25="       *   *            *     *           *   *           *   *           *     *           *   *           *   *           *     *            *   *"
	fila26="       *   *            *     *           *   *           *   *           *     *           *   *           *   *           *     *            *   *"
	fila27="       *   *            *     *           *   *           *   *           *     *           *   *           *   *           *     *            *   *"
	fila28="       *   *            *     *           *   *           *   *           *     *           *   *           *   *           *     *            *   *"
	fila29="       *   *            *     *    "+cantidades2[13]+"     *   *    "+cantidades2[12]+"     *   *    "+cantidades2[11]+"     *     *     "+cantidades2[10]+"    *   *     "+cantidades2[9]+"    *   *     "+cantidades2[8]+"    *     *            *   *"
	fila30="       *   *            *     *           *   *           *   *           *     *           *   *           *   *           *     *            *   *"
	fila31="       *   *            *     *           *   *           *   *           *     *           *   *           *   *           *     *            *   *"
	fila32="       *   *            *     *           *   *           *   *           *     *           *   *           *   *           *     *            *   *"
	fila33="       *   *            *     *           *   *           *   *           *     *           *   *           *   *           *     *            *   *"
	fila34="       *   *            *     *           *   *           *   *           *     *           *   *           *   *           *     *            *   *"
	fila35="       *   **************     *************   *************   *************     *************   *************   *************     **************   *"
	fila36="       *                                                                                                                                           *"
	fila37="       *                                                                                                                                           *"
	fila38="       *                                                                                                                                           *"
	fila39="       *********************************************************************************************************************************************"
	tablero=[fila00,fila01,fila38,fila38,fila02,fila03,fila04,fila05,fila06,fila07,fila08,fila09,fila10,fila11,fila12,fila13,fila14,fila15,fila16,fila17,fila18,fila19,fila20,fila21,fila22,fila23,fila24,fila25,fila26,fila27,fila28,fila29,fila30,fila31,fila32,fila33,fila34,fila35,fila36,fila37,fila38,fila39]
	for i in range(len(tablero)):
		impresion+=tablero[i]+"\n"
	return impresion

def realizar_movimiento(tiro,tiros,turno,cantidades):
	incremento=[]
	repeticion=int(cantidades[tiros.index(tiro)])
	numero=tiros.index(tiro)
	for i in range(repeticion):
		numero-=1
		cantidades[numero]=str(int(cantidades[numero])+1)
		if numero==0 and turno==1 or numero==7 and turno==2:
			cantidades[numero]=str(int(cantidades[numero])-1)
			incremento.append(1)
	for i in range(len(incremento)):
		numero-=1
		cantidades[numero]=str(int(cantidades[numero])+1)
	cantidades[tiros.index(tiro)]="0"
	return (cantidades,numero)

def imprimir_turno(turno,jugador1,jugador2):
	texto=""
	if turno==2:
		turno=1
		texto+="Es el turno de "+jugador1+" (J1): "
	else:
		turno=2
		texto+="Es el truno de "+jugador2+" (J2): "
	return (texto,turno)

def cambiar_turno(numero,turno):
	if numero==0 or numero==7:
		if turno==1:
			turno=2
		else:
			turno=1
	return turno

def robar_semillas(turno,numero,cantidades):
	numeroc=numero
	if numero<0:
		numero=14-(-1*numero)
	if numero!=0 and numeroc!=7:
		if cantidades[numero]=="1":
			if (turno==1 and numero<=13 and numero>=8 or turno==2 and numero>=1 and numero<=6) and cantidades[14-numero]!="0":
				if turno==1:
					cantidades[7]=str(1+int(cantidades[7])+int(cantidades[14-numero]))
				else:
					cantidades[0]=str(1+int(cantidades[0])+int(cantidades[14-numero]))
				cantidades[numero]="0"
				cantidades[14-numero]="0"
	return cantidades 

def realizar_sumas(suma1,suma2,cantidades):
	for i in cantidades[:7]:
		suma1+=int(i)
	suma1-=int(cantidades[0])
	for i in cantidades[7:]:
		suma2+=int(i)
	suma2-=int(cantidades[7])
	if suma1==0 or suma2==0:
		cantidades[0]=str(int(cantidades[0])+suma1)
		cantidades[7]=str(int(cantidades[7])+suma2)
		for i in range(len(cantidades)):
			if i!=0 and i!=7:
				cantidades[i]="0"
	return(suma1,suma2,cantidades)

def establecer_ganador(puntajes,jugador1,jugador2):
	texto=""
	if puntajes[jugador1]!=puntajes[jugador2]:
		if puntajes[jugador1]>puntajes[jugador2]:
			texto+="El juego ha sido ganado por "+jugador1+" con "+str(puntajes[jugador1])+" puntos."
		else:
			texto+="EL juego ha sido ganado por "+jugador2+" con "+str(puntajes[jugador2])+" puntos."
	else:
		texto+="El juego a termindo en un empate felicidades a ambos jugadores."
	return texto
