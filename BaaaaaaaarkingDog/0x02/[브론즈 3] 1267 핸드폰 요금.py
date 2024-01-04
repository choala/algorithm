def y(time):
    return 10 + time // 30 * 10

def m(time):
    return 15 + time // 60 * 15

n = int(input())
times = list(map(int, input().split()))

y_cost = 0
m_cost = 0

for t in times:
    y_cost += y(t)
    m_cost += m(t)

if y_cost < m_cost:
    print("Y", end=" ")
    print(y_cost)
elif y_cost > m_cost:
    print("M", end=" ")
    print(m_cost)
else:
    print("Y M", end= " ")
    print(y_cost)
