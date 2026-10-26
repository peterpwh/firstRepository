"""
PIA01 - Apartado 2 - Problema 2: Frecuencia de palabras en un texto.

Función que recibe una lista de palabras y la ruta de un fichero de texto y
devuelve un diccionario {palabra: frecuencia} con las veces que aparece cada
palabra de la lista en el fichero.
  1. Se eliminan los signos de puntuación y se convierte todo a minúsculas.
  2. Se usa un diccionario cuya clave es la palabra y cuyo valor es su frecuencia.
  3. Las palabras y sus frecuencias se muestran ordenadas por la palabra.
"""

import string
import sys

# Signos ASCII más los propios del español que no incluye string.punctuation
SIGNOS = string.punctuation + "¿¡«»“”‘’—–…"
TABLA_SIN_SIGNOS = str.maketrans("", "", SIGNOS)


def normalizar(texto: str) -> str:
    """Elimina los signos de puntuación y convierte el texto a minúsculas."""
    return texto.translate(TABLA_SIN_SIGNOS).lower()


def frecuencia_palabras(palabras: list[str], ruta_fichero: str) -> dict[str, int]:
    """Cuenta cuántas veces aparece cada palabra de 'palabras' en el fichero."""
    frecuencias = {normalizar(p): 0 for p in palabras}
    with open(ruta_fichero, encoding="utf-8") as fichero:
        for linea in fichero:
            for palabra in normalizar(linea).split():
                if palabra in frecuencias:
                    frecuencias[palabra] += 1
    return dict(sorted(frecuencias.items()))  # Ordenado por la palabra (clave)

if __name__ == "__main__":
    ruta = "texto_prueba.txt"
    palabras_buscadas = ["Python", "datos", "inteligencia", "java", "modelo", "R"]    
    resultado = frecuencia_palabras(palabras_buscadas, ruta)    
    print(f"Frecuencias en '{ruta}':")
    for palabra, veces in resultado.items():
        print(f"  {palabra}: {veces}")
