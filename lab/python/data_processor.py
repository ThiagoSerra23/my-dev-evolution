import pandas as pd

def process_csv(file):
    df = pd.read_csv(file)
    print(df.describe())