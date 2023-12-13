import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

def perform_anova(data_file):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(data_file)

    # Rename the 'Reaction Time' column to 'Reaction_Time'
    df.rename(columns={'Reaction Time': 'Reaction_Time'}, inplace=True)

    # Convert columns to appropriate data types
    df['Reaction_Time'] = df['Reaction_Time'].astype(float)
    df['Correctness'] = df['Correctness'].astype(bool)
    df['Correctness'] = df['Correctness'].astype(int)  # Convert True/False to 1/0
    df['Condition'] = df['Condition'].astype('category')

    # Perform ANOVA for Reaction Time
    reaction_time_anova = ols('Reaction_Time ~ Condition', data=df).fit()
    reaction_time_anova_table = sm.stats.anova_lm(reaction_time_anova, typ=2)

    # Perform ANOVA for Correctness
    correctness_anova = ols('Correctness ~ Condition', data=df).fit()
    correctness_anova_table = sm.stats.anova_lm(correctness_anova, typ=2)

    return reaction_time_anova_table, correctness_anova_table

if __name__ == "__main__":
    data_file = 'results.csv'
    reaction_time_anova_table, correctness_anova_table = perform_anova(data_file)

    print("ANOVA for Reaction Time:")
    print(reaction_time_anova_table)

    print("\nANOVA for Correctness:")
    print(correctness_anova_table)
