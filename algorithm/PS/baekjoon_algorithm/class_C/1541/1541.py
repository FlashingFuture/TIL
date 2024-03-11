char = input()
exp = []
temp_num = []
total_sum = 0
digit_cnt = 1
turn_minus = 0
for item in char:
    if item == '+':
        exp.append(sum(temp_num))
        exp.append('+')
        temp_num = []
    
    elif item == '-':
        exp.append(sum(temp_num))
        exp.append('-')
        temp_num = []

    else:
        temp_num *= 10
        temp_num.append(int(item))


exp.append(sum(temp_num))
total = exp[0]
for i in range(1, len(exp), 2):
    if exp[i] == '+':
        total += exp[i + 1]
    
    elif exp[i] == '-':
        for k in range(i, len(exp), 2):
            total -= exp[k + 1]

        break

print(total)
