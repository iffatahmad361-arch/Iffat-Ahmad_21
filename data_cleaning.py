import pandas as pd
import glob

# Load the original dataset
files = [f for f in glob.glob("*.csv")
         if "cleaned" not in f.lower()]

if not files:
    raise FileNotFoundError("No original CSV file found!")

df = pd.read_csv(files[0])

print("ORIGINAL DATA")
print(df.head())

# 1. Check dataset information
print("\nDataset Information:")
print(df.info())

# 2. Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 3. Check duplicate rows
print("\nDuplicate Rows:", df.duplicated().sum())

# 4. Remove duplicate rows
df = df.drop_duplicates()

# 5. Remove extra spaces from column names
df.columns = df.columns.str.strip()

# 6. Clean text columns
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip()

# 7. Handle missing values
for col in df.columns:
    if pd.api.types.is_numeric_dtype(df[col]):
        df[col] = df[col].fillna(df[col].median())
    else:
        mode = df[col].mode()
        if not mode.empty:
            df[col] = df[col].fillna(mode[0])

# 8. Save cleaned dataset
df.to_csv("AQI_Cleaned_Data.csv", index=False)

print("\nCLEANING COMPLETED!")
print("Cleaned dataset saved successfully.")

# 9. Final dataset information
print("\nFinal Missing Values:")
print(df.isnull().sum())

print("\nFinal Duplicate Rows:", df.duplicated().sum())

print("\nCleaned Dataset Shape:", df.shape)