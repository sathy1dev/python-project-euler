target = 1000
sum_of = []

for i in range(1,target):
    if i % 3 == 0 or i % 5 == 0:
        sum_of.append(i)

print(sum(sum_of))