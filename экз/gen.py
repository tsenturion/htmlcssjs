import random

numbers = list(range(1, 33))
weights = [10 if x in [6, 11, 13, 14, 31, 32] else 8 if 16 <= x <= 25 else 1 for x in numbers]

result = random.choices(numbers, weights=weights, k=5)
result.sort()
print(result)