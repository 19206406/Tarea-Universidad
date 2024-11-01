import pandas as pd 
import numpy as np 
import math
import random

# Importar los datos de los estudiantes 


def leer_estudiantes(archivo_csv):
    return pd.read_csv(archivo_csv)

# Se guardan los nombres de los estudiantes 
nombre_estudiantes = leer_estudiantes('data.csv')
print(nombre_estudiantes)
print(type(nombre_estudiantes))

# Crear listas con los datos
materias = [
    "Inglés 1", "Introducción a la ingeniería industrial", "Lectoescritura",
    "Vivamos la universidad", "Cálculo diferencial", "Álgebra y trigonometría",
    "Geometría vectorial", "Inglés 2", "Gestión de las organizaciones",
    "Habilidades gerenciales", "Cálculo integral", "Álgebra lineal",
    "Descubriendo la física", "Inglés 3", "Gestión contable",
    "Teoría general de sistemas", "Probabilidad e inferencia estadística",
    "Algoritmia y programación", "Física mecánica", "Inglés 4",
    "Ingeniería económica", "Diseño de experimentos y análisis de regresión",
    "Gestión de métodos y tiempos", "Optimización", "Electiva en física 1",
    "Inglés 5", "Gestión financiera", "Dinámica de sistemas",
    "Gestión por procesos", "Muestreo y series de tiempo",
    "Procesos escolásticos y análisis de decisión", "Laboratorio integrado de física",
    "Inglés 6", "Formación ciudadana y constitucional", "Gestión tecnológica",
    "Normalización y control de calidad", "Formulación de proyectos de investigación",
    "Simulación discreta", "Electiva en humanidades 1", "Legislación",
    "Emprendimiento", "Diseño de sistemas productivos", "Énfasis profesional 1",
    "Electiva complementaria 1", "Electiva en humanidades 2",
    "Formulación y evaluación de proyectos de inversión", "Administraión de la producción y del servicio",
    "Énfasis profesional 2", "Electiva complementaria 2", "Electiva en humanidades 3",
    "Gestión de proyectos", "Ingeniería del mejoramiento continuo",
    "Gestión de la cadena de abastecimiento", "Énfasis profesional 3",
    "Electiva complementaria 3", "Electiva en humanidades 4", "Práctica profesional"
]

semestres = [
    1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4,
    5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8,
    9, 9, 9, 9, 9, 9, 10
]

creditos = [
    1, 1, 3, 1, 3, 3, 3, 1, 3, 3, 3, 3, 3, 1, 3, 3, 3, 3, 3, 1, 3, 3, 4, 3, 3,
    1, 3, 3, 3, 3, 3, 1, 1, 1, 3, 3, 3, 3, 3, 1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3,
    3, 3, 3, 3, 3, 3, 12
]

# Crear el DataFrame
df = pd.DataFrame({
    'Materia': materias,
    'Semestre': semestres,
    'Creditos': creditos
})

# Añadir una columna con el número de orden
df.index = range(1, len(df) + 1)
print(df)

# puede ser una opción de almacenamiento
#materias_del_semestre = pd.DataFrame(data_semestre)
#print(materias_del_semestre)

# cantidad de estudiantes
def numero_de_estudiantes(data):
    return len(data)

total_estudiantes = numero_de_estudiantes(nombre_estudiantes)
#print(total_estudiantes)

grupos = [] # el total de grupos que hay por semestre 
cupo_aula_semestre = [40, 40, 40, 35, 35, 35, 25, 25, 25, 10] # Cupos por aula en cada semestre 


# Notas primer semestre de los estudiantes 
# En esta primera función necesitamos generar las notas de las nmaterias del primer
# semestre y de los diez pero necesitamos generar notas por materia serian en total 6000 notas en este primner semestre 
# mas otra linea con el promedio de las notas para descartar el 30 porciento de los estudiantes 


#materias_semestre1 = df[df['Semestre'] == 1]
#print(materias_semestre1)

