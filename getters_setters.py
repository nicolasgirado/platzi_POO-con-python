class Millas:
    def __init__(self):
        self._distancia = 0

    def convertir_a_kilometros(self):
        return (self._distancia * 1.609344)

    # Método getter
    def obtener_distancia(self):
        return self._distancia

    # Método setter
    def definir_distancia(self, valor):
        if valor < 0:
            raise ValueError("No es posible convertir distancias menores a 0.")
        self._distancia = valor


if __name__ == "__main__":
    # Creamos un nuevo objeto
    avion = Millas()

    # Indicamos la distancia
    avion._distancia = 200

    # Obtenemos el atributo distancia
    print(avion._distancia)

    # Obtenemos el método convertir_a_kilometros
    print(avion.convertir_a_kilometros())

    avion.definir_distancia(50)

    print(avion.obtener_distancia())
