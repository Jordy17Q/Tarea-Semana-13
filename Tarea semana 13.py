def calcular_temperatura_promedio(datos_temperaturas):
    """
    Función para calcular la temperatura promedio de múltiples ciudades.
    Parámetros:
        datos_temperaturas (dict): Diccionario con los datos de las temperaturas.
        Ejemplo: {'Ciudad1': [24, 26, 25, 23], 'Ciudad2': [30, 32, 31, 33]}
    Retorna:
        dict: Temperatura promedio por ciudad.
    """
    promedios = {}
    for ciudad, temperaturas in datos_temperaturas.items():
        promedios[ciudad] = sum(temperaturas) / len(temperaturas)
    return promedios

datos = {
    'Quito': [15, 16, 14, 17],
    'Guayaquil': [30, 29, 31, 32],
    'Cuenca': [18, 17, 19, 18]
}
promedios = calcular_temperatura_promedio(datos)
print(promedios)
