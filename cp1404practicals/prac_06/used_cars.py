"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("Jacob's Car", 180)
    my_car.drive(30)
    print(f"fuel: {my_car.fuel}")
    print(my_car)

    # Modification 1
    limo = Car("Limo", 100)
    # Modification 2
    limo.add_fuel(20)
    # Modification 3
    print(f"fuel: {limo.fuel}")
    # Modification 4
    limo.drive(115)
    print(f"fuel: {limo.fuel}")
    print(limo)



main()
