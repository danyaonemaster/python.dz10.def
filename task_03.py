def print_figure(number, symbol):
    print()
    for i in range(number):
        line = " ".join([symbol] * 3)
        print(line)


input_number = int(input("Enter a number: "))
input_symbol = input("Enter a symbol: ")

print_figure(input_number, input_symbol)
