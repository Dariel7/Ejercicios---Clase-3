d1={
    "Nombre": "Sara",
    "Edad": 27,
    "Documento": 100382  
}
d1['Nombre']="Laura"


"""d2={
    "Carrera": "ISC",
    "Asignatura": "AGP",
    "Matricula": 100382  
}
d2['Nombre']="Laura"

d1.update(d2)
print(d1)"""

"""d2=dict([
    ('Nombre', 'Sara'),
    ('Edad', 27),
    ('Documento', 1003882),
    
]
)
print(d2)"""""

"""frutas = {'manzana', 'banana', 'pera'}
frutas.add("Fresa")
print (frutas)"""""

"""numeros = {1,2,3,4}
numeros.remove(3)
print(numeros)"""

"""numeros ={1,2,3,4,5,6}
numeros.discard(5)
print(numeros)"""

"""numeros ={1,2,3}
print(2 in numeros)
print(4 in numeros)"""

"""a={1,2,3}
b={3,4,5}
c=a.union(b)

print(c)"""

"""a={1,2,3}
b={2,3,4}
c=a.intersection(b)

print(c)"""

def suma (a, b):
    total = a + b 
    return total
resultado = suma(2,3)
print(resultado)