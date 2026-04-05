num = int(input())
for i in range(num):
    reverseda, reversedb = input().split()
    originalatext = reverseda[::-1]
    originalbtext = reversedb[::-1]
    originala = int(originalatext)
    originalb = int(originalbtext)
    sum = originala + originalb
    sumtext = str(sum)
    reversedsumtext = sumtext[::-1]
    answer = int(reversedsumtext)
    print(answer)
