import pandas as pd

def preprocess_input_data(df):
    df['storey_range'] = df['storey_range'].apply(lambda x: int(x.split('-')[0]))
    df['flat_type'] = df['flat_type'].apply(lambda x: int(x.split('-')[0]) if '-' in x else 5)
    df['lease_commence_date'] = 2023 - df['lease_commence_date']
    df = pd.get_dummies(df, columns=['town'], drop_first=True)
    return df
