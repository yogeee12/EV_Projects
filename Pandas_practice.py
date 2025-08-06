import pandas as pd

data = pd.read_csv(r".\EV_projects\Book1.csv")

s1 = data.loc[data["Name"] == "Divya"]
# print(s1)

data2 = pd.read_excel(r".\EV_projects\netflix_titles.xlsx")
print(data2.head())