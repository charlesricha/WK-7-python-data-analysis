
""" This imports the Pandas library (which we'll use to load and manipulate the data) 
and the Matplotlib library (which we'll use to create visualizations). """

import pandas as pd
import matplotlib.pyplot as plt

# loading Iris database

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
df = pd.read_csv(url, names=column_names)

# Checking wether the iris database is loaded successfully

print(df.head())
print(df.info())

# A line chart for data visualization

plt.figure(figsize=(10, 5))  # Adjust the figure size for better readability
plt.plot(df.index, df['sepal_length'], marker='.', linestyle='-', color='r')
plt.title('SepalData on a Line Chart')
plt.xlabel('Index')
plt.ylabel('Sepal Length (cm)')
plt.grid(True)  # Add gridlines for better readability
plt.show()

# Bar Chart

plt.figure(figsize=(10, 5))
species_avg_petal_length = df.groupby('species')['petal_length'].mean()
species_avg_petal_length.plot(kind='bar', color=['lightpink', 'lightgreen', 'lightblue'])
plt.title('Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length (cm)')
plt.xticks(rotation=0)  # Keep x-axis labels horizontal
plt.show()

# Histogram

plt.figure(figsize=(8, 6))
plt.hist(df['sepal_width'], bins=10, color='lightblue', edgecolor='black')  # Added edgecolor
plt.title('Distribution of Sepal Width')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.show()

# Scatter Plot

plt.figure(figsize=(8, 6))
plt.scatter(df['sepal_length'], df['petal_length'], color='purple', alpha=0.7) # Added alpha
plt.title('Relationship between Sepal Length and Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.grid(True)
plt.show()