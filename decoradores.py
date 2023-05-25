def funcion_decoradora(funcion):
    def wrapper():
        print("Este es el primer mensaje ;)")
        funcion()
        print("Este es el último mensaje...")
    return wrapper


def zumbido():
    print("Buzzzzzz")

@funcion_decoradora
def otro_sonido():
    print("fiuuum")


if __name__ == "__main__":
    zumbido = funcion_decoradora(zumbido)
    zumbido()

    otro_sonido()
