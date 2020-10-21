import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import linear_model

rawData = pd.read_csv("StudentsPerformance.csv")

#print(rawData.info())

dataNeeded = rawData.drop(['reading score', "writing score"], axis = 1)

femaleFilter = dataNeeded['gender'].isin(['female'])
maleFilter = dataNeeded['gender'].isin(['male'])

#print(dataNeeded)

femaleData = dataNeeded[femaleFilter]
maleData = dataNeeded[maleFilter]

femaleMathScoreAverage = np.average(femaleData["math score"])
maleMathScoreAverage = np.average(maleData["math score"])

#print(femaleMathScoreAverage)
#print(maleMathScoreAverage)

plt.figure()

#grafica promedio en pruebas de matematicas por genero
plt.subplot(3, 2, 1)
plt.title("Promedio de pruebas de matemáticas por género")

plt.bar([1], [maleMathScoreAverage], color = "blue")
plt.bar([2], [femaleMathScoreAverage], color = "pink")

plt.legend(['Hombres', 'Mujeres'])

plt.xlabel('Genero')
plt.ylabel('Puntaje')

#analisis por etnia

gAFilter = dataNeeded["race/ethnicity"].isin(["group A"])
gBFilter = dataNeeded["race/ethnicity"].isin(["group B"])
gCFilter = dataNeeded["race/ethnicity"].isin(["group C"])
gDFilter = dataNeeded["race/ethnicity"].isin(["group D"])
gEFilter = dataNeeded["race/ethnicity"].isin(["group E"])

gAData = dataNeeded[gAFilter]
gBData = dataNeeded[gBFilter]
gCData = dataNeeded[gCFilter]
gDData = dataNeeded[gDFilter]
gEData = dataNeeded[gEFilter]

gAMathScore = gAData["math score"]
gBMathScore = gBData["math score"]
gCMathScore = gCData["math score"]
gDMathScore = gDData["math score"]
gEMathScore = gEData["math score"]

gAScoreAverage = np.average(gAMathScore)
gBScoreAverage = np.average(gBMathScore)
gCScoreAverage = np.average(gCMathScore)
gDScoreAverage = np.average(gDMathScore)
gEScoreAverage = np.average(gEMathScore)

#Grafica promedio en pruebas de matematicas por etnia
plt.subplot(3, 2, 2)
plt.title("Promedio en pruebas de matemáticas por etnia")

plt.bar(1, gAScoreAverage, color = "r")
plt.bar(2, gBScoreAverage, color = "g")
plt.bar(3, gCScoreAverage, color = "b")
plt.bar(4, gDScoreAverage, color = "yellow")
plt.bar(5, gEScoreAverage, color = "cyan")

plt.legend(["grupo A", "grupo B", "grupo C", "grupo D", "grupo E"])

plt.xlabel("Grupo")
plt.ylabel("Puntaje")

#analisis por nivel educativo de los padres
BDFilter = dataNeeded["parental level of education"].isin(["bachelor´s degree"])
SCFilter = dataNeeded["parental level of education"].isin(["some college"])
MDFilter = dataNeeded["parental level of education"].isin(["master´s degree"])
ADFilter = dataNeeded["parental level of education"].isin(["associate's degree"])
HSFilter = dataNeeded["parental level of education"].isin(["high school"])

BDData = dataNeeded[BDFilter]
SCData = dataNeeded[SCFilter]
MDData = dataNeeded[MDFilter]
ADData = dataNeeded[ADFilter]
HSData = dataNeeded[HSFilter]

BDMathScore = BDData["math score"]
SCMathScore = SCData["math score"]
MDMathScore = MDData["math score"]
ADMathScore = ADData["math score"]
HSMathScore = HSData["math score"]

BDScoreAverage = np.average(BDMathScore)
SCScoreAverage = np.average(SCMathScore)
MDScoreAverage = np.average(MDMathScore)
ADScoreAverage = np.average(ADMathScore)
HSScoreAverage = np.average(HSMathScore)

#gráfica promedio en pruebas de matemáticas por nivel educativo ed los padres
plt.subplot(3, 2, 3)
plt.title("promedio de pruebas de matemáticas por nivel educativo de los padres") 

plt.bar(1, SCScoreAverage, color = "g")
plt.bar(2, HSScoreAverage, color = "cyan")
plt.bar(3, ADScoreAverage, color = "yellow")
plt.bar(4, BDScoreAverage, color = "r")
plt.bar(5, MDScoreAverage, color = "b")

plt.legend(["bachelor´s degree", "some college", "master´s degree", "associate´s degree", "high school"])

plt.xlabel("Nivel educativo")
plt.ylabel("Puntaje")

#analisis por alimentación

standardFilter = dataNeeded['lunch'].isin(['standard'])
reducedFilter = dataNeeded['lunch'].isin(['free/reduced'])

standardData = dataNeeded[standardFilter]
reducedData = dataNeeded[reducedFilter]

standardMathScore = standardData['math score']
reducedMathScore = reducedData['math score']

standardScoreAverage = np.average(standardMathScore)
reducedScoreAverage = np.average(reducedMathScore)

plt.subplot(3, 2, 4)
plt.title("Promedio de pruebas de matemáticas por grado de alimentación")

plt.bar(1, standardScoreAverage, color = "g")
plt.bar(2, reducedScoreAverage, color = "r")

plt.legend(["standard", "free/reduced"])

plt.xlabel("tipo de alimentación")
plt.ylabel("promedio en matemáticas")

#analisis por test de preparación

noneFilter = dataNeeded["test preparation course"].isin(["none"])
completedFilter = dataNeeded["test preparation course"].isin(["completed"])

noneData = dataNeeded[noneFilter]
completedData = dataNeeded[completedFilter]

noneMathScore = noneData["math score"]
completedMathScore = completedData["math score"]

noneScoreAverage = np.average(noneMathScore)
completedScoreAverage = np.average(completedMathScore)

plt.subplot(3, 2, 5)

plt.title("Promedio de pruebas de matemáticas por preparación")

plt.bar(1, noneScoreAverage, color = "r")
plt.bar(2, completedScoreAverage, color = "g")

plt.legend(["none", "completed"])

plt.xlabel("preparación")
plt.ylabel("promedio en matemáticas")

plt.subplot(3, 2, 6)

plt.title('relacion entre el score de matematicas y lectura')

plt.scatter(rawData['reading score'], rawData['math score'], color = 'r')
plt.legend(['pruebas de matematicas'])

plt.ylabel('math score')
plt.xlabel('reading score')

reg = linear_model.LinearRegression()

print(rawData['math score'])
print(rawData[['math score']])

reg.fit(rawData[['reading score']], rawData['math score'])

mathScorePredict = reg.predict(rawData[['reading score']])

#print(mathScorePredict)

plt.plot(rawData['reading score'], mathScorePredict, color = 'b')

#plt.show()

#print(reg.coef_)
#print(reg.intercept_)

#print(reg.coef_ * 70 + reg.intercept_) y = mx + b donde m es el coeficiente, la x es la entrada y b es la intercepción o error

plt.show()
