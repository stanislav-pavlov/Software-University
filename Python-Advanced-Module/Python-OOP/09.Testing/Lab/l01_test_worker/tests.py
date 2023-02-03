from test_worker import Worker
from unittest import TestCase, main


class WorkerTests(TestCase):
    NAME = "Stanislav"
    SALARY = 1000
    ENERGY = 2

    def setUp(self) -> None:
        self.worker = Worker(self.NAME, self.SALARY, self.ENERGY)

    def test__init__when_valid_props__expect_correct_values(self):
        self.assertEqual(self.NAME, self.worker.name)
        self.assertEqual(self.SALARY, self.worker.salary)
        self.assertEqual(self.ENERGY, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test__rest__expect_energy_to_be_incremented(self):
        self.worker.rest()
        self.assertEqual(self.ENERGY + 1, self.worker.energy)

    def test__work__when_energy_is_0__expect_error(self):
        worker = Worker(self.NAME, self.SALARY, 0)

        with self.assertRaises(Exception) as ex:
            worker.work()

        self.assertIsNotNone(ex)

    def test__work__when_enough_energy__expect_money_incremented_with_salary(self):
        self.worker.work()
        self.worker.work()
        self.assertEqual(2 * self.SALARY, self.worker.money)

    def test__work__when_enough_energy__expect_energy_decrease(self):
        self.worker.work()
        self.assertEqual(self.ENERGY - 1, self.worker.energy)

    def test__get_info__expect_proper_string_with_correct_values(self):
        expected_info = f'{self.NAME} has saved {0} money.'
        actual_info = self.worker.get_info()

        self.assertEqual(expected_info, actual_info)


if __name__ == '__main__':
    main()