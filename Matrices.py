# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 20:09:21 2020
@author: s112e10
"""

'''
una funcion que reciba dos matrices de tamaño diferente n*m y n*x, 
llenarla con numeros aleatorios,los tamaños se le piden al usuario, 
se les hace el producto punto,cambiar por -1 o 0 los numeros primos
'''
import numpy as np

#funcion para crear matrices
def crearMatrices():
    print("Para la matriz nxm ")
    n=int(input("Ingrese el valor de n: "))
    m=int(input("Ingrese el valor de m: "))
    print("Para la matriz nxy ")
    y=int(input("Ingrese el valor de y: "))
    print("generando matriz...")
    nm=np.random.randint(0,100,size=(n,m))
    my=np.random.randint(0,100,size=(m,y))
    
    nm=np.reshape(nm,(n,m))
    my=np.reshape(my,(m,y))
    
    print(nm,'\n',my)
    print(np.dot(nm,my))
    
    return nm,my

#Funcion para obtener el producto punto
def productoPunto(matriz1,matriz2):
    return np.dot(matriz1,matriz2)



#Funcion para determinar si un numero es primo o no
def esPrimo(numero):
    divisores=0
    for i in range(numero):
        if numero%(i+1)==0:
            divisores=divisores+1
        
        if divisores>2:
            return False
    return True

#Funcion para reemplazar los numeros primos mi compa 
def reemplazarPrimosNorteños(matriz):
    for i in range(matriz.shape[0]):
        for j in range(matriz.shape[1]):
            res=esPrimo(matriz[i][j])
            if res==True:
                matriz[i][j]=-1
            
    return matriz

a,b=crearMatrices()
m=productoPunto(a,b)
print(m) 
print("...")
matriz=reemplazarPrimosNorteños(m)
print(matriz)
 