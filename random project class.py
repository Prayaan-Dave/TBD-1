import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# Create a playful dataset
np.random.seed(42)
categories = ['A', 'B', 'C', 'D', 'E']
values = np.random.randint(10, 100, size=len(categories))
df = pd.DataFrame({
    'Category': categories,
    'Value': values
})

# Create a custom colormap
colors = plt.cm.Set3(np.linspace(0, 1, len(categories)))
cmap = ListedColormap(colors)

# Create a multi-panel figure
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Bar chart with custom colors
ax1 = axes[0]
df.plot(x='Category', y='Value', kind='bar', ax=ax1, color=colors, edgecolor='black')
ax1.set_title("Category Values (Bar Chart)", fontsize=16, fontweight='bold')
ax1.set_xlabel("Category", fontsize=14)
ax1.set_ylabel("Value", fontsize=14)

# Scatter plot with trend line
ax2 = axes[1]
x = np.arange(len(df))
ax2.scatter(x, df['Value'], color='darkorange', s=100, edgecolors='black', zorder=3)
ax2.plot(x, df['Value'], color='darkorange', linewidth=3, zorder=2)
ax2.set_title("Category Values (Scatter + Trend)", fontsize=16, fontweight='bold')
ax2.set_xlabel("Category Index", fontsize=14)
ax2.set_ylabel("Value", fontsize=14)

# Add a pie chart in a third subplot
fig.add_subplot(2, 2, 3)
plt.pie(df['Value'], labels=df['Category'], autopct='%1.1f%%', colors=colors, startangle=90)
plt.title("Value Distribution (Pie Chart)", fontsize=16, fontweight='bold')

# Add a fourth subplot for a histogram
fig.add_subplot(2, 2, 4)
plt.hist(df['Value'], bins=5, color='lightcoral', edgecolor='black', alpha=0.7)
plt.title("Value Distribution (Histogram)", fontsize=16, fontweight='bold')
plt.xlabel("Value Range")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()
