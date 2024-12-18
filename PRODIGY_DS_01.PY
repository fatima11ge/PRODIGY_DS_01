import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv(r'C:\Users\fatem\Desktop\Prodigy\Task 01\dataset01\API_SP.POP.TOTL_DS2_en_csv_v2_9949.csv', skiprows=4)

# Select the latest year with complete data (2023)
latest_year = "2023"

# Filter out rows with missing values for the latest year and sort by population
top_countries = (
    data[["Country Name", latest_year]]
    .dropna()
    .sort_values(by=latest_year, ascending=False)
    .head(10)
)

# Extract top 10 countries' names
top_countries_names = top_countries["Country Name"].tolist()

# Filter the dataset for the top 10 countries
years = [col for col in data.columns if col.isdigit()]
top_countries_population = data[data["Country Name"].isin(top_countries_names)][["Country Name"] + years]
top_countries_population = top_countries_population.set_index("Country Name")

# Convert to numeric and handle missing values by filling with 0
top_countries_population = top_countries_population.apply(pd.to_numeric, errors="coerce").fillna(0)

# Preparing data for a stacked bar chart
x = np.arange(len(years))
width = 0.8

plt.figure(figsize=(30, 10))
bottom_values = np.zeros(len(years))

for country in top_countries_names:
    plt.bar(x, top_countries_population.loc[country, years], width, bottom=bottom_values, label=country)
    bottom_values += top_countries_population.loc[country, years]

plt.title("Population Trends for the 10 Most Crowded Countries (1960-2023)")
plt.ylabel("Population")
plt.xlabel("Year")
plt.xticks(ticks=x, labels=years, rotation=45)
plt.legend(title="Country", loc="upper left", bbox_to_anchor=(1.05, 1), fontsize=10)
plt.tight_layout()
plt.show()
