alpha = [0 for _ in range(26)]

s = input()

for c in s:
    alpha[ord(c) - ord('a')] += 1

for a in alpha:
    print(a, end=" ")
