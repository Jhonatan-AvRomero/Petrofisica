# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 22:18:14 2018
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

"""Crear Divisiones Profundidad"""
Divisiones_Men_Prof = np.array([],dtype=float)
Divisiones_May_Prof = np.array([],dtype=float)
Distancia = int(max(Profundidad)-min(Profundidad)+1)
Step = np.arange(0,Distancia,1)
ds=0
for vstep in Step:
    if vstep%5 == 0:
        if ds%5 == 0:
            Division_Mayor = min(Profundidad)+vstep
            Divisiones_May_Prof = np.append(Divisiones_May_Prof,Division_Mayor)
        else:
            Division_Menor = min(Profundidad)+vstep
            Divisiones_Men_Prof = np.append(Divisiones_Men_Prof,Division_Menor)
        ds=ds+1
"""                                     Rayos Gamma & Caliper                                   """
fig = plt.figure(figsize=(5,45))
Registro_RayosGamma = fig.add_subplot(1,1,1)
Registro_RayosGamma.plot(RayosGamma,Profundidad, color="green", alpha=4, linewidth=4)

Registro_RayosGamma.set_ylim([max(Profundidad),min(Profundidad)])
Registro_RayosGamma.set_xlim([0,100])
Registro_RayosGamma.set_title('Rayos'+'\n'+'Gamma'+'\n\n'+'°API'+'\n',fontsize=16,)

Registro_RayosGamma.set_xticks([10,20,30,40,60,70,80,90],minor=True)
Registro_RayosGamma.set_xticks([0,50,100],minor=False)
#Registro_RayosGamma.set_xticklabels([0,50,100])
Registro_RayosGamma.xaxis.tick_top()

Registro_RayosGamma.set_yticks(Divisiones_Men_Prof,minor=True)
Registro_RayosGamma.set_yticks(Divisiones_May_Prof,minor=False)
Registro_RayosGamma.set_yticklabels(['','',''])
Registro_RayosGamma.yaxis.set_ticks_position('none')

Registro_RayosGamma.grid(which='minor',color="grey", alpha=1,linewidth=1.5)
Registro_RayosGamma.grid(which='major',color="black", alpha=4,linewidth=3)

plt.savefig("Carriles_Registro/RayosGamma.png",bbox_inches='tight',dpi=50)

"""PROFUNDIDAD"""
CERO = np.array([],dtype=int)
for vRG in RayosGamma:
    vCERO = (vRG - vRG)
    CERO = np.append(CERO,vCERO)

fig = plt.figure(figsize=(2.5,45))
Registro_Profundidad = fig.add_subplot(1,1,1)
Registro_Profundidad.plot(CERO,Profundidad,'white')
for vDIV in Divisiones_May_Prof:
    Registro_Profundidad.annotate(vDIV,xy=(0,vDIV),fontsize=22,color="black")    
for vDIV in Divisiones_Men_Prof:
    Registro_Profundidad.annotate(vDIV,xy=(1,vDIV),fontsize=18,color="grey")

Registro_Profundidad.set_ylim([max(Profundidad),min(Profundidad)])
Registro_Profundidad.set_xlim([-1,9])

Registro_Profundidad.set_xticklabels([])
Registro_Profundidad.xaxis.tick_top()
Registro_Profundidad.set_xticks([])
Registro_Profundidad.set_title('Profundidad'+'\n\n',fontsize=16,)

Registro_Profundidad.set_yticks(Divisiones_Men_Prof,minor=True)
Registro_Profundidad.set_yticks(Divisiones_May_Prof,minor=False)
Registro_Profundidad.set_yticklabels([])
Registro_Profundidad.yaxis.set_ticks_position('none')

Registro_Profundidad.grid(which='minor',color="grey", alpha=1,linewidth=1.5)
Registro_Profundidad.grid(which='major',color="black", alpha=4,linewidth=3)

plt.savefig("Carriles_Registro/Profundidades.png",bbox_inches='tight',dpi=50)


"""                                        DLL, LLS & FR                                       """
fig = plt.figure(figsize=(5,45))

"""DLL"""
Registro_ResistividadProfunda = fig.add_subplot(1,1,1)
Registro_ResistividadProfunda.plot(ResistividadProfunda,Profundidad, color="black", alpha=1, linewidth=4)
Registro_ResistividadProfunda.set_xscale("log")


Registro_ResistividadProfunda.set_ylim([max(Profundidad),min(Profundidad)])
Registro_ResistividadProfunda.set_xlim([0.2,2000])
"""Salto de Línea DLL"""
Salto_ResistividadProfunda = np.array([],dtype=float)
for Dato_Salto_ResistividadProfunda in ResistividadProfunda:
            Dato_Salto_ResistividadProfunda = round((Dato_Salto_ResistividadProfunda/10000),4)
            Salto_ResistividadProfunda = np.append(Salto_ResistividadProfunda,Dato_Salto_ResistividadProfunda)
