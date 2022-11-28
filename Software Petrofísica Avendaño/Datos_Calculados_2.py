# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 10:16:18 2018
@author: Jhonatan
"""
import math as math
FR = np.array([],dtype=float)
Archivo_FR = open("Archivos_TXT/FR.txt")
for Linea_FR in Archivo_FR.readlines():
    Nueva_Linea_FR = Linea_FR.rstrip('\n')
    Nueva_Linea_Convertida_FR = float(Nueva_Linea_FR)
    FR = np.append(FR,Nueva_Linea_Convertida_FR)
Archivo_FR.close()
"""Calculando columna m"""
m = np.array([],dtype=float)
i=0
for Valor_FR in FR:
    Valor_m = (-math.log10(Valor_FR))/(math.log10(FITR[i]))
    m = np.append(m,Valor_m)
    i=i+1
Archivo_m = open("Nuevos_Archivos_Creados/m.txt","w")
i=0
for Dato_m in m:
    if i == 0:
        Archivo_m.writelines(str(round(Dato_m,4)))
    else:
        Archivo_m.writelines("\n"+str(round(Dato_m,4)))
    i=i+1
Archivo_m.close()
"""Calculando columna FIF"""
FIF = np.array([],dtype=float)
i=0
for Valor_FITR in FITR:
    Valor_FIF = Valor_FITR**m[i]
    FIF = np.append(FIF,Valor_FIF)
    i=i+1
Archivo_FIF = open("Nuevos_Archivos_Creados/FIF.txt","w")
i=0
for Dato_FIF in FIF:
    if i == 0:
        Archivo_FIF.writelines(str(round(Dato_FIF,4)))
    else:
        Archivo_FIF.writelines("\n"+str(round(Dato_FIF,4)))
    i=i+1
Archivo_FIF.close()
"""Calculando columna FIENT"""
FIENT = np.array([],dtype=float)
i=0
for Valor_FIF in FIF:
    Valor_FIENT = FITR[i]-Valor_FIF
    FIENT = np.append(FIENT,Valor_FIENT)
    i=i+1
Archivo_FIENT = open("Nuevos_Archivos_Creados/FIENT.txt","w")
i=0
for Dato_FIENT in FIENT:
    if i == 0:
        Archivo_FIENT.writelines(str(round(Dato_FIENT,4)))
    else:
        Archivo_FIENT.writelines("\n"+str(round(Dato_FIENT,4)))
    i=i+1
Archivo_FIENT.close()
"""Calculando RO"""
RO = np.array([],dtype=float)
for Valor_FR in FR:
    Valor_RO = Valor_FR*0.275
    RO = np.append(RO,Valor_RO)
Archivo_RO = open("Nuevos_Archivos_Creados/RO.txt","w")
i=0
for Dato_RO in RO:
    if i == 0:
        Archivo_RO.writelines(str(round(Dato_RO,4)))
    else:
        Archivo_RO.writelines("\n"+str(round(Dato_RO,4)))
    i=i+1
Archivo_RO.close()
"""Calculando mSHELL"""
mSHELL = np.array([],dtype=float)
for Valor_FITR in FITR:
    Valor_mSHELL = 1.87+(0.019/Valor_FITR)
    mSHELL = np.append(mSHELL,Valor_mSHELL)
Archivo_mSHELL = open("Nuevos_Archivos_Creados/m_SHELL.txt","w")
i=0
for Dato_mSHELL in mSHELL:
    if i == 0:
        Archivo_mSHELL.writelines(str(round(Dato_mSHELL,4)))
    else:
        Archivo_mSHELL.writelines("\n"+str(round(Dato_mSHELL,4)))
    i=i+1
Archivo_mSHELL.close()
"""Calculando FR SHELL"""
FRSHELL = np.array([],dtype=float)
i=0
for ValormSHELL in mSHELL:
    Valor_FRSHELL = (FITR[i]**(-ValormSHELL))
    if str(Valor_FRSHELL) == 'inf':
        FRSHELL = np.append(FRSHELL,0)
    else:
        FRSHELL = np.append(FRSHELL,Valor_FRSHELL)
    i=i+1
Archivo_FRSHELL = open("Nuevos_Archivos_Creados/FRSHELL.txt","w")
i=0
for Dato_FRSHELL in FRSHELL:
    if i == 0:
        Archivo_FRSHELL.writelines(str(round(Dato_FRSHELL,4)))
    else:
        Archivo_FRSHELL.writelines("\n"+str(round(Dato_FRSHELL,4)))
    i=i+1
Archivo_FRSHELL.close()
"""Calculando error SHELL"""
Error_SHELL = np.array([],dtype=float)
i=0
for Valor_FRSHELL in FRSHELL:
    Valor_error = abs((FR[i]-Valor_FRSHELL)/FR[i])*100
    Error_SHELL = np.append(Error_SHELL,Valor_error)
    i=i+1
Archivo_Error_SHELL = open("Nuevos_Archivos_Creados/Error_SHELL.txt","w")
i=0
for Dato_Error_SHELL in Error_SHELL:
    if i == 0:
        Archivo_Error_SHELL.writelines(str(round(Dato_Error_SHELL,4)))
    else:
        Archivo_Error_SHELL.writelines("\n"+str(round(Dato_Error_SHELL,4)))
    i=i+1
Archivo_Error_SHELL.close()
"""Calculando m Borai"""
mBORAI = np.array([],dtype=float)
for Valor_FITR in FITR:
    Valor_mBORAI = 2.2 - (0.035/(Valor_FITR+0.042))
    mBORAI = np.append(mBORAI,Valor_mBORAI)
Archivo_mBORAI = open("Nuevos_Archivos_Creados/mBORAI.txt","w")
i=0
for Dato_mBORAI in mBORAI:
    if i == 0:
        Archivo_mBORAI.writelines(str(round(Dato_mBORAI,4)))
    else:
        Archivo_mBORAI.writelines("\n"+str(round(Dato_mBORAI,4)))
    i=i+1
Archivo_mBORAI.close()
"""Calculando FR BORAI"""
FRBORAI = np.array([],dtype=float)
i=0
for Valor_mBORAI in mBORAI:
    Valor_FRBORAI = (FITR[i]**-Valor_mBORAI)
    FRBORAI = np.append(FRBORAI,Valor_FRBORAI)
    i=i+1
Archivo_FRBORAI = open("Nuevos_Archivos_Creados/FRBORAI.txt","w")
i=0
for Dato_FRBORAI in FRBORAI:
    if i == 0:
        Archivo_FRBORAI.writelines(str(round(Dato_FRBORAI,4)))
    else:
        Archivo_FRBORAI.writelines("\n"+str(round(Dato_FRBORAI,4)))
    i=i+1
Archivo_FRBORAI.close()
"""Calculando error BORAI"""
Error_BORAI = np.array([],dtype=float)
i=0
for Valor_FRBORAI in FRBORAI:
    Valor_error = abs((FR[i]-Valor_FRBORAI)/FR[i])*100
    Error_BORAI = np.append(Error_BORAI,Valor_error)
    i=i+1
Archivo_Error_BORAI = open("Nuevos_Archivos_Creados/Error_BORAI.txt","w")
i=0
for Dato_Error_BORAI in Error_BORAI:
    if i == 0:
        Archivo_Error_BORAI.writelines(str(round(Dato_Error_BORAI,4)))
    else:
        Archivo_Error_BORAI.writelines("\n"+str(round(Dato_Error_BORAI,4)))
    i=i+1
Archivo_Error_BORAI.close()
"""Calculando Sw Archie Modificado"""
DLL=np.array([],dtype=float)
Archivo_ResistividadProfunda = open("Archivos_TXT/DLL.txt")
for Linea_ResistividadProfunda in Archivo_ResistividadProfunda.readlines():
    Nueva_Linea_ResistividadProfunda = Linea_ResistividadProfunda.rstrip('\n')
    Nueva_Linea_Convertida_ResistividadProfunda =  float(Nueva_Linea_ResistividadProfunda)
    DLL = np.append(DLL,Nueva_Linea_Convertida_ResistividadProfunda)
Archivo_ResistividadProfunda.close()
#
SW_modif = np.array([],dtype=float)
SHCS = np.array([],dtype=float)
i=0
for Valor_DLL in DLL:
    SW = ((Valor_DLL*(FITR[i]**m[i]))/(0.887*0.275))**(-1/1.76)
    Valor_SHCS = 1-SW
    SW_modif = np.append(SW_modif,SW)
    SHCS = np.append(SHCS,Valor_SHCS)
    i=i+1
#
Archivo_SW_modif = open("Nuevos_Archivos_Creados/SW_modif.txt","w")
i=0
for Dato_SW_modif in SW_modif:
    if i == 0:
        Archivo_SW_modif.writelines(str(round(Dato_SW_modif,4)))
    else:
        Archivo_SW_modif.writelines("\n"+str(round(Dato_SW_modif,4)))
    i=i+1
Archivo_SW_modif.close()
#
Archivo_SHCS = open("Nuevos_Archivos_Creados/SHCS.txt","w")
i=0
for Dato_SHCS in SHCS:
    if i == 0:
        Archivo_SHCS.writelines(str(round(Dato_SHCS,4)))
    else:
        Archivo_SHCS.writelines("\n"+str(round(Dato_SHCS,4)))
    i=i+1
Archivo_SHCS.close()
#
#
#
#
"""Calculando Indice de resistividad"""
IR = np.array([],dtype=float)
i=0
for Valor_DLL in DLL:
    Valor_IR = round((Valor_DLL/RO[i]),4)
    IR = np.append(IR,Valor_IR)
    i=i+1
Archivo_IR = open("Nuevos_Archivos_Creados/IR.txt","w")
i=0
for Dato_IR in IR:
    if i == 0:
        Archivo_IR.writelines(str(round(Dato_IR,4)))
    else:
        Archivo_IR.writelines("\n"+str(round(Dato_IR,4)))
    i=i+1
Archivo_IR.close()
"""Calculando Tortuosidades"""
T_FR = np.array([],dtype=float)
i=0
for Valor_FR in FR:
    Valor_T = round((Valor_FR*FITR[i]),4)
    T_FR = np.append(T_FR,Valor_T)
    i=i+1
Archivo_T_FR = open("Nuevos_Archivos_Creados/T_FR.txt","w")
i=0
for Dato_T_FR in T_FR:
    if i == 0:
        Archivo_T_FR.writelines(str(round(Dato_T_FR,4)))
    else:
        Archivo_T_FR.writelines("\n"+str(round(Dato_T_FR,4)))
    i=i+1
Archivo_T_FR.close()
#
T_m = np.array([],dtype=float)
i=0
for Valor_m in m:
    Valor_T = round(((FITR[i])**(-Valor_m+1)),4)
    T_m = np.append(T_m,Valor_T)
    i=i+1
Archivo_T_m = open("Nuevos_Archivos_Creados/T_m.txt","w")
i=0
for Dato_T_m in T_m:
    if i == 0:
        Archivo_T_m.writelines(str(round(Dato_T_m,4)))
    else:
        Archivo_T_m.writelines("\n"+str(round(Dato_T_m,4)))
    i=i+1
Archivo_T_m.close()
#
T_FIF = np.array([],dtype=float)
i=0
for Valor_FIF in FIF:
    Valor_T = round((1+(FIENT[i]/Valor_FIF)),4)
    T_FIF = np.append(T_FIF,Valor_T)
    i=i+1
Archivo_T_FIF = open("Nuevos_Archivos_Creados/T_FIF.txt","w")
i=0
for Dato_T_FIF in T_FIF:
    if i == 0:
        Archivo_T_FIF.writelines(str(round(Dato_T_FIF,4)))
    else:
        Archivo_T_FIF.writelines("\n"+str(round(Dato_T_FIF,4)))
    i=i+1
Archivo_T_FIF.close()
#
T_1 = np.array([],dtype=float)
for Valor_T_FIF in T_FIF:
    Valor_T = round((1/Valor_T_FIF),4)
    T_1 = np.append(T_1,Valor_T)
Archivo_T_1 = open("Nuevos_Archivos_Creados/T_1.txt","w")
i=0
for Dato_T_1 in T_1:
    if i == 0:
        Archivo_T_1.writelines(str(round(Dato_T_1,4)))
    else:
        Archivo_T_1.writelines("\n"+str(round(Dato_T_1,4)))
    i=i+1
Archivo_T_1.close()
"""Calculando r"""
r = np.array([],dtype=float)
i=0
for Valor_FR in FR:
    Valor_r = round(((math.log10((Valor_FR-1)/Valor_FR))/(math.log10(1-FITR[i]))),4)
    r = np.append(r,Valor_r)
    i=i+1
Archivo_r = open("Nuevos_Archivos_Creados/r.txt","w")
i=0
for Dato_r in r:
    if i == 0:
        Archivo_r.writelines(str(round(Dato_r,4)))
    else:
        Archivo_r.writelines("\n"+str(round(Dato_r,4)))
    i=i+1
Archivo_r.close()
"""Calculando COPAR-PIRSON"""
U = np.array([],dtype=float)
i=0
for Valor_FITR in FITR:
    Valor_U = round(((Valor_FITR - FIPR[i])/(Valor_FITR*(1-FIPR[i]))),4)
    U = np.append(U,Valor_U)
    i=i+1
Archivo_U = open("Nuevos_Archivos_Creados/U.txt","w")
i=0
for Dato_U in U:
    if i == 0:
        Archivo_U.writelines(str(round(Dato_U,4)))
    else:
        Archivo_U.writelines("\n"+str(round(Dato_U,4)))
    i=i+1
Archivo_U.close()
"""Calculando COPAR-CLASE"""
U_Clase = np.array([],dtype=float)
i=0
for Valor_FITR in FITR:
    Valor_U = round((FISR[i]/Valor_FITR),4)
    U_Clase = np.append(U_Clase,Valor_U)
    i=i+1
Archivo_U_Clase = open("Nuevos_Archivos_Creados/U_Clase.txt","w")
i=0
for Dato_U_Clase in U_Clase:
    if i == 0:
        Archivo_U_Clase.writelines(str(round(Dato_U_Clase,4)))
    else:
        Archivo_U_Clase.writelines("\n"+str(round(Dato_U_Clase,4)))
    i=i+1
Archivo_U_Clase.close()
"""Calculando FIFRAC - TAREK"""
FIFRAC = np.array([],dtype=float)
i=0
for Valor_FITR in FITR:
    Valor_FIFRAC = round((((Valor_FITR**(m[i]+1))-(Valor_FITR**m[i]))/((Valor_FITR**m[i])-1)),4)
    FIFRAC = np.append(FIFRAC,Valor_FIFRAC)
    i=i+1
Archivo_FIFRAC = open("Nuevos_Archivos_Creados/FIFRAC.txt","w")
i=0
for Dato_FIFRAC in FIFRAC:
    if i == 0:
        Archivo_FIFRAC.writelines(str(round(Dato_FIFRAC,4)))
    else:
        Archivo_FIFRAC.writelines("\n"+str(round(Dato_FIFRAC,4)))
    i=i+1
Archivo_FIFRAC.close()
"""Calculando FIMAT - TAREK"""
FIMAT = np.array([],dtype=float)
i=0
for Valor_FITR in FITR:
    Valor_FIMAT = round((((Valor_FITR**m[i])-Valor_FITR)/((Valor_FITR**m[i])-1)),4)
    FIMAT = np.append(FIMAT,Valor_FIMAT)
    i=i+1
Archivo_FIMAT = open("Nuevos_Archivos_Creados/FIMAT.txt","w")
i=0
for Dato_FIMAT in FIMAT:
    if i == 0:
        Archivo_FIMAT.writelines(str(round(Dato_FIMAT,4)))
    else:
        Archivo_FIMAT.writelines("\n"+str(round(Dato_FIMAT,4)))
    i=i+1
Archivo_FIMAT.close()
"""Calculando Indice de intensidad de Fracturamiento"""
IIF = np.array([],dtype=float)
i=0
for Valor_FITR in FITR:
    Valor_IIF = round(((Valor_FITR-FIPR[i])/(1-FIPR[i])),4)
    IIF = np.append(IIF,Valor_IIF)
    i=i+1
Archivo_IIF = open("Nuevos_Archivos_Creados/IIF.txt","w")
i=0
for Dato_IIF in IIF:
    if i == 0:
        Archivo_IIF.writelines(str(round(Dato_IIF,4)))
    else:
        Archivo_IIF.writelines("\n"+str(round(Dato_IIF,4)))
    i=i+1
Archivo_IIF.close()
"""Calculando Indice de almacenamiento de las fracturas"""
w = np.array([],dtype=float)
i=0
for Valor_FITR in FITR:
    Valor_w = round((((Valor_FITR**m[i])-(Valor_FITR**(m[i]-1)))/((Valor_FITR**m[i])-1)),4)
    w = np.append(w,Valor_w)
    i=i+1
Archivo_w = open("Nuevos_Archivos_Creados/w.txt","w")
i=0
for Dato_w in w:
    if i == 0:
        Archivo_w.writelines(str(round(Dato_w,4)))
    else:
        Archivo_w.writelines("\n"+str(round(Dato_w,4)))
    i=i+1
Archivo_w.close()
"""Calculando Indice de Permeabilidad"""
IK = np.array([],dtype=float)
i=0
for Valor_FITR in FITR:
    Valor_IK = round((84105*((Valor_FITR**(m[i]+2))/(1-(Valor_FITR**2)))),4)
    IK = np.append(IK,Valor_IK)
    i=i+1
Archivo_IK = open("Nuevos_Archivos_Creados/IK.txt","w")
i=0
for Dato_IK in IK:
    if i == 0:
        Archivo_IK.writelines(str(round(Dato_IK,4)))
    else:
        Archivo_IK.writelines("\n"+str(round(Dato_IK,4)))
    i=i+1
Archivo_IK.close()