# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 13:24:09 2018
@author: Jhonatan
"""
"""Importar Librerías"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter;

"""Obtener datos de Profundidad"""
Profundidad = np.array([],dtype=float)
Archivo_Profundidad = open("Archivos_TXT/Profundidad.txt")
for Linea_Profundidad in Archivo_Profundidad.readlines():
    Nueva_Linea_Profundidad = Linea_Profundidad.rstrip('\n')
    Nueva_Linea_Convertida_Profundidad = float(Nueva_Linea_Profundidad)
    Profundidad = np.append(Profundidad,Nueva_Linea_Convertida_Profundidad)
Archivo_Profundidad.close()
"""Obtener datos de Rayos Gamma"""
RayosGamma=np.array([],dtype=float)
Archivo_RayosGamma = open("Archivos_TXT/GR.txt")
for Linea_RayosGamma in Archivo_RayosGamma.readlines():
    Nueva_Linea_RayosGamma = Linea_RayosGamma.rstrip('\n')
    Nueva_Linea_Convertida_RayosGamma =  float(Nueva_Linea_RayosGamma)
    RayosGamma = np.append(RayosGamma,Nueva_Linea_Convertida_RayosGamma)
Archivo_RayosGamma.close()
"""Obtener datos de DLL"""
ResistividadProfunda=np.array([],dtype=float)
Archivo_ResistividadProfunda = open("Archivos_TXT/DLL.txt")
for Linea_ResistividadProfunda in Archivo_ResistividadProfunda.readlines():
    Nueva_Linea_ResistividadProfunda = Linea_ResistividadProfunda.rstrip('\n')
    Nueva_Linea_Convertida_ResistividadProfunda =  float(Nueva_Linea_ResistividadProfunda)
    ResistividadProfunda = np.append(ResistividadProfunda,Nueva_Linea_Convertida_ResistividadProfunda)
Archivo_ResistividadProfunda.close()
"""Obtener datos de LLS"""
ResistividadSomera=np.array([],dtype=float)
Archivo_ResistividadSomera = open("Archivos_TXT/LLS.txt")
for Linea_ResistividadSomera in Archivo_ResistividadSomera.readlines():
    Nueva_Linea_ResistividadSomera = Linea_ResistividadSomera.rstrip('\n')
    Nueva_Linea_Convertida_ResistividadSomera =  float(Nueva_Linea_ResistividadSomera)
    ResistividadSomera = np.append(ResistividadSomera,Nueva_Linea_Convertida_ResistividadSomera)
Archivo_ResistividadSomera.close()
"""Obtener datos de FR"""
ResistividadParedPozo=np.array([],dtype=float)
Archivo_ResistividadParedPozo = open("Archivos_TXT/FR.txt")
for Linea_ResistividadParedPozo in Archivo_ResistividadParedPozo.readlines():
    Nueva_Linea_ResistividadParedPozo = Linea_ResistividadParedPozo.rstrip('\n')
    Nueva_Linea_Convertida_ResistividadParedPozo =  float(Nueva_Linea_ResistividadParedPozo)
    ResistividadParedPozo = np.append(ResistividadParedPozo,Nueva_Linea_Convertida_ResistividadParedPozo)
Archivo_ResistividadParedPozo.close()
"""Obtener datos de DT"""
BHC = np.array([],dtype=float)
Archivo_DT = open("Archivos_TXT/DT.txt")
for Linea_DT in Archivo_DT.readlines():
    Nueva_Linea_DT = Linea_DT.rstrip('\n')
    Nueva_Linea_Convertida_DT = float(Nueva_Linea_DT)
    BHC = np.append(BHC,Nueva_Linea_Convertida_DT)
Archivo_DT.close()
"""Obtener datos de RHOB"""
FDC = np.array([],dtype=float)
Archivo_RHOB = open("Nuevos_Archivos_Creados/RHOB.txt")
for Linea_RHOB in Archivo_RHOB.readlines():
    Nueva_Linea_RHOB = Linea_RHOB.rstrip('\n')
    Nueva_Linea_Convertida_RHOB = float(Nueva_Linea_RHOB)
    FDC = np.append(FDC,Nueva_Linea_Convertida_RHOB)