Registro_Salto_ResistividadProfunda = fig.add_subplot(1,1,1)
Registro_Salto_ResistividadProfunda.plot(Salto_ResistividadProfunda,Profundidad, color="black", alpha=1, linewidth=4)
Registro_Salto_ResistividadProfunda.set_xscale("log")

Registro_Salto_ResistividadProfunda.set_ylim([max(Profundidad),min(Profundidad)])
Registro_Salto_ResistividadProfunda.set_xlim([0.2,2000])

"""LLS"""
Registro_ResistividadSomera = fig.add_subplot(1,1,1)
Registro_ResistividadSomera.plot(ResistividadSomera,Profundidad, color="blue", alpha=1, linewidth=4)
Registro_ResistividadSomera.set_xscale("log")

Registro_ResistividadSomera.set_ylim([max(Profundidad),min(Profundidad)])
Registro_ResistividadSomera.set_xlim([0.2,2000])
"""Salto de Línea LLS"""
Salto_ResistividadSomera = np.array([],dtype=float)
for Dato_Salto_ResistividadSomera in ResistividadSomera:
            Dato_Salto_ResistividadSomera = round((Dato_Salto_ResistividadSomera/10000),4)
            Salto_ResistividadSomera = np.append(Salto_ResistividadSomera,Dato_Salto_ResistividadSomera)
Registro_Salto_ResistividadSomera = fig.add_subplot(1,1,1)
Registro_Salto_ResistividadSomera.plot(Salto_ResistividadSomera,Profundidad, color="blue", alpha=1, linewidth=4)
Registro_Salto_ResistividadSomera.set_xscale("log")

Registro_Salto_ResistividadSomera.set_ylim([max(Profundidad),min(Profundidad)])
Registro_Salto_ResistividadSomera.set_xlim([0.2,2000])

"""FR"""
Registro_ResistividadParedPozo = fig.add_subplot(1,1,1)
Registro_ResistividadParedPozo.semilogx(ResistividadParedPozo,Profundidad, color="red", alpha=1, linewidth=4)
Registro_ResistividadParedPozo.set_xscale("log")

Registro_ResistividadParedPozo.set_ylim([max(Profundidad),min(Profundidad)])
Registro_ResistividadParedPozo.set_xlim([0.2,2000])
"""Salto de Línea FR"""
Salto_ResistividadParedPozo = np.array([],dtype=float)
for Dato_Salto_ResistividadParedPozo in ResistividadParedPozo:
            Dato_Salto_ResistividadParedPozo = round((Dato_Salto_ResistividadParedPozo/10000),4)
            Salto_ResistividadParedPozo = np.append(Salto_ResistividadParedPozo,Dato_Salto_ResistividadParedPozo)
Registro_Salto_ResistividadParedPozo = fig.add_subplot(1,1,1)
Registro_Salto_ResistividadParedPozo.plot(Salto_ResistividadParedPozo,Profundidad, color="blue", alpha=1, linewidth=4)
Registro_Salto_ResistividadParedPozo.set_xscale("log")

Registro_Salto_ResistividadParedPozo.set_ylim([max(Profundidad),min(Profundidad)])
Registro_Salto_ResistividadParedPozo.set_xlim([0.2,2000])

"""Formato del Carril DLL-LLS-FR"""
Registro_Salto_ResistividadParedPozo.set_xticks([.4,.6,.8,1,1.2,1.4,1.6,1.8,4,6,8,10,12,14,16,18,40,60,80,100,120,140,160,180,400,600,800,1000,1200,1400,1600,1800],minor=True)
Registro_Salto_ResistividadParedPozo.set_xticks([0.2,2,20,200,2000],minor=False)
Registro_Salto_ResistividadParedPozo.set_xticklabels([0.2,2,20,200,2000])
Registro_Salto_ResistividadParedPozo.set_title('DLL'+'\n'+'[OHM-m]'+'\n\n'+'LLS'+'\n'+'[OHM-m]'+'\n\n'+'FR'+'\n'+'[OHM-m]'+'\n\n\n\n',fontsize=12)

#Registro_Salto_ResistividadParedPozo.set_xticklabels(['    .2','','20','','2000         '])
Registro_Salto_ResistividadParedPozo.xaxis.set_minor_formatter(FormatStrFormatter(""))
Registro_Salto_ResistividadParedPozo.xaxis.tick_top()

