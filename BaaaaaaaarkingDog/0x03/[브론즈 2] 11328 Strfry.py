def string_to_array(str):
    alpha = [0 for _ in range(26)]

    for s in str:
        alpha[ord(s) - ord('a')] += 1
    
    return alpha

n = int(input())

for _ in range(n):
    str1, str2 = input().split()
    arr1 = string_to_array(str1)
    arr2 = string_to_array(str2)

    if arr1 == arr2:
        print("Possible")
    else:
        print("Impossible")