Archivo_RHOB.close()
"""Obtener datos de NPHI"""
CNL = np.array([],dtype=float)
Archivo_NPHI = open("Archivos_TXT/NPHI.txt")
for Linea_NPHI in Archivo_NPHI.readlines():
    Nueva_Linea_NPHI = Linea_NPHI.rstrip('\n')
    Nueva_Linea_Convertida_NPHI = float(Nueva_Linea_NPHI)
    CNL = np.append(CNL,Nueva_Linea_Convertida_NPHI)
Archivo_NPHI.close()
"""Obtener datos de mORG"""
mORG = np.array([],dtype=float)
Archivo_mORG = open("Nuevos_Archivos_Creados/Archivos_Finales/mORG.txt")
for Linea_mORG in Archivo_mORG.readlines():
    Nueva_Linea_mORG = Linea_mORG.rstrip('\n')
    Nueva_Linea_Convertida_mORG = float(Nueva_Linea_mORG)
    mORG = np.append(mORG,Nueva_Linea_Convertida_mORG)
Archivo_mORG.close()




"""Crear y establecer datos de la sabana"""
Graficar = plt.figure(figsize=(30,50),dpi=80)
Graficar.subplots_adjust(wspace=0.02,hspace=0.055)
"""Crear Divisiones Profundidad"""
Divisiones_Men_Prof = np.array([],dtype=float)
Divisiones_May_Prof = np.array([],dtype=float)
i=min(Profundidad)
j=0
for valor_Profundidad in Profundidad:
    if j%5 == 0:
        Divisiones_May_Prof = np.append(Divisiones_May_Prof,valor_Profundidad)
    else:
        Divisiones_Men_Prof = np.append(Divisiones_Men_Prof,valor_Profundidad)
    i=i+5
    j=j+1


"""                                     Rayos Gamma & Caliper                                   """

Registro_RayosGamma = Graficar.add_subplot(1,10,1)
Registro_RayosGamma.plot(RayosGamma,Profundidad, color="green", alpha=1)
Registro_RayosGamma.set_title("RG"+'\n'+"API°"+'\n\n',fontsize=14)

Registro_RayosGamma.set_ylim([max(Profundidad),min(Profundidad)])
Registro_RayosGamma.set_xlim([0,100])

Registro_RayosGamma.set_xticks([10,20,30,40,60,70,80,90],minor=True)
Registro_RayosGamma.set_xticks([0,50,100],minor=False)
Registro_RayosGamma.set_xticklabels(['      0',50,'100      '])
Registro_RayosGamma.xaxis.tick_top()

Registro_RayosGamma.set_yticks(Divisiones_Men_Prof,minor=True)
Registro_RayosGamma.set_yticks(Divisiones_May_Prof,minor=False)
Registro_RayosGamma.set_yticklabels([])
Registro_RayosGamma.yaxis.set_ticks_position('none')

Registro_RayosGamma.grid(which='minor',color="grey", alpha=.2)
Registro_RayosGamma.grid(which='major',color="black", alpha=.4)


"""                                        DLL, LLS & FR                                       """

"""DLL"""
Registro_ResistividadProfunda = Graficar.add_subplot(1,10,2)
Registro_ResistividadProfunda.plot(ResistividadProfunda,Profundidad, color="black", alpha=1)
Registro_ResistividadProfunda.set_xscale("log")


Registro_ResistividadProfunda.set_ylim([max(Profundidad),min(Profundidad)])
Registro_ResistividadProfunda.set_xlim([0.2,2000])
"""Salto de Línea DLL"""
Salto_ResistividadProfunda = np.array([],dtype=float)
for Dato_Salto_ResistividadProfunda in ResistividadProfunda:
            Dato_Salto_ResistividadProfunda = round((Dato_Salto_ResistividadProfunda/10000),4)
            Salto_ResistividadProfunda = np.append(Salto_ResistividadProfunda,Dato_Salto_ResistividadProfunda)