Registro_Salto_ResistividadParedPozo.set_yticks(Divisiones_Men_Prof,minor=True)
Registro_Salto_ResistividadParedPozo.set_yticks(Divisiones_May_Prof,minor=False)
Registro_Salto_ResistividadParedPozo.set_yticklabels([])
Registro_Salto_ResistividadParedPozo.yaxis.set_ticks_position('none')

Registro_Salto_ResistividadParedPozo.grid(which='minor',color="grey", alpha=1,linewidth=1)
Registro_Salto_ResistividadParedPozo.grid(which='major',color="black", alpha=4,linewidth=3)

plt.savefig("Carriles_Registro/Resistividades.png",bbox_inches='tight',dpi=500)

"""                            DT,RHOB,NPHI - BHC,FDC,CNL                                       """
fig = plt.figure(figsize=(5,45))
"""BHC"""
Registro_BHC = fig.add_subplot(1,1,1)
Registro_BHC.plot(BHC,Profundidad, color="black", alpha=1, linewidth=4)

Registro_BHC.set_ylim([max(Profundidad),min(Profundidad)])
Registro_BHC.set_xlim([140,40])

"""FDC"""
FDC_modif = np.array([],dtype=float)
for valor_FDC in FDC:
    nuevo_valor_FDC = ((2-valor_FDC)*100)+140
    FDC_modif = np.append(FDC_modif,nuevo_valor_FDC)

Registro_FDC = fig.add_subplot(1,1,1)
Registro_FDC.plot(FDC_modif,Profundidad, color="blue", alpha=1, linewidth=4)

Registro_FDC.set_ylim([max(Profundidad),min(Profundidad)])
Registro_FDC.set_xlim([140,40])

"""CNL"""
CNL_modif = np.array([],dtype=float)
for valor_CNL in CNL:
    nuevo_valor_CNL = ((.45-valor_CNL)*-100/.6)+140
    CNL_modif = np.append(CNL_modif,nuevo_valor_CNL)

Registro_CNL = fig.add_subplot(1,1,1)
Registro_CNL.plot(CNL_modif,Profundidad, color="red", alpha=1, linewidth=4)

Registro_CNL.set_ylim([max(Profundidad),min(Profundidad)])
Registro_CNL.set_xlim([140,40])

"""Formato del Carril BHC-FDC-CNL"""
Registro_CNL.set_xticks([130,120,110,100,80,70,60,50],minor=True)
Registro_CNL.set_xticks([140,90,40],minor=False)
#Registro_CNL.set_xticklabels(['      .45',.15,'-.15      '])
Registro_CNL.set_xticklabels([])
Registro_CNL.xaxis.tick_top()

Registro_CNL.set_yticks(Divisiones_Men_Prof,minor=True)
Registro_CNL.set_yticks(Divisiones_May_Prof,minor=False)
Registro_CNL.set_yticklabels([])
Registro_CNL.yaxis.set_ticks_position('none')

Registro_CNL.grid(which='minor',color="grey", alpha=1,linewidth=1)
Registro_CNL.grid(which='major',color="black", alpha=4,linewidth=3)

plt.savefig("Carriles_Registro/Porosidades.png",bbox_inches='tight',dpi=500)


"""                                              mORG                                          """
fig = plt.figure(figsize=(5,45))

Registro_mORG = fig.add_subplot(1,1,1)
Registro_mORG.plot(mORG,Profundidad, color="black", alpha=1)
Registro_mORG.fill_betweenx(Profundidad,0,mORG,mORG >= 0,color='red',alpha=.6)
Registro_mORG.fill_betweenx(Profundidad,0,mORG,mORG < 0,color='blue',alpha=.6)


Registro_mORG.set_ylim([max(Profundidad),min(Profundidad)])
Registro_mORG.set_xlim([-10,10])

Registro_mORG.set_xticks([-9,-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8,9],minor=True)
Registro_mORG.set_xticks([-10,0,10],minor=False)
Registro_mORG.set_xticklabels([])
#Registro_mORG.set_xticklabels(['      -10',0,'10      '])
Registro_mORG.xaxis.tick_top()

Registro_mORG.set_yticks(Divisiones_Men_Prof,minor=True)
Registro_mORG.set_yticks(Divisiones_May_Prof,minor=False)
Registro_mORG.set_yticklabels([])
Registro_mORG.yaxis.set_ticks_position('none')

Registro_mORG.grid(which='minor',color="grey", alpha=1,linewidth=1.5)
Registro_mORG.grid(which='major',color="black", alpha=4,linewidth=3)

plt.savefig("Carriles_Registro/mORG.png",bbox_inches='tight',dpi=500)

"""                                              m                                               """
fig = plt.figure(figsize=(5,45))

