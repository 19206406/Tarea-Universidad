
import pandas as pd
import numpy as np

llantas = pd.read_excel('llantas.xlsx')
# nueva libreria openpyxl 

#print(llantas)

print(llantas.shape) # Tamanho del DataFrame

print(llantas.head()) # Cual son los nombres de las cabeceras
