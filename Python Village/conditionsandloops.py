"""
4185 8473
"""

a = 4185
b = 8473
sum = 0
while a <= b:
    if a % 2 == 1:
        sum = sum + a
    a = a + 1

print(sum)
