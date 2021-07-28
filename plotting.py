import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv", header=1)

#renaming values
data.loc[:,"Position"] = data["Position"].replace({
    0:"middle",
    300:"right",
    -300:"left"
})

data.loc[:,"Colour"] = data["Colour"].replace({
    "Colour(red=200, green=200, blue=200)":"grey",
    "Colour(red=0, green=255, blue=0)":"green",
    "Colour(red=0, green=0, blue=255)":"blue"
})

data.loc[:,"Button"] = data["Button"].replace({
    98:"B",
    102:"F",
    106:"J"
})


print(data)
