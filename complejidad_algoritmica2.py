def f(x):

    # 1 paso
    respuesta = 0

    # 1000 pasos
    for i in range(1000):
        respuesta += 1

    # x pasos
    for i in range(x):
        respuesta += x

    # 2x**2 pasos
    # Este es el término que más importa cuando x va al infinito
    for i in range(x):
        for j in range(x):
            respuesta += 1
            respuesta += 1

    # 1 paso
    return respuesta

    # Total pasos = 1002 + x + 2x**2
