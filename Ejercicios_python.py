# -*- coding: cp1252 -*-
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import math

#calcula la media de tres numeros
def media(_mediaValorA,_mediaValorB,_mediaValorC):
    
    _media=(_mediaValorA+_mediaValorB+_mediaValorC)/3
    print 'la media es: ',_media
    menu()


#calcula el mayor de tres numeros
def mayor(_valorA,_valorB,_valorC):

    if _valorA>_valorB and _valorA>_valorC:
        print 'El mayor: ',_valorA
    elif _valorB>_valorA and _valorB>_valorC:
        print 'El mayor: ',_valorB
    elif _valorC>_valorA and _valorC>_valorB:
        print 'El mayor: ',_valorC
    elif _valorA==_valorB and _valorA>_valorC:
        print 'El mayor: ',_valorA
    elif _valorA==_valorC and _valorA>_valorB:
        print 'El mayor: ',_valorA
    elif _valorB==_valorC and _valorB>_valorA:
        print 'El mayor: ',_valorB
    elif _valorB==_valorC and _valorB==_valorA:
        print 'El mayor: ',_valorA
    menu()


#calcula el volumen de una esfera
def volumen(_radio):
    _vol=(4.0/3.0*math.pi)*(_radio**3.0)
    print _vol
    menu()


#impares de inicio al 13
def impar(_dato):
    print list(range(13,_dato+1,2))
    menu()


#rotacion
def rotacion(_lista,_dato):

    _aux=0   
    while _aux <= _dato:
        _lista.append(_lista[_aux])
        _lista.remove(_lista[_aux])
        _aux+=1
        print _lista
    menu()


#intervalo de cubos
def intervaloSum(x):
    lista=[(i**3) for i in range(1,x+1)]
    print lista
    print (sum(lista))
    menu()


#intervalo de cuadrados
def tipoCuadrado(_datoFin):
    for _inicio in range(1,_datoFin+1):
        if ((_inicio**2)>100):
            print ([(_valor**2) for _valor in range(_inicio,_datoFin+1)])
            menu()


#intervalo de cuadrados 20 a 60
def tipoCuadradoV(_datoFin):
    for _inicio in range(1,_datoFin+1):
        if (_inicio>=20 and _inicio<=60):
            print ([(_valor) for _valor in range(_inicio,_datoFin+1)])
            menu()    
            

#calculo de la hipotenusa
def hipotenusa(_ladoA,_ladoB):
    print (math.sqrt((_ladoA**2)+(_ladoB**2)))
    menu()
    

#suma recursiva maximo 971
def sumaR(_dato,_resultado=0):
    if (_dato >=0):
        _resultado=_resultado+(_dato**2)
        return sumaR(_dato-1,_resultado)
    else:
        print _resultado
        menu()
     
#########################################

def menu():
    print ("\n#1 Media de tres numeros\n#2 Calcula el mayor\n#3 Volumen de esfera\n#4 Numeros impares\n#5 Rotacion de lista\n#6 Suma de cubos\n#7 Intervalo de cuadrados\n#8 Intervalo del 20 al 60\n#9 Hipotenusa\n#10 Suma recursiva\n")
    
    n=int(input('Seleccion: '))
    
    if n == 1:
        print ("Media")
        media(float(input('dato A: ')),float(input('dato B: ')),float(input('dato C: ')))
    elif n == 2:
        print ("Ingrese 3 numeros para calcular el mayor")
        mayor(float(input('dato A: ')),float(input('dato B: ')),float(input('dato C: ')))
    elif n == 3:
        print ("Volumen de una esfera")
        volumen(float(input('Radio: ')))
    elif  n == 4:
        print ("Rango impar")
        impar(int(input('dato final: ')))
    elif  n == 5:
        print ("Rotacion de una lista")
        rotacion(input('lista: '),input('datos a mover: '))
    elif  n == 6:
        print ("Suma de cubos")
        intervaloSum(int(input('dato final de la lista: ')))
    elif  n == 7:
        print ("Intervalo de cuadrados")
        tipoCuadrado(int(input('dato final del rango: ')))
    elif  n == 8:
        print ("Intervalo del 20 al 60")
        tipoCuadradoV(int(input('dato del rango: ')))
    elif  n == 9:
        print ("Hipotenusa")
        hipotenusa(float(input('dato A: ')),float(input('dato B: ')))
    elif  n == 10:
        print ("Suma recusiva")
        sumaR(int(input('dato rango: ')))        
    else:
        menu()
        
menu()
