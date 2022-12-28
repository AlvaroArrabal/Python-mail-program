
def nombre_site(site):
    parte1 = site[0:3]
    parte2 = site[3:]
    return parte1 + "X" + parte2

def primera_parte(techCA,tech,sectores,nodo):
    allTechs = {"Y":(106,9260), "M":(120,6200), "N":(110,1849), "L":(100,3050), "T":(130,201)}
    text1 ="ADD EUTRANINTERNFREQ:LOCALCELLID="
    text2 = ",DLEARFCN="
    text3 = ",ULEARFCNCFGIND=NOT_CFG,CELLRESELPRIORITYCFGIND=CFG,CELLRESELPRIORITY=3,SPEEDDEPENDSPCFGIND=NOT_CFG,MEASBANDWIDTH=MBW50,QOFFSETFREQ=dB0,THRESHXHIGH=7,THRESHXLOW=10,QRXLEVMIN=-64,PMAXCFGIND=NOT_CFG,INTERFREQHOEVENTTYPE=EventA3,QOFFSETFREQCONN=dB0,ANRIND=ALLOWED;"
    textoFinal= ""
    for i in tech:
        if i in allTechs:
            for j in range(sectores):
                textoFinal += text1 + str(allTechs[techCA][0] + j) + text2 + str(allTechs[i][1]) + text3 + "{" + nodo + "}\n"
                #print(f"{allTechs[techCA][0] + j} y {allTechs[i][1]}")
            for j in range(sectores):
                textoFinal += text1 + str(allTechs[i][0] + j) + text2 + str(allTechs[techCA][1]) + text3 + "{" + nodo + "}\n"
                #print(f"{allTechs[i][0] + j} y {allTechs[techCA][1]}")
            textoFinal += "\n"
    return textoFinal

def segunda_parte(techCA,tech,sectores,eNodebID,nodo):
    allTechs = {"Y":(106,9260), "M":(120,6200), "N":(110,1849), "L":(100,3050), "T":(130,201)}
    text1 ="ADD EUTRANINTERFREQNCELL:LOCALCELLID="
    text2=',MCC="214",MNC="03",ENODEBID='
    text3=",CELLID="
    text4=",NOHOFLAG=PERMIT_HO_ENUM;"

    textoFinal = ""

    for i in tech:
        if i in allTechs:
            for j in range(sectores):
                for k in range(sectores):
                    textoFinal += text1 + str(allTechs[i][0] + j) + text2 + eNodebID + text3 + str(allTechs[techCA][0] + k) + text4 + "{" + nodo + "}\n"
                    #print(f"{allTechs[i][0] + j} y {allTechs[techCA][0] + k}")  
        textoFinal += "\n"
    return textoFinal   

def tercera_parte(site,techCA,tech,sectores,nodo,eNodebID):
    allTechs = {"Y":(106,9260), "M":(120,6200), "N":(110,1849), "L":(100,3050), "T":(130,201)}
    text1="ADD EUTRANINTERFREQNCELL:LOCALCELLID="
    text2=',MCC="214",MNC="03",ENODEBID='
    text3=",CELLID="
    text4=',NORMVFLAG=PERMIT_RMV_ENUM,BLINDHOPRIORITY=32,LOCALCELLNAME="'
    text5='",NEIGHBOURCELLNAME="'
    text6='";'
    textoFinal=""
    for i in tech:
        if i in allTechs:
            for j in range(sectores):
                for k in range(sectores):
                    textoFinal += text1 + str(allTechs[i][0] + j) + text2 + eNodebID + text3 + str(allTechs[techCA][0] + k) + text4 + str(site + str(i)) + str(j+1) + "A" + text5 + str(site + techCA) + str(k+1) + "A" + text6 + "{" + nodo + "}\n"
                    #print(f"{allTechs[i][0] + j} y {allTechs[techCA][0] + k} y {site + str(i)}{j+1}A y {site + techCA}{k+1}A")
            textoFinal += "\n"
            for j in range(sectores):
                for k in range(sectores):
                    textoFinal += text1 + str(allTechs[techCA][0] + j) + text2 + eNodebID + text3 + str(allTechs[i][0] + k) + text4 + str(site + techCA) + str(j+1) + "A" + text5 + str(site + str(i)) + str(k+1) + "A" + text6 + "{" + nodo + "}\n"
                    #print(f"{allTechs[techCA][0] + j} y {allTechs[i][0] + k} y {site + techCA}{j+1}A y {site + str(i)}{k+1}A")
            textoFinal += "\n"
    return textoFinal


def crear_txt_CA(site,techCA,tech,sectores,nodo,eNodebID):

    nombreTXT = ".\\scripts\\CA - " + site + " - " + nodo +".txt"
    site = nombre_site(site)
    primeraParte = primera_parte(techCA,tech,sectores,nodo)
    segundaParte = segunda_parte(techCA,tech,sectores,eNodebID,nodo)
    tercerParte = tercera_parte(site,techCA,tech,sectores,nodo,eNodebID)

    salida = open(nombreTXT,"w")
    salida.write(primeraParte + "\n" + segundaParte + "\n" + tercerParte)
    salida.close()
