# 260522

T = int(input())

for t in range(1, T+1):

    P, Q, R, S, W = map(int, input().split())

    def A(w, P):
        total = w * P
        return total

    def B(w, Q, R):
        total = Q
        if w > R:
            total += S * (w-R)
        return total

    print("#{} {}".format(t, min(A(W, P), B(W, Q, R))))