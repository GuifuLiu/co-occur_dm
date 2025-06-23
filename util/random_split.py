import pandas as pd
from sklearn.model_selection import train_test_split
import os

# folder = "dataset/explicit-explicit/discovery/both_pdtb"
folder = "dataset/explicit-explicit/discovery/dm1_pdtb"
os.chdir(folder)
df = pd.read_csv(f'dm1_pdtb.csv')

# First split: 70% train, 30% temp
train, temp = train_test_split(df, test_size=0.3, random_state=42)

# Second split: 10% validation, 20% test from the 30%
val, test = train_test_split(temp, test_size=2/3, random_state=42)

# Save splits
train.to_csv('train.csv', index=False)
val.to_csv('validation.csv', index=False)
test.to_csv('test.csv', index=False)

# print(f"Train: {len(train)} rows ({len(train)/len(df)*100:.1f}%)")
# print(f"Validation: {len(val)} rows ({len(val)/len(df)*100:.1f}%)")
# print(f"Test: {len(test)} rows ({len(test)/len(df)*100:.1f}%)")