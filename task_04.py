def print_square(num, symbol_1, symbol_2):
    s1 = symbol_1 * 2
    s2 = symbol_2 * 2

    print()

    # special case
    if num == 1:
        print(s1)
        print(s2)
        return

    for i in range(num):
        line = ""
        for ii in range(num):
            line += s1
            s1, s2 = s2, s1

        if num % 2 == 0:
            s1, s2 = s2, s1
        print(line)


input_number = int(input("Enter a number: "))
input_symbol_1 = input("Enter a symbol: ")
input_symbol_2 = input("Enter a symbol: ")

print_square(input_number, input_symbol_1, input_symbol_2)