Registro_m = fig.add_subplot(1,1,1)
Registro_m.plot(m,Profundidad, color="#00BFFF", alpha=1,linewidth=4)
Registro_m.fill_betweenx(Profundidad,0,m,color='#00BFFF',alpha=.7)

                
Registro_m.set_ylim([max(Profundidad),min(Profundidad)])
Registro_m.set_xlim([0,5])

Registro_m.set_xticks([.5,1,1.5,2,3,3.5,4,4.5],minor=True)
Registro_m.set_xticks([0,2.5,5],minor=False)
Registro_m.set_xticklabels([])
Registro_m.xaxis.tick_top()

Registro_m.set_yticks(Divisiones_Men_Prof,minor=True)
Registro_m.set_yticks(Divisiones_May_Prof,minor=False)
Registro_m.set_yticklabels([])
Registro_m.yaxis.set_ticks_position('none')

Registro_m.grid(which='minor',color="grey", alpha=1,linewidth=1.5)
Registro_m.grid(which='major',color="black", alpha=4,linewidth=3)

plt.savefig("Carriles_Registro/m.png",bbox_inches='tight',dpi=500)

"""                                  Volumenes                                     """
fig = plt.figure(figsize=(10,45))
Registro_Volumenes = fig.add_subplot(1,1,1)

VANHG = np.array([],dtype=float)
VCALG = np.array([],dtype=float)
VDOLG = np.array([],dtype=float)
VLUTG = np.array([],dtype=float)
VSALG = np.array([],dtype=float)
VSILG = np.array([],dtype=float)
VYESG = np.array([],dtype=float)
i=0
for vANHR in VANHR:
    vCALR = VCALR[i]+vANHR
    vDOLR = VDOLR[i]+vCALR
    vLUTR = VLUTR[i]+vDOLR
    vSALR = VSALR[i]+vLUTR
    vSILR = VSILR[i]+vSALR
    vYESR = VYESR[i]+vSILR
    VANHG = np.append(VANHG,vANHR)
    VCALG = np.append(VCALG,vCALR)
    VDOLG = np.append(VDOLG,vDOLR)
    VLUTG = np.append(VLUTG,vLUTR)
    VSALG = np.append(VSALG,vSALR)
    VSILG = np.append(VSILG,vSILR)
    VYESG = np.append(VYESG,vYESR)    
    i=i+1

Registro_Volumenes.plot(VYESG,Profundidad, color="#F4A460", alpha=1,linewidth=0)
Registro_Volumenes.fill_betweenx(Profundidad,0,VYESG,color='#F4A460')

Registro_Volumenes.plot(VSILG,Profundidad, color="#7B68EE", alpha=1,linewidth=0)
Registro_Volumenes.fill_betweenx(Profundidad,0,VSILG,color='#7B68EE')
                                 
Registro_Volumenes.plot(VSALG,Profundidad, color="#7FFF00", alpha=1,linewidth=0)
Registro_Volumenes.fill_betweenx(Profundidad,0,VSALG,color='#7FFF00')
                                 
Registro_Volumenes.plot(VLUTG,Profundidad, color="#87CEFA", alpha=1,linewidth=0)
Registro_Volumenes.fill_betweenx(Profundidad,0,VLUTG,color='#87CEFA')
                                 
Registro_Volumenes.plot(VDOLG,Profundidad, color="#DC143C", alpha=1,linewidth=0)
Registro_Volumenes.fill_betweenx(Profundidad,0,VDOLG,color='#DC143C')
                                 
Registro_Volumenes.plot(VCALG,Profundidad, color="#FFD700", alpha=1,linewidth=0)
Registro_Volumenes.fill_betweenx(Profundidad,0,VCALG,color='#FFD700')
                                 
Registro_Volumenes.plot(VANHG,Profundidad, color="#8B4513", alpha=1,linewidth=0)
Registro_Volumenes.fill_betweenx(Profundidad,0,VANHG,color='#8B4513')
                             
Registro_Volumenes.set_ylim([max(Profundidad),min(Profundidad)])
Registro_Volumenes.set_xlim([0,1])

Registro_Volumenes.set_xticks([.1,.2,.3,.4,.6,.7,.8,.9],minor=True)
Registro_Volumenes.set_xticks([0,.5,1],minor=False)
Registro_Volumenes.set_xticklabels([])
#Registro_Volumenes.set_xticklabels(['      0',0.5,'1     '])
Registro_Volumenes.xaxis.tick_top()

Registro_Volumenes.set_yticks(Divisiones_Men_Prof,minor=True)
Registro_Volumenes.set_yticks(Divisiones_May_Prof,minor=False)
Registro_Volumenes.set_yticklabels([])
Registro_Volumenes.yaxis.set_ticks_position('none')

