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


# -----------------------------
# STEP 4: Feature / target split
# -----------------------------

X = pilot_df.drop(columns=["Label", "target"])
y = pilot_df["target"]

print("Feature matrix shape:", X.shape)
print("Target shape:", y.shape)


# -----------------------------
# FIX: Handle infinite and extreme values
# -----------------------------


# Replace infinite values with NaN
X = X.replace([np.inf, -np.inf], np.nan)

# Check how many missing values we have
print("\nMissing values before cleaning:")
print(X.isna().sum().sort_values(ascending=False).head(10))

# Drop rows with NaN values (safe for pilot)
X = X.dropna()
y = y.loc[X.index]

print("\nAfter cleaning:")
print("Feature matrix shape:", X.shape)
print("Target shape:", y.shape)


# -----------------------------
# STEP 5: Train Random Forest
# -----------------------------


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

rf = RandomForestClassifier(n_estimators=50, max_depth=10, random_state=42, n_jobs=-1)

rf.fit(X_train, y_train)

print("\nRandom Forest trained successfully")
print("Train samples:", X_train.shape[0])
print("Test samples:", X_test.shape[0])