# Generate a python code for a bar chart using GitHub Copilot

import matplotlib.pyplot as plt

years = ['2015', '2016', '2017', '2018']
age_groups = ['20-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81+']
deaths = {
    '2015': [5, 15, 25, 35, 45, 55, 65],
    '2016': [6, 16, 26, 36, 46, 56, 66],
    '2017': [7, 17, 27, 37, 47, 57, 67],
    '2018': [8, 18, 28, 38, 48, 58, 68]
}

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))

for year in years:
    ax.bar(age_groups, deaths[year], label=year)

ax.set_xlabel('Age Groups')
ax.set_ylabel('Number of Deaths')
ax.set_title('Number of People Died by Heart Attack (2015-2018)')
ax.legend(title='Year')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()