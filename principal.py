import operaciones

operaciones.agregar_producto("PROD001", "Paneton", "1200", "25.50")
operaciones.agregar_producto("PROD002", "Leche", "300", "4.20")

datos_del_archivo = operaciones.leer_catalogo()

print("--- CATÁLOGO RECUPERADO DEL ARCHIVO ---")
print(datos_del_archivo)