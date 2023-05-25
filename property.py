class Millas:
    def __init__(self):
        self._distancia = 0

    # Función para obtener el valor de _distancia
    def obtener_distancia(self):
        print("Llamada al método getter")
        return self._distancia

    # Función para definir el valor de _distancia
    def definir_distancia(self, recorrido):
        print("Llamada al método setter")
        self._distancia = recorrido

    # Función para eliminar el atributo _distancia
    def eliminar_distancia(self):
        print("Llamada al método eliminar distancia")
        del self._distancia

    distancia = property(
        obtener_distancia, definir_distancia, eliminar_distancia)


# Creamos un nuevo objeto
avion = Millas()

# Indicamos la distancia
# Nota: cuando asignamos la property "distancia" pasamos por el segundo método "setter"
avion.distancia = 200

# Obtenemos su atributo distancia
# Nota: cuando solicitamos el valor de la property "distancia" pasamos por el primer método "getter"
print(avion.distancia)

# Nota: Todo esto permite que la variable _distancia quede realmente como privada sin que la podamos manipular