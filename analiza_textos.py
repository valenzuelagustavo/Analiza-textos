def analiza_texto(texto):
    #Convertimos el texto a minuscula
    texto = texto.lower()

    #Separamos las palabras asumiendo que cada palabra está separada por un espacio
    palabras = texto.split()

    #Creamos un diccionario para contar la frecuencia de las palabras
    frecuencia = {}

    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    
    #Encontrar la palabra más común
    palabra_mas_comun = max(frecuencia, key=frecuencia.get)

    #Analizamos el sentimiento del texto
    palabras_positivas = ['Amor', 'Alegría', 'Paz', 'Felicidad', 'Éxito', 'Gratitud', 'Optimismo', 'Esperanza', 'Sonrisa', 'Inspiración', 'Motivación', 'Bienestar', 'Armonía', 'Pasión', 'Entusiasmo', 'Bondad', 'Generosidad', 'Compasión', 'Amistad', 'Confianza', 'Resiliencia', 'Fortaleza', 'Valentía', 'Libertad', 'Creatividad', 'Luz', 'Brillo', 'Triunfo', 'Victoria', 'Abundancia', 'Prosperidad', 'Crecimiento', 'Evolución', 'Magia', 'Milagro', 'Energía', 'Vitalidad', 'Salud', 'Plenitud', 'Dicha', 'Gozo', 'Disfrute', 'Deleite', 'Encanto', 'Belleza', 'Serenidad', 'Calma', 'Tranquilidad', 'Paciencia', 'Sabiduría', 'Claridad', 'Enfoque', 'Determinación', 'Perseverancia', 'Dedicación', 'Compromiso', 'Lealtad', 'Sinceridad', 'Honestidad', 'Respeto', 'Empatía', 'Simpatía', 'Amabilidad', 'Cariño', 'Afecto', 'Ternura', 'Dulzura', 'Asombro', 'Admiración', 'Aprecio', 'Reconocimiento', 'Valor', 'Merito', 'Talento', 'Habilidad', 'Genialidad', 'Brillantez', 'Éxtasis', 'Euforia', 'Ilusión', 'Sueño', 'Anhelo', 'Meta', 'Logro', 'Progreso', 'Avance', 'Triunfante', 'Radiante', 'Espléndido', 'Magnífico', 'Maravilloso', 'Fantástico', 'Increíble', 'Estupendo', 'Formidable', 'Grandioso', 'Espectacular', 'Sublime', 'Auténtico', 'Único']

    palabras_negativas = ['Odio', 'Tristeza', 'Guerra', 'Fracaso', 'Rencor', 'Pajon', 'Pesimismo', 'Desesperanza', 'Llanto', 'Frustración', 'Apatía', 'Malestar', 'Caos', 'Aversión', 'Desgano', 'Maldad', 'Egoísmo', 'Crueldad', 'Enemistad', 'Desconfianza', 'Debilidad', 'Cobardía', 'Opresión', 'Bloqueo', 'Oscuridad', 'Sombra', 'Derrota', 'Pérdida', 'Escasez', 'Pobreza', 'Ruina', 'Decadencia', 'Envidia', 'Celos', 'Inercia', 'Enfermedad', 'Vacío', 'Pena', 'Amargura', 'Desprecio', 'Desdén', 'Fealdad', 'Ansiedad', 'Estrés', 'Angustia', 'Impaciencia', 'Ignorancia', 'Confusión', 'Duda', 'Indecisión', 'Abandono', 'Rechazo', 'Traición', 'Falsedad', 'Mentira', 'Falta', 'Irrespeto', 'Antipatía', 'Hostilidad', 'Desdicha', 'Dolor', 'Sufrimiento', 'Pena', 'Lástima', 'Desprecio', 'Soberbia', 'Arrogancia', 'Culpa', 'Vergüenza', 'Miedo', 'Terror', 'Pánico', 'Desilusión', 'Pesadilla', 'Fracaso', 'Obstáculo', 'Retroceso', 'Atraso', 'Trágico', 'Funesto', 'Pésimo', 'Horrible', 'Terrible', 'Nfasto', 'Desastroso', 'Miserable', 'Deplorable', 'Repugnante', 'Tóxico', 'Nocivo', 'Dañino', 'Feroz', 'Agresivo', 'Violento', 'Cruel', 'Injusto', 'Despiadado', 'Falso', 'Rudeza', 'Soledad']

    puntaje_sentimiento = 0
    for palabra in palabras:
        if palabra in palabras_positivas:
            puntaje_sentimiento += 1
        elif palabra in palabras_negativas:
            puntaje_sentimiento -= 1
        
    sentimiento = ""

    if puntaje_sentimiento > 0:
        sentimiento = "positivo"
    elif puntaje_sentimiento < 0:
        sentimiento = "negativo"
    else:
        sentimiento = "neutro"

    #Devolver los resultados
    return{
        "total_palabras": len(palabras),
        "palabra_mas_comun": palabra_mas_comun,
        "frecuencia": frecuencia,
        "sentimiento": sentimiento
    }

def main():
    #solicitar texto al usuario
    texto_usuario = input("Ingrese el texto que desea analizar: ")

    resultados = analiza_texto(texto_usuario)

    print("\n--- Resultados del Analisis ---")
    print(f"Total de palabras: {resultados['total_palabras']}")
    print(f"Palabra más común: {resultados['palabra_mas_comun']}")
    print(f"Sentimiento estimado: {resultados['sentimiento']}")
    print("\nFrecuencia de cada palabra:")
    for palabra, conteo in resultados['frecuencia'].items():
        print(f"{palabra}: {conteo}")

if __name__ == "__main__":
    main()