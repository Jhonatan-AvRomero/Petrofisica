# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 23:40:04 2018

@author: Jhonatan
"""
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure(figsize=(10,10))
ax = plt.axes(projection='3d')
"""MATRIX COEFFICIENTS AND M & N VALUES FOR SOME COMMON MINERALS"""
M_Litoporosidad = np.array([],dtype=float)
Archivo_M = open("Archivos_TXT/M.txt")
for Linea_M in Archivo_M.readlines():
    Nueva_Linea_M = Linea_M.rstrip('\n')
    Nueva_Linea_Convertida_M = round((float(Nueva_Linea_M)),4)
    M_Litoporosidad = np.append(M_Litoporosidad,Nueva_Linea_Convertida_M)
Archivo_M.close()
"""DTF,den,NEUTRON"""
MUD = [189.0,1.00,1.00]
""" Mineral = [DTma,DENma,DENneutron,M,N,L]"""
SIL = [0.8091,0.6273,1.2899] #Silíce
CAL = [0.8269,0.5848,1.4140] #Calcita
DOL = [0.7781,0.5241,1.4847] #Dolomita
ANH = [0.7020,0.5051,1.3900] #Anhidrita
YES = [1.0148,0.3778,2.6863] #Yeso
SAL = [1.1619,0.9143,1.2708] #Sal
LUT = [0.5308,0.5154,1.0299] #VALOR SUJETO A CAMBIOS - LUTITA

X_LITO = [SIL[1],CAL[1],DOL[1],SIL[1]]#,ANH[1],YES[1],SAL[1],LUT[1]] 
Y_LITO = [SIL[0],CAL[0],DOL[0],SIL[0]]#,ANH[0],YES[0],SAL[0],LUT[0]]
Z_LITO = [SIL[2],CAL[2],DOL[2],SIL[2]]#,ANH[2],YES[2],SAL[2],LUT[2]]
"""M,N_Litoporosidad,L_Litoporosidad"""
ax.plot(X_LITO,Y_LITO,Z_LITO,'-k')

X_LITO1 = [DOL[1],SIL[1],LUT[1],DOL[1]]#,ANH[1],YES[1],SAL[1],LUT[1]] 
Y_LITO1 = [DOL[0],SIL[0],LUT[0],DOL[0]]#,ANH[0],YES[0],SAL[0],LUT[0]]
Z_LITO1 = [DOL[2],SIL[2],LUT[2],DOL[2]]#,ANH[2],YES[2],SAL[2],LUT[2]]

ax.plot(X_LITO1,Y_LITO1,Z_LITO1,'-k')

X_LITO2 = [DOL[1],YES[1]]#,ANH[1],YES[1],SAL[1],LUT[1]] 
Y_LITO2 = [DOL[0],YES[0]]#,ANH[0],YES[0],SAL[0],LUT[0]]
Z_LITO2 = [DOL[2],YES[2]]#,ANH[2],YES[2],SAL[2],LUT[2]]

ax.plot(X_LITO2,Y_LITO2,Z_LITO2,'-k')

X_LITO3 = [DOL[1],DOL[1]]#,ANH[1],YES[1],SAL[1],LUT[1]] 
Y_LITO3 = [DOL[0],1.2]#,ANH[0],YES[0],SAL[0],LUT[0]]
Z_LITO3 = [DOL[2],DOL[2]]#,ANH[2],YES[2],SAL[2],LUT[2]]

ax.plot(X_LITO3,Y_LITO3,Z_LITO3,'-k')

X_LITO4 = [CAL[1],CAL[1]]#,ANH[1],YES[1],SAL[1],LUT[1]] 
Y_LITO4 = [CAL[0],1.2]#,ANH[0],YES[0],SAL[0],LUT[0]]
Z_LITO4 = [CAL[2],CAL[2]]#,ANH[2],YES[2],SAL[2],LUT[2]]

ax.plot(X_LITO4,Y_LITO4,Z_LITO4,'-k')

X_LITO5 = [SIL[1],SIL[1]]#,ANH[1],YES[1],SAL[1],LUT[1]] 
Y_LITO5 = [SIL[0],1.2]#,ANH[0],YES[0],SAL[0],LUT[0]]
Z_LITO5 = [SIL[2],SIL[2]]#,ANH[2],YES[2],SAL[2],LUT[2]]

ax.plot(X_LITO5,Y_LITO5,Z_LITO5,'-k')

X_LITO6 = [SIL[1],CAL[1],DOL[1],SIL[1],ANH[1],YES[1],SAL[1],LUT[1]] 
Y_LITO6 = [SIL[0],CAL[0],DOL[0],SIL[0],ANH[0],YES[0],SAL[0],LUT[0]]
Z_LITO6 = [SIL[2],CAL[2],DOL[2],SIL[2],ANH[2],YES[2],SAL[2],LUT[2]]

ax.plot(X_LITO6,Y_LITO6,Z_LITO6,'o',color='brown')

ax.plot(N_Litoporosidad,M_Litoporosidad,L_Litoporosidad,"o",color="blue",markersize=1)

ax.set_title("Gráfica Litoporosidad 3D")

ax.set_xlim(.3,1)
ax.set_ylim(.3,1.2)
ax.set_xlabel('N',color="r",fontsize=15)
ax.set_ylabel('M',color="g",fontsize=15)
ax.set_zlabel('L',color="y",fontsize=15)
plt.show()