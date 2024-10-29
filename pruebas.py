'''
grupos_semestre = [3, 5]
contador_grupo = 1
materias = ['Ing', 'Cal', 'lec', 'per']
codigo = []

for w in grupos_semestre: # Itera el numero de grupos posibles en un semestre
    while contador_grupo <= w:
        print(contador_grupo)

        for i in materias: 
            codigo.append(i + str(contador_grupo))
            
        print("Hola" + str(contador_grupo))
        contador_grupo += 1
        
        
        if contador_grupo == w + 1: 
            contador_grupo = 1
            break

print(codigo) '''


import pandas as pd

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

# Tenemos medio codigo de materia

print(len(df))


def generar_codigo(dataframe): 
    i = 0
    materias_codigos = []
    
    while i < len(dataframe):
        codex = f'{str(dataframe.iloc[i][0][0:3]).upper()}{dataframe.iloc[i][1]}{dataframe.iloc[i][2]}'
        materias_codigos.append(codex)
        i += 1
    
    return materias_codigos


df['Codigos'] = generar_codigo(df)


# Generar codigo de las materias 





# Calcular estadísticas básicas
#total_creditos = df['Creditos'].sum()
#creditos_por_semestre = df.groupby('Semestre')['Creditos'].sum()
#
## Mostrar el DataFrame y las estadísticas
#print("Plan de Estudios:")
#print(df)
#print("\nTotal de créditos del programa:", total_creditos)
#print("\nCréditos por semestre:")
#print(creditos_por_semestre)
#
## Exportar a Excel para mejor visualización
#df.to_excel('plan_de_estudios.xlsx', index_label='No.')