import pandas as pd
import matplotlib.pyplot as plt

# Data
tests = ['Haptic vs. Visuohaptic', 'Haptic vs. Visual', 'Visuohaptic vs. Visual']
t_statistic = [-6.67, -4.45, 2.20]
p_value = [4.14, 9.48, 0.027]
background_color = '#242424'
text_color = 'white'
line_color = 'white'
cell_colors = [background_color, background_color, background_color]  # Bar color for cells

# Create a DataFrame for the t-test results
data = {'Test': tests, 'T-Statistic': t_statistic, 'P-Value': p_value}
df = pd.DataFrame(data)

# Create a table
fig, ax = plt.subplots(figsize=(8, 4))
ax.axis('tight')
ax.axis('off')

# Set the table background color
ax.set_facecolor(background_color)

# Create the table with custom cell colors
table = ax.table(cellText=df.values, colLabels=df.columns, cellColours=[cell_colors]*len(df), loc='center', cellLoc='center')

# Set text color and line color
for i, key in enumerate(table.get_celld().keys()):
    cell = table.get_celld()[key]
    if key[0] == 0:
        cell.set_text_props(weight='bold', color=text_color)
        cell.set_fontsize(12)
        cell.set_facecolor(background_color)
    else:
        cell.set_fontsize(12)
        cell.set_text_props(color=text_color)
        cell.set_facecolor(background_color)
    if key[1] == 0:
        cell.set_facecolor(background_color)

# Adjust the column widths for better formatting
table.auto_set_column_width([0, 1, 2])

plt.title('T-Test Results for Different Conditions', color=text_color)

plt.show()
