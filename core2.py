x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].
print(x[1])
x[1][0]=15
print(x)

#Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
print(estudiantes[0])
estudiantes[0]["last_name"] = "Bryant"
print(estudiantes[0])

#En el directorio_deportes, cambia "Messi" por "Andrés".
print(directorio_deportes["fútbol"])
directorio_deportes["fútbol"][0] = "Andres"
print(directorio_deportes["fútbol"])

#Cambia el valor 20 en z a 30.
print (z[0])
z[0]['y'] = 30
print (z[0])


estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# debería devolver: (está bien si cada par clave-valor termina en 2 líneas separadas;
# un bonus para que aparezcan exactamente como se muestra a continuación)
#first_name - Michael, last_name - Jordan
#first_name - John, last_name - Rosales
#first_name - Mark, last_name - Guillen
#first_name - KB, last_name - Tonel

def iterateDictionary(estudiantes):
    for x in range(len(estudiantes)):
        print("first_name - " + estudiantes[x]["first_name"]+", "+"last_name - "+estudiantes[x]["last_name"])

iterateDictionary(estudiantes) 

#Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios y un nombre de clave, la función imprima el valor almacenado en esa clave para cada diccionario. Por ejemplo, iterateDictionary2('name', estudiantes) debería generar:

def iterateDictionary2(valor_llave,diccionario):
    for x in range(len(diccionario)):
        print(estudiantes[x][valor_llave])

iterateDictionary2("first_name",estudiantes)
iterateDictionary2("last_name",estudiantes)


#Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todos listas, imprima el nombre de cada clave junto con el tamaño de su lista, y luego imprima los valores asociados dentro de la lista de cada clave. Por ejemplo:

dojo = {
   'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dicc):
    for x in dicc.keys():
        print(  str(len(dicc[x])) +" "+ x.upper()  )
        for datos in dicc[x]:
            print(datos)       

printInfo(dojo)

