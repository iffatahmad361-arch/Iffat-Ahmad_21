import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("AQI_Cleaned_Data.csv")

# Dataset overview
print("Dataset Shape:", df.shape)
print("\nColumn Names:")
print(df.columns.tolist())

# Statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Check AQI column
aqi_col = next(
    (c for c in df.columns if "aqi" in c.lower()),
    None
)

if aqi_col:
    print("\nAQI Statistics:")
    print(df[aqi_col].describe())

    plt.figure(figsize=(8, 5))
    sns.histplot(df[aqi_col], kde=True)
    plt.title("Distribution of AQI")
    plt.xlabel("AQI")
    plt.savefig("aqi_distribution.png")
    plt.show()
else:
    print("AQI column not found. Check column names.")

print("\nEDA COMPLETED!")