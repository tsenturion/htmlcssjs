import random

numbers = list(range(1, 33))
weights = [6 if x in [6, 11, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 31, 32] else 1 for x in numbers]

result = random.choices(numbers, weights=weights, k=5)
result.sort()

print("Сгенерированные числа:", result)

priority_numbers = [6, 11, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 31, 32]
priority_found = [num for num in result if num in priority_numbers]

if priority_found:
    print("Приоритетные числа:", priority_found)
else:
    print("Приоритетные числа не выпали")