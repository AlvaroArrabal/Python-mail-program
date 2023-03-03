dic_problems = {"PUSCH" : "- Valores elevados de PUSCH",
                "RSSI" : "- Valores elevados de RSSI",
                "SRVCC" : "- No hay intentos de SRVCC",
                "Sin tráfico 5G" : "- No hay valores de tráfico 5G",
                "MIMO Rank2 Bajo" : "- Valores bajos de MIMO Rank2",
                "Sin MIMO Rank2" : "- No hay valores de MIMO Rank2",
                "MIMO Rank4 Bajo" : "- Valores bajos de MIMO Rank4",
                "Sin MIMO Rank4" : "- No hay valores de MIMO Rank4",
                "CA PCELL" : "- No hay valores de CA Pcell",
                "CA SCELL" : "- No hay valores de CA Scell",
                "Sin llamadas 4G":"- No hay llamadas iniciadas 4G",
                "Sin datos 5G":"- No se obtienen datos sobre 5G de la banda ",
                "ICM Band" : "- Valores elevados de ICM Band",
                "RTWP" : "- Valores elevados de RTWP",
                "Speech Discon.(3dB)":"- Valores elevados de Speech Disconnection 2G",
                "3G Ending 2G (3dB)":"- Valores elevados de 3G calls ending in 2G",
                "CSFallBack":"- Sin valores de CSFB",
                "Sin llamadas 2G":"- No hay llamadas iniciadas 2G",
                "Sin llamadas 3G":"- No hay llamadas iniciadas 3G",
                }



def insert(sectors,techs,problem):
    textoAux = ""
    textoAux += f"{dic_problems[problem]}"
    if problem == "Sin datos 5G":
        techaux = techs.get().upper().split()
        textoAux += techaux[0] + ". Por favor ¿podrían comprobar que la configuración es correcta o si hay alarmas?\n\n"
    else:
        listAux = sectors.get().split(";")
        techaux = techs.get().upper().split()
        cont2 = 0
        sectorAux = listAux[0].split()
                    
        if len(listAux) == 1 and len(sectorAux) == 1:
            textoAux += " en el sector"
        else:
            textoAux += " en los sectores"
                    

        for j in techaux:
            sectorNumbers = listAux[cont2].split()
                        
            cont3 = 0
            for k in sectorNumbers:
                textoAux += f" {j}{k}"
                if cont3 < len(sectorNumbers)   and cont2 != len(techaux)-1:
                    textoAux += ","
                else:
                    if cont3 < len(sectorNumbers)-1:
                        textoAux += ","
                    else:
                        textoAux += "."
                cont3 += 1
            cont2 += 1
        
        if problem == "PUSCH" or problem == "RSSI" or problem == "Sin MIMO Rank2" or problem == "Sin MIMO Rank4" or problem == "MIMO Rank2 Bajo" or problem == "MIMO Rank4 Bajo" or problem == "Sin llamadas 4G" or problem == "Sin llamadas 3G" or problem == "RTWP" or problem == "ICM Band" or problem == "CSFallBack":
            textoAux += " Por favor ¿podrían comprobar que la configuración es correcta o si hay alarmas?\n\n"
        if problem == "CA PCELL" or problem == "CA SCELL" or problem == "SRVCC":
            textoAux += " Por favor ¿podrían cargar el script adjunto?\n\n"
        if problem == "Sin tráfico 5G":
            textoAux += " Por favor ¿podrían comprobar que la configuración X2 es correcta?\n\n"
        if problem == "Speech Discon.(3dB)":
            textoAux += " Por favor ¿podrían comprobar que la definición del CORE es correcta?\n\n"
        if problem == "3G Ending 2G (3dB)":
            textoAux += " Por favor ¿podrían comprobar que las vecinas están correctamente definidas?\n\n"
        if problem == "Sin llamadas 2G":
            textoAux += " Por favor ¿podrían comprobar que la configuración del parámetro gcellospmap es correcta?\n\n"
    
    return textoAux