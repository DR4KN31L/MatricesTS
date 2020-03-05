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
#recibe los tamños n,m,y dados por el usuario
#retorna una matriz NxM y una matriz MxY
def crearMatrices():
    print("Para la matriz nxm ")
    n=int(input("Ingrese el valor de n: "))
    m=int(input("Ingrese el valor de m: "))
    print("Para la matriz nxy ")
    y=int(input("Ingrese el valor de y: "))
    print("generando matriz...")
    matrizNxM=np.random.randint(0,100,size=(n,m))
    matrizMxY=np.random.randint(0,100,size=(m,y))
    
    matrizNxM=np.reshape(nm,(n,m))
    matrizMxY=np.reshape(my,(m,y))
    
    print(matrizNxM,'\n',matrizMxY)
    print(np.dot(matrizNxM,matrizMxY))
    
    return matrizNxM,matrizMxY

#Funcion para obtener el producto punto
#Requiere dos matrices n*m y m*x
#retorna el producto punto
def productoPunto(matriz1,matriz2):
    return np.dot(matriz1,matriz2)



#Funcion para determinar si un numero es primo o no
#La funcion requiere un numero
#retorna true si es un primo o false si no es primo
def esPrimo(numero):
    divisores=0
    for i in range(numero):
        if numero%(i+1)==0:
            divisores=divisores+1
        
        if divisores>2:
            return False
    return True

#Funcion para reemplazar los numeros primos
#requiere la matriz 
#retorna la matriz con los numeros primos cambiados por -1 
def reemplazarPrimosMatriz(matriz):
    for i in range(matriz.shape[0]):
        for j in range(matriz.shape[1]):
            res=esPrimo(matriz[i][j])
            if res==True:
                matriz[i][j]=-1
            
    return matriz
#Main 
def main():
    matrizNxM,matrizMxY=crearMatrices()
    matrizPunto=productoPunto(matrizNxM,matrizMxY)
    print(matrizPunto) 
    print("...")
    matrizPrimos=reemplazarPrimosMatriz(matrizPunto)
    print(matrizPrimos)
 
 
