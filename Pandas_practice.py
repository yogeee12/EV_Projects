import pandas as pd

data = pd.read_csv(r"C:/Users/Documents/Book1.csv")
print(type(data))
df = pd.DataFrame(data)
print(type(data))
# print(df)