def notas_primer_semestre(estudiantes, numero_de_estudiantes, materias): # voy a intentar generar un dataframe  

    num_es_aprobados = int(numero_de_estudiantes * 0.7) # 700
    num_es_reprobados = numero_de_estudiantes - num_es_aprobados # 300  

    info_semestre1 = materias[materias['Semestre'] == 1] # Materias primer semestre 

    materias_semestre1 = np.array(info_semestre1['Materia']) # solo las materias 

    # Notas del 70 porciento mayor a 3 
    notas_aprobados = np.random.uniform(3, 5, size=(num_es_aprobados, len(materias_semestre1)))
    notas_reprobados = np.random.uniform(0, 3, size=(num_es_reprobados, len(materias_semestre1)))
    
    # vstack para combinar las dos matrices
    notas = np.vstack((notas_aprobados, notas_reprobados))

    # generar promedio notas 
    promedio_semestre = notas.mean(axis=1)

    notas_semestre = pd.DataFrame(notas, columns=materias_semestre1)
    notas_semestre['Promedio'] = promedio_semestre
    notas_semestre.index = estudiantes['Nombre&Apellido'] 

    return notas_semestre

resultado = notas_primer_semestre(nombre_estudiantes, total_estudiantes, df)

estudiantes_aprobados_semestre1 = resultado[resultado['Promedio'] >= 3]
print("Estudiantes con promedio mayor o igual a 3: ")
print(estudiantes_aprobados_semestre1)


#Notas del segundo semestre 

def notas_segundo_semestre(estudiantes_aprobados_semestre1, materias):

    num_es_aprobados = int(len(estudiantes_aprobados_semestre1) * 0.7) # 700
    num_es_reprobados = len(estudiantes_aprobados_semestre1) - num_es_aprobados # 300  

    info_semestre2 = materias[materias['Semestre'] == 2] # Materias primer semestre 

    materias_semestre2 = np.array(info_semestre2['Materia']) # solo las materias 

    # Notas del 70 porciento mayor a 3 
    notas_aprobados = np.random.uniform(3, 5, size=(num_es_aprobados, len(materias_semestre2)))
    notas_reprobados = np.random.uniform(0, 3, size=(num_es_reprobados, len(materias_semestre2)))

    # vstack para combinar las dos matrices
    notas = np.vstack((notas_reprobados, notas_aprobados))

    # generar promedio notas 
    promedio_semestre = notas.mean(axis=1)

    notas_semestre = pd.DataFrame(notas, columns=materias_semestre2)
    notas_semestre['Promedio'] = promedio_semestre
    notas_semestre.index = estudiantes_aprobados_semestre1.index 

    return notas_semestre

resultado = notas_segundo_semestre(estudiantes_aprobados_semestre1, df)

estudiantes_aprobados_semestre2 = resultado[resultado['Promedio'] >= 3]
print("Estudiantes con promedio mayor o igual a 3: ")
print(estudiantes_aprobados_semestre2)
































# Esta función esta hecha pero necesitamos eliminar los estuidantes que se van sacando por cada semestre
'''def gen_total_grupo(semestre):
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


# GENERAR CODIGOS DE LAS ASIGNATURAS A MEDIAS JAJAJJA 

def generar_codigo(dataframe): 
    i = 0
    materias_codigos = []
    
    while i < len(dataframe):
        codex = f'{str(dataframe.iloc[i][0][0:3]).upper()}{dataframe.iloc[i][1]}{dataframe.iloc[i][2]}'
        materias_codigos.append(codex)
        i += 1
    
    return materias_codigos


df['Codigos'] = generar_codigo(df)
#print(df.iloc[0][1])


# Cupos de las materias 
def grupos_por_materia(dataframe): 
    frame_cupos = []
    j = 0
    
    while j < len(dataframe):

        match int(dataframe.iloc[j][1]): 
            case 1: 
                frame_cupos.append(grupos_semestre[0])
            case 2: 
                frame_cupos.append(grupos_semestre[1])
            case 3: 
                frame_cupos.append(grupos_semestre[2])
            case 4: 
                frame_cupos.append(grupos_semestre[3])
            case 5: 
                frame_cupos.append(grupos_semestre[4])
            case 6: 
                frame_cupos.append(grupos_semestre[5])
            case 7: 
                frame_cupos.append(grupos_semestre[6])
            case 8:
                frame_cupos.append(grupos_semestre[7])
            case 9: 
                frame_cupos.append(grupos_semestre[8])
            case 10: 
                frame_cupos.append(grupos_semestre[9])

        j += 1

    return frame_cupos

df['Cupo'] = grupos_por_materia(df)
print(df)
'''