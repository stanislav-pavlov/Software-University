initial_input = input().split('#')
water_available = int(input())
effort = 0
total_fire = 0

print(f"Cells:")
for current_fire in initial_input:
    fire_info = current_fire.split(" = ")
    type_of_fire = fire_info[0]
    quant_value_of_fire = int(fire_info[1])
    valid_data = False

    if type_of_fire == "Low" and 1 <= quant_value_of_fire <= 50:
        valid_data = True
    elif type_of_fire == "Medium" and 51 <= quant_value_of_fire <= 80:
        valid_data = True
    elif type_of_fire == "High" and 81 <= quant_value_of_fire <= 125:
        valid_data = True

    if valid_data:
        if water_available >= quant_value_of_fire:
            water_available -= quant_value_of_fire
            effort += quant_value_of_fire * 0.25
            total_fire += quant_value_of_fire
            print(f" - {quant_value_of_fire}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")