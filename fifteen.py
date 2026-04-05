rows = int(input())
row = []
for i in range(num_rows):
    newrow = []
    newrow.append(1)
    if len(row) > 1:
        for j in range(len(row) - 1):
            sum = row[j] + row[j+1]
            newrow.append(sum)
    if len(row) > 0:
        newrow.append(1)
    row = newrow
    for num in row:
        print(num, end=" ")
    print()
