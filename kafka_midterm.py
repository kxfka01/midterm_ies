
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import plotly.graph_objs as go




# part 2 
#2pt task 1 - answ 45

import pandas as pd 

df = pd.read_csv('/Users/lukaskafka/Desktop/IES_Midterm/companies_no_subindustry.csv')
print(df.included.isna().sum())

#2pt task 2 (rest of the code doesn't work when written as usual code because of error)

# df = pd.read_csv('/Users/lukaskafka/Desktop/IES_Midterm/companies_no_subindustry.csv')
# df.dropna(subset=["included"], inplace=True)
# print(df.dropna(subset=["included"], inplace=True))

# import pandas as pd
# file_path = "/Users/lukaskafka/Desktop/IES_Midterm/companies_no_subindustry.csv"
# df = pd.read_csv(file_path)
# df["Founded"] = pd.to_datetime(df["Founded"])
# earliest_date = df["Founded"].min()
# latest_date = df["Founded"].max()
# print("earliest_date")
# print("latest_date")

#2pt task 3

#2pt task 4

#2pt task 5
import pandas as pd

df1 = pd.read_csv('/Users/lukaskafka/Desktop/IES_Midterm/companies_no_subindustry.csv')
df2 = pd.read_csv('/Users/lukaskafka/Desktop/IES_Midterm/companies_subindustry.csv')

merged_df = pd.merge(df1, df2, on="Symbol")
merged_df = pd.merge(df1, df2, on="Symbol", how='left')
print(merged_df)
