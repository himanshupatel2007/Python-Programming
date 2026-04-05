val = 0xCAFE

print(f"The starting number is: {hex(val)}")
last = val + 0xF

bit= bin(last).count('1')

print(f"The number of 'on' bits I found is: {bit}")

if bit >= 3:
    print("Result: Yes, at least three of the last four bits are on.")
else:
    print("Result: No, fewer than three of the last four bits are on.")
high = val << 8
low = val >> 8
reversed = high + low
print(f"The original value was: {hex(val)}")
print(f"The new reversed value is: {hex(reversed)}")
rotated = val >> 4

print(f"The original value was: {hex(val)}")
print(f"The rotated value is: {hex(rotated)}")