Registro_Volumenes.grid(which='minor',color="grey", alpha=1,linewidth=1.5)
Registro_Volumenes.grid(which='major',color="black", alpha=4,linewidth=3)

plt.savefig("Carriles_Registro/VolumenesLito.png",bbox_inches='tight',dpi=500)

"""                                Porosidad Total                                  """
fig = plt.figure(figsize=(5,45))
Registro_FI = fig.add_subplot(1,1,1)

Registro_FI.plot(FITR,Profundidad, color="black", alpha=.8,linewidth=1)
Registro_FI.fill_betweenx(Profundidad,0,FITR,color='#FFFF00')

Registro_FI.plot(FISR,Profundidad, color="#228B22", alpha=1,linewidth=1)
Registro_FI.fill_betweenx(Profundidad,0,FISR,color='#228B22')

Registro_FI.set_ylim([max(Profundidad),min(Profundidad)])
Registro_FI.set_xlim([0,.3])

Registro_FI.set_xticks([.03,.06,.09,.12,.18,.21,.24,.27],minor=True)
Registro_FI.set_xticks([0,.15,.3],minor=False)
Registro_FI.set_xticklabels([])
#Registro_FI.set_xticklabels(['      0',.15,'0.3      '])
Registro_FI.xaxis.tick_top()

Registro_FI.set_yticks(Divisiones_Men_Prof,minor=True)
Registro_FI.set_yticks(Divisiones_May_Prof,minor=False)
Registro_FI.set_yticklabels([])
Registro_FI.yaxis.set_ticks_position('none')

Registro_FI.grid(which='minor',color="grey", alpha=1,linewidth=1.5)
Registro_FI.grid(which='major',color="black", alpha=4,linewidth=3)

plt.savefig("Carriles_Registro/FITR.png",bbox_inches='tight',dpi=500)

"""                  mBORAI, msHELL, mPICKETT                                   """
fig = plt.figure(figsize=(5,45))
Registro_mBSP = fig.add_subplot(1,1,1)

mPICKETT = np.array([],dtype=float)
for vS in mSHELL:
    vP = 1.1003
    mPICKETT = np.append(mPICKETT,vP)

Registro_mBSP.plot(mSHELL,Profundidad, color="green", alpha=1, linewidth=3)
Registro_mBSP.plot(mBORAI,Profundidad, color="blue", alpha=1, linewidth=3)
Registro_mBSP.plot(mPICKETT,Profundidad, color="red", alpha=1, linewidth=3)
    
Registro_mBSP.set_ylim([max(Profundidad),min(Profundidad)])
Registro_mBSP.set_xlim([0,5])

Registro_mBSP.set_xticks([1,2,3,4],minor=True)
Registro_mBSP.set_xticks([0,2.5,5],minor=False)
Registro_mBSP.set_xticklabels([])
#Registro_mBSP.set_xticklabels(['      0',2.5,'5      '])
Registro_mBSP.xaxis.tick_top()

Registro_mBSP.set_yticks(Divisiones_Men_Prof,minor=True)
Registro_mBSP.set_yticks(Divisiones_May_Prof,minor=False)
Registro_mBSP.set_yticklabels([])
Registro_mBSP.yaxis.set_ticks_position('none')

Registro_mBSP.grid(which='minor',color="grey", alpha=1,linewidth=1.5)
Registro_mBSP.grid(which='major',color="black", alpha=4,linewidth=3)

plt.savefig("Carriles_Registro/mBSP.png",bbox_inches='tight',dpi=500)

"""                 T vs r             """
fig = plt.figure(figsize=(5,45))

Registro_T = fig.add_subplot(1,2,1)
fig.subplots_adjust(wspace=0.0)

Registro_T.plot(T_m,Profundidad, color="blue", alpha=1, linewidth=4)

Registro_T.set_ylim([max(Profundidad),min(Profundidad)])
Registro_T.set_xlim([100,0])

Registro_T.set_xticks([10,20,30,40,60,70,80,90],minor=True)
Registro_T.set_xticks([0,50,100],minor=False)
Registro_T.set_xticklabels([])
#Registro_T.set_xticklabels(['      0',50,'100      '])
Registro_T.xaxis.tick_top()

Registro_T.set_yticks(Divisiones_Men_Prof,minor=True)
Registro_T.set_yticks(Divisiones_May_Prof,minor=False)
Registro_T.set_yticklabels([])
Registro_T.yaxis.set_ticks_position('none')

Registro_T.grid(which='minor',color="grey", alpha=1,linewidth=1.5)
Registro_T.grid(which='major',color="black", alpha=4,linewidth=3)

Registro_r = fig.add_subplot(1,2,2)

Registro_r.plot(r,Profundidad, color="green", alpha=1,linewidth=4)

