# Programa feito para ler o CSV contido na página:
# https://github.com/pandas-dev/pandas/blob/master/doc/data/titanic.csv

from urllib.request import urlopen
import matplotlib.pyplot as plt
import pandas as pd

#Letra a
csv = pd.read_csv("https://raw.githubusercontent.com/pandas-dev/pandas/master/doc/data/titanic.csv", nrows=10)
print("\n")
print("Letra A: \n", csv)
print("\n")

#Letra b
csv = pd.read_csv("https://raw.githubusercontent.com/pandas-dev/pandas/master/doc/data/titanic.csv")
sorted_csv = csv.sort_values(by=["Name"], ascending=True)
print("\n")
print("Letra B: \n", sorted_csv)
print("\n")

#Letra c
csv = pd.read_csv("https://raw.githubusercontent.com/pandas-dev/pandas/master/doc/data/titanic.csv")
csv.insert(2, "Sobrevivente", "Não")

for i in range(len(csv)): 
    if csv["Survived"][i] == 1: 
        csv["Sobrevivente"][i]="Sim"

print("\n")
print("Letra C: \n", csv)
print("\n")

#Letra d
csv = csv.drop(columns=['SibSp', 'Parch', 'Ticket'])

print("\n")
print("Letra D: \n", csv)
print("\n")

#Letra e
csv = csv.rename(columns={"PassengerId" : "IdPassageiro", "Survived": "Sobreviveu", "Pclass" : "PClasse", "Name": "Nome", "Sex": "Sexo", "Age": "Idade", "Fare": "Tarifa", "Cabin": "Cabine", "Embarked": "Embarcou"})

print("\n")
print("Letra E: \n", csv)
print("\n")

#Letra f
for i in range(len(csv)): 
    if csv["Sexo"][i] == "male": 
        csv["Sexo"][i]="masculino"
    if csv["Sexo"][i] == "female": 
        csv["Sexo"][i]="FEMININO"

print("\n")
print("Letra F: \n", csv)
print("\n")

#Letra g
filtered_csv1 = csv.drop(columns=['IdPassageiro', 'Sobrevivente', 'Nome', 'Sexo', 'Idade', 'Tarifa', 'Cabine', 'Embarcou'])
filtered_csv1 = filtered_csv1.groupby(['PClasse']).sum()

print("\n")
print("Letra G: \n", filtered_csv1)
print("\n")

#Letra h
filtered_csv2 = csv.drop(columns=['IdPassageiro', 'Sobrevivente', 'Nome', 'PClasse', 'Idade', 'Tarifa', 'Cabine', 'Embarcou'])
filtered_csv2 = filtered_csv2.groupby(['Sexo']).sum()

print("\n")
print("Letra H: \n", filtered_csv2)
print("\n")

#Letra j
csv.to_excel("output.xlsx", sheet_name='Sheet_name_1')

#Letra i
filtered_csv1.plot(x='Sobreviveu', y='PClasse')
plt.show()
