import random
with open("random_data.csv", "w") as f:
    for _ in range(10):
        row = [random.randint(1, 100) for _ in range(3)]
        f.write(','.join(map(str, row)) + '\n')
second_column = []
with open("random_data.csv", "r") as f:
    for line in f:
        second_col = int(line.strip().split(',')[1])
        second_column.append(second_col)
max_value = max(second_column)
min_value = min(second_column)
average_value= sum(second_column) / len(second_column)

sorted_col = sorted(second_column)
n = len(sorted_col)
if n % 2 == 1:
    median = sorted_col[n//2]
else:
    median = (sorted_col[n//2 - 1] + sorted_col[n//2]) / 2

print(f"第二列最大值：{max_value}")
print(f"第二列最小值：{min_value}")
print(f"第二列平均值：{average_value:.2f}")
print(f"第二列中位数：{median}")