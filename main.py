#MapPlot.py
#Name: Aurora Gunubu    
#Date: 4/20/25
#Assignment: Lab 10

import opioids
import pandas
import matplotlib.pyplot as plt
import numpy as np 

opioid_deaths = opioids.get_opioid_deaths()

years = []
maleDeaths = []
femaleDeaths = []

for x in opioid_deaths:
    year = x["Year"]
    males = x["Rate"]["Opioid"]["Any"]["Sex"]["Male"]
    females = x["Rate"]["Opioid"]["Any"]["Sex"]["Female"]
    
    
    if males or females != 0:
        years.append(year)
        maleDeaths.append(males)
        femaleDeaths.append(females)

        #print(year, males, females)


#Opioid Deaths are decimals, rather have them be integers
def round_integer(opioid_deaths):
    return [int(round(x)) for x in opioid_deaths]

maleDeaths = np.array(maleDeaths)
femaleDeaths = np.array(femaleDeaths)

maleDeaths = round_integer(maleDeaths)
femaleDeaths = round_integer(femaleDeaths)

width = 0.8

fig, ax = plt.subplots()
bottom = np.zeros(len(years))

for sex, deaths in {"Female": femaleDeaths, "Male": maleDeaths}.items():
    s = ax.bar(years, deaths, width, label=sex, bottom=bottom)
    bottom = bottom + deaths
    ax.bar_label(s, label_type="center")

ax.set_title("Opioid Related Deaths by Sex")
ax.set_xlabel("Year")
ax.set_ylabel("Total Deaths Per 100,000 people")
ax.legend()
plt.savefig("output")


df = pandas.DataFrame({"Year": years, "Male Deaths": maleDeaths,
"Female Deaths": femaleDeaths})
print(df)

print ("""The data tells us that opioid use increases yearly, in both males and females. Males tend to die from opioid usage much more frequently than females.
        The visualization helped make this clear by showing a distinction between male and female opioid deaths using different colors in the bar graph.""")