def primera_parte(tech,node,cells):
    allTechs = {"Y":106 , "M":120 , "N": 110 , "L":100 , "T":130}
    text1 = "MOD CELLALGOSWITCH:LOCALCELLID="
    text2 = ",MULTIFREQPRICONTROLSWITCH=FixedMeasObjIDSwitch-0&VoipMeasFreqPriSwitch-1&PsMeasFreqPriSwitch-1,HOALLOWEDSWITCH=SrvBasedInterFreqHoSw-1&GeranSepOpMobilitySwitch-0&UtranCsfbSwitch-1&GeranCsfbSwitch-1&UtranFlashCsfbSwitch-1&GeranFlashCsfbSwitch-0&UtranCsfbSteeringSwitch-1&GeranCsfbSteeringSwitch-1&ServBasedHoBackSwitch-0&ServiceReqInterFreqHoSwitch-0&IdleCsfbRedirectOptSwitch-0&ServBasedNrHoSwitch-0;"
    textoFinal= ""
    for i in tech:
        if i in allTechs:
            for j in range(cells):
                textoFinal += text1+ str(allTechs[i]+j) + text2 + "{" + node + "}\n"
                
    return textoFinal

def segunda_parte(tech,node,cells):
    allTechs = {"Y":106 , "M":120 , "N": 110 , "L":100 , "T":130}
    text1 = "MOD CELLHOPARACFG:LOCALCELLID="
    text2 = ",HOMODESWITCH=BlindHoSwitch-1&UtranPsHoSwitch-1&UtranSrvccSwitch-1&GeranSrvccSwitch-1&UtranRedirectSwitch-1&GeranRedirectSwitch-0&UFCsfbBlindHoDisSwitch-0&HighSpeedCsfbBlindSwitch-0&NrRedirectSwitch-0,SRVCCHOOPTSWITCH=SRVCCWITHPSCSRETRYSWITCH-1;"
    textoFinal= ""
    for i in tech:
        if i in allTechs:
            for j in range(cells):
                textoFinal += text1+ str(allTechs[i]+j) + text2 + "{" + node + "}\n"
                
    return textoFinal

def tercera_parte(tech,node,cells):
    allTechs = {"Y":106 , "M":120 , "N": 110 , "L":100 , "T":130}
    text1 = "MOD UTRANNFREQ:LOCALCELLID="
    text2 = ",UTRANDLARFCN=10688,PSPRIORITY=16;"
    textoFinal= ""
    for i in tech:
        if i in allTechs:
            for j in range(cells):
                textoFinal += text1+ str(allTechs[i]+j) + text2 + "{" + node + "}\n"
                
    return textoFinal

def crear_txt(siteName,tech,node,cells):
    
    primeraParte = primera_parte(tech,node,cells)
    segundaParte = segunda_parte(tech,node,cells)
    terceraParte = tercera_parte(tech,node,cells)

    nombreTXT = ".\\scripts\\SRVCC - " + siteName + " - " + node + ".txt"

    salida = open(nombreTXT,"w")

    salida.write(primeraParte + "\n" + segundaParte + "\n" + terceraParte)

    salida.close()