Registro_r.set_ylim([max(Profundidad),min(Profundidad)])
Registro_r.set_xlim([0,10])

Registro_r.set_xticks([1,2,3,4,6,7,8,9],minor=True)
Registro_r.set_xticks([0,5,10],minor=False)
Registro_r.set_xticklabels([])
#Registro_T.set_xticklabels(['      0',50,'100      '])
Registro_r.xaxis.tick_top()

Registro_r.set_yticks(Divisiones_Men_Prof,minor=True)
Registro_r.set_yticks(Divisiones_May_Prof,minor=False)
Registro_r.set_yticklabels([])
Registro_r.yaxis.set_ticks_position('none')

Registro_r.grid(which='minor',color="grey", alpha=1,linewidth=1.5)
Registro_r.grid(which='major',color="black", alpha=4,linewidth=3)

plt.savefig("Carriles_Registro/T-r.png",bbox_inches='tight',dpi=500)


"""            FIF    FIENT         """
fig = plt.figure(figsize=(5,45))
Registro_FIENT = fig.add_subplot(1,2,1)
fig.subplots_adjust(wspace=0.0)

Registro_FIENT.plot(FIENT,Profundidad, color="red", alpha=1)
Registro_FIENT.fill_betweenx(Profundidad,0,FIENT,color='red')

Registro_FIENT.set_ylim([max(Profundidad),min(Profundidad)])
Registro_FIENT.set_xlim([.3,0])

Registro_FIENT.set_xticks([.03,.06,.09,.12,.18,.21,.24,.27],minor=True)
Registro_FIENT.set_xticks([0,0.15,0.3],minor=False)
Registro_FIENT.set_xticklabels([])
#Registro_T.set_xticklabels(['      0',50,'100      '])
Registro_FIENT.xaxis.tick_top()

Registro_FIENT.set_yticks(Divisiones_Men_Prof,minor=True)
Registro_FIENT.set_yticks(Divisiones_May_Prof,minor=False)
Registro_FIENT.set_yticklabels([])
Registro_FIENT.yaxis.set_ticks_position('none')

Registro_FIENT.grid(which='minor',color="grey", alpha=1,linewidth=1.5)
Registro_FIENT.grid(which='major',color="black", alpha=4,linewidth=3)


Registro_FIF = fig.add_subplot(1,2,2)

Registro_FIF.plot(FIF,Profundidad, color="green", alpha=1)
Registro_FIF.fill_betweenx(Profundidad,0,FIF,color='green')

Registro_FIF.set_ylim([max(Profundidad),min(Profundidad)])
Registro_FIF.set_xlim([0,.02])

Registro_FIF.set_xticks([.002,.004,.006,.008,.012,.014,.016,.018],minor=True)
Registro_FIF.set_xticks([0,0.010,0.020],minor=False)
Registro_FIF.set_xticklabels([])
#Registro_T.set_xticklabels(['      0',50,'100      '])
Registro_FIF.xaxis.tick_top()

Registro_FIF.set_yticks(Divisiones_Men_Prof,minor=True)
Registro_FIF.set_yticks(Divisiones_May_Prof,minor=False)
Registro_FIF.set_yticklabels([])
Registro_FIF.yaxis.set_ticks_position('none')

Registro_FIF.grid(which='minor',color="grey", alpha=1,linewidth=1.5)
Registro_FIF.grid(which='major',color="black", alpha=4,linewidth=3)

plt.savefig("Carriles_Registro/FIENT-FIF.png",bbox_inches='tight',dpi=500)

"""                             SW    SHCS                     """
fig = plt.figure(figsize=(5,45))
Registro_SHCS = fig.add_subplot(1,1,1)

Registro_SHCS.plot(SHCS,Profundidad, color="k", alpha=1)
Registro_SHCS.fill_betweenx(Profundidad,1,SHCS,color='#00FFFF')
Registro_SHCS.fill_betweenx(Profundidad,0,SHCS,color='#2F4F4F')

Registro_SHCS.set_ylim([max(Profundidad),min(Profundidad)])
Registro_SHCS.set_xlim([0,1])

Registro_SHCS.set_xticks([.1,.2,.3,.4,.6,.7,.8,.9],minor=True)
Registro_SHCS.set_xticks([0,.5,1],minor=False)
Registro_SHCS.set_xticklabels([])
#Registro_T.set_xticklabels(['      0',50,'100      '])
Registro_SHCS.xaxis.tick_top()

Registro_SHCS.set_yticks(Divisiones_Men_Prof,minor=True)
Registro_SHCS.set_yticks(Divisiones_May_Prof,minor=False)
Registro_SHCS.set_yticklabels([])
Registro_SHCS.yaxis.set_ticks_position('none')

