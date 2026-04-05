amount = int(input("Enter the total amount of money: "))
denomination = int(input("Enter the highest denomination you have: "))

if denomination == 100:
    notes100 = amount // 100
    amount = amount % 100 
    print(f"100 rupees note: {notes100}")

if denomination >= 50:
    notes50 = amount // 50
    amount = amount % 50
    print(f"50 rupees note: {notes50}")

if denomination >= 20:
    notes20 = amount // 20
    amount = amount % 20
    print(f"20 rupees note: {notes20}")

if denomination >= 10:
    notes10 = amount // 10
    amount = amount % 10
    print(f"10 rupees note: {notes10}")

if denomination >= 5:
    notes5 = amount // 5
    amount = amount % 5
    print(f"5 rupees note: {notes5}")

if denomination >= 2:
    notes2 = amount // 2
    amount = amount % 2
    print(f"2 rupees note: {notes2}")

if denomination >= 1:
    notes1 = amount // 1
    amount = amount % 1
    print(f"1 rupees note: {notes1}")
