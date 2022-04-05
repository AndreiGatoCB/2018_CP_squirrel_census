import csv

import pandas

data = pandas.read_csv("weather_data.csv")

data_dict = data.to_dict()
monday = data[data.day == "Monday"]
monday_f = (monday.temp * 9/5) + 32
print(monday_f)

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
datos = pandas.DataFrame(data_dict)
datos.to_csv("new_data.csv")

ardillas = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
ardillas_grises_cuenta = len(ardillas[ardillas["Primary Fur Color"] == "Gray"])
ardillas_rojas_cuenta = len(ardillas[ardillas["Primary Fur Color"] == "Cinnamon"])
ardillas_negras_cuenta = len(ardillas[ardillas["Primary Fur Color"] == "Black"])

print(ardillas_grises_cuenta)
print(ardillas_rojas_cuenta)
print(ardillas_negras_cuenta)

ardillas_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [ardillas_grises_cuenta, ardillas_rojas_cuenta, ardillas_negras_cuenta]
}

df = pandas.DataFrame(ardillas_dict)
df.to_csv("ardillas_conteo.csv")