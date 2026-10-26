"""
PIA01 - Apartado 2 - Problema 1: Procesamiento de una lista de enteros.

Función que recibe una lista de enteros y devuelve otra lista en la que:
  1. Se eliminan los números negativos.
  2. Se eliminan los valores repetidos, conservando uno de ellos.
  3. Los números resultantes quedan ordenados de menor a mayor.
"""
def procesar_lista(numeros: list[int]) -> list[int]:
    """Devuelve los enteros no negativos de 'números', sin repetidos y ordenados."""
    no_negativos = [n for n in numeros if n >= 0]  # 1. Eliminar negativos
    sin_repetidos = set(no_negativos)              # 2. Un set no admite duplicados
    return sorted(sin_repetidos)                   # 3. Orden ascendente


if __name__ == "__main__":
    entrada = [4, -1, 2, 4, 3, -5, 2]
    print(f"Entrada: {entrada}")
    print(f"Salida:  {procesar_lista(entrada)}")
