import pandas as pd
import math
import re 

df = pd.read_csv('data.csv')

total_estudiantes = len(df)
#print(total_estudiantes) numero de estudiantes totales 

# Guardar materias semestres en series o listas 

data_semestre = {
    'semestre1': ['IngesI', 'Intr Ing Industrial', 'Lectoescritura', 'Viva Universidad', 'Calculo Diferencial', 'Geo Vec y Analitica', 'Algebra y Trigonometria'],
    'semestre2': ['InglesII', 'Gestion Organizaciones', 'Habilidades Gerenciales', 'Habilidades Gerenciales', 'Cálculo Integral', 'Álgebra lineal', 'Desc Fisica'],
    'semestre3': ['InglesIII', 'Gestión Contable', 'TGS', 'Pro. Inf. Estadistica', 'Algoritmia y programación', 'Fisica Mecanica'],
    'semestre4': ['InglesIV', 'Ingeniería Económica', 'Ges de Met y Tiempos', 'D.E y Analisis de Regreción', 'Optimización', 'Electiva Fisica'],
    'semestre5': ['InglesV', 'Gestión Financiera', 'Dinámica de sistemas', 'Gestión por Procesos', 'Muestreo y series de tiempo', 'P.E y Análisis de decisión', 'Laboratorio Fisica'],
    'semestre6': ['InglesVI', 'Formación Ciudadana', 'Gestión tecnologica', 'N y C de la Calidad', 'Formulación proyecto de Investigación', 'Simulación deiscreta', 'Elec Humanidades I'],
    'semestre7': ['Legislación I', 'Emprendimiento', 'Dis de Sis Productivos', 'Enfacis Profesional I', 'Electiva ComplementariaI', 'Electiva Humanidades II'],
    'semestre8': ['F. E de P de Inversion', 'A. de la y del Servicio', 'Enfacis Profesional II', 'Electiva Complementaria II', 'Electiva Humanidades III'],
    'semestre9': ['Gestión de proyectos', 'Ing. del Mejoramiento Continuo', 'Ges de la Cadena de Abastecimiento', 'Enfasis Profesional III', 'Electiva Complementaria III', 'Electiva en Humanidades IV'],
    'semestre10': ['Practica Profesional']
}


def eliminar_estudiantes(): # Función para eliminar el 30% de los estudiantes cada semestre 
    return 0



grupos = [] # el total de grupos que hay por semestre 
cupo_aula_semestre = [40, 40, 40, 35, 35, 35, 25, 25, 25, 10] # Cupos por aula en cada semestre 


# Esta función esta hecha pero necesitamos eliminar los estuidantes que se van sacando por cada semestre
def gen_total_grupo(semestre):
    contador = 0 # para seguir cada semestre 
    while contador < 10: 
        semestre = list(semestre)
        grup_total_semestre = total_estudiantes / cupo_aula_semestre[contador]

        grupos.append(math.ceil(grup_total_semestre))

        if contador == 9: 
            return grupos

        contador += 1

grupos_semestre = gen_total_grupo(grupos)
print(grupos_semestre)

# Fin de esta función de generar los grupos del semestre 

#Código Asignatura (CA): Generar un código único para cada asignatura, este debe 
#representar en máximo 6 caracteres una combinación de los elementos de la tabla de 
#asignaturas al final del documento, por ejemplo, inglés 1 podría tener un código así, ING111, 
#para este caso se han utilizado las primeras tres letras del curso, el código del semestre, la 
#cantidad de créditos y un consecutivo de orden al ser el primer curso de una serie

def generar_codigo_materia(materias_semestre): # necesito guardar los valores de otra manera para poder acceder a ellos de forma separada
    valores = materias_semestre.values() # me suelta los valores en una lista   
    #print(valores)

    primeras_iniciales = []
    contador_semestre = 0
    contador_grupo = 1


    #for i in valores: # recorrer cada semestre [1, 2, 3, 4...]
    #    contador_semestre += 1
    #    for j in i:
    #        #print(j) desde aca esta bien todo bien 
    #        cadena_limpia = j.replace(' ', '') # Borrar caracteres especiales 
    #        iniciales = cadena_limpia[0:3] # corta el nombre en sus tres primera iniciales
    #        primeras_iniciales.append(iniciales + str(contador_semestre) + str(contador_grupo))  # Guarda las tres primeras iniciales de cada materia

    for w in grupos_semestre: # Itera el numero de grupos posibles en un semestre
        while contador_grupo <= w:

            for i in valores: # recorrer cada semestre [1, 2, 3, 4...]
                for j in i:
                    #print(j) desde aca esta bien todo bien 
                    cadena_limpia = j.replace(' ', '') # Borrar caracteres especiales 
                    iniciales = cadena_limpia[0:3] # corta el nombre en sus tres primera iniciales
                    primeras_iniciales.append(iniciales + str(contador_semestre) + str(contador_grupo))  # Guarda las tres primeras iniciales de cada materia


            contador_grupo += 1
        
            if contador_grupo == w + 1: 
                contador_grupo = 1
                break
             
            #print(primeras_iniciales            

    return primeras_iniciales

print(generar_codigo_materia(data_semestre)) 
# lo que nos devuelva la función toca que guardarlo en un dataframe para guardarlo en un archivo todo bien 










