import pandas as pd

# Load the data from a CSV file on Google Drive
df = pd.read_csv('/content/drive/My Drive/MSDS-Orientation-Computer-Survey(in).csv')
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

import matplotlib.pyplot as plt

# Group the data by 'RAM (in GB)' and count the number of occurrences
df_ram = df.groupby('RAM (in GB)').size()

# Create a stacked histogram
df_ram.plot(kind='hist', stacked=True)

# Add labels and title
plt.xlabel('RAM (in GB)')
plt.ylabel('Number of Respondents')
plt.title('Distribution of RAM')

# Show the plot
plt.show()
