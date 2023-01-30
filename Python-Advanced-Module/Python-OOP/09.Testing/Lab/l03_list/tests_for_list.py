from extended_list import IntegerList
from unittest import TestCase, main


class IntegerListTests(TestCase):

    def setUp(self) -> None:
        self.my_list = IntegerList(1, "asd", True, 2, 8.5, 3)

    def test__init__expect_correct_values(self):
        self.assertEqual([1, 2, 3], self.my_list._IntegerList__data)

    def test__get_data__expect_correct_list(self):
        self.assertEqual([1, 2, 3], self.my_list.get_data())

    def test__add__when_element_not_int__expect_to_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.my_list.add('some_text')

        self.assertEqual("Element is not Integer", str(ve.exception))
        self.assertIsNotNone(ve)

    def test__add__when_int_element_added__expect_element_to_be_added(self):
        result = self.my_list.add(8)
        self.assertEqual([1, 2, 3, 8], result)
        self.assertEqual([1, 2, 3, 8], self.my_list._IntegerList__data)

    def test__remove_index__when_invalid_index__expect_to_raise_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.my_list.remove_index(3)

        self.assertEqual("Index is out of range", str(ie.exception))
        self.assertIsNotNone(ie)

    def test__remove_index__when_valid_index__expect_element_to_be_removed(self):
        result = self.my_list.remove_index(2)
        self.assertEqual([1, 2], self.my_list._IntegerList__data)
        self.assertNotIn(3, self.my_list._IntegerList__data)
        self.assertEqual(result, 3)

    def test__get__when_invalid_index__expect_to_raise_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.my_list.get(3)

        self.assertEqual("Index is out of range", str(ie.exception))
        self.assertIsNotNone(ie)

    def test__get__when_valid_index__expect_to_return_element_at_index(self):
        result = self.my_list.get(2)
        self.assertEqual(result, 3)

        self.assertEqual(3, self.my_list.get(2))

    def test__insert__when_invalid_index__expect_to_raise_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.my_list.insert(4, 10)

        self.assertEqual("Index is out of range", str(ie.exception))
        self.assertIsNotNone(ie)

    def test__insert__when_valid_index_and_invalid_element__expect_to_raise_type_error(self):
        with self.assertRaises(ValueError) as ve:
            self.my_list.insert(2, 'some element of invalid type')

        self.assertEqual("Element is not Integer", str(ve.exception))
        self.assertIsNotNone(ve)

    def test__insert_when_both_values_correct__expect_element_insertion_at_index(self):
        self.my_list.insert(2, 10)
        self.assertEqual([1, 2, 10, 3], self.my_list._IntegerList__data)

    def test__get_biggest__expect_largest_num(self):
        self.assertEqual(3, self.my_list.get_biggest())

    def test__get_index__expect_index_by_given_element(self):
        self.assertEqual(2, self.my_list.get_index(3))


if __name__ == '__main__':
    main()