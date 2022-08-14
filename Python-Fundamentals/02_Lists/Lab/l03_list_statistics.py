count = int (input())
positive = list()
negative = list()
pos_count = 0
neg_sum = 0

for i in range(count):
    current_num = int(input())
    if current_num >= 0:
        positive.append(current_num)
        pos_count += 1
    else:
        negative.append(current_num)
        neg_sum += current_num

print(positive)
print(negative)
print(f"Count of positives: {pos_count}")
print(f"Sum of negatives: {neg_sum}")