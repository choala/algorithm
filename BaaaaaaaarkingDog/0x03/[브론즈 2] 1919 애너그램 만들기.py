str1 = input()
str2 = input()

alpha1 = [0 for _ in range(26)]
alpha2 = [0 for _ in range(26)]
        
for s in str1:
    alpha1[ord(s) - ord('a')] += 1

for s in str2:
    alpha2[ord(s) - ord('a')] += 1

count = 0
for i in range(26):
    if alpha1[i] != alpha2[i]:
        count += max(alpha1[i], alpha2[i]) - min(alpha1[i], alpha2[i])

print(count)
