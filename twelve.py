cases = int(input())

for i in range(cases):
    x, y = map(int, input().split())
    a = x
    b = y
   
    while b != 0:
        temp = b  
        b = a % b
        a = temp
      
    gcd = a
    lcm = (x * y) / gcd
    print(gcd, lcm)
