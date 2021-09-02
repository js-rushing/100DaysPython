import pandas as pd

df = pd.read_csv('salaries_by_college_major.csv')

# Panda options
# Display numbers as floats with two decimal places
pd.options.display.float_format = '{:,.2f}'.format

# head() - first five rows of sheet
# pprint(df.head())

# columns - List containing the names of all columns
# print(df.columns)

# isna() - Prints spreadsheet replacing every cell with either 'True' or 'False' based on whether
#          the data in the cell is NaN or not
# print(df.isna())

# tail() - last 5 rows
# print(df.tail())

# dropna() - Remove missing values - Non-destructive
#            DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
# df.dropna()
# print(df.tail())
clean_df = df.dropna()
# print(clean_df.tail())

# Print single column
# print(clean_df['Starting Median Salary'])

# max() - Print max value from single column
# print(clean_df['Starting Median Salary'].max())

# idxmax() - Return index of row with largest value
# print(clean_df['Starting Median Salary'].idxmax())

# .loc - Show desired value at particular location
# print(clean_df['Undergraduate Major'].loc[clean_df['Starting Median Salary'].idxmax()])
# Can also be achieved without using '.loc'
# print(clean_df['Undergraduate Major'][clean_df['Starting Median Salary'].idxmax()])
# Can be used to print entire row
# print(clean_df.loc[43])What am I gonna do with that little rascal?

# CHALLENGE #
# What major has the highest mid-career salary?
# How much do graduates with this major earn?
# Row with highest mid-career salary
# hi_mid_index = clean_df['Mid-Career Median Salary'].idxmax()
# hi_mid_maj = clean_df['Undergraduate Major'][hi_mid_index]
# hi_mid_sal = clean_df['Mid-Career Median Salary'][hi_mid_index]
# print(f"The highest mid-career salary is earned by {hi_mid_maj} graduates earning ${int(hi_mid_sal)} yearly on average.")

# Which major has the lowest starting salary?
# How much to graduates earn after university?
# lo_start_index = clean_df['Starting Median Salary'].idxmin()
# lo_start_maj = clean_df['Undergraduate Major'][lo_start_index]
# lo_start_sal = clean_df['Mid-Career Median Salary'][lo_start_index]
# print(f"The lowest starting salary is earned by {lo_start_maj} graduates earning ${int(lo_start_sal)} yearly on average.")

# Which major has the lowest mid-career salary?
# How much can people expect to ear with this degree?
# lo_mid_index = clean_df['Mid-Career Median Salary'].idxmin()
# lo_mid_maj = clean_df['Undergraduate Major'][lo_mid_index]
# lo_mid_sal = clean_df['Mid-Career Median Salary'][lo_mid_index]
# print(f"The lowest mid-career salary is earned by {lo_mid_maj} graduates earning ${int(lo_mid_sal)} yearly on average.")

# .subtract() - Subtract value from other value
# .insert() - Insert new column into sheet
spread_col = clean_df['Mid-Career 90th Percentile Salary'].subtract(clean_df['Mid-Career 10th Percentile Salary'])
clean_df.insert(1, 'Spread', spread_col)
# print(clean_df.head())

# .sort_values() - Sort by value along either axis
#                  DataFrame.sort_values(by, axis=0, ascending=True, inplace=False, kind='quicksort',
#                  na_position='last', ignore_index=False, key=None)
# CHALLENGE
# Find the degrees with the highest potential? Top 5 with highest 90th percentile values
hi_potential = clean_df.sort_values(by='Mid-Career 90th Percentile Salary', ascending=False)
hi_spread = clean_df.sort_values(by='Spread', ascending=False)
# print(hi_potential[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head())
# print(hi_spread[['Undergraduate Major', 'Spread']].head())

# .groupby() - Group DataFrame using a mapper or by a Series of columns
#              DataFrame.groupby(by=None, axis=0, level=None, as_index=True, sort=True,
#              group_keys=True, squeeze=<no_default>, observed=False, dropna=True)
print(clean_df.groupby('Group').count())

# CHALLENGE
# Use the .mean() method to find the average salary by group?
print(clean_df.groupby('Group').mean())
