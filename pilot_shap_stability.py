import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv("data/ddos.csv")

# Clean column names (important for CICIDS datasets)
df.columns = df.columns.str.strip()

# Basic dataset checks
print("Dataset shape:", df.shape)

print("\nColumn names:")
print(df.columns)

print("\nFirst 5 rows:")
print(df.head())

# Check label distribution
print("\nClass distribution:")
print(df["Label"].value_counts())

# -----------------------------
# STEP 2: Binary label creation
# -----------------------------

# Create binary target
df["target"] = df["Label"].apply(lambda x: 0 if x == "BENIGN" else 1)

print("\nBinary class distribution:")
print(df["target"].value_counts())

# -----------------------------
# STEP 3: Small pilot sample
# -----------------------------

pilot_df = df.sample(n=5000, random_state=42)

print("\nPilot dataset shape:", pilot_df.shape)
print(pilot_df["target"].value_counts())
