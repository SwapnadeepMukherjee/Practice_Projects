# Question 1:
#
# Write a program to take an array as an input and print the count of the number of occurances of each element of the array.
#
# Solution_Approach:

# # import requests
# # import json
# # from collections import Counter
# import pandas as pd
#
# # input: "2,2,2,4,4,1,1"
# # Output:
# # 2 -> 3
# # 4 -> 2
#
# data = list(map(str, input("Enter Input List").split(",")))
# print("Initial List", data)
#
# # list2 = list(set(data))
#
# # list4 = []
# # for i in range(len(data)):
# #     count1 = 0
# #     for j in range(i, len(data)):
# #         if data[i] == data[j]:
# #             count1 += 1
# #     print("Count", count1)
# #     if count1 > 1:
# #         if data[i] not in list4:
# #             list4.append(data[i])
#
# # print("Final list", list4)
# # print("Count", count1)
#
# print(pd.Series(data).value_counts())

# Question 2:
#
# Write a program to remove top row from a dataframe.
#
# Solution_Approach:

import numpy as np
import pandas as pd

df = pd.read_csv(
    "D:\Study\Data_Science_CourseWork\Academic_Data\Statistics & EDA\GDP Assesment\Video_Games_Sales_as_at_22_Dec_2016.csv")
print("Initial dataframe", df)
df1 = df.drop(df.head(0).index, inplace=True, axis=0)
print("Modified dataframe", df1)

# https://www.geeksforgeeks.org/remove-last-n-rows-of-a-pandas-dataframe/
