import time

ahora = time.strftime("%X")
textoPUSCH = "- Valores elevados de PUSCH"
textoRSSI = "- Valores elevados de RSSI"
textoSRVCC = "- No hay intentos de SRVCC"
textoTrafico5G = "- No hay valores de tráfico 5G"
textoMIMORank2Bajo = "- Valores bajos de MIMO Rank2"
textoSinMIMORank2 = "- No hay valores de MIMO Rank2"
textoMIMORank4Bajo = "- Valores bajos de MIMO Rank4"
textoSinMIMORank4 = "- No hay valores de MIMO Rank4"
textoSinCAPCELL = "- No hay valores de CA Pcell"
textoSinCASCELL = "- No hay valores de CA Scell"

justificaciones = {"PUSCH":textoPUSCH,"RSSI":textoRSSI,"SRVCC":textoSRVCC,"Trafico5G":textoTrafico5G,"MIMORank2Bajo":textoMIMORank2Bajo,
                    "SinMIMORank2":textoSinMIMORank2,"MIMORank4Bajo":textoMIMORank4Bajo,"SinMIMORank4":textoSinMIMORank4}

def crear_txt(texto,site):
    nombreTXT = "Justificación " + str(site) + ".txt"

    salida = open(nombreTXT,"w")
    salida.write(texto)
    salida.close()
    print("- DONE -")

def obtener_informacion():
    datos = open("justificaciones.txt","r")
    lineas = datos.read().splitlines()
    datos.close()

    site = lineas[0]
    site = site.split().pop(1)
    #print(site)

    cont =1
    lista =[]
    while cont < len(lineas):
        if cont < len(lineas):
            sectores = lineas[cont+2].split()
            sectores.pop(0)

            aux = [lineas[cont].split().pop(1),lineas[cont+1].split().pop(1),sectores]
            lista.append(aux)
        cont+=3
    return site, lista

def crear_justificacion(lista,justificaciones,site):
    textojustificaciones = ""
    if ahora < str(12):
        textojustificaciones += "Buenos días,\n"
    else:
        textojustificaciones += "Buenas tardes,\n"

    textojustificaciones += f"Hemos detectado las siguientes inconsistencias en el site {site}:\n"

    for i in lista:
        #print(i[0])
        if i[0] in justificaciones:
            textojustificaciones += str(justificaciones[i[0]])
            if len(i[2]) == 1:
                textojustificaciones +=" en el sector "
            else:
                textojustificaciones +=" en los sectores "
            for j in i[2]:
                textojustificaciones += str(i[1])
                textojustificaciones += str(j)
                if int(j)<len(i[2]):
                    textojustificaciones += ", "
            if i[0] == "PUSCH" or i[0] == "RSSI" or i[0] == "MIMORank2Bajo" or i[0] == "MIMORank4Bajo" or i[0] == "SinMIMORank2" or i[0] == "SinMIMORank4":
                textojustificaciones += ". Por favor ¿podrían comprobar que la configuración es correcta o si hay alarmas?\n\n\n"
            elif i[0] == "SRVCC":
                textojustificaciones += ". Por favor ¿podrían cargar el script adjunto?\n\n\n"
            elif i[0] == "Trafico5G":
                textojustificaciones += ". Por favor ¿podrían comprobar que la configuración X2 es correcta?\n\n\n"
           
    return textojustificaciones





site, listaJustificacion = obtener_informacion()

texto = crear_justificacion(listaJustificacion,justificaciones,site)
crear_txt(texto,site)