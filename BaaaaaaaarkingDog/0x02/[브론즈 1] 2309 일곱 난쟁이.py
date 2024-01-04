import itertools

height = []
cases = []
result = []

for _ in range(9):
    height.append(int(input()))

cases = itertools.combinations(height, 7)

for case in cases:
    if sum(case) == 100:
        # itertools.combinations는 튜플들의 집합을 반환하기 때문에 list로 형변환을 해주어야 sort()를 사용할 수 있음
        result = list(case)
        break

result.sort()

for r in result:
    print(r)
