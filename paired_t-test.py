import pandas as pd
from scipy import stats
import statsmodels.api as sm
from statsmodels.stats.anova import AnovaRM
import matplotlib.pyplot as plt
import seaborn as sns


# Load the data
df = pd.read_csv('results.csv')

# Calculate response time
df['Response Time'] = (pd.to_datetime(df['End Timestamp']) - pd.to_datetime(df['Start Timestamp'])).dt.total_seconds()

# Convert 'Correctness' to integers
df['Correctness'] = df['Correctness'].astype(int)

# Assuming you have a 'Condition' column in your data
conditions = ['V', 'VH', 'H']

# Paired t-tests for Response Time
for i in range(len(conditions)):
    for j in range(i+1, len(conditions)):
        condition1 = df[df['Condition'] == conditions[i]]['Response Time']
        condition2 = df[df['Condition'] == conditions[j]]['Response Time']
        t_stat, p_val = stats.ttest_rel(condition1, condition2)
        print(f"Paired t-test for Response Time between {conditions[i]} and {conditions[j]}: t = {t_stat}, p = {p_val}")

# Paired t-tests for Correctness
for i in range(len(conditions)):
    for j in range(i+1, len(conditions)):
        condition1 = df[df['Condition'] == conditions[i]]['Correctness']
        condition2 = df[df['Condition'] == conditions[j]]['Correctness']
        t_stat, p_val = stats.ttest_rel(condition1, condition2)
        print(f"Paired t-test for Correctness between {conditions[i]} and {conditions[j]}: t = {t_stat}, p = {p_val}")

# Aggregate the data by taking the mean response time and correctness for each subject and condition
df_agg = df.groupby(['Participant ID', 'Condition'])[['Response Time', 'Correctness']].mean().reset_index()

# Replace space in column name with underscore
df_agg = df_agg.rename(columns={'Participant ID': 'Participant_ID'})

# Repeated measures ANOVA for Response Time
anova_rt = AnovaRM(df_agg, 'Response Time', 'Participant_ID', within=['Condition'])
res_rt = anova_rt.fit()

print(res_rt)

# Repeated measures ANOVA for Correctness
anova_corr = AnovaRM(df_agg, 'Correctness', 'Participant_ID', within=['Condition'])
res_corr = anova_corr.fit()

print(res_corr)

# Calculate standard deviation for Response Time
for condition in conditions:
    sd = df[df['Condition'] == condition]['Response Time'].std()
    print(f"Standard Deviation of Response Time for {condition}: {sd}")

# Calculate standard deviation for Correctness
for condition in conditions:
    sd = df[df['Condition'] == condition]['Correctness'].std()
    print(f"Standard Deviation of Correctness for {condition}: {sd}")

# Create a barplot for the mean Response Time for each condition
sns.barplot(x='Condition', y='Response Time', data=df_agg, palette='Set2', ci='sd')
plt.title('Mean Response Time for Each Condition')
plt.show()

# Create a barplot for the mean Correctness for each condition
sns.barplot(x='Condition', y='Correctness', data=df_agg, palette='Set2', ci='sd')
plt.title('Mean Correctness for Each Condition')
plt.show()

# Create a strip plot for the individual Response Time for each condition
sns.stripplot(x='Condition', y='Response Time', data=df, palette='Set2')
plt.title('Individual Response Time for Each Condition')
plt.show()

# Calculate the mean correctness for each participant in each condition
df_agg = df.groupby(['Condition', 'Participant ID'])['Correctness'].mean().reset_index()

# Create a point plot for the mean correctness for each participant in each condition
sns.pointplot(x='Condition', y='Correctness', data=df_agg, palette='Set2', ci='sd')
plt.title('Mean Correctness for Each Participant in Each Condition')
plt.show()

# Create a violin plot for the Response Time for each condition
sns.violinplot(x='Condition', y='Response Time', data=df, palette='Set2')
plt.title('Response Time Distribution for Each Condition')
plt.show()

participant_mean_correctness = df.groupby(['Participant ID', 'Condition'])['Correctness'].mean().reset_index()

# Create violin plots for Correctness
plt.figure(figsize=(10, 6))
sns.violinplot(x='Condition', y='Correctness', data=participant_mean_correctness, inner='stick', palette='Set2')
plt.title("Correctness by Condition with Violin Plot")
plt.xlabel("Condition")
plt.ylabel("Mean Correctness")
plt.xticks(rotation=45)
plt.show()