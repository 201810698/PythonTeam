# module2.py — 혼잡도 분류 모듈 (요일별)

import pandas as pd

def preprocess(csv_path):
    df = pd.read_csv(csv_path)
    return df
    
# 요일 필터링 추가
def standard(df, day):
    df_scaled = df[(df['day'] == day)]

    car_count = df_scaled['count']

    low_count = car_count.quantile(0.20)
    high_count = car_count.quantile(0.60)

    return low_count, high_count


def classify(count, low, high):
    if count <= low:
        return '원활'
    elif count <= high:
        return '보통'
    else:
        return '혼잡'

def expected_count(df, day):
    df_scaled = df[(df['day'] == day)]

    return df_scaled['count'].mean()
