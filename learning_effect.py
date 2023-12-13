import pandas as pd
from scipy.stats import f_oneway


# Check for significance level (e.g., 0.05)
alpha = 0.05

# Read the CSV file into a DataFrame
data = pd.read_csv('results.csv')

# Calculate the block number for each trial
data['Block'] = (data['Trial Number'] - 1) // 15 + 1

# Calculate the average correctness for each participant, block, and condition
avg_correctness = data.groupby(['Participant ID', 'Block', 'Condition'])['Correctness'].mean().reset_index()

# Pivot the data to have each block and condition as a column
pivoted_data = avg_correctness.pivot(index='Participant ID', columns=['Block', 'Condition'], values='Correctness')

# Calculate the average correctness for each block and condition
block_averages = pivoted_data.mean()

# Perform ANOVA on the pivoted data for each condition
for condition in pivoted_data.columns.levels[1]:
    f_statistic, p_value = f_oneway(*[pivoted_data[block][condition] for block in pivoted_data.columns.levels[0]])
    print("\nANOVA Results for Condition", condition)
    print("F-statistic:", f_statistic)
    print("p-value:", p_value)
    if p_value < alpha:
        print("There is a significant difference between blocks for Condition", condition)
    else:
        print("There is no significant difference between blocks for Condition", condition)

# Print the overall block averages
print("\nBlock Averages:")
print(block_averages)

# Perform ANOVA on the pivoted data
f_statistic, p_value = f_oneway(*[pivoted_data[block] for block in pivoted_data.columns.levels[0]])

# Print the overall ANOVA results
print("\nOverall ANOVA Results:")
print("F-statistic:", f_statistic)
print("p-value:", p_value)
