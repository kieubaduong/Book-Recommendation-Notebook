import pandas as pd

df = pd.read_csv('../../dataset/raw_dataset/Users.csv')

df = df.dropna(subset=['user-id', 'location', 'age'])

df.to_csv("../../dataset/processed_dataset/users.csv", index=False)