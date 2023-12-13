import matplotlib.pyplot as plt

# Data
conditions = ['Haptic', 'Visual', 'Visuohaptic']
correctness = [0.64, 0.76, 0.82]
response_time = [10.78, 9.17, 9.05]
background_color = '#242424'
text_color = 'white'
line_color = 'white'
bar_color = '#05c3b4'

# Set the figure and axis background color
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
fig.patch.set_facecolor(background_color)
ax1.set_facecolor(background_color)
ax2.set_facecolor(background_color)

# Bar chart for Correctness by Condition
ax1.bar(conditions, correctness, color=bar_color)
ax1.set_xlabel('Condition', color=text_color)
ax1.set_ylabel('Correctness', color=text_color)
ax1.set_title('Correctness by Condition', color=text_color)
ax1.set_ylim(0, 1)
ax1.tick_params(axis='x', colors=text_color)
ax1.tick_params(axis='y', colors=text_color)
ax1.spines['bottom'].set_color(line_color)
ax1.spines['top'].set_color(line_color)
ax1.spines['right'].set_color(line_color)
ax1.spines['left'].set_color(line_color)

# Bar chart for Response Time by Condition
ax2.bar(conditions, response_time, color=bar_color)
ax2.set_xlabel('Condition', color=text_color)
ax2.set_ylabel('Response Time', color=text_color)
ax2.set_title('Response Time by Condition', color=text_color)
ax2.tick_params(axis='x', colors=text_color)
ax2.tick_params(axis='y', colors=text_color)
ax2.spines['bottom'].set_color(line_color)
ax2.spines['top'].set_color(line_color)
ax2.spines['right'].set_color(line_color)
ax2.spines['left'].set_color(line_color)

plt.tight_layout()

plt.show()
