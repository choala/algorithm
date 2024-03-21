import sys

input = sys.stdin.readline

n, s = map(int, input().split())
sequence = list(map(int, input().split()))

count = 0

def subsequence(k, total):
    global count
    
    # base condition
    if k == n:
        if total == s:
            count += 1
        return
    
    subsequence(k + 1, total)
    subsequence(k + 1, total + sequence[k])

subsequence(0, 0)

if s == 0:
    print(count - 1)
else:
    print(count)
