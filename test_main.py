from unittest import TestCase
from main import MatrixProcessor


class TestMatrixProcessor(TestCase):

    def setUp(self):
        # авт зап мет
        # ств баз матр
        self.matrix_a = [
            [1.0, 2.0],
            [3.0, 4.0]
        ]
        self.matrix_b = [
            [5.0, 6.0],
            [7.0, 8.0]
        ]

    def test_add_matrices(self):
        # ініц кл
        processor = MatrixProcessor(self.matrix_a, self.matrix_b)

        # очік рез
        expected = [
            [6.0, 8.0],
            [10.0, 12.0]
        ]

        # пер рез
        self.assertEqual(processor.add_matrices(), expected)

    def test_calculate_column_averages(self):
        # ініц кл
        processor = MatrixProcessor(self.matrix_a, self.matrix_b)

        # матр рез
        matrix_c = [
            [6.0, 8.0],
            [10.0, 12.0]
        ]
        expected_averages = [8.0, 10.0]

        # пер сер знач
        self.assertEqual(processor.calculate_column_averages(matrix_c), expected_averages)

    def test__validate_matrices(self):
        # ств інш матр
        bad_matrix = [[1.0, 2.0]]

        # пер вик пом
        with self.assertRaises(ValueError):
            MatrixProcessor(self.matrix_a, bad_matrix)