# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 18:05:29 2018
@author: Jhonatan
"""
import numpy as np
from scipy import linalg
NPHIf = MUD[2]
DENf = MUD[1]
DTf = MUD[0]
""" Mineral = [DTma,DENma,DENneutron,M,N]"""
VDOL = np.array([],dtype=float)
VCAL = np.array([],dtype=float)
VSIL = np.array([],dtype=float)
VLUT = np.array([],dtype=float)
VANH = np.array([],dtype=float)
VYES = np.array([],dtype=float)
VSAL = np.array([],dtype=float)
FIP = np.array([],dtype=float)
FIS = np.array([],dtype=float)

"""Porosidad Primaria y Secundaria"""
i = 0
for tipo_porosidad in Tipo_Porosidad:
    if str(tipo_porosidad) == "FIS" and str(region_final[i]) == "R1":
        DTL = DT[i]
        NPHIL = NPHI[i]
        DENL = RHOB[i]
        DT1 = DOL[0]
        DT2 = CAL[0]
        NPHI1 = DOL[2]
        NPHI2 = CAL[2]
        DEN1 = DOL[1]
        DEN2 = CAL[1]
        Variables_Ecuacion_2 = np.array([[DTf,45.55,DT1,DT2],[NPHIf,NPHIf,NPHI1,NPHI2],[DENf,DENf,DEN1,DEN2],[1,1,1,1]])
        Resultados_Ecuacion_2 = np.array([DTL,NPHIL,DENL,1])
        Soluciones_Sistema_2 = np.linalg.solve(Variables_Ecuacion_2,Resultados_Ecuacion_2)
        FIP = np.append(FIP,Soluciones_Sistema_2[0])
        FIS = np.append(FIS,Soluciones_Sistema_2[1])
        VDOL = np.append(VDOL,Soluciones_Sistema_2[2])
        VCAL = np.append(VCAL,Soluciones_Sistema_2[3])
        VSIL = np.append(VSIL,0)
        VLUT = np.append(VLUT,0)
        VANH = np.append(VANH,0)
        VYES = np.append(VYES,0)
        VSAL = np.append(VSAL,0)
    elif str(tipo_porosidad) == "FIS" and str(region_final[i]) == "R2":
        DTL = DT[i]
        NPHIL = NPHI[i]
        DENL = RHOB[i]
        DT1 = CAL[0]
        DT2 = SIL[0]
        NPHI1 = CAL[2]
        NPHI2 = SIL[2]
        DEN1 = CAL[1]
        DEN2 = SIL[1]
        Variables_Ecuacion_1 = np.array([[DTf,51.55,DT1,DT2],[NPHIf,NPHIf,NPHI1,NPHI2],[DENf,DENf,DEN1,DEN2],[1,1,1,1]])
        Resultados_Ecuacion_1 = np.array([DTL,NPHIL,DENL,1])
        Soluciones_Sistema_1 = np.linalg.solve(Variables_Ecuacion_1,Resultados_Ecuacion_1)
        FIP = np.append(FIP,Soluciones_Sistema_1[0])
        FIS = np.append(FIS,Soluciones_Sistema_1[1])
        VCAL = np.append(VCAL,Soluciones_Sistema_1[2])
        VSIL = np.append(VSIL,Soluciones_Sistema_1[3])
        VDOL = np.append(VDOL,0)
        VLUT = np.append(VLUT,0)
        VANH = np.append(VANH,0)
        VYES = np.append(VYES,0)
        VSAL = np.append(VSAL,0)
    elif str(tipo_porosidad) == "FIP" and str(region_final[i]) == "YES-DOL-ANH":
        DTL = DT[i]
        NPHIL = NPHI[i]
        DENL = RHOB[i]
        DT1 = YES[0]
        DT2 = DOL[0]
        DT3 = ANH[0]
        NPHI1 = YES[2]
        NPHI2 = DOL[2]
        NPHI3 = ANH[2]
        DEN1 = YES[1]
        DEN2 = DOL[1]
        DEN3 = ANH[1]
        Variables_Ecuacion = np.array([[DTf,DT1,DT2,DT3],[NPHIf,NPHI1,NPHI2,NPHI3],[DENf,DEN1,DEN2,DEN3],[1,1,1,1]])
        Resultados_Ecuacion = np.array([DTL,NPHIL,DENL,1])
        Soluciones_Sistema = np.linalg.solve(Variables_Ecuacion,Resultados_Ecuacion)
        FIP = np.append(FIP,Soluciones_Sistema[0])
        VYES = np.append(VYES,Soluciones_Sistema[1])
        VDOL = np.append(VDOL,Soluciones_Sistema[2])
        VANH = np.append(VANH,Soluciones_Sistema[3])
        VCAL = np.append(VCAL,0)
        VSIL = np.append(VSIL,0)
        VLUT = np.append(VLUT,0)
        VSAL = np.append(VSAL,0)
        FIS = np.append(FIS,0)
    elif str(tipo_porosidad) == "FIP" and str(region_final[i]) == "ANH-DOL-LUT":
        DTL = DT[i]
        NPHIL = NPHI[i]
        DENL = RHOB[i]
        DT1 = ANH[0]
        DT2 = DOL[0]
        DT3 = LUT[0]
        NPHI1 = ANH[2]
        NPHI2 = DOL[2]
        NPHI3 = LUT[2]
        DEN1 = ANH[1]
        DEN2 = DOL[1]
        DEN3 = LUT[1]
        Variables_Ecuacion = np.array([[DTf,DT1,DT2,DT3],[NPHIf,NPHI1,NPHI2,NPHI3],[DENf,DEN1,DEN2,DEN3],[1,1,1,1]])
        Resultados_Ecuacion = np.array([DTL,NPHIL,DENL,1])
        Soluciones_Sistema = np.linalg.solve(Variables_Ecuacion,Resultados_Ecuacion)
        FIP = np.append(FIP,Soluciones_Sistema[0])
        VANH = np.append(VANH,Soluciones_Sistema[1])
        VDOL = np.append(VDOL,Soluciones_Sistema[2])
        VLUT = np.append(VLUT,Soluciones_Sistema[3])
        VCAL = np.append(VCAL,0)
        VSIL = np.append(VSIL,0)
        VYES = np.append(VYES,0)
        VSAL = np.append(VSAL,0)
        FIS = np.append(FIS,0)
        """---------------------------------------------------------------------------------------------"""
    elif str(tipo_porosidad) == "FIP" and str(region_final[i]) == "SIL-SAL-LUT":
        DTL = DT[i]
        NPHIL = NPHI[i]
        DENL = RHOB[i]
        DT1 = SIL[0]
        DT2 = SAL[0]
        DT3 = LUT[0]
        NPHI1 = SIL[2]
        NPHI2 = SAL[2]
        NPHI3 = LUT[2]
        DEN1 = SIL[1]
        DEN2 = SAL[1]
        DEN3 = LUT[1]
        Variables_Ecuacion = np.array([[DTf,DT1,DT2,DT3],[NPHIf,NPHI1,NPHI2,NPHI3],[DENf,DEN1,DEN2,DEN3],[1,1,1,1]])
        Resultados_Ecuacion = np.array([DTL,NPHIL,DENL,1])
        Soluciones_Sistema = np.linalg.solve(Variables_Ecuacion,Resultados_Ecuacion)
        FIP = np.append(FIP,Soluciones_Sistema[0])
        VSIL = np.append(VSIL,Soluciones_Sistema[1])
        VSAL = np.append(VSAL,Soluciones_Sistema[2])
        VLUT = np.append(VLUT,Soluciones_Sistema[3])
        VDOL = np.append(VDOL,0)
        VCAL = np.append(VCAL,0)
        VANH = np.append(VANH,0)
        VYES = np.append(VYES,0)
        FIS = np.append(FIS,0)
    elif str(tipo_porosidad) == "FIP" and str(region_final[i]) == "DOL-SIL-LUT":
        DTL = DT[i]
        NPHIL = NPHI[i]
        DENL = RHOB[i]
        DT1 = DOL[0]
        DT2 = SIL[0]
        DT3 = LUT[0]
        NPHI1 = DOL[2]
        NPHI2 = SIL[2]
        NPHI3 = LUT[2]
        DEN1 = DOL[1]
        DEN2 = SIL[1]
        DEN3 = LUT[1]
        Variables_Ecuacion = np.array([[DTf,DT1,DT2,DT3],[NPHIf,NPHI1,NPHI2,NPHI3],[DENf,DEN1,DEN2,DEN3],[1,1,1,1]])
        Resultados_Ecuacion = np.array([DTL,NPHIL,DENL,1])
        Soluciones_Sistema = np.linalg.solve(Variables_Ecuacion,Resultados_Ecuacion)
        FIP = np.append(FIP,Soluciones_Sistema[0])
        VDOL = np.append(VDOL,Soluciones_Sistema[1])
        VSIL = np.append(VSIL,Soluciones_Sistema[2])
        VLUT = np.append(VLUT,Soluciones_Sistema[3])
        VCAL = np.append(VCAL,0)
        VANH = np.append(VANH,0)
        VYES = np.append(VYES,0)
        VSAL = np.append(VSAL,0)
        FIS = np.append(FIS,0)
    elif str(tipo_porosidad) == "FIP" and str(region_final[i]) == "DOL-CAL-SIL":
        DTL = DT[i]
        NPHIL = NPHI[i]
        DENL = RHOB[i]
        DT1 = DOL[0]
        DT2 = CAL[0]
        DT3 = SIL[0]
        NPHI1 = DOL[2]
        NPHI2 = CAL[2]
        NPHI3 = SIL[2]
        DEN1 = DOL[1]
        DEN2 = CAL[1]
        DEN3 = SIL[1]
        Variables_Ecuacion = np.array([[DTf,DT1,DT2,DT3],[NPHIf,NPHI1,NPHI2,NPHI3],[DENf,DEN1,DEN2,DEN3],[1,1,1,1]])
        Resultados_Ecuacion = np.array([DTL,NPHIL,DENL,1])
        Soluciones_Sistema = np.linalg.solve(Variables_Ecuacion,Resultados_Ecuacion)
        FIP = np.append(FIP,Soluciones_Sistema[0])
        VDOL = np.append(VDOL,Soluciones_Sistema[1])
        VCAL = np.append(VCAL,Soluciones_Sistema[2])
        VSIL = np.append(VSIL,Soluciones_Sistema[3])
        VLUT = np.append(VLUT,0)
        VANH = np.append(VANH,0)
        VYES = np.append(VYES,0)
        VSAL = np.append(VSAL,0)
        FIS = np.append(FIS,0)
    else:
        VDOL = np.append(VDOL,0)
        VCAL = np.append(VCAL,0)
        VSIL = np.append(VSIL,0)
        VLUT = np.append(VLUT,0)
        VANH = np.append(VANH,0)
        VYES = np.append(VYES,0)
        VSAL = np.append(VSAL,0)
        FIP = np.append(FIP,0)
        FIS = np.append(FIS,0)
        print("error")
    i=i+1
"""Guardar Archivos"""
Archivo_VDOL = open("Nuevos_Archivos_Creados/Volumen/VDOL.txt","w")
i=0
for Dato_VDOL in VDOL:
    if i == 0:
        Archivo_VDOL.writelines(str(round(Dato_VDOL,4)))
    else:
        Archivo_VDOL.writelines("\n"+str(round(Dato_VDOL,4)))
    i=i+1
Archivo_VDOL.close()
#
Archivo_VCAL = open("Nuevos_Archivos_Creados/Volumen/VCAL.txt","w")
i=0
for Dato_VCAL in VCAL:
    if i == 0:
        Archivo_VCAL.writelines(str(round(Dato_VCAL,4)))
    else:
        Archivo_VCAL.writelines("\n"+str(round(Dato_VCAL,4)))
    i=i+1
Archivo_VCAL.close()
#
Archivo_VSIL = open("Nuevos_Archivos_Creados/Volumen/VSIL.txt","w")
i=0
for Dato_VSIL in VSIL:
    if i == 0:
        Archivo_VSIL.writelines(str(round(Dato_VSIL,4)))
    else:
        Archivo_VSIL.writelines("\n"+str(round(Dato_VSIL,4)))
    i=i+1
Archivo_VSIL.close()
#
Archivo_VLUT = open("Nuevos_Archivos_Creados/Volumen/VLUT.txt","w")
i=0
for Dato_VLUT in VLUT:
    if i == 0:
        Archivo_VLUT.writelines(str(round(Dato_VLUT,4)))
    else:
        Archivo_VLUT.writelines("\n"+str(round(Dato_VLUT,4)))
    i=i+1
Archivo_VLUT.close()
#
Archivo_VANH = open("Nuevos_Archivos_Creados/Volumen/VANH.txt","w")
i=0
for Dato_VANH in VANH:
    if i == 0:
        Archivo_VANH.writelines(str(round(Dato_VANH,4)))
    else:
        Archivo_VANH.writelines("\n"+str(round(Dato_VANH,4)))
    i=i+1
Archivo_VANH.close()
#
Archivo_VYES = open("Nuevos_Archivos_Creados/Volumen/VYES.txt","w")
i=0
for Dato_VYES in VYES:
    if i == 0:
        Archivo_VYES.writelines(str(round(Dato_VYES,4)))
    else:
        Archivo_VYES.writelines("\n"+str(round(Dato_VYES,4)))
    i=i+1
Archivo_VYES.close()
#
Archivo_VSAL = open("Nuevos_Archivos_Creados/Volumen/VSAL.txt","w")
i=0
for Dato_VSAL in VSAL:
    if i == 0:
        Archivo_VSAL.writelines(str(round(Dato_VSAL,4)))
    else:
        Archivo_VSAL.writelines("\n"+str(round(Dato_VSAL,4)))
    i=i+1
Archivo_VSAL.close()
#
Archivo_FIP = open("Nuevos_Archivos_Creados/Volumen/FIP.txt","w")
i=0
for Dato_FIP in FIP:
    if i == 0:
        Archivo_FIP.writelines(str(round(Dato_FIP,4)))
    else:
        Archivo_FIP.writelines("\n"+str(round(Dato_FIP,4)))
    i=i+1
Archivo_FIP.close()
#
Archivo_FIS = open("Nuevos_Archivos_Creados/Volumen/FIS.txt","w")
i=0
for Dato_FIS in FIS:
    if i == 0:
        Archivo_FIS.writelines(str(round(Dato_FIS,4)))
    else:
        Archivo_FIS.writelines("\n"+str(round(Dato_FIS,4)))
    i=i+1
Archivo_FIS.close()
#
FIT = np.array([],dtype=float)
i=0
for Valor_FIS in FIS:
    Valor_FIT = (FIP[i] + Valor_FIS)
    FIT = np.append(FIT,Valor_FIT)
    i=i+1
Archivo_FIP.close()
"""Creando Archivo FIT.txt"""
Archivo_FIT = open("Nuevos_Archivos_Creados/Volumen/FIT.txt","w")
i=0
for Dato_FIT in FIT:
    if i == 0:
        Archivo_FIT.writelines(str(round(Dato_FIT,4)))
    else:
        Archivo_FIT.writelines("\n"+str(round(Dato_FIT,4)))
    i=i+1
Archivo_FIT.close()
"""Obteniendo Suma Total"""
Suma_Total = np.array([],dtype=float)
i=0
for Dato_FIP in FIP:
    Valor_Suma_Total = VDOL[i] + VCAL[i] + VLUT[i] + VSIL[i] + VSAL[i] + VYES[i] + VANH[i] + FIT[i]
    Suma_Total = np.append(Suma_Total,Valor_Suma_Total)
    i=i+1
Archivo_SUM_TOTAL = open("Nuevos_Archivos_Creados/Volumen/SUM_TOTAL.txt","w")
i=0
for Dato_SUM_TOTAL in Suma_Total:
    if i == 0:
        Archivo_SUM_TOTAL.writelines(str(round(Dato_SUM_TOTAL,4)))
    else:
        Archivo_SUM_TOTAL.writelines("\n"+str(round(Dato_SUM_TOTAL,4)))
    i=i+1
Archivo_SUM_TOTAL.close()
"""Calculando Valores Reales"""
Dividendo = np.array([],dtype=float)
i=0
for Dato_FIP in FIP:
    Valor_Dividendo = abs(VDOL[i]) + abs(VCAL[i]) + abs(VLUT[i]) + abs(VSIL[i]) + abs(VSAL[i]) + abs(VYES[i]) + abs(VANH[i]) + abs(Dato_FIP) + abs(FIS[i])
    Dividendo = np.append(Dividendo,Valor_Dividendo)
    i=i+1
"""www"""
VDOLR = np.array([],dtype=float)
VSILR = np.array([],dtype=float)
VCALR = np.array([],dtype=float)
VLUTR = np.array([],dtype=float)
VYESR = np.array([],dtype=float)
VANHR = np.array([],dtype=float)
VSALR = np.array([],dtype=float)
FIPR = np.array([],dtype=float)
FISR = np.array([],dtype=float)
i=0
for Valor_VDOL in VDOL:
    Resultado_VDOL = abs(Valor_VDOL)/Dividendo[i]
    VDOLR = np.append(VDOLR,Resultado_VDOL)
    
    Resultado_VCAL = abs(VCAL[i])/Dividendo[i]
    VCALR = np.append(VCALR,Resultado_VCAL)
    
    Resultado_VSIL = abs(VSIL[i])/Dividendo[i]
    VSILR = np.append(VSILR,Resultado_VSIL)
    
    Resultado_VLUT = abs(VLUT[i])/Dividendo[i]
    VLUTR = np.append(VLUTR,Resultado_VLUT)
    
    Resultado_VYES = abs(VYES[i])/Dividendo[i]
    VYESR = np.append(VYESR,Resultado_VYES)
    
    Resultado_VANH = abs(VANH[i])/Dividendo[i]
    VANHR = np.append(VANHR,Resultado_VANH)
    
    Resultado_VSAL = abs(VSAL[i])/Dividendo[i]
    VSALR = np.append(VSALR,Resultado_VSAL)
    
    Resultado_FIP = abs(FIP[i])/Dividendo[i]
    FIPR = np.append(FIPR,Resultado_FIP)
    
    Resultado_FIS = abs(FIS[i])/Dividendo[i]
    FISR = np.append(FISR,Resultado_FIS)
    i=i+1
FITR = np.array([],dtype=float)
i=0
for Valor_FIPR in FIPR:
    Resultado_FITR = Valor_FIPR + FISR[i]
    FITR = np.append(FITR,Resultado_FITR)
    i=i+1
"""Creando Suma Real"""
Suma_Total_Real = np.array([],dtype=float)
i=0
for Valor_FITR in FITR:
    Resultado_FITR = VDOLR[i] + VCALR[i] + VSILR[i] + VLUTR[i] + VYESR[i] + VANHR[i] + VSALR[i] + Valor_FITR
    Suma_Total_Real = np.append(Suma_Total_Real,Resultado_FITR)
    i=i+1
"""Guardando Valores en Archivos de TEXTO"""
Archivo_VDOLR = open("Nuevos_Archivos_Creados/Volumen_Real/VDOLR.txt","w")
i=0
for Dato_VDOLR in VDOLR:
    if i == 0:
        Archivo_VDOLR.writelines(str(round(Dato_VDOLR,4)))
    else:
        Archivo_VDOLR.writelines("\n"+str(round(Dato_VDOLR,4)))
    i=i+1
Archivo_VDOLR.close()
#
Archivo_VSILR = open("Nuevos_Archivos_Creados/Volumen_Real/VSILR.txt","w")
i=0
for Dato_VSILR in VSILR:
    if i == 0:
        Archivo_VSILR.writelines(str(round(Dato_VSILR,4)))
    else:
        Archivo_VSILR.writelines("\n"+str(round(Dato_VSILR,4)))
    i=i+1
Archivo_VSILR.close()
#
Archivo_VCALR = open("Nuevos_Archivos_Creados/Volumen_Real/VCALR.txt","w")
i=0
for Dato_VCALR in VCALR:
    if i == 0:
        Archivo_VCALR.writelines(str(round(Dato_VCALR,4)))
    else:
        Archivo_VCALR.writelines("\n"+str(round(Dato_VCALR,4)))
    i=i+1
Archivo_VCALR.close()
#
Archivo_VYESR = open("Nuevos_Archivos_Creados/Volumen_Real/VYESR.txt","w")
i=0
for Dato_VYESR in VYESR:
    if i == 0:
        Archivo_VYESR.writelines(str(round(Dato_VYESR,4)))
    else:
        Archivo_VYESR.writelines("\n"+str(round(Dato_VYESR,4)))
    i=i+1
Archivo_VYESR.close()
#
Archivo_VSALR = open("Nuevos_Archivos_Creados/Volumen_Real/VSALR.txt","w")
i=0
for Dato_VSALR in VSALR:
    if i == 0:
        Archivo_VSALR.writelines(str(round(Dato_VSALR,4)))
    else:
        Archivo_VSALR.writelines("\n"+str(round(Dato_VSALR,4)))
    i=i+1
Archivo_VSALR.close()
#
Archivo_VANHR = open("Nuevos_Archivos_Creados/Volumen_Real/VANHR.txt","w")
i=0
for Dato_VANHR in VANHR:
    if i == 0:
        Archivo_VANHR.writelines(str(round(Dato_VANHR,4)))
    else:
        Archivo_VANHR.writelines("\n"+str(round(Dato_VANHR,4)))
    i=i+1
Archivo_VANHR.close()
#
Archivo_VLUTR = open("Nuevos_Archivos_Creados/Volumen_Real/VLUTR.txt","w")
i=0
for Dato_VLUTR in VLUTR:
    if i == 0:
        Archivo_VLUTR.writelines(str(round(Dato_VLUTR,4)))
    else:
        Archivo_VLUTR.writelines("\n"+str(round(Dato_VLUTR,4)))
    i=i+1
Archivo_VLUTR.close()
#
Archivo_FIPR = open("Nuevos_Archivos_Creados/Volumen_Real/FIPR.txt","w")
i=0
for Dato_FIPR in FIPR:
    if i == 0:
        Archivo_FIPR.writelines(str(round(Dato_FIPR,4)))
    else:
        Archivo_FIPR.writelines("\n"+str(round(Dato_FIPR,4)))
    i=i+1
Archivo_FIPR.close()
#
Archivo_FISR = open("Nuevos_Archivos_Creados/Volumen_Real/FISR.txt","w")
i=0
for Dato_FISR in FISR:
    if i == 0:
        Archivo_FISR.writelines(str(round(Dato_FISR,4)))
    else:
        Archivo_FISR.writelines("\n"+str(round(Dato_FISR,4)))
    i=i+1
Archivo_FISR.close()
#
Archivo_FITR = open("Nuevos_Archivos_Creados/Volumen_Real/FITR.txt","w")
i=0
for Dato_FITR in FITR:
    if i == 0:
        Archivo_FITR.writelines(str(round(Dato_FITR,4)))
    else:
        Archivo_FITR.writelines("\n"+str(round(Dato_FITR,4)))
    i=i+1
Archivo_FITR.close()
#
Archivo_Suma_Total_Real = open("Nuevos_Archivos_Creados/Volumen_Real/SUM_TOTAL_REAL.txt","w")
i=0
for Dato_Suma_Total_Real in Suma_Total_Real:
    if i == 0:
        Archivo_Suma_Total_Real.writelines(str(round(Dato_Suma_Total_Real,4)))
    else:
        Archivo_Suma_Total_Real.writelines("\n"+str(round(Dato_Suma_Total_Real,4)))
    i=i+1
Archivo_Suma_Total_Real.close()