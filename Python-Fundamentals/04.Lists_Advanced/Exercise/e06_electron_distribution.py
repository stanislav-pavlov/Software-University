def electron_distribution(electrons):
    remaining_electrons = electrons_to_fill
    shell_num = 1
    shells = []
    while remaining_electrons > 0:
        shell_filling = 2 * (shell_num ** 2)

        if shell_filling > remaining_electrons:
            shell_filling = remaining_electrons

        remaining_electrons -= shell_filling
        shell_num += 1
        shells.append(shell_filling)

    print(shells)


electrons_to_fill = int(input())
electron_distribution(electrons_to_fill)