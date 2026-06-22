# 📊 Text Analyzer & Sentiment Estimator

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Un pequeño script interactivo en Python desarrollado para procesar bloques de texto a través de la terminal. El programa realiza un conteo de palabras, calcula la frecuencia de aparición de cada término, identifica la palabra más común y estima si el sentimiento general del texto es **positivo**, **negativo** o **neutro** mediante un diccionario local de palabras clave.

---

## ✨ Características

* **Conteo Global:** Calcula de forma precisa el total de palabras ingresadas.
* **Métrica de Frecuencia:** Desglosa cuántas veces aparece cada palabra de manera individual.
* **Detección de Tendencias:** Identifica automáticamente cuál fue el término más repetido.
* **Análisis de Sentimiento:** Evalúa el tono emocional del texto cruzando la entrada con listas predefinidas de más de 90 palabras positivas y negativas.
* **Normalización Automática:** Convierte el texto a minúsculas para evitar duplicados por diferencias de mayúsculas/minúsculas.

---

## 🛠️ Requisitos Previos

* **Python 3.x** instalado en tu sistema.
* No requiere la instalación de librerías de terceros (`pip`), ya que utiliza únicamente módulos y estructuras nativas de Python (`Standard Library`).

---

## 🚀 Instalación y Ejecución

1. **Clona este repositorio** o descarga el archivo fuente:
   ```bash
   git clone [https://github.com/tu-usuario/tu-repositorio.git](https://github.com/tu-usuario/tu-repositorio.git)
   cd tu-repositorio