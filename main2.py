# main.py
import matplotlib.pyplot as plt
from module1 import func1, func2, URLS
from module2 import preprocess, standard, expected_count, classify
from datetime import datetime

# 현재 시각 정보 추출+출력용 시간 
now = datetime.now()
day = now.strftime("%A")  
minute_5 = (now.minute // 5) * 5
time = f"{now.hour:02d}:{minute_5:02d}"  
time_d = now.strftime("%H:%M")

# 실시간 차량 수 감지
frame = func1(URLS["경복궁"])
main_count = func2(frame) 

# 혼잡도 기준 및 예측값 계산
df = preprocess("data/traffic_log.csv")
low, high = standard(df, day)
expected = expected_count(df, day)
level = classify(main_count, low, high)

# 결과 출력
print(f"[{day} {time_d}]")
print(f"- 예상 차량 수: {expected:.1f}대" if expected else "- 예측 데이터 없음")
print(f"- 실제 차량 수: {main_count}대")
print(f"- 혼잡도 수준: {level} (기준: 원활≤{low:.1f}, 혼잡>{high:.1f})")


#그래프 추가
def plot_congestion_trend(df, day, current_time, current_count):
    # 해당 요일 데이터만 필터링
    day_df = df[df['day'] == day]

    # 시간대별 평균 차량 수 계산
    avg_by_time = day_df.groupby('time')['count'].mean()

    # x, y 데이터 준비
    times = avg_by_time.index.tolist()
    values = avg_by_time.values.tolist()

    # 그래프 그리기
    plt.figure(figsize=(12, 5))
    plt.plot(times, values, label=f"{day}")

    # 현재 시간대 강조 표시
    if current_time in avg_by_time.index:
        current_avg = avg_by_time[current_time]
        plt.scatter(current_time, current_avg, color='black', s=50, label="now_average")
        plt.axvline(current_time, color='black', linestyle='--', alpha=0.5)

    # 현재 측정값도 점으로 추가
    plt.scatter(current_time, current_count, color='red', s=50, label="now")

    plt.title(f"{day} average car counts ({time_d})")
    plt.xlabel("time(per 5min.)")
    plt.ylabel("counts")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

plot_congestion_trend(df, day, time, main_count)
