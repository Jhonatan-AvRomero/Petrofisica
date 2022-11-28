# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 21:10:38 2018
@author: Jhonatan
"""
"""Gráfica de Litoporosidad"""
import matplotlib.pyplot as plt
import numpy as np
M_Minerales = [SIL[3],CAL[3],DOL[3],ANH[3],YES[3],SAL[3],LUT[3]]
N_Minerales = [SIL[4],CAL[4],DOL[4],ANH[4],YES[4],SAL[4],LUT[4]]
fig = plt.figure(figsize=(9,7))
plt.plot(N_Minerales,M_Minerales,"o",color="black",markersize=2)
ax = plt.gca()
fig.patch.set_facecolor('#87CEFA')
ax.set_facecolor('#DCDCDC')
plt.axis([0.3,1.0,0.3,1.2])
plt.grid(True,which="both")
#CREACIÓN DE TRIÁNGULOS
plt.plot([DOL[4],CAL[4]],[DOL[3],CAL[3]],color="black",linewidth=.7)
plt.plot([CAL[4],SIL[4]],[CAL[3],SIL[3]],color="black",linewidth=.7)
plt.plot([SIL[4],DOL[4]],[SIL[3],DOL[3]],color="black",linewidth=.7)
plt.plot([SIL[4],LUT[4]],[SIL[3],LUT[3]],color="black",linewidth=.7)
plt.plot([LUT[4],DOL[4]],[LUT[3],DOL[3]],color="black",linewidth=.7)
#DOLOMITA CON YESO
plt.plot([DOL[4],YES[4]],[DOL[3],YES[3]],color="black",linewidth=.7)
#CREACIÓN DE REGIONES 1 Y 2
plt.plot([DOL[4],DOL[4]],[DOL[3],1.2],color="black",linewidth=.7)
plt.plot([CAL[4],CAL[4]],[CAL[3],1.2],color="black",linewidth=.7)
plt.plot([SIL[4],SIL[4]],[SIL[3],1.2],color="black",linewidth=.7)
plt.annotate('CAL',xy=(CAL[4],CAL[3]),fontsize=7)
plt.annotate('DOL',xy=(DOL[4],DOL[3]),fontsize=7)
plt.annotate('SIL',xy=(SIL[4],SIL[3]),fontsize=7)
plt.annotate('YES',xy=(YES[4],YES[3]),fontsize=7)
plt.annotate('LUT',xy=(LUT[4],LUT[3]),fontsize=7)
plt.annotate('SAL',xy=(SAL[4],SAL[3]),fontsize=7)
plt.annotate('ANH',xy=(ANH[4],ANH[3]),fontsize=7)
#
plt.xlabel("N",fontsize=15)
plt.ylabel("M",fontsize=15)
plt.title("Gráfica de Lito-Porosidad\n")
#GRAFICAR VALORES CALCULADOS
M = np.array([],dtype=float)
Archivo_M = open("Archivos_TXT/M.txt")
for Linea_M in Archivo_M.readlines():
    Nueva_Linea_M = Linea_M.rstrip('\n')
    Nueva_Linea_Convertida_M = round((float(Nueva_Linea_M)),4)
    M = np.append(M,Nueva_Linea_Convertida_M)
Archivo_M.close()
N = np.array([],dtype=float)
Archivo_N = open("Nuevos_Archivos_Creados/N.txt")
for Linea_N in Archivo_N.readlines():
    Nueva_Linea_N = Linea_N.rstrip('\n')
    Nueva_Linea_Convertida_N = round((float(Nueva_Linea_N)),4)
    N = np.append(N,Nueva_Linea_Convertida_N)
Archivo_N.close()
"""Graficar puntos por color"""
i=0
color=0
for M_valor in M:
    if color <= int(len(M)/7):
        nombre_color="red"
        plt.plot(N[i],M[i],"o",color="#FF0000",markersize=1,alpha=1)
    elif color > int(len(M)/7) and color <= int(len(M)*2/7):
        nombre_color="orange"
        plt.plot(N[i],M[i],"o",color="#FF8C00",markersize=1,alpha=1)
    elif color > int(len(M)*2/7) and color <= int(len(M)*3/7):
        nombre_color="yellow"
        plt.plot(N[i],M[i],"o",color="#FFD700",markersize=1,alpha=1)
    elif color > int(len(M)*3/7) and color <= int(len(M)*4/7):
        nombre_color="green"
        plt.plot(N[i],M[i],"o",color="#32CD32",markersize=1,alpha=1)
    elif color > int(len(M)*4/7) and color <= int(len(M)*5/7):
        nombre_color="blue"
        plt.plot(N[i],M[i],"o",color="#4169E1",markersize=1,alpha=1)
    elif color > int(len(M)*5/7) and color <= int(len(M)*6/7):
        nombre_color="indigo"
        plt.plot(N[i],M[i],"o",color="#4169E1",markersize=1,alpha=1)
    elif color > int(len(M)*6/7):
        nombre_color="violet"
        plt.plot(N[i],M[i],"o",color="#C71585",markersize=1,alpha=1)
    i=i+1
    color=color+1
plt.savefig("Graficas_Generadas/Gráfica de Litoporosidad.pdf",facecolor=fig.get_facecolor())

""" Desmarcar solo si se desea mostrar el número del punto graficado
i=0
for numeracion in M:
    plt.annotate(i+1,xy=(N[i],M[i]),fontsize=.5)
    i=i+1
