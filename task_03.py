def print_square_v01(number, symbol):
    print()
    for i in range(number):
        line = " ".join([symbol] * round(number / 2))
        print(f"{symbol if number == 1 else line}{"" if number % 2 != 0 else " "}")


def print_square_v02(number, symbol):
    besa = [symbol, " "]
    line = create_line(besa,input_number)

    print(f"{line}\n" * number)


def create_line(besa, number):
    line = ""
    for i in range(number):
        line += besa[i % 2]
    return line


input_number = int(input("Enter a number: "))
input_symbol = input("Enter a symbol: ")

print_square_v01(input_number, input_symbol)
print("\nV02\n")
print_square_v02(input_number, input_symbol)
