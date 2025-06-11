import time
from datetime import datetime
from data import data_func2

INTERVAL = 5 * 60  # 5분 간격

if __name__ == "__main__":
    print("[LOOP 시작] 프로그램 작동 중... (5분마다 갱신)")
    while True:
        try:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"\n[{now}] 수집 시도")
            stats = data_func2()

            if stats is None:
                print("[경고] stats=None → 프레임 실패 or YOLO 실패")
            else:
                print(f"[수집 성공] 평균: {stats['average']:.2f}, 최대: {stats['max']}, 최소: {stats['min']}")

        except Exception as e:
            print(f"[LOOP 오류 발생] {e}")

        print(f"[대기 중] {INTERVAL // 5}분 후 재시도 예정...")
        time.sleep(INTERVAL)
