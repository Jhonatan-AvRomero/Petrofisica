# -*- coding: utf-8 -*-
"""
Created on Sun May 20 20:18:22 2018
@author: Jhonatan
"""
import numpy as np
import matplotlib.pyplot as plt
import math as math
"""Gráfica DT vs PHI"""
"""Abriendo DT"""
DT = np.array([],dtype=float)
Archivo_DT = open("Archivos_TXT/DT.txt")
for Linea_DT in Archivo_DT.readlines():
    Nueva_Linea_DT = Linea_DT.rstrip('\n')
    Nueva_Linea_Convertida_DT = round((float(Nueva_Linea_DT)),4)
    DT = np.append(DT,Nueva_Linea_Convertida_DT)
Archivo_DT.close()
"""Abriendo RT"""
RT = np.array([],dtype=float)
Archivo_RT = open("Archivos_TXT/DLL.txt")
for Linea_RT in Archivo_RT.readlines():
    Nueva_Linea_RT = Linea_RT.rstrip('\n')
    Nueva_Linea_Convertida_RT = round((float(Nueva_Linea_RT)),4)
    RT = np.append(RT,Nueva_Linea_Convertida_RT)
Archivo_RT.close()
"""Abriendo PHITR"""
FITR = np.array([],dtype=float)
Archivo_FITR = open("Nuevos_Archivos_Creados/Volumen_Real/FITR.txt")
for Linea_FITR in Archivo_FITR.readlines():
    Nueva_Linea_FITR = Linea_FITR.rstrip('\n')
    Nueva_Linea_Convertida_FITR = round((float(Nueva_Linea_FITR)),4)
    FITR = np.append(FITR,Nueva_Linea_Convertida_FITR)
Archivo_FITR.close()
"""Determinación de DTmatriz"""
DTmatriz = np.array([],dtype=float)
i=0
for valor_DT in DT:
    Valor_DTmatriz = round(((valor_DT-(FITR[i]*189))/(1-FITR[i])),4)
    DTmatriz = np.append(DTmatriz,round(Valor_DTmatriz,4))
    i=i+1
"""Determinando DT-DTma"""
DD = np.array([],dtype=float)
i=0
for valor_DT in DT:
    Valor_DD = (valor_DT-DTmatriz[i])
    DD = np.append(DD,round(Valor_DD,4))
    i=i+1
"""Graficando para encontrar mvsphi"""
fig = plt.figure(figsize=(11,7),dpi=800)
plt.xlabel("FITR")
plt.ylabel("DT - DTm")
plt.title("Pendiente mvsp")
i=0
color=0
for DD_valor in DD:
    if color <= int(len(DD)/7):
        plt.plot(FITR[i],DD[i],"o",color="#FF0000",markersize=2,alpha=1)
    elif color > int(len(DD)/7) and color <= int(len(DD)*2/7):
        plt.plot(FITR[i],DD[i],"o",color="#FF8C00",markersize=2,alpha=1)
    elif color > int(len(DD)*2/7) and color <= int(len(DD)*3/7):
        plt.plot(FITR[i],DD[i],"o",color="#FFD700",markersize=2,alpha=1)
    elif color > int(len(DD)*3/7) and color <= int(len(DD)*4/7):
        plt.plot(FITR[i],DD[i],"o",color="#32CD32",markersize=2,alpha=1)
    elif color > int(len(DD)*4/7) and color <= int(len(DD)*5/7):
        plt.plot(FITR[i],DD[i],"o",color="#4169E1",markersize=2,alpha=1)
    elif color > int(len(DD)*5/7) and color <= int(len(DD)*6/7):
        plt.plot(FITR[i],DD[i],"o",color="#4169E1",markersize=2,alpha=1)
    elif color > int(len(DD)*6/7):
        plt.plot(FITR[i],DD[i],"o",color="#C71585",markersize=2,alpha=1)
    i=i+1
    color=color+1
ax = plt.gca()
fig.patch.set_facecolor('#F0E68C')
ax.set_facecolor('#E0FFFF')
plt.grid(True,which="both")
"""Obteniendo Pendiente por ponderación"""
"""Tengo array FITR - X"""
"""Tengo array DD - Y"""
n_d = len(DD)
sumFITR = sum(FITR)
sumDD = sum(DD)
sumFITR2 = sum(FITR*FITR)
sumDD2 = sum(DD*DD)
sumFD = sum(FITR*DD)
promFITR = sumFITR/n_d
promDD = sumDD/n_d
"""Pendiente y ordenada al origen grafica"""
mg = round(((sumFITR*sumDD - n_d*sumFD)/(sumFITR**2-n_d*sumFITR2)),4)
bg = promDD-mg*promFITR
plt.plot(FITR,mg*FITR+bg,label='msvp  '+str(mg),color='k')
plt.legend(loc='best')

