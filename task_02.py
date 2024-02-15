def letters_list(txt: str):
    return [ord(i) for i in txt]


def limitation(txt):
    if len(txt) <= 5:
        return f"sum letters: {sum(letters_list(txt))}"
    else:
        return "Invalid input"


text = input("Enter a word 1-5 letters: ")
print(limitation(text))
