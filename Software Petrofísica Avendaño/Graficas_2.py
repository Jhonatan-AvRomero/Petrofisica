# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 11:42:32 2018
@author: Jhonatan
"""
"""Grafica IR"""
import numpy as np
import matplotlib.pyplot as plt
plt.figure(figsize=(9,9))
i=0
color=0
for DLL_valor in DLL:
    if color <= int(len(DLL)/7):
        nombre_color="red"
        plt.loglog(RO[i],DLL[i],"o",color="#FF0000",markersize=2,alpha=1)
    elif color > int(len(DLL)/7) and color <= int(len(DLL)*2/7):
        nombre_color="orange"
        plt.loglog(RO[i],DLL[i],"o",color="#FF8C00",markersize=2,alpha=1)
    elif color > int(len(DLL)*2/7) and color <= int(len(DLL)*3/7):
        nombre_color="yellow"
        plt.loglog(RO[i],DLL[i],"o",color="#ffcc00",markersize=2,alpha=1)
    elif color > int(len(DLL)*3/7) and color <= int(len(DLL)*4/7):
        nombre_color="green"
        plt.loglog(RO[i],DLL[i],"o",color="#32CD32",markersize=2,alpha=1)
    elif color > int(len(DLL)*4/7) and color <= int(len(DLL)*5/7):
        nombre_color="blue"
        plt.loglog(RO[i],DLL[i],"o",color="#4169E1",markersize=2,alpha=1)
    elif color > int(len(DLL)*5/7) and color <= int(len(DLL)*6/7):
        nombre_color="indigo"
        plt.loglog(RO[i],DLL[i],"o",color="#4169E1",markersize=2,alpha=1)
    elif color > int(len(DLL)*6/7):
        nombre_color="violet"
        plt.loglog(RO[i],DLL[i],"o",color="#C71585",markersize=2,alpha=1)
    i=i+1
    color=color+1
plt.loglog(RO,DLL,"o",color="black",markersize=.4,alpha=4)
ax = plt.gca()
ax.set_facecolor('#b3ffff')
plt.axis([10,100000,10,100000])
plt.grid(True,which='both',color="black",alpha=.6)
plt.xlabel("RO",fontsize=11)
plt.ylabel("RT",fontsize=11)
plt.title('Gráfica '+'$I_{R}$',fontsize=15)
etiquetas = ['10','100','1,000','10,000','100,000']
div = [10,100,1000,10000,100000]
plt.xticks(div,etiquetas)
plt.yticks(div,etiquetas)
plt.savefig("Graficas_Generadas/Gráfica IR.pdf")
#
"""Gráfica m vs Tortuosidad"""
plt.figure(figsize=(10,9))
i=0
color=0
for m_valor in m:
    if color <= int(len(m)/7):
        nombre_color="red"
        plt.plot(m[i],T_m[i],"o",color="#FF0000",markersize=2,alpha=9)
    elif color > int(len(m)/7) and color <= int(len(m)*2/7):
        nombre_color="orange"
        plt.plot(m[i],T_m[i],"o",color="#FF8C00",markersize=2,alpha=9)
    elif color > int(len(m)*2/7) and color <= int(len(m)*3/7):
        nombre_color="yellow"
        plt.plot(m[i],T_m[i],"o",color="#ffcc00",markersize=2,alpha=9)
    elif color > int(len(m)*3/7) and color <= int(len(m)*4/7):
        nombre_color="green"
        plt.plot(m[i],T_m[i],"o",color="#32CD32",markersize=2,alpha=9)
    elif color > int(len(m)*4/7) and color <= int(len(m)*5/7):
        nombre_color="blue"
        plt.plot(m[i],T_m[i],"o",color="#4169E1",markersize=2,alpha=9)
    elif color > int(len(m)*5/7) and color <= int(len(m)*6/7):
        nombre_color="indigo"
        plt.plot(m[i],T_m[i],"o",color="#4169E1",markersize=2,alpha=9)
    elif color > int(len(m)*6/7):
        nombre_color="violet"
        plt.plot(m[i],T_m[i],"o",color="#C71585",markersize=2,alpha=9)
    i=i+1
    color=color+1
plt.plot(m,T_m,"o",color="black",markersize=.4,alpha=1)
ax = plt.gca()
ax.set_facecolor('#ffccff')
plt.grid(True,which='both',color="black",alpha=.4)
plt.xlabel("m",fontsize=13)
plt.ylabel("T  ",fontsize=13,rotation=0)
plt.title("Gráfica m vs T",fontsize=15)
plt.savefig("Graficas_Generadas/Gráfica m_T.pdf")
#
"""Gráfica m vs r"""
plt.figure(figsize=(10,9))
i=0
color=0
for r_valor in r:
    if color <= int(len(r)/7):
        nombre_color="red"
        plt.plot(r[i],m[i],"o",color="#FF0000",markersize=2,alpha=9)
    elif color > int(len(r)/7) and color <= int(len(r)*2/7):
        nombre_color="orange"
        plt.plot(r[i],m[i],"o",color="#FF8C00",markersize=2,alpha=9)
    elif color > int(len(r)*2/7) and color <= int(len(r)*3/7):
        nombre_color="yellow"
        plt.plot(r[i],m[i],"o",color="#ffcc00",markersize=2,alpha=9)
    elif color > int(len(r)*3/7) and color <= int(len(r)*4/7):
        nombre_color="green"
        plt.plot(r[i],m[i],"o",color="#32CD32",markersize=2,alpha=9)
    elif color > int(len(r)*4/7) and color <= int(len(r)*5/7):
        nombre_color="blue"
        plt.plot(r[i],m[i],"o",color="#4169E1",markersize=2,alpha=9)
    elif color > int(len(r)*5/7) and color <= int(len(r)*6/7):
        nombre_color="indigo"
        plt.plot(r[i],m[i],"o",color="#4169E1",markersize=2,alpha=9)
    elif color > int(len(r)*6/7):
        nombre_color="violet"
        plt.plot(r[i],m[i],"o",color="#C71585",markersize=2,alpha=9)
    i=i+1
    color=color+1
#plt.plot(r,m,"o",color="black",markersize=.4,alpha=5)
ax = plt.gca()
ax.set_facecolor('#c4e3ed')
plt.grid(True,which='both',color="black",alpha=.4)
plt.xlabel("r",fontsize=13)
plt.ylabel("m",fontsize=13,rotation=0)
plt.title("Gráfica r vs m",fontsize=15)
plt.savefig("Graficas_Generadas/Gráfica m_r.pdf")
#
"""Gráfica 1/T vs r"""
plt.figure(figsize=(10,9))
i=0
color=0
for T_1_valor in T_1:
    if color <= int(len(T_1)/7):
        nombre_color="red"
        plt.plot(T_1[i],r[i],"o",color="red",markersize=2,alpha=9)
    elif color > int(len(T_1)/7) and color <= int(len(T_1)*2/7):
        nombre_color="orange"
        plt.plot(T_1[i],r[i],"o",color="orange",markersize=2,alpha=9)
    elif color > int(len(T_1)*2/7) and color <= int(len(T_1)*3/7):
        nombre_color="yellow"
        plt.plot(T_1[i],r[i],"o",color="#ffcc00",markersize=2,alpha=9)
    elif color > int(len(T_1)*3/7) and color <= int(len(T_1)*4/7):
        nombre_color="green"
        plt.plot(T_1[i],r[i],"o",color="green",markersize=2,alpha=9)
    elif color > int(len(T_1)*4/7) and color <= int(len(T_1)*5/7):
        nombre_color="blue"
        plt.plot(T_1[i],r[i],"o",color="blue",markersize=2,alpha=9)
    elif color > int(len(T_1)*5/7) and color <= int(len(T_1)*6/7):
        nombre_color="indigo"
        plt.plot(T_1[i],r[i],"o",color="#4169E1",markersize=2,alpha=9)
    elif color > int(len(T_1)*6/7):
        nombre_color="violet"
        plt.plot(T_1[i],r[i],"o",color="#C71585",markersize=2,alpha=9)
    i=i+1
    color=color+1
#plt.plot(T_1,r,"o",color="black",markersize=.4,alpha=5)
ax = plt.gca()
ax.set_facecolor('#fff0b3')
plt.grid(True,which='both',color="black",alpha=.4)
plt.xlabel(r"$\frac{1}{T}$",fontsize=18)
plt.ylabel("r",fontsize=14,rotation=0)
plt.title("Gráfica "r"$\frac{1}{T}$ vs r",fontsize=15)
plt.savefig("Graficas_Generadas/Gráfica T_r.pdf")
#
"""Gráfica m vs FIENT"""
plt.figure(figsize=(10,9))
i=0
color=0
for FIENT_valor in FIENT:
    if color <= int(len(FIENT)/7):
        nombre_color="red"
        plt.plot(FIENT[i],m[i],"o",color="red",markersize=2,alpha=9)
    elif color > int(len(FIENT)/7) and color <= int(len(FIENT)*2/7):
        nombre_color="orange"
        plt.plot(FIENT[i],m[i],"o",color="orange",markersize=2,alpha=9)
    elif color > int(len(FIENT)*2/7) and color <= int(len(FIENT)*3/7):
        nombre_color="yellow"
        plt.plot(FIENT[i],m[i],"o",color="#ffcc00",markersize=2,alpha=9)
    elif color > int(len(FIENT)*3/7) and color <= int(len(FIENT)*4/7):
        nombre_color="green"
        plt.plot(FIENT[i],m[i],"o",color="green",markersize=2,alpha=9)
    elif color > int(len(FIENT)*4/7) and color <= int(len(FIENT)*5/7):
        nombre_color="blue"
        plt.plot(FIENT[i],m[i],"o",color="blue",markersize=2,alpha=9)
    elif color > int(len(FIENT)*5/7) and color <= int(len(FIENT)*6/7):
        nombre_color="indigo"
        plt.plot(FIENT[i],m[i],"o",color="#4169E1",markersize=2,alpha=9)
    elif color > int(len(FIENT)*6/7):
        nombre_color="violet"
        plt.plot(FIENT[i],m[i],"o",color="#C71585",markersize=2,alpha=9)
    i=i+1
    color=color+1
plt.plot(FIENT,m,"o",color="black",markersize=.4,alpha=5)
ax = plt.gca()
ax.set_facecolor('#b3ffb3')
plt.grid(True,which='both',color="black",alpha=.4)
plt.xlabel("FIent",fontsize=18)
plt.ylabel("m",fontsize=14,rotation=0)
plt.title("Gráfica FIent vs m",fontsize=15)
plt.savefig("Graficas_Generadas/Gráfica FIent_m.pdf")