plt.savefig("AGUILERA_GRAFICAS/Yacimientos_Fracturados_Aguilera/Gráfica msvp.png",facecolor=fig.get_facecolor())
"""CREAR GRÁFICA POROSIDAD VS RT"""
fig = plt.figure(figsize=(11,7))
plt.axis([1,100000,.0001,1])
plt.xlabel("log RT")
plt.ylabel("log FITR")
plt.grid(True,which="both")
i=0
color=0
for valor_RT in RT:
    if color <= int(len(RT)/7):
        plt.loglog(RT[i],FITR[i],"o",color="#FF0000",markersize=2,alpha=1)
    elif color > int(len(RT)/7) and color <= int(len(RT)*2/7):
        plt.loglog(RT[i],FITR[i],"o",color="#FF8C00",markersize=2,alpha=1)
    elif color > int(len(RT)*2/7) and color <= int(len(RT)*3/7):
        plt.loglog(RT[i],FITR[i],"o",color="#FFD700",markersize=2,alpha=1)
    elif color > int(len(RT)*3/7) and color <= int(len(RT)*4/7):
        plt.loglog(RT[i],FITR[i],"o",color="#32CD32",markersize=2,alpha=1)
    elif color > int(len(RT)*4/7) and color <= int(len(RT)*5/7):
        plt.loglog(RT[i],FITR[i],"o",color="#4169E1",markersize=2,alpha=1)
    elif color > int(len(RT)*5/7) and color <= int(len(RT)*6/7):
        plt.loglog(RT[i],FITR[i],"o",color="#4169E1",markersize=2,alpha=1)
    elif color > int(len(RT)*6/7):
        plt.loglog(RT[i],FITR[i],"o",color="#C71585",markersize=2,alpha=1)
    i=i+1
    color=color+1
ax = plt.gca()
fig.patch.set_facecolor('#F0E68C')
ax.set_facecolor('#E0FFFF')
RT_orden = sorted(RT)
j=0
"""---"""
RT_pendiente = np.array([],dtype=float)
for valor_RT in RT_orden:
    if j<=2:
        RT_pendiente = np.append(RT_pendiente,valor_RT)
    j=j+1
FITR_pendiente = np.array([],dtype=float)
for valor_RT in RT_pendiente:
    i=0
    for valor_rt in RT:
        if valor_RT == valor_rt:
            FITR_pendiente = np.append(FITR_pendiente,FITR[i])
        i=i+1
"""---"""
RT1 = np.array([],dtype=float)
FITR1 = np.array([],dtype=float)
i=0
for v_RT in RT_pendiente:
    n_RT = math.log10(v_RT)
    n_FITR = math.log10(FITR_pendiente[i])
    RT1 = np.append(RT1,n_RT)
    FITR1 = np.append(FITR1,n_FITR)
    i=i+1
"""---"""
X1 = RT_pendiente
X2 = RT1
Y1 = FITR_pendiente
Y2 = FITR1
X = np.array(X1)
Xo = np.array(X2)
Y = np.array(Y1)
Yo = np.array(Y2)
n_d = len(Y)
sumX = sum(X)
sumXo = sum(Xo)
sumY = sum(Y)
sumYo = sum(Yo)
sumX2 = sum(X*X)
sumX2o = sum(Xo*Xo)
sumY2 = sum(Y*Y)
sumY2o = sum(Yo*Yo)
sumXY = sum(X*Y)
sumXYo = sum(Xo*Yo)
"""Pendiente y ordenada al origen grafica"""
m_G = round((((sumX*sumY)-(n_d*sumXY))/((sumX**2)-(n_d*sumX2))),4)
m_G2 = round((((sumXo*sumYo)-(n_d*sumXYo))/((sumXo**2)-(n_d*sumX2o))),4)
b_G = (sumY/n_d)-(m_G*sumX/n_d)
plt.loglog(X,m_G*X+b_G,color="k")
print(m_G2)
m_pickett = m_G2
plt.savefig("AGUILERA_GRAFICAS/Yacimientos_Fracturados_Aguilera/Gráfica RT vs FITR log.png",facecolor=fig.get_facecolor())
from matplotlib.ticker import FormatStrFormatter;
"""Profundidad"""
Profundidad = np.array([],dtype=float)
Archivo_Profundidad = open("Archivos_TXT/Profundidad.txt")
for Linea_Profundidad in Archivo_Profundidad.readlines():
    Nueva_Linea_Profundidad = Linea_Profundidad.rstrip('\n')
    Nueva_Linea_Convertida_Profundidad = float(Nueva_Linea_Profundidad)
    Profundidad = np.append(Profundidad,Nueva_Linea_Convertida_Profundidad)
