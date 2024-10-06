target = int(input())

cache = [0] * (target + 1)

for i in range(2, target + 1):
    cache[i] = cache[i - 1] + 1
    if i % 3 == 0:
        cache[i] = min(cache[i], cache[i // 3] + 1)
    if i % 2 == 0:
        cache[i] = min(cache[i], cache[i // 2] + 1)

print(cache[target])