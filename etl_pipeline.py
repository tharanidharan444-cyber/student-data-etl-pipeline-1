import pandas as pd

df = pd.read_csv("student_data.csv")

print("Original Data:")
print(df)

df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

df.to_csv("cleaned_data.csv", index=False)

print("\nCleaned Data:")
print(df)

print("\nData successfully processed!")