"""
#
"""DETERMINAR EN QUÉ REGIÓN SE ENCUENTRA CADA PUNTO"""
#
"""Determinando si el punto está en el triángulo DOL-CAL-SIL"""
X_LUT_SIL = round((SIL[4] - LUT[4]),4)
ContadorFinal_X_LUT_SIL = X_LUT_SIL/0.0001
int(ContadorFinal_X_LUT_SIL)
Conjunto_Coordenadas_X_LUT_SIL = np.array([],dtype=float)
Conjunto_Coordenadas_Y_LUT_SIL = np.array([],dtype=float)
Conjunto_Coordenadas_Y2_LUT_SIL = np.array([],dtype=float)
Pendiente_DOL_SIL = round(((SIL[3]-DOL[3])/(SIL[4]-DOL[4])),4)
Pendiente_SIL_LUT = round(((SIL[3]-LUT[3])/(SIL[4]-LUT[4])),4)
Pendiente_LUT_DOL = round(((LUT[3]-DOL[3])/(LUT[4]-DOL[4])),4)
Ordenada_DOL_SIL = round((DOL[3]-(Pendiente_DOL_SIL*DOL[4])),4)
Ordenada_SIL_LUT = round((SIL[3]-(Pendiente_SIL_LUT*SIL[4])),4)
Ordenada_LUT_DOL = round((LUT[3]-(Pendiente_LUT_DOL*LUT[4])),4)
Contador_Inicial_X_LUT_SIL = 0
Valor_X_LUT_SIL = LUT[4]
while Contador_Inicial_X_LUT_SIL < ContadorFinal_X_LUT_SIL + 1:
    if Valor_X_LUT_SIL >= DOL[4]:
        Conjunto_Coordenadas_X_LUT_SIL = np.append(Conjunto_Coordenadas_X_LUT_SIL,Valor_X_LUT_SIL)
        Valor_Y_LUT_SIL = round(((Pendiente_DOL_SIL*Valor_X_LUT_SIL) + Ordenada_DOL_SIL),4)
        Valor_Y2_LUT_SIL = round(((Pendiente_SIL_LUT*Valor_X_LUT_SIL) + Ordenada_SIL_LUT),4)
        Valor_X_LUT_SIL = round((Valor_X_LUT_SIL + .0001),4)
        Conjunto_Coordenadas_Y_LUT_SIL = np.append(Conjunto_Coordenadas_Y_LUT_SIL,Valor_Y_LUT_SIL)
        Conjunto_Coordenadas_Y2_LUT_SIL = np.append(Conjunto_Coordenadas_Y2_LUT_SIL,Valor_Y2_LUT_SIL)
        Contador_Inicial_X_LUT_SIL = Contador_Inicial_X_LUT_SIL + 1
    else:
        Conjunto_Coordenadas_X_LUT_SIL = np.append(Conjunto_Coordenadas_X_LUT_SIL,Valor_X_LUT_SIL)
        Valor_Y_LUT_SIL = round(((Pendiente_LUT_DOL*Valor_X_LUT_SIL) + Ordenada_LUT_DOL),4)
        Valor_Y2_LUT_SIL = round(((Pendiente_SIL_LUT*Valor_X_LUT_SIL) + Ordenada_SIL_LUT),4)
        Valor_X_LUT_SIL = round((Valor_X_LUT_SIL + .0001),4)
        Conjunto_Coordenadas_Y_LUT_SIL = np.append(Conjunto_Coordenadas_Y_LUT_SIL,Valor_Y_LUT_SIL)
        Conjunto_Coordenadas_Y2_LUT_SIL = np.append(Conjunto_Coordenadas_Y2_LUT_SIL,Valor_Y2_LUT_SIL)
        Contador_Inicial_X_LUT_SIL = Contador_Inicial_X_LUT_SIL + 1
i_400 = 0
region_tri = np.array([],dtype=str)
for x_punto in N:
    if x_punto >= LUT[4] and x_punto <= SIL[4] and M[i_400] >= LUT[3] and M[i_400] <= SIL[3]:
        i_1120 = 0
        for x_coor in Conjunto_Coordenadas_X_LUT_SIL:
            if x_coor == x_punto:
                if M[i_400] >= Conjunto_Coordenadas_Y2_LUT_SIL[i_1120] and M[i_400] <= Conjunto_Coordenadas_Y_LUT_SIL[i_1120]:
                    dato = "DOL-SIL-LUT"
                    region_tri = np.append(region_tri,dato)
                else:
                    dato = "Indefinido"
                    region_tri = np.append(region_tri,dato)
            i_1120 = i_1120 + 1
    else:
        dato = "Indefinido"
        region_tri = np.append(region_tri,dato)
    i_400 = i_400 + 1
"""Determinando si el punto está en el triángulo DOL-CAL-SIL"""
X_DOL_SIL = round((SIL[4] - DOL[4]),4)
ContadorFinal_X_DOL_SIL = X_DOL_SIL/0.0001
int(ContadorFinal_X_DOL_SIL)
Conjunto_Coordenadas_X_DOL_SIL = np.array([],dtype=float)
Conjunto_Coordenadas_Y_DOL_SIL = np.array([],dtype=float)
Conjunto_Coordenadas_Y2_DOL_SIL = np.array([],dtype=float)
Pendiente_DOL_CAL = round(((CAL[3]-DOL[3])/(CAL[4]-DOL[4])),4)
Pendiente_CAL_SIL = round(((SIL[3]-CAL[3])/(SIL[4]-CAL[4])),4)
Pendiente_SIL_DOL = round(((SIL[3]-DOL[3])/(SIL[4]-DOL[4])),4)
Ordenada_DOL_CAL = round((DOL[3]-(Pendiente_DOL_CAL*DOL[4])),4)
Ordenada_CAL_SIL = round((SIL[3]-(Pendiente_CAL_SIL*SIL[4])),4)
Ordenada_SIL_DOL = round((DOL[3]-(Pendiente_SIL_DOL*DOL[4])),4)
Contador_Inicial_X_DOL_SIL = 0
Valor_X_DOL_SIL = DOL[4]
while Contador_Inicial_X_DOL_SIL < ContadorFinal_X_DOL_SIL + 1:
    if Valor_X_DOL_SIL >= CAL[4]:
        Conjunto_Coordenadas_X_DOL_SIL = np.append(Conjunto_Coordenadas_X_DOL_SIL,Valor_X_DOL_SIL)
        Valor_Y_DOL_SIL = round(((Pendiente_CAL_SIL*Valor_X_DOL_SIL) + Ordenada_CAL_SIL),4)
        Valor_Y2_DOL_SIL = round(((Pendiente_SIL_DOL*Valor_X_DOL_SIL) + Ordenada_SIL_DOL),4)
        Valor_X_DOL_SIL = round((Valor_X_DOL_SIL + .0001),4)
        Conjunto_Coordenadas_Y_DOL_SIL = np.append(Conjunto_Coordenadas_Y_DOL_SIL,Valor_Y_DOL_SIL)
        Conjunto_Coordenadas_Y2_DOL_SIL = np.append(Conjunto_Coordenadas_Y2_DOL_SIL,Valor_Y2_DOL_SIL)
        Contador_Inicial_X_DOL_SIL = Contador_Inicial_X_DOL_SIL + 1
    else:
        Conjunto_Coordenadas_X_DOL_SIL = np.append(Conjunto_Coordenadas_X_DOL_SIL,Valor_X_DOL_SIL)
        Valor_Y_DOL_SIL = round(((Pendiente_DOL_CAL*Valor_X_DOL_SIL) + Ordenada_DOL_CAL),4)
        Valor_Y2_DOL_SIL = round(((Pendiente_SIL_DOL*Valor_X_DOL_SIL) + Ordenada_SIL_DOL),4)
        Valor_X_DOL_SIL = round((Valor_X_DOL_SIL + .0001),4)
        Conjunto_Coordenadas_Y_DOL_SIL = np.append(Conjunto_Coordenadas_Y_DOL_SIL,Valor_Y_DOL_SIL)
        Conjunto_Coordenadas_Y2_DOL_SIL = np.append(Conjunto_Coordenadas_Y2_DOL_SIL,Valor_Y2_DOL_SIL)
        Contador_Inicial_X_DOL_SIL = Contador_Inicial_X_DOL_SIL + 1
i_400 = 0
region_tri2 = np.array([],dtype=str)
for x_punto in N:
    if x_punto >= DOL[4] and x_punto <= SIL[4] and M[i_400] >= DOL[3] and M[i_400] <= CAL[3]:
        i_1120 = 0
        for x_coor in Conjunto_Coordenadas_X_DOL_SIL:
            if x_coor == x_punto:
                if M[i_400] >= Conjunto_Coordenadas_Y2_DOL_SIL[i_1120] and M[i_400] <= Conjunto_Coordenadas_Y_DOL_SIL[i_1120]:
                    dato = "DOL-CAL-SIL"
                    region_tri2 = np.append(region_tri2,dato)
                else:
                    dato = "Indefinido"
                    region_tri2 = np.append(region_tri2,dato)
            i_1120 = i_1120 + 1
    else:
        dato = "Indefinido"
        region_tri2 = np.append(region_tri2,dato)
    i_400 = i_400 + 1
"""Determinando si el punto está en la región 1"""
X_DOL_CAL = round((CAL[4] - DOL[4]),4)
ContadorFinal_X_DOL_CAL = X_DOL_CAL/0.0001
int(ContadorFinal_X_DOL_CAL)
Conjunto_Coordenadas_X_DOL_CAL = np.array([],dtype=float)
Conjunto_Coordenadas_Y_DOL_CAL = np.array([],dtype=float)
Pendiente_DOL_CAL = round(((CAL[3]-DOL[3])/(CAL[4]-DOL[4])),4)
Ordenada_DOL_CAL = round((DOL[3]-(Pendiente_DOL_CAL*DOL[4])),4)
Contador_Inicial_X_DOL_CAL = 0
Valor_X_DOL_CAL = DOL[4]
while Contador_Inicial_X_DOL_CAL < ContadorFinal_X_DOL_CAL + 1:
        Conjunto_Coordenadas_X_DOL_CAL = np.append(Conjunto_Coordenadas_X_DOL_CAL,Valor_X_DOL_CAL)
        Valor_Y_DOL_CAL = round(((Pendiente_DOL_CAL*Valor_X_DOL_CAL) + Ordenada_DOL_CAL),4)
        Valor_X_DOL_CAL = round((Valor_X_DOL_CAL + .0001),4)
        Conjunto_Coordenadas_Y_DOL_CAL = np.append(Conjunto_Coordenadas_Y_DOL_CAL,Valor_Y_DOL_CAL)
        Contador_Inicial_X_DOL_CAL = Contador_Inicial_X_DOL_CAL + 1
i_400 = 0
region_tri3 = np.array([],dtype=str)
for x_punto in N:
    if x_punto >= DOL[4] and x_punto <= CAL[4] and M[i_400] >= DOL[3] and M[i_400] <= 1.2:
        i_1120 = 0
        for x_coor in Conjunto_Coordenadas_X_DOL_CAL:
            if x_coor == x_punto:
                if M[i_400] >= Conjunto_Coordenadas_Y_DOL_CAL[i_1120] and M[i_400] <= 1.2:
                    dato = "R1"
                    region_tri3 = np.append(region_tri3,dato)
                else:
                    dato = "Indefinido"
                    region_tri3 = np.append(region_tri3,dato)
            i_1120 = i_1120 + 1
    else:
        dato = "Indefinido"
        region_tri3 = np.append(region_tri3,dato)
    i_400 = i_400 + 1
"""Determinando si el punto está en la región 2"""
X_CAL_SIL = round((SIL[4] - CAL[4]),4)
ContadorFinal_X_CAL_SIL = X_CAL_SIL/0.0001
int(ContadorFinal_X_CAL_SIL)
Conjunto_Coordenadas_X_CAL_SIL = np.array([],dtype=float)
Conjunto_Coordenadas_Y_CAL_SIL = np.array([],dtype=float)
Pendiente_CAL_SIL = round(((SIL[3]-CAL[3])/(SIL[4]-CAL[4])),4)
Ordenada_CAL_SIL = round((SIL[3]-(Pendiente_CAL_SIL*SIL[4])),4)
Contador_Inicial_X_CAL_SIL = 0
Valor_X_CAL_SIL = CAL[4]
while Contador_Inicial_X_CAL_SIL < ContadorFinal_X_CAL_SIL + 1:
        Conjunto_Coordenadas_X_CAL_SIL = np.append(Conjunto_Coordenadas_X_CAL_SIL,Valor_X_CAL_SIL)
        Valor_Y_CAL_SIL = round(((Pendiente_CAL_SIL*Valor_X_CAL_SIL) + Ordenada_CAL_SIL),4)
        Valor_X_CAL_SIL = round((Valor_X_CAL_SIL + .0001),4)
        Conjunto_Coordenadas_Y_CAL_SIL = np.append(Conjunto_Coordenadas_Y_CAL_SIL,Valor_Y_CAL_SIL)
        Contador_Inicial_X_CAL_SIL = Contador_Inicial_X_CAL_SIL + 1
i_400 = 0
region_tri4 = np.array([],dtype=str)
for x_punto in N:
    if x_punto >= CAL[4] and x_punto <= SIL[4] and M[i_400] >= SIL[3] and M[i_400] <= 1.2:
        i_1120 = 0
        for x_coor in Conjunto_Coordenadas_X_CAL_SIL:
            if x_coor == x_punto:
                if M[i_400] >= Conjunto_Coordenadas_Y_CAL_SIL[i_1120] and M[i_400] <= 1.2:
                    dato = "R2"
                    region_tri4 = np.append(region_tri4,dato)
                else:
                    dato = "Indefinido"
                    region_tri4 = np.append(region_tri4,dato)
            i_1120 = i_1120 + 1
    else:
        dato = "Indefinido"
        region_tri4 = np.append(region_tri4,dato)
    i_400 = i_400 + 1
"""Determinando que puntos no están en los triángulos ("DOL-CAL-SIL" & "DOL-SIL-LUT") ni en las regiones 1 & 2"""
region_prefinal = np.array([],dtype=float)
i = 0
for dato_region in region_tri:
    if str(dato_region) == "Indefinido":
       if str(dato_region) == region_tri2[i]:
           if str(dato_region) == region_tri3[i]:
               if str(dato_region) == region_tri4[i]:
                   region_prefinal = np.append(region_prefinal,dato_region)
               else:
                   region_prefinal = np.append(region_prefinal,region_tri4[i])
           else:
               region_prefinal = np.append(region_prefinal,region_tri3[i])
       else:
           region_prefinal = np.append(region_prefinal,region_tri2[i])
    else:
        region_prefinal = np.append(region_prefinal,dato_region)
    i = i + 1
"""CREAR GRÁFICAS M,N & L para los puntos cuya región sigue indefinida para finalmente clasificarlos"""
"""Gráfica M"""
DEN_Minerales = [MUD[1],SIL[1],CAL[1],DOL[1],ANH[1],YES[1],SAL[1],LUT[1]]
DT_Minerales = [MUD[0],SIL[0],CAL[0],DOL[0],ANH[0],YES[0],SAL[0],LUT[0]]
NPHI_Minerales = [MUD[2],SIL[2],CAL[2],DOL[2],ANH[2],YES[2],SAL[2],LUT[2]]
fig = plt.figure(figsize=(9,7))
ax = plt.gca()
plt.plot(DEN_Minerales,DT_Minerales,"o",color="black",markersize=2)
fig.patch.set_facecolor('#D8BFD8')
ax.set_facecolor('#FFE4C4')
plt.axis([4,1,0,200])
plt.grid(which='major',color="black",alpha=.2)
#
plt.plot([MUD[1],CAL[1]],[MUD[0],CAL[0]],color="black",linewidth=.5)
plt.annotate('CAL',xy=(CAL[1],CAL[0]),fontsize=7)
plt.plot([MUD[1],SIL[1]],[MUD[0],SIL[0]],color="black",linewidth=.5)
plt.annotate('SIL',xy=(SIL[1],SIL[0]),fontsize=7)
plt.plot([MUD[1],DOL[1]],[MUD[0],DOL[0]],color="black",linewidth=.5)
plt.annotate('DOL',xy=(DOL[1],DOL[0]),fontsize=7)
plt.plot([MUD[1],ANH[1]],[MUD[0],ANH[0]],color="black",linewidth=.5)
plt.annotate('ANH',xy=(ANH[1],ANH[0]),fontsize=7)
plt.plot([MUD[1],YES[1]],[MUD[0],YES[0]],color="black",linewidth=.5)
plt.annotate('YES',xy=(YES[1],YES[0]),fontsize=7)
plt.plot([MUD[1],SAL[1]],[MUD[0],SAL[0]],color="black",linewidth=.5)
plt.annotate('SAL',xy=(SAL[1],SAL[0]),fontsize=7)
plt.plot([MUD[1],LUT[1]],[MUD[0],LUT[0]],color="black",linewidth=.5)
plt.annotate('LUT',xy=(LUT[1],LUT[0]),fontsize=7)
i=0
for dato_region in region_prefinal:
    if str(dato_region) == "Indefinido":
        plt.plot(RHOB[i],DT[i],"o",color="red",markersize=1,alpha=7)
    i=i+1
plt.xlabel("RHOB",fontsize=11)
plt.ylabel("DT",fontsize=11)
plt.title("M\n",fontsize=13)
plt.savefig("Graficas_Generadas/Gráfica M.pdf",facecolor=fig.get_facecolor())
"""Gráfica N"""
fig = plt.figure(figsize=(9,7))
plt.plot(DEN_Minerales,NPHI_Minerales,"o",color="black",markersize=2)
ax = plt.gca()
fig.patch.set_facecolor('#00e6ac')
ax.set_facecolor('#ffff80')
plt.axis([4,1,-0.2,1.1])
plt.grid(which='major',color="black",alpha=.2)
#
plt.plot([MUD[1],CAL[1]],[MUD[2],CAL[2]],color="black",linewidth=.5)
plt.annotate('CAL',xy=(CAL[1],CAL[2]),fontsize=7)
plt.plot([MUD[1],SIL[1]],[MUD[2],SIL[2]],color="black",linewidth=.5)
plt.annotate('SIL',xy=(SIL[1],SIL[2]),fontsize=7)
plt.plot([MUD[1],DOL[1]],[MUD[2],DOL[2]],color="black",linewidth=.5)
plt.annotate('DOL',xy=(DOL[1],DOL[2]),fontsize=7)
plt.plot([MUD[1],ANH[1]],[MUD[2],ANH[2]],color="black",linewidth=.5)
plt.annotate('ANH',xy=(ANH[1],ANH[2]),fontsize=7)
plt.plot([MUD[1],YES[1]],[MUD[2],YES[2]],color="black",linewidth=.5)
plt.annotate('YES',xy=(YES[1],YES[2]),fontsize=7)
plt.plot([MUD[1],SAL[1]],[MUD[2],SAL[2]],color="black",linewidth=.5)
plt.annotate('SAL',xy=(SAL[1],SAL[2]),fontsize=7)
plt.plot([MUD[1],LUT[1]],[MUD[2],LUT[2]],color="black",linewidth=.5)
plt.annotate('LUT',xy=(LUT[1],LUT[2]),fontsize=7)
i=0
for dato_region in region_prefinal:
    if str(dato_region) == "Indefinido":
        plt.plot(RHOB[i],NPHI[i],"o",color="green",markersize=1)
    i=i+1
plt.xlabel("RHOB",fontsize=11)
plt.ylabel("NPHI",fontsize=11)
plt.title("N\n",fontsize=13)
plt.savefig("Graficas_Generadas/Gráfica N.pdf",facecolor=fig.get_facecolor())
"""Gráfica L"""
fig = plt.figure(figsize=(9,7))
plt.plot(NPHI_Minerales,DT_Minerales,"o",color="black",markersize=2)
ax = plt.gca()
fig.patch.set_facecolor('#ffe0b3')
ax.set_facecolor('#ffcccc')
plt.axis([-0.2,1,0,200])
plt.grid(which='major',color="black",alpha=.2)
#
plt.plot([MUD[2],CAL[2]],[MUD[0],CAL[0]],color="black",linewidth=.5)
plt.annotate('CAL',xy=(CAL[2],CAL[0]),fontsize=7)
plt.plot([MUD[2],SIL[2]],[MUD[0],SIL[0]],color="black",linewidth=.5)
plt.annotate('SIL',xy=(SIL[2],SIL[0]),fontsize=7)
plt.plot([MUD[2],DOL[2]],[MUD[0],DOL[0]],color="black",linewidth=.5)
plt.annotate('DOL',xy=(DOL[2],DOL[0]),fontsize=7)
plt.plot([MUD[2],ANH[2]],[MUD[0],ANH[0]],color="black",linewidth=.5)
plt.annotate('ANH',xy=(ANH[2],ANH[0]),fontsize=7)
plt.plot([MUD[2],YES[2]],[MUD[0],YES[0]],color="black",linewidth=.5)
plt.annotate('YES',xy=(YES[2],YES[0]),fontsize=7)
plt.plot([MUD[2],SAL[2]],[MUD[0],SAL[0]],color="black",linewidth=.5)
plt.annotate('SAL',xy=(SAL[2],SAL[0]),fontsize=7)
plt.plot([MUD[2],LUT[2]],[MUD[0],LUT[0]],color="black",linewidth=.5)
plt.annotate('LUT',xy=(LUT[2],LUT[0]),fontsize=7)
i=0
for dato_region in region_prefinal:
    if str(dato_region) == "Indefinido":
        plt.plot(NPHI[i],DT[i],"o",color="blue",markersize=1)
    i=i+1
plt.xlabel("NPHI",fontsize=11)
plt.ylabel("DT",fontsize=11)
plt.title("L\n",fontsize=13)
plt.savefig("Graficas_Generadas/Gráfica L.pdf",facecolor=fig.get_facecolor())
#
#
#
"""Analizando Gráfica M"""
#Pendiente y Ordenada Lutita
Pendiente_MUD_LUT = round(((MUD[0]-LUT[0])/(MUD[1]-LUT[1])),4)
Ordenada_MUD_LUT = round((LUT[0]-(Pendiente_MUD_LUT*LUT[1])),4)
#Pendiente  Anhidrita
Pendiente_MUD_ANH = round(((MUD[0]-ANH[0])/(MUD[1]-ANH[1])),4)
Ordenada_MUD_ANH = round((ANH[0]-(Pendiente_MUD_ANH*ANH[1])),4)
#Pendiente y Ordenada Dolomita
Pendiente_MUD_DOL = round(((MUD[0]-DOL[0])/(MUD[1]-DOL[1])),4)
Ordenada_MUD_DOL = round((DOL[0]-(Pendiente_MUD_DOL*DOL[1])),4)
#Pendiente y Ordenada Silice
Pendiente_MUD_SIL = round(((MUD[0]-SIL[0])/(MUD[1]-SIL[1])),4)
Ordenada_MUD_SIL = round((SIL[0]-(Pendiente_MUD_SIL*SIL[1])),4)
#Pendiente y Ordenada Calcita
Pendiente_MUD_CAL = round(((MUD[0]-CAL[0])/(MUD[1]-CAL[1])),4)
Ordenada_MUD_CAL = round((CAL[0]-(Pendiente_MUD_CAL*CAL[1])),4)
#Pendiente y Ordenada Yeso
Pendiente_MUD_YES = round(((MUD[0]-YES[0])/(MUD[1]-YES[1])),4)
Ordenada_MUD_YES = round((YES[0]-(Pendiente_MUD_YES*YES[1])),4)
#Pendiente y Ordenada Sal
Pendiente_MUD_SAL = round(((MUD[0]-SAL[0])/(MUD[1]-SAL[1])),4)
Ordenada_MUD_SAL = round((SAL[0]-(Pendiente_MUD_SAL*SAL[1])),4)
#
Clasificacion_M = np.array([],dtype=str)
i=0
for dato_region in region_prefinal:
    if str(dato_region) == "Indefinido":
        Valor_X_MUD_LUT = round(((DT[i]-Ordenada_MUD_LUT)/Pendiente_MUD_LUT),4)
        Valor_X_MUD_ANH = round(((DT[i]-Ordenada_MUD_ANH)/Pendiente_MUD_ANH),4)
        Valor_X_MUD_DOL = round(((DT[i]-Ordenada_MUD_DOL)/Pendiente_MUD_DOL),4)
        Valor_X_MUD_SIL = round(((DT[i]-Ordenada_MUD_SIL)/Pendiente_MUD_SIL),4)
        Valor_X_MUD_CAL = round(((DT[i]-Ordenada_MUD_CAL)/Pendiente_MUD_CAL),4)
        Valor_X_MUD_YES = round(((DT[i]-Ordenada_MUD_YES)/Pendiente_MUD_YES),4)
        Valor_X_MUD_SAL = round(((DT[i]-Ordenada_MUD_SAL)/Pendiente_MUD_SAL),4)
        if RHOB[i] <= Valor_X_MUD_LUT and RHOB[i] > Valor_X_MUD_ANH:
            Clasificacion_M = np.append(Clasificacion_M,"LUT-ANH")
        else:
            if RHOB[i] <= Valor_X_MUD_ANH and RHOB[i] > Valor_X_MUD_DOL:
                Clasificacion_M = np.append(Clasificacion_M,"ANH-DOL")
            else:
                if RHOB[i] <= Valor_X_MUD_DOL and RHOB[i] > Valor_X_MUD_SIL:
                    Clasificacion_M = np.append(Clasificacion_M,"DOL-SIL")
                else:
                    if RHOB[i] <= Valor_X_MUD_SIL and RHOB[i] > Valor_X_MUD_CAL:
                        Clasificacion_M = np.append(Clasificacion_M,"SIL-CAL")
                    else:
                        if RHOB[i] <= Valor_X_MUD_CAL and RHOB[i] > Valor_X_MUD_YES:
                            Clasificacion_M = np.append(Clasificacion_M,"CAL-YES")
                        else:
                            if RHOB[i] <= Valor_X_MUD_YES and RHOB[i] > Valor_X_MUD_SAL:
                                Clasificacion_M = np.append(Clasificacion_M,"YES-SAL")
                            else:
                                Clasificacion_M = np.append(Clasificacion_M,"Indefinido")
    else:
        Clasificacion_M = np.append(Clasificacion_M,"Definido")
    i=i+1
"""Analizando Gráfica N"""
#Pendiente y Ordenada Yeso
Pendiente_MUD_YES = round(((MUD[2]-YES[2])/(MUD[1]-YES[1])),4)
Ordenada_MUD_YES = round((YES[2]-(Pendiente_MUD_YES*YES[1])),4)
#Pendiente  Anhidrita
Pendiente_MUD_ANH = round(((MUD[2]-ANH[2])/(MUD[1]-ANH[1])),4)
Ordenada_MUD_ANH = round((ANH[2]-(Pendiente_MUD_ANH*ANH[1])),4)
#Pendiente y Ordenada Lutita
Pendiente_MUD_LUT = round(((MUD[2]-LUT[2])/(MUD[1]-LUT[1])),4)
Ordenada_MUD_LUT = round((LUT[2]-(Pendiente_MUD_LUT*LUT[1])),4)
#Pendiente y Ordenada Dolomita
Pendiente_MUD_DOL = round(((MUD[2]-DOL[2])/(MUD[1]-DOL[1])),4)
Ordenada_MUD_DOL = round((DOL[2]-(Pendiente_MUD_DOL*DOL[1])),4)
#Pendiente y Ordenada Calcita
Pendiente_MUD_CAL = round(((MUD[2]-CAL[2])/(MUD[1]-CAL[1])),4)
Ordenada_MUD_CAL = round((CAL[2]-(Pendiente_MUD_CAL*CAL[1])),4)
#Pendiente y Ordenada Silice
Pendiente_MUD_SIL = round(((MUD[2]-SIL[2])/(MUD[1]-SIL[1])),4)
Ordenada_MUD_SIL = round((SIL[2]-(Pendiente_MUD_SIL*SIL[1])),4)
#Pendiente y Ordenada Sal
Pendiente_MUD_SAL = round(((MUD[2]-SAL[2])/(MUD[1]-SAL[1])),4)
Ordenada_MUD_SAL = round((SAL[2]-(Pendiente_MUD_SAL*SAL[1])),4)
#
Clasificacion_N = np.array([],dtype=str)
i=0
for dato_region in region_prefinal:
    if str(dato_region) == "Indefinido":
        Valor_X_MUD_LUT = round(((NPHI[i]-Ordenada_MUD_LUT)/Pendiente_MUD_LUT),4)
        Valor_X_MUD_ANH = round(((NPHI[i]-Ordenada_MUD_ANH)/Pendiente_MUD_ANH),4)
        Valor_X_MUD_DOL = round(((NPHI[i]-Ordenada_MUD_DOL)/Pendiente_MUD_DOL),4)
        Valor_X_MUD_SIL = round(((NPHI[i]-Ordenada_MUD_SIL)/Pendiente_MUD_SIL),4)
        Valor_X_MUD_CAL = round(((NPHI[i]-Ordenada_MUD_CAL)/Pendiente_MUD_CAL),4)
        Valor_X_MUD_YES = round(((NPHI[i]-Ordenada_MUD_YES)/Pendiente_MUD_YES),4)
        Valor_X_MUD_SAL = round(((NPHI[i]-Ordenada_MUD_SAL)/Pendiente_MUD_SAL),4)
        if RHOB[i] <= Valor_X_MUD_YES and RHOB[i] > Valor_X_MUD_ANH:
            Clasificacion_N = np.append(Clasificacion_N,"YES-ANH")
        else:
            if RHOB[i] <= Valor_X_MUD_ANH and RHOB[i] > Valor_X_MUD_LUT and NPHI[i] < LUT[2]:
                Clasificacion_N = np.append(Clasificacion_N,"ANH-DOL")
            else:
                if RHOB[i] <= Valor_X_MUD_ANH and RHOB[i] > Valor_X_MUD_LUT and NPHI[i] >= LUT[2]:
                     Clasificacion_N = np.append(Clasificacion_N,"ANH-LUT")
                else:
                    if RHOB[i] <= Valor_X_MUD_LUT and RHOB[i] > Valor_X_MUD_DOL and NPHI[i] < LUT[2]:
                         Clasificacion_N = np.append(Clasificacion_N,"ANH-DOL")
                    else:
                        if RHOB[i] <= Valor_X_MUD_LUT and RHOB[i] > Valor_X_MUD_DOL and NPHI[i] >=LUT[2]:
                             Clasificacion_N = np.append(Clasificacion_N,"LUT-DOL")
                        else:
                            if RHOB[i] <= Valor_X_MUD_DOL and RHOB[i] > Valor_X_MUD_CAL:
                                 Clasificacion_N = np.append(Clasificacion_N,"DOL-CAL")
                            else:
                                if RHOB[i] <= Valor_X_MUD_CAL and RHOB[i] > Valor_X_MUD_SIL:
                                     Clasificacion_N = np.append(Clasificacion_N,"CAL-SIL")
                                else:
                                    if RHOB[i] <= Valor_X_MUD_SIL and RHOB[i] > Valor_X_MUD_SAL:
                                         Clasificacion_N = np.append(Clasificacion_N,"SIL-SAL")
                                    else:
                                         Clasificacion_N = np.append(Clasificacion_N,"Indefinido")
    else:
        Clasificacion_N = np.append(Clasificacion_N,"Definido")
    i=i+1
"""Analizando Gráfica L"""
#Pendiente y Ordenada Lutita
Pendiente_MUD_LUT = round(((MUD[0]-LUT[0])/(MUD[2]-LUT[2])),4)
Ordenada_MUD_LUT = round((LUT[0]-(Pendiente_MUD_LUT*LUT[2])),4)
#Pendiente y Ordenada Sal
Pendiente_MUD_SAL = round(((MUD[0]-SAL[0])/(MUD[2]-SAL[2])),4)
Ordenada_MUD_SAL = round((SAL[0]-(Pendiente_MUD_SAL*SAL[2])),4)
#Pendiente y Ordenada Silice
Pendiente_MUD_SIL = round(((MUD[0]-SIL[0])/(MUD[2]-SIL[2])),4)
Ordenada_MUD_SIL = round((SIL[0]-(Pendiente_MUD_SIL*SIL[2])),4)
#Pendiente  Anhidrita
Pendiente_MUD_ANH = round(((MUD[0]-ANH[0])/(MUD[2]-ANH[2])),4)
Ordenada_MUD_ANH = round((ANH[0]-(Pendiente_MUD_ANH*ANH[2])),4)
#Pendiente y Ordenada Calcita
Pendiente_MUD_CAL = round(((MUD[0]-CAL[0])/(MUD[2]-CAL[2])),4)
Ordenada_MUD_CAL = round((CAL[0]-(Pendiente_MUD_CAL*CAL[2])),4)
#Pendiente y Ordenada Dolomita
Pendiente_MUD_DOL = round(((MUD[0]-DOL[0])/(MUD[2]-DOL[2])),4)
Ordenada_MUD_DOL = round((DOL[0]-(Pendiente_MUD_DOL*DOL[2])),4)
#Pendiente y Ordenada Yeso
Pendiente_MUD_YES = round(((MUD[0]-YES[0])/(MUD[2]-YES[2])),4)
Ordenada_MUD_YES = round((YES[0]-(Pendiente_MUD_YES*YES[2])),4)
#
Clasificacion_L = np.array([],dtype=str)
i=0
for dato_region in region_prefinal:
    if str(dato_region) == "Indefinido":
        Valor_X_MUD_LUT = round(((DT[i]-Ordenada_MUD_LUT)/Pendiente_MUD_LUT),4)
        Valor_X_MUD_ANH = round(((DT[i]-Ordenada_MUD_ANH)/Pendiente_MUD_ANH),4)
        Valor_X_MUD_DOL = round(((DT[i]-Ordenada_MUD_DOL)/Pendiente_MUD_DOL),4)
        Valor_X_MUD_SIL = round(((DT[i]-Ordenada_MUD_SIL)/Pendiente_MUD_SIL),4)
        Valor_X_MUD_CAL = round(((DT[i]-Ordenada_MUD_CAL)/Pendiente_MUD_CAL),4)
        Valor_X_MUD_YES = round(((DT[i]-Ordenada_MUD_YES)/Pendiente_MUD_YES),4)
        Valor_X_MUD_SAL = round(((DT[i]-Ordenada_MUD_SAL)/Pendiente_MUD_SAL),4)
        if NPHI[i] < Valor_X_MUD_SAL and NPHI[i] >= Valor_X_MUD_LUT:
            Clasificacion_L = np.append(Clasificacion_L,"LUT-SAL")
        else:
            if NPHI[i] < Valor_X_MUD_SIL and NPHI[i] >= Valor_X_MUD_SAL:
                Clasificacion_L = np.append(Clasificacion_L,"SAL-SIL")
            else:
                if NPHI[i] < Valor_X_MUD_ANH and NPHI[i] >= Valor_X_MUD_SIL:
                    Clasificacion_L = np.append(Clasificacion_L,"SIL-ANH")
                else:
                    if NPHI[i] < Valor_X_MUD_CAL and NPHI[i] >= Valor_X_MUD_ANH:
                        Clasificacion_L = np.append(Clasificacion_L,"ANH-CAL")
                    else:
                        if NPHI[i] < Valor_X_MUD_DOL and NPHI[i] >= Valor_X_MUD_CAL:
                            Clasificacion_L = np.append(Clasificacion_L,"CAL-DOL")
                        else:
                            if NPHI[i] < Valor_X_MUD_YES and NPHI[i] >= Valor_X_MUD_DOL:
                                Clasificacion_L = np.append(Clasificacion_L,"DOL-YES")
                            else:
                                Clasificacion_L = np.append(Clasificacion_L,"Indefinido")
    else:
        Clasificacion_L = np.append(Clasificacion_L,"Definido")
    i=i+1
"""Crear Archivo Temporal"""
Archivo_Region_Prefinal = open("Temporal/Region_Prefinal.txt","w")
i=0
for Dato_region in region_prefinal:
    if i == 0:
        Archivo_Region_Prefinal.writelines(str(Dato_region))
    else:
        Archivo_Region_Prefinal.writelines("\n"+str(Dato_region))
    i=i+1
Archivo_Region_Prefinal.close()