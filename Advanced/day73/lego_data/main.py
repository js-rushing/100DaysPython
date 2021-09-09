import pandas as pd
import matplotlib.pyplot as plt

color_df = pd.read_csv('./data/colors.csv')
set_df = pd.read_csv('./data/sets.csv')
theme_df = pd.read_csv('./data/themes.csv')

# print(color_df.shape)
# print(color_df.nunique())

# Find number of unique colors
unique_colors = color_df['name'].nunique()

# Find number of transparent blocks
transparent_blocks = color_df.groupby('is_trans').count()
trans_block_count = color_df.is_trans.value_counts()

# print(f'unique colors: {unique_colors}')
# print(transparent_blocks)
# print(trans_block_count)

# SETS
# In which year were the first LEGO sets released and what were these sets called?
earliest_year = set_df.year.min()
latest_year = set_df.year.max()
# print(set_df.loc[set_df['year'] == earliest_year])

# What are the top 5 LEGO sets with the most parts?
# print(set_df.sort_values('num_parts', ascending=False).head())

# Use .groupby() and .count() to show the number of LEGO sets released
# year-by-year.  How do the number of sets released in 1955 compare to
# number of sets released in 2019?
sets_by_year = set_df.groupby('year').count()
# print(sets_by_year['set_num'].head())

# Visualize with matplotlib
roll_df = set_df.rolling(window=6).mean()
# plt.xlabel('Year')
# plt.ylabel('Sets')
# plt.ylim(earliest_year, latest_year)
# plt.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2])
# plt.legend()

# plt.show()

# USE .agg() FUNCTION
# USE .agg() FUNCTION
# Work out the number of different themes by year
themes_by_year = set_df.groupby('year').agg({'theme_id': pd.Series.nunique})
# Give column more appropriate name
themes_by_year.rename(columns={'theme_id': 'nr_themes'}, inplace=True)
# print(themes_by_year.head())

# Visualize with matplotlib
# roll_df = themes_by_year.rolling(window=6).mean()
# plt.xlabel('Year')
# plt.ylabel('Themes')
# plt.ylim(0, 150)
# plt.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2])
# plt.show()

# SUPERIMPOSE LINE CHARTS WITH SEPARATE AXES
# SUPERIMPOSE LINE CHARTS WITH SEPARATE AXES

# Looks terrible
# plt.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2])
# plt.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2])
# plt.show()
# The number of themes and the number of sets have very different scales

# Two Separate Axes
# get current axes
# ax1 = plt.gca()
# ax2 = ax1.twinx()

# Add styling
# ax1.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2], color='g')
# ax2.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2], color='b')

# ax1.set_xlabel('Year')
# ax1.set_ylabel('Number of Sets', color='green')
# ax2.set_ylabel('Number of Themes', color='blue')
# plt.show()

# SCATTER PLOTS
# SCATTER PLOTS
# Challenge
# Create a Pandas Series called parts_per_set that has the year as the index and
# contains the average number of parts per LEGO set in that year.
parts_per_set = set_df.groupby('year').agg({'num_parts': pd.Series.mean})
# print(parts_per_set.head())
# print(parts_per_set.tail())

# Challenge
# See if you can use the Matplotlib documentation to generate the scatter plot chart.
# Do you spot a trend in the chart? Again, you'll have to exclude the last two observations.
# plt.scatter(parts_per_set.index[:-2], parts_per_set.num_parts[:-2])
# plt.show()

# RELATIONAL DATABASE SCHEMAS
# RELATIONAL DATABASE SCHEMAS
# Count the number of sets per Theme
set_theme_count = set_df.theme_id.value_counts()
# print(set_theme_count[:5])

# Challenge
# How many id's correspond to the 'Star Wars' name in the themes.csv
star_wars_themes = theme_df[theme_df['name'] == 'Star Wars']
# print(star_wars_themes)

# Use the id's you just found and look for the corresponding sets in the sets.csv
# print(set_df[set_df.theme_id == 18])
# print(set_df[set_df.theme_id == 209])

# MERGE DATAFRAMES AND CREATE BAR CHARTS
# MERGE DATAFRAMES AND CREATE BAR CHARTS
# Give names to set_theme_count columns
# Convert Panda Series into a Pandas DataFrame
set_theme_count = pd.DataFrame({'id': set_theme_count.index,
                                'set_count': set_theme_count.values})
# print(set_theme_count.head())

# Merge two DataFrames
# To .merge() two DataFrames along a particular column, we need to provide
# our two DataFrames and then the column name on which to merge. This is why
# we set on='id'. Both our set_theme_count and our theme_df DataFrames have a
# column with this name.
merged_df = pd.merge(set_theme_count, theme_df, on='id')
# print(merged_df[:3])

# Creating a Bar Chart
# Add styling
plt.figure(figsize=(14, 8))
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)
plt.ylabel('Nr of Sets', fontsize=14)
plt.xlabel('Theme Name', fontsize=14)

plt.bar(merged_df.name[:10], merged_df.set_count[:10])
plt.show()
