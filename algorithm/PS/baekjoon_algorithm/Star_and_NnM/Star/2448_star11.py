C = input()
count = {}
for item in C:
    if item not in count:
        count[item] = 1
    else:
        count[item] += 1

print(max(count))