Registro_Salto_ResistividadProfunda = Graficar.add_subplot(1,10,2)
Registro_Salto_ResistividadProfunda.plot(Salto_ResistividadProfunda,Profundidad, color="black", alpha=1)
Registro_Salto_ResistividadProfunda.set_xscale("log")

Registro_Salto_ResistividadProfunda.set_ylim([max(Profundidad),min(Profundidad)])
Registro_Salto_ResistividadProfunda.set_xlim([0.2,2000])

"""LLS"""
Registro_ResistividadSomera = Graficar.add_subplot(1,10,2)
Registro_ResistividadSomera.plot(ResistividadSomera,Profundidad, color="blue", alpha=1)
Registro_ResistividadSomera.set_xscale("log")

Registro_ResistividadSomera.set_ylim([max(Profundidad),min(Profundidad)])
Registro_ResistividadSomera.set_xlim([0.2,2000])
"""Salto de Línea LLS"""
Salto_ResistividadSomera = np.array([],dtype=float)
for Dato_Salto_ResistividadSomera in ResistividadSomera:
            Dato_Salto_ResistividadSomera = round((Dato_Salto_ResistividadSomera/10000),4)
            Salto_ResistividadSomera = np.append(Salto_ResistividadSomera,Dato_Salto_ResistividadSomera)
Registro_Salto_ResistividadSomera = Graficar.add_subplot(1,10,2)
Registro_Salto_ResistividadSomera.plot(Salto_ResistividadSomera,Profundidad, color="blue", alpha=1)
Registro_Salto_ResistividadSomera.set_xscale("log")

Registro_Salto_ResistividadSomera.set_ylim([max(Profundidad),min(Profundidad)])
Registro_Salto_ResistividadSomera.set_xlim([0.2,2000])

"""FR"""
Registro_ResistividadParedPozo = Graficar.add_subplot(1,10,2)
Registro_ResistividadParedPozo.semilogx(ResistividadParedPozo,Profundidad, color="red", alpha=1)
Registro_ResistividadParedPozo.set_xscale("log")

Registro_ResistividadParedPozo.set_ylim([max(Profundidad),min(Profundidad)])
Registro_ResistividadParedPozo.set_xlim([0.2,2000])
"""Salto de Línea FR"""
Salto_ResistividadParedPozo = np.array([],dtype=float)
for Dato_Salto_ResistividadParedPozo in ResistividadParedPozo:
            Dato_Salto_ResistividadParedPozo = round((Dato_Salto_ResistividadParedPozo/10000),4)
            Salto_ResistividadParedPozo = np.append(Salto_ResistividadParedPozo,Dato_Salto_ResistividadParedPozo)
Registro_Salto_ResistividadParedPozo = Graficar.add_subplot(1,10,2)
Registro_Salto_ResistividadParedPozo.plot(Salto_ResistividadParedPozo,Profundidad, color="blue", alpha=1)
Registro_Salto_ResistividadParedPozo.set_xscale("log")

Registro_Salto_ResistividadParedPozo.set_ylim([max(Profundidad),min(Profundidad)])
Registro_Salto_ResistividadParedPozo.set_xlim([0.2,2000])

"""Formato del Carril DLL-LLS-FR"""
Registro_Salto_ResistividadParedPozo.set_xticks([.4,.6,.8,1,1.2,1.4,1.6,1.8,4,6,8,10,12,14,16,18,40,60,80,100,120,140,160,180,400,600,800,1000,1200,1400,1600,1800],minor=True)
Registro_Salto_ResistividadParedPozo.set_xticks([0.2,2,20,200,2000],minor=False)
Registro_Salto_ResistividadParedPozo.set_xticklabels([])
Registro_Salto_ResistividadParedPozo.set_title('DLL'+'\n'+'[OHM-m]'+'\n'+'LLS'+'\n'+'[OHM-m]'+'\n'+'FR'+'\n'+'[OHM-m]'+'\n\n',fontsize=10)

Registro_Salto_ResistividadParedPozo.set_xticklabels(['    .2','','20','','2000       '])
Registro_Salto_ResistividadParedPozo.xaxis.set_minor_formatter(FormatStrFormatter(""))
Registro_Salto_ResistividadParedPozo.xaxis.tick_top()

