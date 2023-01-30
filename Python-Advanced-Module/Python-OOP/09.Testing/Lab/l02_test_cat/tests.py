from cat_test import Cat
from unittest import TestCase, main


class CatTests(TestCase):
    SIZE = 0

    def setUp(self) -> None:
        self.cat = Cat(self.SIZE)

    def test__eat__expect_increased_size(self):
        self.cat.eat()
        self.assertEqual(self.SIZE + 1, self.cat.size)

    def test__eat__expect_fed_to_be_true(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test__eat__when_fed_is_true__expect_to_raise(self):
        self.cat.eat()

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertIsNotNone(ex)

    def test__sleep__when_fed_is_false__expect_to_raise(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertIsNotNone(ex)

    def test__sleep__expect_sleepy_to_be_false(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    main()