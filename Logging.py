import logging
#Configuracion basica del logger
logging.basicConfig(level=logging.INFO)
def calcular_precio(producto, cantidad):
    precio_unitario=10
    logging.info(f"Calculando precio de {cantidad} unidades de {producto}")
    precio_total=cantidad*precio_unitario
    logging.info(f"Precio total de {cantidad}unidades de {producto}: {precio_total}")
    return precio_total
#ejemplo de uso de la funcion
calcular_precio("Camisa", 3)