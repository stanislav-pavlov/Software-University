number_of_lines = int(input())

total_amount_of_liters = 0

for x in range(number_of_lines):
    liters = int(input())

    if total_amount_of_liters + liters <= 255:
        total_amount_of_liters += liters
        continue

    print("Insufficient capacity!")

print(total_amount_of_liters)

# ALTERNATIVE SOLUTION:

# for x in range(number_of_lines):
#     liters = int(input())
    # total_amount_of_liters += liters
    #
    # if total_amount_of_liters > 255:
    #     print("Insufficient capacity!")
    #     total_amount_of_liters = total_amount_of_liters - liters
#
# print(total_amount_of_liters)