Registro_Salto_ResistividadParedPozo.set_yticks(Divisiones_Men_Prof,minor=True)
Registro_Salto_ResistividadParedPozo.set_yticks(Divisiones_May_Prof,minor=False)
Registro_Salto_ResistividadParedPozo.set_yticklabels([])
Registro_Salto_ResistividadParedPozo.yaxis.set_ticks_position('none')

Registro_Salto_ResistividadParedPozo.grid(which='minor',color="grey", alpha=.2)
Registro_Salto_ResistividadParedPozo.grid(which='major',color="black", alpha=.4)


"""                            DT,RHOB,NPHI - BHC,FDC,CNL                                       """
"""BHC"""
Registro_BHC = Graficar.add_subplot(1,10,3)
Registro_BHC.plot(BHC,Profundidad, color="black", alpha=1)

Registro_BHC.set_ylim([max(Profundidad),min(Profundidad)])
Registro_BHC.set_xlim([140,40])

#Registro_BHC = Graficar.add_subplot(133)
"""FDC"""
FDC_modif = np.array([],dtype=float)
for valor_FDC in FDC:
    nuevo_valor_FDC = ((2-valor_FDC)*100)+140
    FDC_modif = np.append(FDC_modif,nuevo_valor_FDC)

Registro_FDC = Graficar.add_subplot(1,10,3)
Registro_FDC.plot(FDC_modif,Profundidad, color="blue", alpha=1)

Registro_FDC.set_ylim([max(Profundidad),min(Profundidad)])
Registro_FDC.set_xlim([140,40])

"""CNL"""
CNL_modif = np.array([],dtype=float)
for valor_CNL in CNL:
    nuevo_valor_CNL = ((.45-valor_CNL)*-100/.6)+140
    CNL_modif = np.append(CNL_modif,nuevo_valor_CNL)

Registro_CNL = Graficar.add_subplot(1,10,3)
Registro_CNL.plot(CNL_modif,Profundidad, color="red", alpha=1)

Registro_CNL.set_ylim([max(Profundidad),min(Profundidad)])
Registro_CNL.set_xlim([140,40])

"""Formato del Carril BHC-FDC-CNL"""
Registro_CNL.set_xticks([130,120,110,100,80,70,60,50],minor=True)
Registro_CNL.set_xticks([140,90,40],minor=False)
Registro_CNL.set_xticklabels(['      .45',.15,'-.15      '])
Registro_CNL.xaxis.tick_top()

Registro_CNL.set_yticks(Divisiones_Men_Prof,minor=True)
Registro_CNL.set_yticks(Divisiones_May_Prof,minor=False)
Registro_CNL.set_yticklabels([])
Registro_CNL.yaxis.set_ticks_position('none')

Registro_CNL.grid(which='minor',color="grey", alpha=.2)
Registro_CNL.grid(which='major',color="black", alpha=.4)

"""                                              mORG                                          """
Registro_mORG = Graficar.add_subplot(1,10,4)
Registro_mORG.plot(mORG,Profundidad, color="black", alpha=1)
Registro_mORG.fill_betweenx(Profundidad,0,mORG,mORG >= 0,color='red',alpha=.4)
Registro_mORG.fill_betweenx(Profundidad,0,mORG,mORG < 0,color='blue',alpha=.4)


Registro_mORG.set_ylim([max(Profundidad),min(Profundidad)])
Registro_mORG.set_xlim([-10,10])

Registro_mORG.set_xticks([-9,-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8,9],minor=True)
Registro_mORG.set_xticks([-10,0,10],minor=False)
Registro_mORG.set_xticklabels(['      -10',0,'10      '])
Registro_mORG.xaxis.tick_top()

Registro_mORG.set_yticks(Divisiones_Men_Prof,minor=True)
Registro_mORG.set_yticks(Divisiones_May_Prof,minor=False)
Registro_mORG.set_yticklabels([])
Registro_mORG.yaxis.set_ticks_position('none')

Registro_mORG.grid(which='minor',color="grey", alpha=.2)
Registro_mORG.grid(which='major',color="black", alpha=.4)


"""Guardar Archivo"""
plt.savefig("Carriles_Pozo.png")