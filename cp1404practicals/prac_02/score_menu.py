MENU = "A. Get a valid score\nB. Print result\nC. Print stars\nD. Quit"


def main():
    score = 0
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "D":
        if choice == "A":
            score = get_valid_score()
        elif choice == "B":
            print_result(score)
        elif choice == "C":
            print_stars(score)
        print(MENU)
        choice = input(">>> ").upper()
    print("cya later :)")


def get_valid_score():
    score = int(input("Enter score between 1 and 100: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = input("Enter score between 1 and 100: ")
    return score


def print_result(score):
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    print(result)


def print_stars(score):
    print("*" * score)


main()

