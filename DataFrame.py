import matplotlib.pyplot as plt

years = [1950, 1970, 1990, 2010]

population = [2.519, 3.692, 5.263, 6.972]
deaths = [1.519, 1.629, 10.263, 2.972]

plt.title("Población anual")

plt.xlabel("Año")
plt.ylabel("Población")


plt.plot(years, population, "r")
plt.plot(years, deaths, "g")
plt.scatter(years, population, color = "orange")
plt.scatter(years, deaths, color = "b")
plt.legend(["crecimiento", "muertes"])

plt.show()