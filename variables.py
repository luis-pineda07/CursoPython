#Variables
x = 10
y = 5.5
z = x + y

print ("el valor de z es : " + str(z))

#variables de cadena
nombre= "Jose"
apellido= "Fernandez"

nombre_completo = nombre + " " + apellido
print("El nombre es: " + nombre_completo)

#variables logicas
es_verdadero = True
es_falso = not es_verdadero

print(es_falso)

#secuencia
mi_list = [1, 2, 3, 4, 5]
mi_tupla = (6, 7, 8, 9, 10)

print(mi_tupla)
print("Mi primer elemento " + str(mi_tupla[0]))
print("Mi ultimo elemento " + str(mi_tupla[len(mi_tupla) - 1]))

#dicciionario
mi_diccionario = {
    "nombre": "Jose",
    "apellido": "Fernandez",
    "nationality": "Suecia",
    "age": 26,

}    
print(mi_diccionario) 
print("El nombre es: " + mi_diccionario["nombre"])
