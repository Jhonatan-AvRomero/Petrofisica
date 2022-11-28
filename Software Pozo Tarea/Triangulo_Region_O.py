# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 14:31:52 2018
@author: Jhonatan
"""
"""CLASIFICACIÓN FINAL"""
region_final = np.array([],dtype=str)
i = 0
for dato_region in region_prefinal:
    if str(dato_region) == "Indefinido":
        if Clasificacion_M[i] == "ANH-DOL" and Clasificacion_N[i] == "ANH-DOL" and Clasificacion_L[i] == "DOL-YES":
            region_final =  np.append(region_final,"YES-DOL-ANH")
        elif Clasificacion_M[i] == "ANH-DOL" and Clasificacion_N[i] == "ANH-DOL" and Clasificacion_L[i] == "CAL-DOL":
            region_final =  np.append(region_final,"ANH-DOL-LUT")
        elif Clasificacion_M[i] == "ANH-DOL" and Clasificacion_N[i] == "ANH-DOL" and Clasificacion_L[i] == "SIL-ANH":
            region_final =  np.append(region_final,"ANH-DOL-LUT")
        elif Clasificacion_M[i] == "ANH-DOL" and Clasificacion_N[i] == "ANH-DOL" and Clasificacion_L[i] == "ANH-CAL":
            region_final =  np.append(region_final,"ANH-DOL-LUT")
        elif Clasificacion_M[i] == "ANH-DOL" and Clasificacion_N[i] == "YES-ANH" and Clasificacion_L[i] == "CAL-DOL":
            region_final =  np.append(region_final,"YES-DOL-ANH")
        elif Clasificacion_M[i] == "ANH-DOL" and Clasificacion_N[i] == "YES-ANH" and Clasificacion_L[i] == "DOL-YES":
            region_final =  np.append(region_final,"YES-DOL-ANH")
        elif Clasificacion_M[i] == "LUT-ANH" and Clasificacion_N[i] == "ANH-DOL" and Clasificacion_L[i] == "SAL-SIL":
            region_final =  np.append(region_final,"ANH-DOL-LUT")
        elif Clasificacion_M[i] == "LUT-ANH" and Clasificacion_N[i] == "ANH-DOL" and Clasificacion_L[i] == "SIL-ANH":
            region_final =  np.append(region_final,"ANH-DOL-LUT")
        elif Clasificacion_M[i] == "LUT-ANH" and Clasificacion_N[i] == "LUT-DOL" and Clasificacion_L[i] == "SAL-SIL":
            region_final =  np.append(region_final,"ANH-DOL-LUT")
        elif Clasificacion_M[i] == "LUT-ANH" and Clasificacion_N[i] == "LUT-DOL" and Clasificacion_L[i] == "SIL-ANH":
            region_final =  np.append(region_final,"ANH-DOL-LUT")
        elif Clasificacion_M[i] == "LUT-ANH" and Clasificacion_N[i] == "ANH-LUT" and Clasificacion_L[i] == "SAL-SIL":
            region_final =  np.append(region_final,"ANH-DOL-LUT")
        elif Clasificacion_M[i] == "LUT-ANH" and Clasificacion_N[i] == "ANH-LUT" and Clasificacion_L[i] == "SIL-ANH":
            region_final =  np.append(region_final,"ANH-DOL-LUT")
        elif Clasificacion_M[i] == "LUT-ANH" and Clasificacion_N[i] == "YES-ANH" and Clasificacion_L[i] == "LUT-SAL":
            region_final =  np.append(region_final,"ANH-DOL-LUT")
        elif Clasificacion_M[i] == "LUT-ANH" and Clasificacion_N[i] == "YES-ANH" and Clasificacion_L[i] == "CAL-DOL":
            region_final =  np.append(region_final,"ANH-DOL-LUT")
        elif Clasificacion_M[i] == "LUT-ANH" and Clasificacion_N[i] == "YES-ANH" and Clasificacion_L[i] == "SIL-ANH":
            region_final =  np.append(region_final,"ANH-DOL-LUT")
        elif Clasificacion_M[i] == "DOL-SIL" and Clasificacion_N[i] == "ANH-DOL" and Clasificacion_L[i] == "DOL-YES":
            region_final =  np.append(region_final,"YES-DOL-ANH")
        elif Clasificacion_M[i] == "SIL-CAL" and Clasificacion_N[i] == "ANH-DOL" and Clasificacion_L[i] == "DOL-YES":
            region_final =  np.append(region_final,"YES-DOL-ANH")
        elif Clasificacion_M[i] == "DOL-SIL" and Clasificacion_N[i] == "SIL-SAL" and Clasificacion_L[i] == "SAL-SIL":
            region_final =  np.append(region_final,"SIL-SAL-LUT")
        elif Clasificacion_M[i] == "SIL-CAL" and Clasificacion_N[i] == "SIL-SAL" and Clasificacion_L[i] == "SAL-SIL":
            region_final =  np.append(region_final,"SIL-SAL-LUT")
        elif Clasificacion_M[i] == "SIL-CAL" and Clasificacion_N[i] == "SIL-SAL" and Clasificacion_L[i] == "LUT-SAL":
            region_final =  np.append(region_final,"SIL-SAL-LUT")
        elif Clasificacion_M[i] == "ANH-DOL" and Clasificacion_N[i] == "SIL-SAL" and Clasificacion_L[i] == "LUT-SAL":
            region_final =  np.append(region_final,"SIL-SAL-LUT")
        elif Clasificacion_M[i] == "DOL-SIL" and Clasificacion_N[i] == "SIL-SAL" and Clasificacion_L[i] == "LUT-SAL":
            region_final =  np.append(region_final,"SIL-SAL-LUT")
        elif Clasificacion_M[i] == "CAL-YES" and Clasificacion_N[i] == "SIL-SAL" and Clasificacion_L[i] == "SIL-ANH":
            region_final =  np.append(region_final,"R2")
        elif Clasificacion_M[i] == "SIL-CAL" and Clasificacion_N[i] == "SIL-SAL" and Clasificacion_L[i] == "SIL-ANH":
            region_final =  np.append(region_final,"R2")
        elif Clasificacion_M[i] == "ANH-DOL" and Clasificacion_N[i] == "CAL-SIL" and Clasificacion_L[i] == "LUT-SAL":
            region_final =  np.append(region_final,"DOL-SIL-LUT")
        elif Clasificacion_M[i] == "DOL-SIL" and Clasificacion_N[i] == "CAL-SIL" and Clasificacion_L[i] == "LUT-SAL":
            region_final =  np.append(region_final,"DOL-SIL-LUT")
        elif Clasificacion_M[i] == "CAL-YES" and Clasificacion_N[i] == "SIL-SAL" and Clasificacion_L[i] == "CAL-DOL":
            region_final =  np.append(region_final,"R2")
        elif Clasificacion_M[i] == "YES-SAL" and Clasificacion_N[i] == "SIL-SAL" and Clasificacion_L[i] == "DOL-YES":
            region_final =  np.append(region_final,"R2")
        elif Clasificacion_M[i] == "CAL-YES" and Clasificacion_N[i] == "SIL-SAL" and Clasificacion_L[i] == "DOL-YES":
            region_final =  np.append(region_final,"R2")
        elif Clasificacion_M[i] == "YES-SAL" and Clasificacion_N[i] == "SIL-SAL" and Clasificacion_L[i] == "CAL-DOL":
            region_final =  np.append(region_final,"R2")
        elif Clasificacion_M[i] == "LUT-ANH" and Clasificacion_N[i] == "DOL-CAL" and Clasificacion_L[i] == "LUT-SAL":
            region_final =  np.append(region_final,"DOL-SIL-LUT")
        elif Clasificacion_M[i] == "LUT-ANH" and Clasificacion_N[i] == "CAL-SIL" and Clasificacion_L[i] == "LUT-SAL":
            region_final =  np.append(region_final,"DOL-SIL-LUT")
        elif Clasificacion_M[i] == "LUT-ANH" and Clasificacion_N[i] == "YES-ANH" and Clasificacion_L[i] == "SAL-SIL":
            region_final =  np.append(region_final,"ANH-DOL-LUT")
       
    else:
        region_final = np.append(region_final,dato_region)
    i=i+1
"""CREAR ARCHIVO TXT"""
i = 0 
for d in region_final:
    if str(d) == "Indefinido":
        print(i,Clasificacion_M[i],Clasificacion_N[i],Clasificacion_L[i])
    i=i+1
"""DETERMINACION POROSIDAD"""
Tipo_Porosidad = np.array([],dtype=str)
for dato_region in region_final:
    if str(dato_region) == "YES-DOL-ANH":
        Tipo_Porosidad = np.append(Tipo_Porosidad,"FIP")
    elif str(dato_region) == "ANH-DOL-LUT":
        Tipo_Porosidad = np.append(Tipo_Porosidad,"FIP")
    elif str(dato_region) == "SIL-SAL-LUT":
        Tipo_Porosidad = np.append(Tipo_Porosidad,"FIP")
    elif str(dato_region) == "DOL-SIL-LUT":
        Tipo_Porosidad = np.append(Tipo_Porosidad,"FIP")
    elif str(dato_region) == "DOL-CAL-SIL":
        Tipo_Porosidad = np.append(Tipo_Porosidad,"FIP")
    elif str(dato_region) == "R1":
        Tipo_Porosidad = np.append(Tipo_Porosidad,"FIS")
    elif str(dato_region) == "R2":
        Tipo_Porosidad = np.append(Tipo_Porosidad,"FIS")
#
Archivo_Tipo_Porosidad = open("Temporal/Tipo_Porosidad.txt","w")
i=0
for tipo_porosidad in Tipo_Porosidad:
    if i == 0:
        Archivo_Tipo_Porosidad.writelines(str(tipo_porosidad))
    else:
        Archivo_Tipo_Porosidad.writelines("\n"+str(tipo_porosidad))
    i=i+1
Archivo_Tipo_Porosidad.close()
#
Archivo_Triangulo_Region = open("Nuevos_Archivos_Creados/Triangulo_Region.txt","w")
i=0
for Dato_region in region_final:
    if i == 0:
        Archivo_Triangulo_Region.writelines(str(Dato_region)+" "+str(Tipo_Porosidad[i]))
    else:
        Archivo_Triangulo_Region.writelines("\n"+str(Dato_region)+" "+str(Tipo_Porosidad[i]))
    i=i+1
Archivo_Triangulo_Region.close()