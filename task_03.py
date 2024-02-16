def print_figure(number, symbol):
    print()
    num = round(number / 2)
    for i in range(number):
        line = " ".join([symbol] * round(number / 2))
        print(f"{line}{""if number % 2 == 0 else " "}")


input_number = int(input("Enter a number: "))
input_symbol = input("Enter a symbol: ")

print_figure(input_number, input_symbol)
