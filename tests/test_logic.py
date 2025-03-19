# tests/test_logic.py

import unittest
import numpy as np
import src.logic as logic

class TestMatrixOperations(unittest.TestCase):

    def setUp(self):
        """
        Configuración inicial: definimos matrices de prueba.
        """
        self.matrix_a = np.array([[1, 2], [3, 4]])
        self.matrix_b = np.array([[5, 6], [7, 8]])
        self.scalar = 2

    # =============================
    # Pruebas para Funciones Básicas
    # =============================

    def test_add_matrices(self):
        result = logic.add_matrices(self.matrix_a, self.matrix_b)
        expected = np.array([[6, 8], [10, 12]])
        np.testing.assert_array_equal(result, expected)

    def test_subtract_matrices(self):
        result = logic.subtract_matrices(self.matrix_a, self.matrix_b)
        expected = np.array([[-4, -4], [-4, -4]])
        np.testing.assert_array_equal(result, expected)

    def test_multiply_matrices(self):
        result = logic.multiply_matrices(self.matrix_a, self.matrix_b)
        expected = np.array([[19, 22], [43, 50]])
        np.testing.assert_array_equal(result, expected)

    def test_transpose(self):
        result = logic.transpose(self.matrix_a)
        expected = np.array([[1, 3], [2, 4]])
        np.testing.assert_array_equal(result, expected)

    def test_scalar_multiply(self):
        result = logic.scalar_multiply(self.matrix_a, self.scalar)
        expected = np.array([[2, 4], [6, 8]])
        np.testing.assert_array_equal(result, expected)

    # =============================
    # Pruebas para Funciones Avanzadas
    # =============================

    def test_determinant(self):
        result = logic.determinant(self.matrix_a)
        expected = -2.0
        self.assertAlmostEqual(result, expected)

    def test_inverse(self):
        result = logic.inverse(self.matrix_a)
        expected = np.array([[-2.0, 1.0], [1.5, -0.5]])
        np.testing.assert_almost_equal(result, expected, decimal=6)

    def test_rank(self):
        result = logic.rank(self.matrix_a)
        expected = 2
        self.assertEqual(result, expected)

    def test_eigenvalues_and_eigenvectors(self):
        eigenvalues, _ = logic.eigenvalues_and_eigenvectors(self.matrix_a)
        expected = np.linalg.eigvals(self.matrix_a)
        np.testing.assert_almost_equal(eigenvalues, expected, decimal=6)

    def test_solve_linear_system(self):
        coeff_matrix = np.array([[2, 3], [1, 2]])
        constants = np.array([5, 3])
        result = logic.solve_linear_system(coeff_matrix, constants)
        expected = np.linalg.solve(coeff_matrix, constants)
        np.testing.assert_almost_equal(result, expected, decimal=6)

    # =============================
    # Pruebas para Errores Esperados
    # =============================

    def test_invalid_addition(self):
        with self.assertRaises(ValueError):
            logic.add_matrices(self.matrix_a, np.array([[1, 2, 3], [4, 5, 6]]))

    def test_invalid_determinant(self):
        with self.assertRaises(ValueError):
            logic.determinant(np.array([[1, 2, 3], [4, 5, 6]]))  # No es cuadrada

    def test_singular_matrix_inverse(self):
        singular_matrix = np.array([[1, 2], [2, 4]])  # Determinante = 0
        with self.assertRaises(ValueError):
            logic.inverse(singular_matrix)

if __name__ == '__main__':
    unittest.main()
