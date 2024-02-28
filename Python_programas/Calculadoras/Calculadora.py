import statistics

def calcular_estadisticas(numeros):
    try:
        media = statistics.mean(numeros)
        mediana = statistics.median(numeros)
        moda = statistics.mode(numeros)
        desviacion_estandar = statistics.stdev(numeros)

        return media, mediana, moda, desviacion_estandar
    except statistics.StatisticsError as e:
        return f"No se puede calcular la moda: {e}", None, None, None

# Ejemplo de uso
numeros_ejemplo = [2, 4, 4, 4, 5, 5, 7, 9]

media, mediana, moda, desviacion_estandar = calcular_estadisticas(numeros_ejemplo)

print(f"Lista de números: {numeros_ejemplo}")
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
print(f"Desviación Estándar: {desviacion_estandar}")
