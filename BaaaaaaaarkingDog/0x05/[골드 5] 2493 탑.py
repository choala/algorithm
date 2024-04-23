n = int(input())
tops = list(map(int, input().split()))

receivers = []
results = []

for top in tops:
    if receivers:
        target = receivers[-1]

        while target < top:
            receivers.pop()

            if receivers:
                target = receivers[-1]
            else:
                results.append(0)
                break

        if target >= top:
            results.append(tops.index(target) + 1)
    else:
        results.append(0)

    receivers.append(top)

for result in results:
    print(result, end=' ')
