import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
data = pd.read_csv('results.csv')

# Convert Sample Number into a numerical variable (assuming it's categorical)
data['Sample Number'] = data['Sample Number'].astype(int)

# Correlation analysis between Sample Number and Reaction Time
correlation_reaction_time = data['Sample Number'].corr(data['Reaction Time'])

# Correlation analysis between Sample Number and Correctness
correlation_correctness = data['Sample Number'].corr(data['Correctness'])

# Regression analysis for Reaction Time
reaction_time_model = sns.lmplot(x='Sample Number', y='Reaction Time', data=data)

# Regression analysis for Correctness
correctness_model = sns.lmplot(x='Sample Number', y='Correctness', data=data, logistic=True)

# Display the results
print("Correlation between Sample Number and Reaction Time:", correlation_reaction_time)
print("Correlation between Sample Number and Correctness:", correlation_correctness)

plt.show()  # Show the regression plots
