def multiplicador_palabras(texto, cantidad):
    return texto * cantidad

resultado = multiplicador_palabras('Hammer', 10)
print(resultado)

def multiplicador_notacion(texto: str, cantidad: int)-> str:
    return texto * cantidad

resultado_notacion = multiplicador_notacion('Carlos', 50)
print(resultado_notacion)