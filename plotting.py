import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv", header=1)

#renaming values
data.loc[:,"Position"] = data["Position"].replace({
    0:"middle",
    350:"right",
    -350:"left"
})

data.loc[:,"Colour"] = data["Colour"].replace({
    "Colour(red=200, green=200, blue=200)":"white",
    "Colour(red=0, green=255, blue=0)":"green",
    "Colour(red=0, green=0, blue=255)":"blue"
})

data.loc[:,"Button"] = data["Button"].replace({
    98:"white",
    100:"green",
    107:"blue"
})


def check_Congruency(row):
    but = row["Button"]
    pos = row["Position"]
    if but == "white":
        return "no"
    if (but == "green" and pos== "left") or (but== "blue" and pos== "right"):
        return "congruent"
    if (but == "green" and pos== "right") or (but== "blue" and pos== "left"):
        return "incongruent"


data["Correctness"] = data["Colour"] == data["Button"]
data = data.loc[data['Correctness'] == True]
data["Congruency"] = data.apply(lambda row: check_Congruency(row), axis=1)

print(data)
