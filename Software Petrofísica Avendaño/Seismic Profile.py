# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 22:36:59 2021

@author: Jhonatan
"""
#Instrucciones de paro
def BubleSortOptimized (lista):
  swapped = True
  steps_ = len(lista)-1
  while steps_ > 0 and swapped:
    print('Step: ', steps_)
    swapped = False
    for i in range(steps_):
      print('indice: ',i,' comparado con: ', i+1)
      if lista[i] > lista[i+1]:
        swapped = True
        temp = lista[i]
        lista[i] = lista[i+1]
        lista[i+1] = temp
    steps_ = steps_ - 1
  return lista

x = BubleSortOptimized([1,2,3,4])
print(x)
