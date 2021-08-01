"""This programm plots the data accumulated from the Simon Task"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

# reading the data
data = pd.read_csv("data.csv", header=1)

# renaming values
data.loc[:,"Position"] = data["Position"].replace({
    0: "middle",
    350: "right",
    -350: "left"
})

data.loc[:,"Colour"] = data["Colour"].replace({
    "Colour(red=255, green=255, blue=255)": "white",
    "Colour(red=0, green=255, blue=0)": "green",
    "Colour(red=0, green=0, blue=255)": "blue"
})

data.loc[:,"Button"] = data["Button"].replace({
    98: "white",
    100: "green",
    107: "blue"
})

# filtering data for correct button presses
data["Correctness"] = data["Colour"] == data["Button"]
data = data.loc[data['Correctness'] == True]

def check_congruency(row):
    """
    Args:
        row     (Series)     row in the dataframe

    checks which button is pressed with which stimuli

    Returns:
        baseline  -  if we have baseline condition (i.e. white button pressed)
        congruent -  if colour/stimulus appears on same side as it's button is located
        incongruent - if colour/stimulus appears on different side that the button's location
    """
    but = row["Button"]
    pos = row["Position"]
    if but == "white":
        return "baseline"
    if (but == "green" and pos == "left") or (but == "blue" and pos == "right"):
        return "congruent"
    if (but == "green" and pos == "right") or (but == "blue" and pos == "left"):
        return "incongruent"

# applying check_congruency function on every row
data["Congruency"] = data.apply(lambda row: check_congruency(row), axis=1)

# printing basic information about data
print(data.info())

# deleting outliers in data with zscore > 3
data_cleaned = data[(np.abs(stats.zscore(data['RT'])) < 3)]

# getting main experiment data
data_main = data_cleaned.loc[data_cleaned['Trials'] == 'Main']

# calculating mean of RT for every congruency condition
mean_RT = data_main.groupby('Congruency', as_index=False)['RT'].mean().round(3)

# plotting data
ax = sns.barplot(x="Congruency", y="RT", data=mean_RT)
plt.show()
