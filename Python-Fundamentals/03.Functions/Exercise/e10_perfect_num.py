def perfect_num_check(number):
    sum = 0
    for x in range(1, number):
        if number % x == 0:
            sum += x

    if sum == number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


num = int(input())
perfect_num_check(num)