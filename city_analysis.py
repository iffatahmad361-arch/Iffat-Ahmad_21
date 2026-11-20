import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("AQI_Cleaned_Data.csv")

# Convert AQI column to numeric
df["US AQI"] = pd.to_numeric(
    df["US AQI"], errors="coerce"
)

# Remove rows with missing city or AQI
df = df.dropna(subset=["City", "US AQI"])

# Calculate average AQI for each city
city_aqi = df.groupby("City")["US AQI"].mean()

# Sort cities by AQI
city_aqi = city_aqi.sort_values(ascending=False)

print("\nTOP 10 MOST POLLUTED CITIES:")
print(city_aqi.head(10))

print("\nTOP 10 CLEANEST CITIES:")
print(city_aqi.tail(10))

# Graph 1: Most polluted cities
plt.figure(figsize=(12, 6))

city_aqi.head(10).plot(
    kind="bar",
    color="tomato"
)

plt.title("Top 10 Most Polluted Cities in India")
plt.xlabel("City")
plt.ylabel("Average US AQI")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("top_10_polluted_cities.png")
plt.show()

# Graph 2: Cleanest cities
plt.figure(figsize=(12, 6))

city_aqi.tail(10).sort_values().plot(
    kind="bar",
    color="green"
)

plt.title("Top 10 Cleanest Cities in India")
plt.xlabel("City")
plt.ylabel("Average US AQI")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("top_10_cleanest_cities.png")
plt.show()

print("\nCITY ANALYSIS COMPLETED!")