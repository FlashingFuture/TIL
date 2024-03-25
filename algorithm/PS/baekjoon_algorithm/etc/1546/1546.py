N = int(input())
results = list(map(int, input().split()))
max_point = max(results)
new_results = []
for item in results:
    new_results.append(item / max_point * 100)

res = sum(new_results) / len(new_results)
print(res)
