#모듈2 혼잡도 분류

import pandas as pd

def preprocess(csv_path):
    df = pd.read_csv(csv_path)
    return df

def standard(df):
    low = df['count'].quantile(0.20)
    high = df['count'].quantile(0.60)
    return low, high

def classify(count, low, high):
    if count <= low:
        return '원활'
    elif count <= high:
        return '보통'
    else:
        return '혼잡'

def expected_count(df, day, time):
    filtered = df[(df['day'] == day) & (df['time'] == time)]
    if filtered.empty:
        return None
    return filtered['count'].mean() 