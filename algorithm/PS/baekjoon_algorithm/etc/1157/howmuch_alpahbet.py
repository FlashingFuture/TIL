C = input()
C= C.upper()
count = {}

for item in C:
    if item not in count:
        count[item] = 1
    else:
        count[item] += 1

max_count = 0
max_alphabet = []
for k, v in count.items():
    if v > max_count:
        max_count = v
        max_alphabet.clear()
        max_alphabet.append(k)
    elif v == max_count:
        max_alphabet.append(k)

res = max_alphabet.pop()
if max_alphabet:
    print('?')
else:
    print(res)