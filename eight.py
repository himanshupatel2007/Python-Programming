num = int(input())


for i in range(num ):

    a, b = map(int, input().split())

    if b == 0:
        print(1)
        continue 

    last = a % 10
    position = b % 4
    if position == 0:
        position = 4
      
    result = last ** position
    final = result % 10
    print(final)