Registro_SHCS.grid(which='minor',color="white", alpha=1,linewidth=1.5)
Registro_SHCS.grid(which='major',color="black", alpha=4,linewidth=3)

plt.savefig("Carriles_Registro/SW-SHCS.png",bbox_inches='tight',dpi=500)

"""                  IK                          """
fig = plt.figure(figsize=(5,45))
Registro_IK = fig.add_subplot(1,1,1)

Registro_IK.plot(IK,Profundidad, color="orange", alpha=1)
Registro_IK.fill_betweenx(Profundidad,0,IK,color='#FF8C00')

Registro_IK.set_ylim([max(Profundidad),min(Profundidad)])
Registro_IK.set_xlim([0,10])

Registro_IK.set_xticks([1,2,3,4,6,7,8,9],minor=True)
Registro_IK.set_xticks([0,5,10],minor=False)
Registro_IK.set_xticklabels([])
#Registro_T.set_xticklabels(['      0',50,'100      '])
Registro_IK.xaxis.tick_top()

Registro_IK.set_yticks(Divisiones_Men_Prof,minor=True)
Registro_IK.set_yticks(Divisiones_May_Prof,minor=False)
Registro_IK.set_yticklabels([])
Registro_IK.yaxis.set_ticks_position('none')

Registro_IK.grid(which='minor',color="grey", alpha=1,linewidth=1.5)
Registro_IK.grid(which='major',color="black", alpha=4,linewidth=3)

plt.savefig("Carriles_Registro/IK.png",bbox_inches='tight',dpi=500)

"""                         rp35                      """
fig = plt.figure(figsize=(2.5,45))
Registro_rp35 = fig.add_subplot(1,1,1)

Registro_rp35.plot(rp35,Profundidad, color="black",linewidth=.5)

Registro_rp35.fill_betweenx(Profundidad,0,rp35, where=rp35<.5, color="black")
Registro_rp35.fill_betweenx(Profundidad,0,rp35, where=rp35>.5, color="brown")
Registro_rp35.fill_betweenx(Profundidad,0,rp35, where=rp35>2, color="yellow")
Registro_rp35.fill_betweenx(Profundidad,0,rp35, where=rp35>4, color="green")

Registro_rp35.set_ylim([max(Profundidad),min(Profundidad)])
Registro_rp35.set_xlim([0,5])

Registro_rp35.set_xticks([.5,1,1.5,2,3,3.5,4,4.5],minor=True)
Registro_rp35.set_xticks([0,2.5,5],minor=False)
Registro_rp35.set_xticklabels([])
Registro_rp35.xaxis.tick_top()

Registro_rp35.set_yticks(Divisiones_Men_Prof,minor=True)
Registro_rp35.set_yticks(Divisiones_May_Prof,minor=False)
Registro_rp35.set_yticklabels([])
Registro_rp35.yaxis.set_ticks_position('none')

Registro_rp35.grid(which='minor',color="grey", alpha=1,linewidth=1.5)
Registro_rp35.grid(which='major',color="black", alpha=4,linewidth=3)

plt.savefig("Carriles_Registro/rp35.png",bbox_inches='tight',dpi=500)

"""           IIF                              """
fig = plt.figure(figsize=(2.5,45))
Registro_IIF = fig.add_subplot(1,1,1)

Registro_IIF.plot(IIF,Profundidad, color="#DC143C", alpha=1)
Registro_IIF.fill_betweenx(Profundidad,0,IIF,color='#DC143C')

Registro_IIF.set_ylim([max(Profundidad),min(Profundidad)])
Registro_IIF.set_xlim([0,.1])

Registro_IIF.set_xticks([.01,.02,.03,.04,.06,.07,.08,.09],minor=True)
Registro_IIF.set_xticks([0,.05,.1],minor=False)
Registro_IIF.set_xticklabels([])
#Registro_T.set_xticklabels(['      0',50,'100      '])
Registro_IIF.xaxis.tick_top()

Registro_IIF.set_yticks(Divisiones_Men_Prof,minor=True)
Registro_IIF.set_yticks(Divisiones_May_Prof,minor=False)
Registro_IIF.set_yticklabels([])
Registro_IIF.yaxis.set_ticks_position('none')

Registro_IIF.grid(which='minor',color="grey", alpha=1,linewidth=1.5)
Registro_IIF.grid(which='major',color="black", alpha=4,linewidth=3)

plt.savefig("Carriles_Registro/IIF.png",bbox_inches='tight',dpi=500)

"""                w                      """
fig = plt.figure(figsize=(2.5,45))
Registro_w = fig.add_subplot(1,1,1)

Registro_w.plot(w,Profundidad, color="#7B68EE", alpha=1)
Registro_w.fill_betweenx(Profundidad,0,w,color="#7B68EE")

