"""
PIA01 - Apartado 2 - Problema 3: Trabajo con conjuntos.

Función que recibe dos listas de enteros y devuelve un diccionario con:
  1. La intersección (elementos comunes).
  2. La unión (todos los elementos sin duplicados).
  3. La diferencia simétrica (elementos de uno u otro conjunto, pero no de ambos).
Todos los cálculos se realizan obligatoriamente con conjuntos (set).
"""


def operaciones_conjuntos(lista_a: list[int],
                          lista_b: list[int]) -> dict[str, set[int]]:
    """Devuelve intersección, unión y diferencia simétrica de ambas listas."""
    conjunto_a = set(lista_a)
    conjunto_b = set(lista_b)
    return {
        "interseccion": conjunto_a & conjunto_b,
        "union": conjunto_a | conjunto_b,
        "diferencia_simetrica": conjunto_a ^ conjunto_b,
    }

if __name__ == "__main__":
    a, b = [1, 2, 3, 3, 4], [3, 4, 5, 6]
    print(f"Lista A: {a}")
    print(f"Lista B: {b}")
    for operacion, resultado in operaciones_conjuntos(a, b).items():
        print(f"  {operacion}: {sorted(resultado)}")
