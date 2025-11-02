import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

buf = [0] * N   # 병합용 버퍼 (매 쿼리 재사용)

for _ in range(K):
    L, R, X = map(int, input().split())
    L -= 1; R -= 1

    i = 0        # left: [0 .. L-1]
    j = L        # mid : [L .. R]     (값에 +X 해서 비교/출력)
    p = R + 1    # tail: [R+1 .. N-1]
    k = 0        # buf 채우는 인덱스

    # 세 구간을 한 번에 병합 (정렬 상태 유지)
    while i < L or j <= R or p < N:
        # 후보 값 가져오기 (없으면 None)
        lv = A[i]       if i < L else None
        mv = A[j] + X   if j <= R else None
        tv = A[p]       if p < N else None

        # 세 후보 중 가장 작은 값을 선택
        if lv is not None and (mv is None or lv <= mv) and (tv is None or lv <= tv):
            buf[k] = lv
            i += 1
        elif mv is not None and (tv is None or mv <= tv):
            buf[k] = mv
            j += 1
        else:
            buf[k] = tv
            p += 1
        k += 1

    # 버퍼와 A를 스왑 (복사 비용 줄이기)
    A, buf = buf, A

print(*A)
