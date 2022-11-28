# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 12:29:02 2018
@author: Jhonatan
"""
"""Importar Librerías"""
import numpy as np
"""MATRIX COEFFICIENTS AND M & N VALUES FOR SOME COMMON MINERALS"""
MUD = [189.0,1.00,1.00]
""" Mineral = [DTma,DENma,DENneutron,M,N]"""
SIL = [55.5,2.65,-0.035,0.8091,0.6273] #Silíce
CAL = [47.6,2.71,0.00,0.8269,0.5848] #Calcita
DOL = [43.5,2.87,0.02,0.7781,0.5241] #Dolomita
ANH = [50.0,2.98,0.00,0.702,0.5051] #Anhidrita
YES = [52.0,2.35,0.49,1.0148,0.3778] #Yeso
SAL = [67.0,2.05,0.04,1.1619,0.9143] #Sal
LUT = [120.0,2.30,0.33,0.5308,0.5154] #VALOR SUJETO A CAMBIOS - LUTITA
"""RHOB,NPHI,DT.Tenemos columna M."""

"""CALCULO DE M,N & L"""
RHOB = np.array([],dtype=float)
Archivo_RHOB = open("Archivos_TXT/RHOB.txt")
for Linea_RHOB in Archivo_RHOB.readlines():
    Nueva_Linea_RHOB = Linea_RHOB.rstrip('\n')
    Nueva_Linea_Convertida_RHOB = float(Nueva_Linea_RHOB)
    RHOB = np.append(RHOB,Nueva_Linea_Convertida_RHOB)
Archivo_RHOB.close()
DT = np.array([],dtype=float)
Archivo_DT = open("Archivos_TXT/DT.txt")
for Linea_DT in Archivo_DT.readlines():
    Nueva_Linea_DT = Linea_DT.rstrip('\n')
    Nueva_Linea_Convertida_DT = float(Nueva_Linea_DT)
    DT = np.append(DT,Nueva_Linea_Convertida_DT)
Archivo_DT.close()
NPHI = np.array([],dtype=float)
Archivo_NPHI = open("Archivos_TXT/NPHI.txt")
for Linea_NPHI in Archivo_NPHI.readlines():
    Nueva_Linea_NPHI = Linea_NPHI.rstrip('\n')
    Nueva_Linea_Convertida_NPHI = float(Nueva_Linea_NPHI)
    NPHI = np.append(NPHI,Nueva_Linea_Convertida_NPHI)
Archivo_NPHI.close()
"""Calcular M"""
M_Litoporosidad = np.array([],dtype=float)
DT_Aumento = 0
for Dato_RHOB in RHOB:
    M = ((MUD[0] - DT[DT_Aumento])/(Dato_RHOB - MUD[1]))*0.01
    M_Litoporosidad = np.append(M_Litoporosidad,M)
    DT_Aumento = DT_Aumento + 1
Archivo_M = open("Archivos_TXT/M.txt","w")
i=0
for Dato_M in M_Litoporosidad:
    if i == 0:
        Archivo_M.writelines(str(round(Dato_M)))
    else:
        Archivo_M.writelines("\n"+str(round(Dato_M,4)))
    i=i+1
Archivo_M.close()
#
N_Litoporosidad = np.array([],dtype=float)
RHOB_Aumento = 0
for Dato_NPHI in NPHI:
    N = (MUD[2]-Dato_NPHI)/(RHOB[RHOB_Aumento]-MUD[1])
    N_Litoporosidad = np.append(N_Litoporosidad,N)
    RHOB_Aumento = RHOB_Aumento + 1
Archivo_N = open("Nuevos_Archivos_Creados/N.txt","w")
i=0
for Dato_N in N_Litoporosidad:
    if i == 0:
        Archivo_N.writelines(str(round(Dato_N,4)))
    else:
        Archivo_N.writelines("\n"+str(round(Dato_N,4)))
    i=i+1
Archivo_N.close()
#
L_Litoporosidad = np.array([],dtype=float)
NPHI_Aumento = 0
for Dato_DT  in DT:
    L = (((MUD[0] - Dato_DT)/(MUD[2] - NPHI[NPHI_Aumento]))*0.01)
    L_Litoporosidad = np.append(L_Litoporosidad,L)
    NPHI_Aumento = NPHI_Aumento +1
Archivo_L = open("Nuevos_Archivos_Creados/L.txt","w")
i=0
for Dato_L in L_Litoporosidad:
    if i==0:
        Archivo_L.writelines(str(round(Dato_L,4)))
    else:
        Archivo_L.writelines("\n"+str(round(Dato_L,4)))
    i=i+1
Archivo_L.close()