Registro_w.set_ylim([max(Profundidad),min(Profundidad)])
Registro_w.set_xlim([0,10])

Registro_w.set_xticks([1,2,3,4,6,7,8,9],minor=True)
Registro_w.set_xticks([0,5,10],minor=False)
Registro_w.set_xticklabels([])
Registro_w.xaxis.tick_top()

Registro_w.set_yticks(Divisiones_Men_Prof,minor=True)
Registro_w.set_yticks(Divisiones_May_Prof,minor=False)
Registro_w.set_yticklabels([])
Registro_w.yaxis.set_ticks_position('none')

Registro_w.grid(which='minor',color="grey", alpha=1,linewidth=1.5)
Registro_w.grid(which='major',color="black", alpha=4,linewidth=3)

plt.savefig("Carriles_Registro/w.png",bbox_inches='tight',dpi=500)

"""                  ICY                  """
fig = plt.figure(figsize=(2.5,45))
Registro_ICY = fig.add_subplot(1,1,1)

Registro_ICY.plot(ICY,Profundidad, color="#DB7093",linewidth=1)
Registro_ICY.fill_betweenx(Profundidad,0,ICY,color="#DB7093")

Registro_ICY.set_ylim([max(Profundidad),min(Profundidad)])
Registro_ICY.set_xlim([0,1])

Registro_ICY.set_xticks([.1,.2,.3,.4,.6,.7,.8,.9],minor=True)
Registro_ICY.set_xticks([0,.5,1],minor=False)
Registro_ICY.set_xticklabels([])
Registro_ICY.xaxis.tick_top()

Registro_ICY.set_yticks(Divisiones_Men_Prof,minor=True)
Registro_ICY.set_yticks(Divisiones_May_Prof,minor=False)
Registro_ICY.set_yticklabels([])
Registro_ICY.yaxis.set_ticks_position('none')

Registro_ICY.grid(which='minor',color="grey", alpha=1,linewidth=1.5)
Registro_ICY.grid(which='major',color="black", alpha=4,linewidth=3)

plt.savefig("Carriles_Registro/ICY.png",bbox_inches='tight',dpi=500)

"""                  IZF                  """
fig = plt.figure(figsize=(2.5,45))
Registro_IZF = fig.add_subplot(1,1,1)

Registro_IZF.plot(IZF,Profundidad, color="#7CFC00",linewidth=1)
Registro_IZF.fill_betweenx(Profundidad,0,IZF,color="#7CFC00")

Registro_IZF.set_ylim([max(Profundidad),min(Profundidad)])
Registro_IZF.set_xlim([0,10])

Registro_IZF.set_xticks([1,2,3,4,6,7,8,9],minor=True)
Registro_IZF.set_xticks([0,5,10],minor=False)
Registro_IZF.set_xticklabels([])
Registro_IZF.xaxis.tick_top()

Registro_IZF.set_yticks(Divisiones_Men_Prof,minor=True)
Registro_IZF.set_yticks(Divisiones_May_Prof,minor=False)
Registro_IZF.set_yticklabels([])
Registro_IZF.yaxis.set_ticks_position('none')

Registro_IZF.grid(which='minor',color="grey", alpha=1,linewidth=1.5)
Registro_IZF.grid(which='major',color="black", alpha=4,linewidth=3)

plt.savefig("Carriles_Registro/IZF.png",bbox_inches='tight',dpi=500)

"""                  IZC                  """
fig = plt.figure(figsize=(2.5,45))
Registro_IZC = fig.add_subplot(1,1,1)

Registro_IZC.plot(IZC,Profundidad, color="#00BFFF",linewidth=1)
Registro_IZC.fill_betweenx(Profundidad,0,IZC,color="#00BFFF")

Registro_IZC.set_ylim([max(Profundidad),min(Profundidad)])
Registro_IZC.set_xlim([0,3])

Registro_IZC.set_xticks([.3,.6,.9,1.2,1.8,2.1,2.4,2.7],minor=True)
Registro_IZC.set_xticks([0,1.5,3],minor=False)
Registro_IZC.set_xticklabels([])
Registro_IZC.xaxis.tick_top()

Registro_IZC.set_yticks(Divisiones_Men_Prof,minor=True)
Registro_IZC.set_yticks(Divisiones_May_Prof,minor=False)
Registro_IZC.set_yticklabels([])
Registro_IZC.yaxis.set_ticks_position('none')

Registro_IZC.grid(which='minor',color="grey", alpha=1,linewidth=1.5)
Registro_IZC.grid(which='major',color="black", alpha=4,linewidth=3)

plt.savefig("Carriles_Registro/IZC.png",bbox_inches='tight',dpi=500)