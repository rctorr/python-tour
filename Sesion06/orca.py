#!/usr/bin/python

import random #esto es para que funciones la opcion de aleatorio

E=int(np) #convierte np a entero
le= " _ "*E
np=len(P) #obtiene la longitud de p
B=["gato","perro","bandera","ornitorrinco","lampara","anime","espejo","motocicleta","television","libreta"]
lp=list(P)
I=int(dead)
dead=str()
dead=[" O \n   \n   \n  \n"," O \n/  \n   \n   \n"," O \n/| \n   \n   \n"," O \n/|\\\n   \n   \n"," O \n/|\\\n |\n   \n"," O \n/|\\\n |\n/  \n"," O \n/|\\\n |\n/ \\\n"," O \n/|\\\n |\n/ \\\n"]

horca= [" +----+ \n |    | \n |      \n |      \n |      \n========"]

print "Juguemos al ahorcado"
print horca[0]
P=random.choice(B) #selecciona una opcio de la lista B
print le
print 'Intenta una letra'
L=raw_input() #lee algo de teclado
if P.__contains__(L)# revisa si existe la letra en la palabra

#pregunta como imprimir la letra, en caso de q este en la posicion correcta??






#if L in P
	
#print dead[2] #imprime lo que hay en dead

#for item in dead:
#	print item

