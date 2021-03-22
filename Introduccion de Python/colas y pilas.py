# Las colas son estructuras que consisten en entrada y salida
# Son colecciones de elementos ordenados que únicamente permiten dos acciones:
# Añadir un elemento a la pila.
# Sacar un elemento de la pila.


cola = ["Pablo", "Dario", "Lucio", "Martin"]
print(cola)

cola.append("Paola")
cola.append("Romina")

print(cola)


# De esta forma elimina al ultimo de la fila
cola.pop()

print(cola)

# Para eliminar al ultimo
cola.pop(0)

print(cola)

# Para cortar y mostrar a uno de ellos

x = cola.pop(1)

print(f"Estan atendiendo a {x}")

