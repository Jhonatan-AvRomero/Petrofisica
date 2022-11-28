# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 21:51:13 2018
@author: Jhonatan
"""
import matplotlib.pyplot as plt
"""Gráfica 3D"""

"""Gráfica rp35 vs m"""
plt.figure(figsize=(10,9))
i=0
color=0
for valor_rp35 in rp35:
    if color <= int(len(rp35)/7):
        plt.plot(rp35[i],m[i],"o",color="#FF0000",markersize=2,alpha=9)
    elif color > int(len(rp35)/7) and color <= int(len(rp35)*2/7):
        plt.plot(rp35[i],m[i],"o",color="#FF8C00",markersize=2,alpha=9)
    elif color > int(len(rp35)*2/7) and color <= int(len(rp35)*3/7):
        plt.plot(rp35[i],m[i],"o",color="#ffcc00",markersize=2,alpha=9)
    elif color > int(len(rp35)*3/7) and color <= int(len(rp35)*4/7):
        plt.plot(rp35[i],m[i],"o",color="#32CD32",markersize=2,alpha=9)
    elif color > int(len(rp35)*4/7) and color <= int(len(rp35)*5/7):
        plt.plot(rp35[i],m[i],"o",color="#4169E1",markersize=2,alpha=9)
    elif color > int(len(rp35)*5/7) and color <= int(len(rp35)*6/7):
        plt.plot(rp35[i],m[i],"o",color="#4169E1",markersize=2,alpha=9)
    elif color > int(len(rp35)*6/7):
        plt.plot(rp35[i],m[i],"o",color="#C71585",markersize=2,alpha=9)
    i=i+1
    color=color+1
ax = plt.gca()
ax.set_facecolor('#ffbfbf')
plt.grid(True,which='both',color="black",alpha=.4)
plt.xlabel("rp35",fontsize=13)
plt.ylabel("m",fontsize=13,rotation=0)
plt.title("Gráfica rp35 vs m",fontsize=15)
plt.savefig("Graficas_Generadas/Graficas_Finales/Gráfica rp35.pdf")

"""Gráfica CKC vs Sp"""
plt.figure(figsize=(10,9))
i=0
color=0
for valor_CKC in CKC:
    if color <= int(len(CKC)/7):
        plt.plot(CKC[i],SpH[i],"o",color="#FF0000",markersize=2,alpha=9)
    elif color > int(len(CKC)/7) and color <= int(len(CKC)*2/7):
        plt.plot(CKC[i],SpH[i],"o",color="#FF8C00",markersize=2,alpha=9)
    elif color > int(len(CKC)*2/7) and color <= int(len(CKC)*3/7):
        plt.plot(CKC[i],SpH[i],"o",color="#ffcc00",markersize=2,alpha=9)
    elif color > int(len(CKC)*3/7) and color <= int(len(CKC)*4/7):
        plt.plot(CKC[i],SpH[i],"o",color="#32CD32",markersize=2,alpha=9)
    elif color > int(len(CKC)*4/7) and color <= int(len(CKC)*5/7):
        plt.plot(CKC[i],SpH[i],"o",color="#4169E1",markersize=2,alpha=9)
    elif color > int(len(CKC)*5/7) and color <= int(len(CKC)*6/7):
        plt.plot(CKC[i],SpH[i],"o",color="#4169E1",markersize=2,alpha=9)
    elif color > int(len(CKC)*6/7):
        plt.plot(CKC[i],SpH[i],"o",color="#C71585",markersize=2,alpha=9)
    i=i+1
    color=color+1
ax = plt.gca()
ax.set_facecolor('#d6ff85')
plt.grid(True,which='both',color="black",alpha=.4)
plt.xlabel("CKC",fontsize=13)
plt.ylabel("Sp",fontsize=13,rotation=0)
plt.title("Gráfica CKC vs Sp",fontsize=15)
plt.savefig("Graficas_Generadas/Graficas_Finales/Gráfica CKC Sp.pdf")

"""Gráfica Re vs rp35"""
plt.figure(figsize=(10,9))
i=0
color=0
for valor_Re_radio in Re_radio:
    if color <= int(len(Re_radio)/7):
        plt.plot(Re_radio[i],rp35[i],"o",color="#FF0000",markersize=2,alpha=9)
    elif color > int(len(Re_radio)/7) and color <= int(len(CKC)*2/7):
        plt.plot(Re_radio[i],rp35[i],"o",color="#FF8C00",markersize=2,alpha=9)
    elif color > int(len(Re_radio)*2/7) and color <= int(len(CKC)*3/7):
        plt.plot(Re_radio[i],rp35[i],"o",color="#ffcc00",markersize=2,alpha=9)
    elif color > int(len(Re_radio)*3/7) and color <= int(len(CKC)*4/7):
        plt.plot(Re_radio[i],rp35[i],"o",color="#32CD32",markersize=2,alpha=9)
    elif color > int(len(Re_radio)*4/7) and color <= int(len(CKC)*5/7):
        plt.plot(Re_radio[i],rp35[i],"o",color="#4169E1",markersize=2,alpha=9)
    elif color > int(len(Re_radio)*5/7) and color <= int(len(CKC)*6/7):
        plt.plot(Re_radio[i],rp35[i],"o",color="#4169E1",markersize=2,alpha=9)
    elif color > int(len(Re_radio)*6/7):
        plt.plot(Re_radio[i],rp35[i],"o",color="#C71585",markersize=2,alpha=9)
    i=i+1
    color=color+1
ax = plt.gca()
ax.set_facecolor('#EEE8AA')
plt.grid(True,which='both',color="black",alpha=.4)
plt.xlabel("Re",fontsize=13)
plt.ylabel("rp35   ",fontsize=13,rotation=0)
plt.title("Gráfica Re vs rp35",fontsize=15)
plt.savefig("Graficas_Generadas/Graficas_Finales/Gráfica Re rp35.pdf")

"""LOG FR VS FITR"""
"""i=0
for vFR in FR:
    mm = vFR/FITR[i]
    print(mm)
    i=i+1"""
plt.figure(figsize=(10,9))
X1 = min(FITR)
X2 = max(FITR)
Y1 = -2*math.log10((min(FITR)))
Y2 = -2*math.log10((max(FITR)))
X_f = [X1,X2]
Y_f = [10**Y1,10**Y2]
plt.loglog(X_f,Y_f,"red")
i=0
color=0
for valor_FR in FR:
    if color <= int(len(FR)/7):
        plt.loglog(FITR[i],FR[i],"o",color="#FF0000",markersize=2,alpha=9)
    elif color > int(len(FR)/7) and color <= int(len(CKC)*2/7):
        plt.loglog(FITR[i],FR[i],"o",color="#FF8C00",markersize=2,alpha=9)
    elif color > int(len(FR)*2/7) and color <= int(len(CKC)*3/7):
        plt.loglog(FITR[i],FR[i],"o",color="#ffcc00",markersize=2,alpha=9)
    elif color > int(len(FR)*3/7) and color <= int(len(CKC)*4/7):
        plt.loglog(FITR[i],FR[i],"o",color="#32CD32",markersize=2,alpha=9)
    elif color > int(len(FR)*4/7) and color <= int(len(CKC)*5/7):
        plt.loglog(FITR[i],FR[i],"o",color="#4169E1",markersize=2,alpha=9)
    elif color > int(len(FR)*5/7) and color <= int(len(CKC)*6/7):
        plt.loglog(FITR[i],FR[i],"o",color="#4169E1",markersize=2,alpha=9)
    elif color > int(len(FR)*6/7):
        plt.loglog(FITR[i],FR[i],"o",color="#C71585",markersize=2,alpha=9)
    i=i+1
    color=color+1
    
TSPRASMUS = np.array([],dtype=str)
i=0
for vFR in FR:
    valor_m = abs(math.log10(vFR)/math.log10(FITR[i]))
    if valor_m >= 1 and valor_m <=2:
        TSPRASMUS = np.append(TSPRASMUS,"FRAC")
    elif valor_m > 2:
        TSPRASMUS = np.append(TSPRASMUS,"VUGS")
    else:
        TSPRASMUS = np.append(TSPRASMUS,"INDEF")
    i=i+1
ax = plt.gca()
ax.set_facecolor('#e6cce6')
plt.grid(True,which='both',color="black",alpha=1)
plt.xlabel("log FITR",fontsize=13)
plt.ylabel("log FR     ",fontsize=13,rotation=0)
plt.title("Gráfica log FITR vs log FR (TSP-RASMUS)",fontsize=15)
plt.savefig("Graficas_Generadas/Graficas_Finales/Gráfica log FR FITR.pdf")

Archivo_TSPRASMUS = open("Nuevos_Archivos_Creados/Archivos_Finales/TSPRASMUS.txt","w")
i=0
for Dato_TSPRASMUS in TSPRASMUS:
    if i == 0:
        Archivo_TSPRASMUS.writelines(str(Dato_TSPRASMUS))
    else:
        Archivo_TSPRASMUS.writelines("\n"+str(Dato_TSPRASMUS))
    i=i+1
Archivo_TSPRASMUS.close() 


    