Archivo_Profundidad.close()
"""Calcular P12"""
m = abs(m_G2)
P12 = np.array([],dtype=float)
i=0
for v_rt in RT:
    v_P12 = round((math.sqrt((v_rt*((FITR[i])**m)))),4)
    P12 = np.append(P12,v_P12)
    i=i+1
"""Calculando el número de intervalos"""
Nin = int(1+(3.3*math.log10(len(P12))))
"""Calculando Rango"""
Rango = max(P12)-min(P12)
"""Calculando Amplitud"""
Amplitud = (Rango/Nin)
"""Frecuencia"""
i= min(P12)
j= i + Amplitud
Frecuencia = np.array([],dtype=int)
rango = np.array([],dtype=str)
for v_fitr in FITR:
    k=0
    for v_P12 in P12:
        if P12[k] >= i and P12[k]<j:
            Frecuencia = np.append(Frecuencia,1)
            vrango = str(i)+'--'+str(j)
            rango = np.append(rango,vrango)
        k=k+1
    i=j
    j=i+Amplitud
"""---"""
i= min(P12)
j= i + Amplitud
r = rango.tolist()
"""---"""
veces_def = np.array([],dtype=int)
rango_def = np.array([],dtype=str)
rango_graf = np.array([],dtype=float)
"""---"""
for v_veces in Frecuencia:
    categoria = str(i)+'--'+str(j)
    repeticiones = r.count(categoria)
    if repeticiones != 0:
        veces_def = np.append(veces_def,repeticiones)
        rango_op = (i+((j-i)/2))
        rango_def = np.append(rango_def,categoria)
        rango_graf = np.append(rango_graf,rango_op)
    i=j
    j=i+Amplitud
"""Frecuencia Acumulada"""
i=0
Frecuencia_Acum = np.array([],dtype=int)
for vr in veces_def:
    frecacum = round(vr+i,4)
    Frecuencia_Acum = np.append(Frecuencia_Acum,frecacum)
    i=frecacum
"""Frecuencia Relativa"""
Frecuencia_Relatif = np.array([],dtype=float)
for vr in veces_def:
    frecrelat = vr/len(P12)
    Frecuencia_Relatif = np.append(Frecuencia_Relatif,frecrelat)
"""Frecuancia Relativa Acumulada"""
i=0
Frecuencia_R_Acum = np.array([],dtype=int)
for vr in Frecuencia_Relatif:
    frecacum = vr+i
    Frecuencia_R_Acum = np.append(Frecuencia_R_Acum,frecacum)
    i=frecacum
"""Crear Archivo Rangos"""
Archivo_R_def = open("AGUILERA_ARCHIVOS/Yacimientos_Fracturados_Aguilera/Valores_P12.txt","w")
i=0
for Dato_R in rango_def:
    if i == 0:
        Archivo_R_def.writelines(str(Dato_R))
    else:
        Archivo_R_def.writelines("\n"+str(Dato_R))
    i=i+1
Archivo_R_def.close()

Archivo_veces = open("AGUILERA_ARCHIVOS/Yacimientos_Fracturados_Aguilera/Frecuencia_Absoluta.txt","w")
i=0
for Dato_veces in veces_def:
    if i == 0:
        Archivo_veces.writelines(str(Dato_veces))
    else:
        Archivo_veces.writelines("\n"+str(Dato_veces))
    i=i+1
Archivo_veces.close()

Archivo_R_graf = open("AGUILERA_ARCHIVOS/Yacimientos_Fracturados_Aguilera/Marca_Clase.txt","w")
i=0
for Dato_R in rango_graf:
    if i == 0:
        Archivo_R_graf.writelines(str(Dato_R))
    else:
        Archivo_R_graf.writelines("\n"+str(Dato_R))
    i=i+1
Archivo_R_graf.close()

