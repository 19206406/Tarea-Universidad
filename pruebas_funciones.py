import numpy as np
import pandas as pd

def generar_notas(num_estudiantes, num_materias, porcentaje_aprobados=0.7):
    """
    Genera notas aleatorias para estudiantes, con el porcentaje dado de promedios >= 3.
    Luego filtra a los estudiantes cuyo promedio es mayor o igual a 3.
    
    Parámetros:
    num_estudiantes (int): Número de estudiantes
    num_materias (int): Número de materias por estudiante
    porcentaje_aprobados (float): Proporción de estudiantes con promedio >= 3
    
    Retorna:
    DataFrame: DataFrame con las notas de los estudiantes y sus promedios
    """
    num_aprobados = int(num_estudiantes * porcentaje_aprobados)
    num_reprobados = num_estudiantes - num_aprobados

    # Generamos notas para el 70% de los estudiantes con promedios >= 3
    notas_aprobados = np.random.uniform(3, 5, size=(num_aprobados, num_materias))
    notas_reprobados = np.random.uniform(0, 3, size=(num_reprobados, num_materias))

    # Combinamos ambas matrices para obtener todas las notas
    notas = np.vstack((notas_aprobados, notas_reprobados))

    # Calculamos el promedio por estudiante
    promedios = notas.mean(axis=1)

    # Creamos un DataFrame para ver mejor los datos
    df = pd.DataFrame(notas, columns=[f'Materia {i+1}' for i in range(num_materias)])
    df['Promedio'] = promedios

    return df

# Ejemplo de uso
num_estudiantes = 100
num_materias = 5
resultado = generar_notas(num_estudiantes, num_materias)
print("Estudiantes y sus promedios:")
print(resultado)
print(len(resultado))

# Filtramos para ver el porcentaje de estudiantes con promedio >= 3
estudiantes_aprobados = resultado[resultado['Promedio'] >= 3]
print(estudiantes_aprobados)
print(f"\nNúmero de estudiantes con promedio >= 3: {len(estudiantes_aprobados)}")
print(f"Porcentaje de estudiantes con promedio >= 3: {len(estudiantes_aprobados) / num_estudiantes * 100}%")
