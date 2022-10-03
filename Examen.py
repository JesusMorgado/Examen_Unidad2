# Jesus Morgado Marquez
#18420469

import json

lista = []

def M():
    try:
        archivo = open("Kardex.txt", "r")
    except FileNotFoundError:
        print('¡No se puede abrir el archivo especificado!')
    except UnicodeDecodeError:
        print('¡Error al decodificar al leer el archivo!')

    mate = set()
    for linea in archivo:
        d = linea.split("|")
        datos = int(str(d[2]))
        mate.add((linea[0:8], d[1], datos))
    archivo.close()
    return mate


def E():
    try:
        archivo = open("Estudiantes.prn", "r")
    except FileNotFoundError:
        print('¡No se puede abrir el archivo especificado!')
    except UnicodeDecodeError:
        print('¡Error al decodificar al leer el archivo!')

    c = set()
    for linea in archivo:
        c.add((linea[0:8], linea[8:-1]))
    return c


def mostrar(lista):
    mostrar = []
    alumnos = E()
    materias = M()

    if len(lista) == 0:
        for alu in alumnos:
            c1, n1 = alu
            mostrar.append({"Nombre del Alumno": n1})
            for mat in materias:
                c, n, p = mat
                if c1 == c:
                    mostrar.append({"Materia": n})

    else:

        for lis in lista:
            ctr = lis
            for alu in alumnos:
                c, n = alu
                if ctr == c:
                    mostrar.append({"Nombre del Alumno": n})
                    for mat in materias:
                        c1, n,p = mat
                        if ctr == c1:
                            mostrar.append({"Materia": n})
    return json.dumps(mostrar, indent=3)

print(mostrar(lista))


















