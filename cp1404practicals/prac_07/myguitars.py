"""
CP1404 prac_07 guitar program
"""

from guitar import Guitar


def main():
    """Guitar program, using Guitar class"""
    # guitars = []
    # print("My guitars!")
    # name = input("Name: ")
    # while name != "":
    #     year = int(input("Year: "))
    #     cost = float(input("Cost: "))
    #     guitar_to_add = Guitar(name, year, cost)
    #     guitars.append(guitar_to_add)
    #     print(guitar_to_add, "added")
    #     name = input("Name: ")
    #
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    guitars = []
    with open('guitars.csv', 'r') as in_file:
        for line in in_file:
            line = line.strip()
            parts = line.split(' ')
            guitars.append(parts)
    # print(guitars)

    if guitars:
        guitars.sort()
        print("These are my guitars:")
        for guitar in guitars:
            if guitar.lt():
            # print("Guitar {0}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{2}".format(i, guitar))
                print(guitar)
    else:
        print("No guitars :( Quick, go and buy one!")

main()