Archivo_Frec_Acum = open("AGUILERA_ARCHIVOS/Yacimientos_Fracturados_Aguilera/Frecuencia_Absoluta_Acumulada.txt","w")
i=0
for Dato_f in Frecuencia_Acum:
    if i == 0:
        Archivo_Frec_Acum.writelines(str(Dato_f))
    else:
        Archivo_Frec_Acum.writelines("\n"+str(Dato_f))
    i=i+1
Archivo_Frec_Acum.close()

Archivo_Frec_Rel = open("AGUILERA_ARCHIVOS/Yacimientos_Fracturados_Aguilera/Frecuencia_Relativa.txt","w")
i=0
for Dato_f in Frecuencia_Relatif:
    if i == 0:
        Archivo_Frec_Rel.writelines(str(Dato_f))
    else:
        Archivo_Frec_Rel.writelines("\n"+str(Dato_f))
    i=i+1
Archivo_Frec_Rel.close()

Archivo_Frec_Rel_A = open("AGUILERA_ARCHIVOS/Yacimientos_Fracturados_Aguilera/Frecuencia_Relativa_Acumulada.txt","w")
i=0
for Dato_f in Frecuencia_R_Acum:
    if i == 0:
        Archivo_Frec_Rel_A.writelines(str(Dato_f))
    else:
        Archivo_Frec_Rel_A.writelines("\n"+str(Dato_f))
    i=i+1
Archivo_Frec_Rel_A.close()
"""Crear Archivo P12"""
Archivo_P12 = open("AGUILERA_ARCHIVOS/Yacimientos_Fracturados_Aguilera/P12.txt","w")
i=0
for Dato_P12 in P12:
    if i == 0:
        Archivo_P12.writelines(str(Dato_P12))
    else:
        Archivo_P12.writelines("\n"+str(Dato_P12))
    i=i+1
Archivo_P12.close()
"""Graficar P12 vs Frecuencia Relativa Acumulada"""

x = Frecuencia_R_Acum
y = rango_graf

fig,ax = plt.subplots(figsize=(9, 6), dpi=80, facecolor='w', edgecolor='k');
ax.set_xlim([0.0001,.9999]);
ax.spines['left']._adjust_location()
ax.set_xscale('logit');
ax.xaxis.set_minor_formatter(FormatStrFormatter(""));
ax.set_xticks([0.0005,.01,.02,.05,.1,.2,.3,.4,.5,.6,.7,.8,.9,.95,.98,.99,.9999])  
ax.set_xticklabels(['0.0005','.01','.02','.05','.1','.2','.3','.4','.5','.6','.7','.8','.9','.95','.98','.99','.9999'])
ax.set_xlabel("Frecuencia Relativa Acumulada",fontsize=12);
ax.set_ylabel("P$^{1/2}$        ",rotation='0',fontsize=14); #set y axis label (logit scale)
ax.grid()
ax.plot(x,y,"o");
ax = plt.gca()
fig.patch.set_facecolor('#F0E68C')
ax.set_facecolor('#E0FFFF')
X1 = [Frecuencia_R_Acum[0],Frecuencia_R_Acum[6]]
X2 = [Frecuencia_R_Acum[7],Frecuencia_R_Acum[8]]
Y1 = [rango_graf[0],rango_graf[6]]
Y2 = [rango_graf[7],rango_graf[8]]
X = np.array(X1)
Xo = np.array(X2)
Y = np.array(Y1)
Yo = np.array(Y2)
n_d = len(Y)
n_d2 = len(Yo)
sumX = sum(X)
sumXo = sum(Xo)
sumY = sum(Y)
sumYo = sum(Yo)
sumX2 = sum(X*X)
sumX2o = sum(Xo*Xo)
sumY2 = sum(Y*Y)
sumY2o = sum(Yo*Yo)
sumXY = sum(X*Y)
sumXYo = sum(Xo*Yo)
"""Pendiente y ordenada al origen grafica"""
m_G = round((((sumX*sumY)-(n_d*sumXY))/((sumX**2)-(n_d*sumX2))),4)
m_G2 = round((((sumXo*sumYo)-(n_d2*sumXYo))/((sumXo**2)-(n_d2*sumX2o))),4)
b_G = (sumY/n_d)-(m_G*sumX/n_d)
b_G2 = (sumYo/n_d2)-(m_G2*sumXo/n_d2)
ax.plot(X,m_G*X+b_G,color="green")
ax.plot(Xo,m_G2*Xo+b_G2,color="red")
plt.savefig("AGUILERA_GRAFICAS/Yacimientos_Fracturados_Aguilera/Frecuencia P12.png",facecolor=fig.get_facecolor())

