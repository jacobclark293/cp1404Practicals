from unreliable_car import UnreliableCar


def main():
    """Test some UnreliableCars."""

    # create cars with different reliabilities
    good_car = UnreliableCar("My car", 100, 90)
    bad_car = UnreliableCar("Ryans car", 100, 5)

    # attempt to drive the cars many times
    # output what distance they drove
    for i in range(1, 12):
        print(f"Attempting to drive {i}km:")
        print(f"{good_car.name:12} drove {good_car.drive(i):2}km")
        print(f"{bad_car.name:12} drove {bad_car.drive(i):2}km")

    # print the final states of the cars
    print(good_car)
    print(bad_car)


main()