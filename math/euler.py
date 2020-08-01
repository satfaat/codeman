# Multiples of 3 and 5
n = 0
for i in range(1,500):
     if not i % 5 or not i % 3:
         n = n + i
print(n)