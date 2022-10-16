COLOUR_TO_HEX = {"absolutezero": "#0048ba", "amethyst": "#9966cc", "asparagus": "#87a96b"}

print(COLOUR_TO_HEX)
colour = input("Enter colour name: ").lower()
while colour != "":
    if colour in COLOUR_TO_HEX:
        print(f"{colour} is {COLOUR_TO_HEX[colour]}")
    else:
        print("Invalid colour name")
    colour = input("Enter colour name: ").lower()
