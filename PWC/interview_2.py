# 3. What do you understand by SQL merge / Pandas merge?

import pandas as pd

# First dataframe -

df1 = pd.DataFrame({
    "city": ["New York", "Chicago", "Orlando", "Baltimore"],
    "temperature": [21, 14, 35, 32],
})
print('Data-Frame:1', df1)

# Second dataframe -

df2 = pd.DataFrame({
    "city": ["Chicago", "New York", "Orlando"],
    "humidity": [65, 68, 75],
})
print("Data-Frame:2", df2)

# Joining based on column:

df3 = pd.merge(df1, df2, on="city")
print("Data-Frame:3", df3)

# Joining based on column and type:

df3 = pd.merge(df1, df2, on="city", how="inner")
print("Data-Frame:3", df3)

# Indicator Flag shows which columns came from which table:

df3 = pd.merge(df1, df2, on="city", how="inner", indicator=True)
print("Data-Frame:3", df3)

# Suffixes Flag shows which columns came from which table:

df3 = pd.merge(df1, df2, on="city", how="inner", indicator=True)
print("Data-Frame:3", df3)
