import sys
input = sys.stdin.readline

# ---------------------------
# 1. 입력 처리
# ---------------------------
n, k = map(int, input().split())         # N: 인형 개수, K: 필요한 라이언 개수
dolls = list(map(int, input().split()))  # 인형 정보 (1=라이언, 2=어피치)

# ---------------------------
# 2. 라이언(=1)의 인덱스만 모으기
# ---------------------------
lion_idx = []
for i in range(n):
    if dolls[i] == 1:
        lion_idx.append(i)

# ---------------------------
# 3. 라이언 개수 확인
# ---------------------------
if len(lion_idx) < k:
    # 라이언이 K개 미만이면 조건을 만족할 수 없음
    print(-1)
else:
    answer = n + 1  # 충분히 큰 값으로 초기화
    # 연속된 K개의 라이언을 선택했을 때 구간 길이 계산
    for i in range(len(lion_idx) - k + 1):
        # i번째 라이언부터 i+k-1번째 라이언까지 포함
        left = lion_idx[i]
        right = lion_idx[i + k - 1]
        length = right - left + 1
        answer = min(answer, length)

    print(answer)