x = [Frecuencia_R_Acum[0],Frecuencia_R_Acum[1],Frecuencia_R_Acum[2],Frecuencia_R_Acum[3],Frecuencia_R_Acum[4],Frecuencia_R_Acum[5],Frecuencia_R_Acum[6]]
y = [rango_graf[0],rango_graf[1],rango_graf[2],rango_graf[3],rango_graf[4],rango_graf[5],rango_graf[6]]

fig,ax = plt.subplots(figsize=(9, 6), dpi=80, facecolor='w', edgecolor='k');
ax.set_xlim([0.0001,.9999]);
ax.spines['left']._adjust_location()
ax.set_xscale('logit');
ax.xaxis.set_minor_formatter(FormatStrFormatter(""));
ax.set_xticks([0.0005,.01,.02,.05,.1,.2,.3,.4,.5,.6,.7,.8,.9,.95,.98,.99,.9999])  
ax.set_xticklabels(['0.0005','.01','.02','.05','.1','.2','.3','.4','.5','.6','.7','.8','.9','.95','.98','.99','.9999'])
ax.set_xlabel("Frecuencia Relativa Acumulada",fontsize=12);
ax.set_ylabel("P$^{1/2}$        ",rotation='0',fontsize=14); #set y axis label (logit scale)
ax.set_yticks([0,1,2,4,6,8,10,12,13.3,16,18,20,22,24,26,28,30,32])
ax.grid()
ax.plot(x,y,"o");
ax = plt.gca()
fig.patch.set_facecolor('#F0E68C')
ax.set_facecolor('#E0FFFF')

X1 = [Frecuencia_R_Acum[0],Frecuencia_R_Acum[6]]
Y1 = [rango_graf[0],rango_graf[6]]
X = np.array(X1)
Y = np.array(Y1)
n_d = len(Y)
sumX = sum(X)
sumY = sum(Y)
sumX2 = sum(X*X)
sumY2 = sum(Y*Y)
sumXY = sum(X*Y)
"""Pendiente y ordenada al origen grafica"""
m_G = round((((sumX*sumY)-(n_d*sumXY))/((sumX**2)-(n_d*sumX2))),4)
b_G = (sumY/n_d)-(m_G*sumX/n_d)
ax.plot(X,m_G*X+b_G,color="green")
P50 = 13.3
plt.savefig("AGUILERA_GRAFICAS/Yacimientos_Fracturados_Aguilera/P12 Agua.png",facecolor=fig.get_facecolor())

"""m_picket"""
Archivo_mpickett = open("AGUILERA_ARCHIVOS/Yacimientos_Fracturados_Aguilera/m_pickett.txt","w")
i=0
for Dato_P12 in P12:
    Dato_P12 = abs(m_pickett)
    if i == 0:
        Archivo_mpickett.writelines(str(Dato_P12))
    else:
        Archivo_mpickett.writelines("\n"+str(Dato_P12))
    i=i+1
Archivo_mpickett.close()

"""FR PICKETT"""
FR_PICKETT = np.array([],dtype=float)
Error_PICKETT = np.array([],dtype=float)
i=0
for vFITR in FITR:
    vFR = vFITR**m_pickett
    error = abs((FR[i]-vFR)/FR[i])*100
    FR_PICKETT = np.append(FR_PICKETT,vFR)
    Error_PICKETT = np.append(Error_PICKETT,error)
    i=i+1

Archivo_FR_PICKETT = open("AGUILERA_ARCHIVOS/Yacimientos_Fracturados_Aguilera/FR_PICKETT.txt","w")
i=0
for Dato_FR_PICKETT in FR_PICKETT:
    if i == 0:
        Archivo_FR_PICKETT.writelines(str(Dato_FR_PICKETT))
    else:
        Archivo_FR_PICKETT.writelines("\n"+str(Dato_FR_PICKETT))
    i=i+1
Archivo_FR_PICKETT.close()

Archivo_Error_PICKETT = open("AGUILERA_ARCHIVOS/Yacimientos_Fracturados_Aguilera/Error_PICKETT.txt","w")
i=0
for Dato_Error_PICKETT in Error_PICKETT:
    if i == 0:
        Archivo_Error_PICKETT.writelines(str(Dato_Error_PICKETT))
    else:
        Archivo_Error_PICKETT.writelines("\n"+str(Dato_Error_PICKETT))
    i=i+1
Archivo_Error_PICKETT.close()