import pandas as pd
import matplotlib.pyplot as plt
import os

# Create DataFrame and provide column names
df = pd.read_csv('QueryResults.csv', header=0, names=['DATE', 'TAG', 'POSTS'])

# Panda options
# Display numbers as floats with two decimal places
pd.options.display.float_format = '{:,.2f}'.format

# print(df.head())
# print(df.tail())

# DataFrame table dimensions - (rows, columns)
# print(df.shape)

# print(df.count())

# Array of unique values in the TAG column
lang_list = df.TAG.unique()

# print(df.groupby('TAG').sum())
# print(df.groupby('TAG').count())
# print(df.TAG.value_counts())

# CONVERT DATE STRINGS TO DATETIME OBJECTS
# print(df.DATE[1])
# print(type(pd.to_datetime(df.DATE[1])))
# print(df.head())
df.DATE = pd.to_datetime(df.DATE)
# print(df.head())

# Pivot
# Mini-Challenge - pivot the df so that each row is a date and each column is a language
reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
reshaped_df.fillna(0, inplace=True)
column_names = reshaped_df.columns
# print(reshaped_df)
# print(column_names)

# Using pandas.rolling() & pandas.mean() to smooth out chart lines
roll_df = reshaped_df.rolling(window=6).mean()

# Resize chart
plt.figure(figsize=(16, 10))

# Increase fontsize
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

# Create chart labels
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)

# set limits for y-axis
plt.ylim(0, 35000)

# Plot chart
# Java
# plt.plot(reshaped_df.index, reshaped_df.java)
# WORKS THE SAME
# plot = plt.plot(reshaped_df.java)

# Python
# plt.plot(reshaped_df.index, reshaped_df.python)

# Plot all languages with for loop
for column in roll_df.columns:
    plt.plot(roll_df[column], linewidth=3, label=reshaped_df[column].name)

# Create chart legend
plt.legend(fontsize=16)

plt.show()
