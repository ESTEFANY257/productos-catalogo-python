def agregar_producto(codigo, descripcion, cantidad, precio):
    crear_registro = open("catalogo.txt", "a")
    crear_registro.close() 

    lectura_datos = open("catalogo.txt", "r")
    informacion_actual = lectura_datos.read()
    lectura_datos.close() 

    if codigo in informacion_actual:
        print("El código " + codigo + " ya existe en el catálogo.")
    else:
        nuevo_registro = open("catalogo.txt", "a") 
        nuevo_registro.write(codigo + "," + descripcion + "," + cantidad + "," + precio + "\n")
        nuevo_registro.close()
        print("Producto " + codigo + " guardado exitosamente.")

def leer_catalogo():
    archivo = open("catalogo.txt", "r")
    informacion_recuperada = archivo.read()
    archivo.close()
    
    return informacion_recuperada