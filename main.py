# main.py

from module1 import func1, func2, URLS
from module2 import preprocess, standard, expected_count, classify
from datetime import datetime

# 현재 시각 정보 추출
now = datetime.now()
day = now.strftime("%A")  
minute_5 = (now.minute // 5) * 5
time = f"{now.hour:02d}:{minute_5:02d}"  

# 실시간 차량 수 감지
frame = func1(URLS["경복궁"])
main_count = func2(frame) 

# 혼잡도 기준 및 예측값 계산
df = preprocess("data/traffic_log.csv")
low, high = standard(df, day)
expected = expected_count(df, day)
level = classify(main_count, low, high)

# 결과 출력
print(f"[{day} {time}]")
print(f"- 예상 차량 수: {expected:.1f}대" if expected else "- 예측 데이터 없음")
print(f"- 실제 차량 수: {main_count}대")
print(f"- 혼잡도 수준: {level} (기준: 원활≤{low:.1f}, 혼잡>{high:.1f})")
