# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 19:49:38 2018
@author: Jhonatan
"""
import numpy as np
import math as math
"""Importar LLS"""
LLS = np.array([],dtype=float)
Archivo_LLS = open("Archivos_TXT/LLS.txt")
for Linea_LLS in Archivo_LLS.readlines():
    Nueva_Linea_LLS = Linea_LLS.rstrip('\n')
    Nueva_Linea_Convertida_LLS = float(Nueva_Linea_LLS)
    LLS = np.append(LLS,Nueva_Linea_Convertida_LLS)
Archivo_LLS.close()

"""Calculando b"""
b = np.array([],dtype=float)
for valor_FIF in FIF:
    valor_b = (1-valor_FIF)**(1/3)
    b = np.append(b,valor_b)

Archivo_b = open("Nuevos_Archivos_Creados/Archivos_Finales/b.txt","w")
i=0
for Dato_b in b:
    if i == 0:
        Archivo_b.writelines(str(round(Dato_b,4)))
    else:
        Archivo_b.writelines("\n"+str(round(Dato_b,4)))
    i=i+1
Archivo_b.close()

"""Calculando Columna DLL/LLS"""
i=0
DLL_LLS = np.array([],dtype=float)
for valor_LLS in LLS:
    valor_div = DLL[i]/valor_LLS
    DLL_LLS = np.append(DLL_LLS,valor_div)
    i=i+1
Archivo_DLL_LLS = open("Nuevos_Archivos_Creados/Archivos_Finales/DLL_LLS.txt","w")
i=0
for Dato_DLL_LLS in DLL_LLS:
    if i == 0:
        Archivo_DLL_LLS.writelines(str(round(Dato_DLL_LLS,4)))
    else:
        Archivo_DLL_LLS.writelines("\n"+str(round(Dato_DLL_LLS,4)))
    i=i+1
Archivo_DLL_LLS.close()

"""Calculando TSPRASMUS"""


"""Calculando log a"""
A = 2.03 #"""Por tratarse de Carbonatos"""
B = 0.9 #"""Por tratarse de Carbonatos"""
log_a = np.array([],dtype=float)
i=0
for valor_FITR in FITR:
    valor_log_a = (A*(math.log10(valor_FITR))+(math.log10(FR[i])))/(1+(B*(math.log10(valor_FITR))))
    log_a = np.append(log_a,valor_log_a)
    i=i+1
Archivo_log_a = open("Nuevos_Archivos_Creados/Archivos_Finales/log_a.txt","w")
i=0
for Dato_log_a in log_a:
    if i == 0:
        Archivo_log_a.writelines(str(round(Dato_log_a,4)))
    else:
        Archivo_log_a.writelines("\n"+str(round(Dato_log_a,4)))
    i=i+1
Archivo_log_a.close()

"""Calculando mORG"""
mORG = np.array([],dtype=float)
for valor_log_a in log_a:
    m_org = A-(B*valor_log_a)
    mORG = np.append(mORG,m_org)
Archivo_mORG = open("Nuevos_Archivos_Creados/Archivos_Finales/mORG.txt","w")
i=0
for Dato_mORG in mORG:
    if i == 0:
        Archivo_mORG.writelines(str(round(Dato_mORG,4)))
    else:
        Archivo_mORG.writelines("\n"+str(round(Dato_mORG,4)))
    i=i+1
Archivo_mORG.close()

"""Calculando TSPOGR"""
"""Calculando FIZ"""
FIZ = np.array([],dtype=float)
for valor_FITR in FITR:
    valor_FIZ = valor_FITR/(1-valor_FITR)
    FIZ = np.append(FIZ,valor_FIZ)
Archivo_FIZ = open("Nuevos_Archivos_Creados/Archivos_Finales/FIZ.txt","w")
i=0
for Dato_FIZ in FIZ:
    if i == 0:
        Archivo_FIZ.writelines(str(round(Dato_FIZ,4)))
    else:
        Archivo_FIZ.writelines("\n"+str(round(Dato_FIZ,4)))
    i=i+1
Archivo_FIZ.close()

"""Calculando rp35"""
rp35 = np.array([],dtype=float)
i=0
for valor_FITR in FITR:
    valor_rp35 = (2.66*(IK[i]/(valor_FITR*100))**0.45)
    rp35 = np.append(rp35,valor_rp35)
    i=i+1
Archivo_rp35 = open("Nuevos_Archivos_Creados/Archivos_Finales/rp35.txt","w")
i=0
for Dato_rp35 in rp35:
    if i == 0:
        Archivo_rp35.writelines(str(round(Dato_rp35,4)))
    else:
        Archivo_rp35.writelines("\n"+str(round(Dato_rp35,4)))
    i=i+1
Archivo_rp35.close()

"""TGP"""
TGP = np.array([],dtype=str)
for valor_rp35 in rp35:
    if valor_rp35 < .5:
        TGP = np.append(TGP,"NANO")
    elif valor_rp35 >= .5 and valor_rp35 < 2:
        TGP = np.append(TGP,"MICRO")
    elif valor_rp35 >= 2 and valor_rp35 < 4:
        TGP = np.append(TGP,"MESO")
    elif valor_rp35 >= 4 and valor_rp35 < 10:
        TGP = np.append(TGP,"MACRO")
    elif valor_rp35 >= 10:
        TGP = np.append(TGP,"MEGA")
Archivo_TGP = open("Nuevos_Archivos_Creados/Archivos_Finales/TGP.txt","w")
i=0
for Dato_TGP in TGP:
    if i == 0:
        Archivo_TGP.writelines(str(Dato_TGP))
    else:
        Archivo_TGP.writelines("\n"+str(Dato_TGP))
    i=i+1
Archivo_TGP.close()

"""ICY"""
ICY = np.array([],dtype=float)
i=0
for valor_FITR in FITR:
    valor_ICY = 0.0314*(math.sqrt(IK[i]/valor_FITR))
    ICY = np.append(ICY,valor_ICY)
    i=i+1

Archivo_ICY = open("Nuevos_Archivos_Creados/Archivos_Finales/ICY.txt","w")
i=0
for Dato_ICY in ICY:
    if i == 0:
        Archivo_ICY.writelines(str(round(Dato_ICY,4)))
    else:
        Archivo_ICY.writelines("\n"+str(round(Dato_ICY,4)))
    i=i+1
Archivo_ICY.close()

"""IZF"""
IZF = np.array([],dtype=float)
i=0
for valor_FIZ in FIZ:
    valor_IZF = ICY[i]/valor_FIZ
    IZF = np.append(IZF,valor_IZF)
    i=i+1

Archivo_IZF = open("Nuevos_Archivos_Creados/Archivos_Finales/IZF.txt","w")
i=0
for Dato_IZF in IZF:
    if i == 0:
        Archivo_IZF.writelines(str(round(Dato_IZF,4)))
    else:
        Archivo_IZF.writelines("\n"+str(round(Dato_IZF,4)))
    i=i+1
Archivo_IZF.close()

"""Calculando IRE"""
IRE = np.array([],dtype=float)
i=0
for valor_FITR in FITR:
    valor_IRE = math.sqrt(valor_FITR/FR[i])
    IRE = np.append(IRE,valor_IRE)
    i=i+1

Archivo_IRE = open("Nuevos_Archivos_Creados/Archivos_Finales/IRE.txt","w")
i=0
for Dato_IRE in IRE:
    if i == 0:
        Archivo_IRE.writelines(str(round(Dato_IRE,4)))
    else:
        Archivo_IRE.writelines("\n"+str(round(Dato_IRE,4)))
    i=i+1
Archivo_IRE.close()

"""Calculando IZC"""
IZC = np.array([],dtype=float)
i=0
for valor_IRE in IRE:
    valor_IZC = valor_IRE/FIZ[i]
    IZC = np.append(IZC,valor_IZC)
    i=i+1

Archivo_IZC = open("Nuevos_Archivos_Creados/Archivos_Finales/IZC.txt","w")
i=0
for Dato_IZC in IZC:
    if i == 0:
        Archivo_IZC.writelines(str(round(Dato_IZC,4)))
    else:
        Archivo_IZC.writelines("\n"+str(round(Dato_IZC,4)))
    i=i+1
Archivo_IZC.close()

"""Calculando CKC"""
CKC = np.array([],dtype=float)
i=0
for valor_T_FR in T_FR:
    valor_CKC = valor_T_FR*m[i]
    CKC = np.append(CKC,valor_CKC)
    i=i+1

Archivo_CKC = open("Nuevos_Archivos_Creados/Archivos_Finales/CKC.txt","w")
i=0
for Dato_CKC in CKC:
    if i == 0:
        Archivo_CKC.writelines(str(round(Dato_CKC,4)))
    else:
        Archivo_CKC.writelines("\n"+str(round(Dato_CKC,4)))
    i=i+1
Archivo_CKC.close()

"""Calculando Sp"""
SpH = np.array([],dtype=float)
i=0
for v_FITR in FITR:
    v_SP_Hil = (44600000000/((FR[i]**2.2)*(v_FITR**1.2)*(IK[i])))**(1/2)
    SpH = np.append(SpH,v_SP_Hil)
    i=i+1

Archivo_SpHilmi = open("Nuevos_Archivos_Creados/Archivos_Finales/Sp.txt","w")
i=0
for Dato_SpHilmi in SpH:
    if i == 0:
        Archivo_SpHilmi.writelines(str(round(Dato_SpHilmi,4)))
    else:
        Archivo_SpHilmi.writelines("\n"+str(round(Dato_SpHilmi,4)))
    i=i+1
Archivo_SpHilmi.close()

"""Calculando GS - Tamaño de Grano"""
GS  = np.array([],dtype=float)
i=0
for v_FITR in FITR:
    v_GS = (6*(1-v_FITR))/(SpH[i])
    GS = np.append(GS,v_GS)
    i=i+1
    
Archivo_GS = open("Nuevos_Archivos_Creados/Archivos_Finales/GS.txt","w")
i=0
for Dato_GS in GS:
    if i == 0:
        Archivo_GS.writelines(str(round(Dato_GS,4)))
    else:
        Archivo_GS.writelines("\n"+str(round(Dato_GS,4)))
    i=i+1
Archivo_GS.close()

"""Calculando TFORM"""
"""Obtener datos de Profundidad"""
Profundidad = np.array([],dtype=float)
Archivo_Profundidad = open("Archivos_TXT/Profundidad.txt")
for Linea_Profundidad in Archivo_Profundidad.readlines():
    Nueva_Linea_Profundidad = Linea_Profundidad.rstrip('\n')
    Nueva_Linea_Convertida_Profundidad = float(Nueva_Linea_Profundidad)
    Profundidad = np.append(Profundidad,Nueva_Linea_Convertida_Profundidad)
Archivo_Profundidad.close()
Tem_Sup = 84
T_MAX = 280
P_max = 4000
TFORM = np.array([],dtype=float)

for v_Prof in Profundidad:
    v_TFORM = (((T_MAX-Tem_Sup)/P_max)*v_Prof)+Tem_Sup
    TFORM = np.append(TFORM,v_TFORM)

Archivo_TFORM = open("Nuevos_Archivos_Creados/Archivos_Finales/TFORM.txt","w")
i=0
for Dato_TFORM in TFORM:
    if i == 0:
        Archivo_TFORM.writelines(str(round(Dato_TFORM,4)))
    else:
        Archivo_TFORM.writelines("\n"+str(round(Dato_TFORM,4)))
    i=i+1
Archivo_TFORM.close()

"""RW Variable"""
Rw_sup = .275
VX = 10**(-.3404*math.log10(Rw_sup)+.6414)
Rw_var = np.array([],dtype=float)
for v_TFORM in TFORM:
    v_RW = (Rw_sup*(Tem_Sup+VX))/(v_TFORM+VX)
    Rw_var = np.append(Rw_var,v_RW)

Archivo_RwVAR = open("Nuevos_Archivos_Creados/Archivos_Finales/Rw_var.txt","w")
i=0
for Dato_RwVAR in Rw_var:
    if i == 0:
        Archivo_RwVAR.writelines(str(round(Dato_RwVAR,4)))
    else:
        Archivo_RwVAR.writelines("\n"+str(round(Dato_RwVAR,4)))
    i=i+1
Archivo_RwVAR.close()

"""Calculando nOGR"""
nORG = np.array([],dtype=float)
i=0
for v_IK in IK:
    v_n = 0.904 - (0.515*math.log10(Rw_var[i])) + (0.325*math.log10(v_IK))
    nORG = np.append(nORG,v_n)
    i = i +1

Archivo_nORG = open("Nuevos_Archivos_Creados/Archivos_Finales/nORG.txt","w")
i=0
for Dato_nORG in nORG:
    if i == 0:
        Archivo_nORG.writelines(str(round(Dato_nORG,4)))
    else:
        Archivo_nORG.writelines("\n"+str(round(Dato_nORG,4)))
    i=i+1
Archivo_nORG.close()

"""Calculando Sw_mdif2 y SHCS_modif2"""
Sw_modif2 = np.array([],dtype=float)
SHCS_modif2 = np.array([],dtype=float)
i=0
for vFITR in FITR:
    vSW = ((DLL[i]*(vFITR**m[i]))/(.887*Rw_var[i]))**(-1/nORG[i])
    vSHC = 1-vSW
    Sw_modif2 = np.append(Sw_modif2,vSW)
    SHCS_modif2 = np.append(SHCS_modif2,vSHC)
    i=i+1
    
Archivo_SwModf = open("Nuevos_Archivos_Creados/Archivos_Finales/Sw_modif2.txt","w")
i=0
for Dato_SwModf in Sw_modif2:
    if i == 0:
        Archivo_SwModf.writelines(str(round(Dato_SwModf,4)))
    else:
        Archivo_SwModf.writelines("\n"+str(round(Dato_SwModf,4)))
    i=i+1
Archivo_SwModf.close()

Archivo_SHCS_modif2 = open("Nuevos_Archivos_Creados/Archivos_Finales/SHCS_modif2.txt","w")
i=0
for Dato_SHCS_modif2 in SHCS_modif2:
    if i == 0:
        Archivo_SHCS_modif2.writelines(str(round(Dato_SHCS_modif2,4)))
    else:
        Archivo_SHCS_modif2.writelines("\n"+str(round(Dato_SHCS_modif2,4)))
    i=i+1
Archivo_SHCS_modif2.close()

"""Calculando SwDOBLEAGUA"""
SwIndonesia = np.array([],dtype=float)
SHCSIndonesia = np.array([],dtype=float)
Rcl = 5
i=0
for vFITR in FITR:
    vSW = ((1/math.sqrt(DLL[i]))*((math.sqrt((vFITR**m[i])/(.887*Rw_var[i])))+((VLUTR[i]**((1-VLUTR[i])/2))/math.sqrt(Rcl))))**(2/nORG[i])
    vSHC = 1-vSW
    SwIndonesia = np.append(SwIndonesia,vSW)
    SHCSIndonesia = np.append(SHCSIndonesia,vSHC)
    i=i+1

Archivo_SWIND = open("Nuevos_Archivos_Creados/Archivos_Finales/SwIndonesia.txt","w")
i=0
for Dato_SWIND in SwIndonesia:
    if i == 0:
        Archivo_SWIND.writelines(str(round(Dato_SWIND,4)))
    else:
        Archivo_SWIND.writelines("\n"+str(round(Dato_SWIND,4)))
    i=i+1
Archivo_SWIND.close()

Archivo_SHCIND = open("Nuevos_Archivos_Creados/Archivos_Finales/SHCIndonesia.txt","w")
i=0
for Dato_SHCIND in SHCSIndonesia:
    if i == 0:
        Archivo_SHCIND.writelines(str(round(Dato_SHCIND,4)))
    else:
        Archivo_SHCIND.writelines("\n"+str(round(Dato_SHCIND,4)))
    i=i+1
Archivo_SHCIND.close()

"""Porosidad Fracturamiento RASMUS"""
FIFRAC_RASMUS = np.array([],dtype=float)
i=0
for vFITR in FITR:
    vFIFRAC = ((+2*vFITR+(vFITR**2)-1) + math.sqrt((((-2*vFITR-(vFITR**2)+1)**2)+(4*(1+2*vFITR)*((1/FR[i])-vFITR**2)))))/(2*(1+2*vFITR))
    FIFRAC_RASMUS = np.append(FIFRAC_RASMUS,vFIFRAC)
    i=i+1

Archivo_FIFRAC_RASMUS = open("Nuevos_Archivos_Creados/Archivos_Finales/FIFRAC_RASMUS.txt","w")
i=0
for Dato_FIFRAC_RASMUS in FIFRAC_RASMUS:
    if i == 0:
        Archivo_FIFRAC_RASMUS.writelines(str(round(Dato_FIFRAC_RASMUS,4)))
    else:
        Archivo_FIFRAC_RASMUS.writelines("\n"+str(round(Dato_FIFRAC_RASMUS,4)))
    i=i+1
Archivo_FIFRAC_RASMUS.close()

"""mb SURO RAMOS"""
mb_SURORAMOS = np.array([],dtype=float)
i=0
for vFITR in FITR:
    if vFITR <= 0.06:
        vmb = 0.7*((-1/2)*((vFITR**3)/(.06**3))*(3/2)*(vFITR/.06))+1.5
    elif vFITR > 0.06:
        vmb = 2.2*((-1/2)*((vFITR**3)/(.06**3))*(3/2)*(vFITR/.06))+1.5
    mb_SURORAMOS = np.append(mb_SURORAMOS,vmb)

Archivo_mb_SURORAMOS = open("Nuevos_Archivos_Creados/Archivos_Finales/mb_SURORAMOS.txt","w")
i=0
for Dato_mb_SURORAMOS in mb_SURORAMOS:
    if i == 0:
        Archivo_mb_SURORAMOS.writelines(str(round(Dato_mb_SURORAMOS,4)))
    else:
        Archivo_mb_SURORAMOS.writelines("\n"+str(round(Dato_mb_SURORAMOS,4)))
    i=i+1
Archivo_mb_SURORAMOS.close()

"""FIMAT SURO-RAMOS"""
FIMAT_SURO = np.array([],dtype=float)
i=0
for vFITR in FITR:
    vFIB = (-(1-(vFITR**-m[i]))-math.sqrt(((1-(vFITR**-m[i]))**2)-4*((vFITR**-m[i])-(vFITR**(1-m[i])))*((vFITR**(1-m[i]))-1)))/(2*((vFITR**-m[i])-(vFITR**(1-m[i]))))
    FIMAT_SURO = np.append(FIMAT_SURO,vFIB)
    i=i+1

Archivo_FIMAT_SURO = open("Nuevos_Archivos_Creados/Archivos_Finales/FIMAT_SURO.txt","w")
i=0
for Dato_FIMAT_SURO in FIMAT_SURO:
    if i == 0:
        Archivo_FIMAT_SURO.writelines(str(round(Dato_FIMAT_SURO,4)))
    else:
        Archivo_FIMAT_SURO.writelines("\n"+str(round(Dato_FIMAT_SURO,4)))
    i=i+1
Archivo_FIMAT_SURO.close()

"""FIVUG_SURO"""
FIVUG_SURO = np.array([],dtype=float)
i=0
for vFITR in FITR:
    vFIV = vFITR - FIMAT_SURO[i]
    FIVUG_SURO = np.append(FIVUG_SURO,vFIV)
    i=i+1
    
Archivo_FIVUG_SURO = open("Nuevos_Archivos_Creados/Archivos_Finales/FIVUG_SURO.txt","w")
i=0
for Dato_FIVUG_SURO in FIVUG_SURO:
    if i == 0:
        Archivo_FIVUG_SURO.writelines(str(round(Dato_FIVUG_SURO,4)))
    else:
        Archivo_FIVUG_SURO.writelines("\n"+str(round(Dato_FIVUG_SURO,4)))
    i=i+1
Archivo_FIVUG_SURO.close()    

"""QV INTERCAMBIO CATIÓNICO"""
QV = np.array([],dtype=float)
i=0
for vFITR in FITR:
    vQV = 10**(2.28*math.log10(FR[i])+7.476*vFITR+3.14*vFITR*math.log10(FR[i])-6.245)
    QV = np.append(QV,vQV)
    i=i+1

Archivo_QV = open("Nuevos_Archivos_Creados/Archivos_Finales/QV.txt","w")
i=0
for Dato_QV in QV:
    if i == 0:
        Archivo_QV.writelines(str(round(Dato_QV,4)))
    else:
        Archivo_QV.writelines("\n"+str(round(Dato_QV,4)))
    i=i+1
Archivo_QV.close()  

"""FR DOBLE AGUA"""
FR2AGUA = np.array([],dtype=float)
i=0
vhq = 0.3
for vQV in QV:
    vFR2W = FR[i]*(1-(vhq*vQV))
    FR2AGUA = np.append(FR2AGUA,vFR2W)
    i=i+1
    
Archivo_FR2AGUA = open("Nuevos_Archivos_Creados/Archivos_Finales/FR2AGUA.txt","w")
i=0
for Dato_FR2AGUA in FR2AGUA:
    if i == 0:
        Archivo_FR2AGUA.writelines(str(round(Dato_FR2AGUA,4)))
    else:
        Archivo_FR2AGUA.writelines("\n"+str(round(Dato_FR2AGUA,4)))
    i=i+1
Archivo_FR2AGUA.close()  

"""RE"""
Re_radio = np.array([],dtype=float)
i=0
for vFITR in FITR:
    vRe = math.sqrt(IK[i]/(125*(vFITR**m[i])))
    Re_radio = np.append(Re_radio,vRe)
    i=i+1

Archivo_Re_radio = open("Nuevos_Archivos_Creados/Archivos_Finales/Re_radio.txt","w")
i=0
for Dato_Re_radio in Re_radio:
    if i == 0:
        Archivo_Re_radio.writelines(str(round(Dato_Re_radio,4)))
    else:
        Archivo_Re_radio.writelines("\n"+str(round(Dato_Re_radio,4)))
    i=i+1
Archivo_Re_radio.close()  
