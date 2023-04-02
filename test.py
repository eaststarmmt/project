# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys


def input_data():
	readl = sys.stdin.readline
	N = int(readl())
	led = readl().split()
	return N, led

# dfsdfsdf
sol = 0

# 입력받는 부분
N, led = input_data()

# 여기서부터 작성
def main():
    global N, led, sol
    pattern = []

    seq = 1     # 연속되는 횟수
    for i in range(1, len(led)):
        # 이전이랑 다르면 패턴 유지되는 중
        if led[i - 1] != led[i]:
            seq += 1    # 패턴 카운팅
        else:
            pattern.append(seq)     # 패턴 끊겼으므로 지금까지 이어진 횟수 저장
            seq = 1     # 다시 시작할 수 있도록 1로 초기화

    pattern.append(seq)     # 마지막 패턴은 저장이 안되므로 저장

    if len(pattern) < 3:    # 패턴이 3개 미만이면 아무거나 하나만 반전 시키면 전부 다 이어짐
        sol = N
        return

    sol = cnt = sum(pattern[0:3])

    for i in range(3, len(pattern)):
        cnt += pattern[i] - pattern[i - 3]  # 가장 앞에꺼 뺴주고 현재 인덱스 더해줌. 슬라이딩 윈도우
        sol = max(cnt, sol)


main()

# 출력하는 부분
print(sol)
