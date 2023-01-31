from car_manager import Car
from unittest import TestCase, main


class CarManagerTests(TestCase):

    def setUp(self) -> None:
        self.car = Car("Lotus", "Elise", 8, 40)

    def test__init(self):
        self.assertEqual("Lotus", self.car.make)
        self.assertEqual("Elise", self.car.model)
        self.assertEqual(8, self.car.fuel_consumption)
        self.assertEqual(40, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test__make__when_value_is_empty__expect_to_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test__model__when_value_is_empty__expect_to_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test__fuel_consumption__when_value_is_negative_or_zero__expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test__fuel_capacity__when_value_is_negative_or_zero__expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -1
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test__fuel_amount__when_value_is_negative__expect_to_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test__refuel__when_value_is_negative_or_zero_expect_to_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test__refuel__when_fuel_amount_exceeds_fuel_cap__expect_equality(self):
        self.car.refuel(55)
        self.assertEqual(self.car.fuel_amount, self.car.fuel_capacity)

    def test__drive__when_fuel_amount_is_less_than_needed_expect_exception(self):
        self.car.fuel_amount = 18

        with self.assertRaises(Exception) as ex:
            self.car.drive(250)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive__when_fuel_amount_is_larger_than_needed_expect_fuel_amount_decrease(self):
        self.car.fuel_amount = 32
        self.car.drive(250)

        self.assertEqual(32-20, self.car.fuel_amount)


if __name__ == "__main__":
    main()