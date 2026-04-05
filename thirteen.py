stones = int(input())
round = 1
while stones > 0:
    
    ramesh = round
    if stones >= ramesh:
        stones = stones - ramesh
    else:
        print("Ramesh")
        break
    if stones == 0:
        print("Ramesh")
        break
    suresh = round * 2

    if stones >= suresh:
        stones = stones - suresh
    else:
        print("Suresh")
        break
    if stones == 0:
        print("Suresh")
        break
    round = round + 1
