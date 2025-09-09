N = int(input())

# Please write your code here.

def sq(N):
    if N < 10:
        return N*N

    return sq( N // 10 )  + (N % 10) * (N % 10)

print(sq(N))