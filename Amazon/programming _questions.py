# Question 1:
#
# Write a program to take an array as an input and print the count of the number of occurrences of each element of the array.
#
# input: "2,2,2,4,4,1,1"
# Output:
# 2 -> 3
# 4 -> 2
#
# Solution_Approach:


# Approach - 1:
import pandas as pd

data = list(map(str, input("Enter Input List").split(",")))
print("Initial List", data)

print(pd.Series(data).value_counts())

# Approach - 2:

# list2 = list(set(data))
# list4 = []

# for i in range(len(data)):
#     count1 = 0
#     for j in range(i, len(data)):
#         if data[i] == data[j]:
#             count1 += 1
#     print("Count", count1)
#     if count1 > 1:
#         if data[i] not in list4:
#             list4.append(data[i])

# print("Final list", list4)
# print("Count", count1)

# Question 2:
#
# Write a program to remove top n row(s) from a dataframe.
#
# Solution_Approach:

import pandas as pd

df = pd.read_csv(
    "D:\Study\Data_Science_CourseWork\Academic_Data\Statistics & EDA\GDP Assesment\Video_Games_Sales_as_at_22_Dec_2016.csv")
print("Initial dataframe", df)

n = 3
df.drop(df.head(n).index, inplace=True)

print("Modified dataframe", df)

# Reference -
# 1. https://sparkbyexamples.com/pandas/pandas-drop-first-n-rows-from-dataframe/
# 2. https://stackoverflow.com/questions/16396903/delete-the-first-three-rows-of-a-dataframe-in-pandas

# Question 3:
#
# Write a program to remove bottom n row(s) from a dataframe.
#
# Solution_Approach:

import pandas as pd

df = pd.read_csv(
    "D:\Study\Data_Science_CourseWork\Academic_Data\Statistics & EDA\GDP Assesment\Video_Games_Sales_as_at_22_Dec_2016.csv")
print("Initial dataframe", df)

# 1. First -

df.drop(df.tail(3).index, inplace=True, axis=0)
print("Modified dataframe", df)

# 2. Second -

# df1 = df[:-3]
# print("Modified dataframe", df1)

# 3. Thrid -

# df1 = df.iloc[:-3]
# print("Modified dataframe", df1)

# 4. Fourth -

# df1 = df.head(3)
# print("Modified dataframe", df1)

# Reference -
# 1. https://www.geeksforgeeks.org/remove-last-n-rows-of-a-pandas-dataframe/
