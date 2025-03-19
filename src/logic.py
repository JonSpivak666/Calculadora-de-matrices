# src/logic.py

import numpy as np
import scipy.linalg

# =======================
# Funciones Básicas
# =======================

def add_matrices(matrix_a, matrix_b):
    """
    Suma dos matrices si tienen las mismas dimensiones.
    """
    matrix_a = np.array(matrix_a)
    matrix_b = np.array(matrix_b)
    if matrix_a.shape != matrix_b.shape:
        raise ValueError("Las matrices deben tener las mismas dimensiones para sumarse.")
    return matrix_a + matrix_b

def subtract_matrices(matrix_a, matrix_b):
    """
    Resta dos matrices si tienen las mismas dimensiones.
    """
    matrix_a = np.array(matrix_a)
    matrix_b = np.array(matrix_b)
    if matrix_a.shape != matrix_b.shape:
        raise ValueError("Las matrices deben tener las mismas dimensiones para restarse.")
    return matrix_a - matrix_b

def multiply_matrices(matrix_a, matrix_b):
    """
    Multiplica dos matrices si sus dimensiones son compatibles.
    """
    matrix_a = np.array(matrix_a)
    matrix_b = np.array(matrix_b)
    if matrix_a.shape[1] != matrix_b.shape[0]:
        raise ValueError("El número de columnas de la primera matriz debe coincidir con el número de filas de la segunda matriz.")
    return np.dot(matrix_a, matrix_b)

def transpose(matrix):
    """
    Devuelve la transpuesta de una matriz.
    """
    matrix = np.array(matrix)
    return matrix.T

def scalar_multiply(matrix, scalar):
    """
    Multiplica una matriz por un escalar.
    """
    matrix = np.array(matrix)
    return scalar * matrix

# =======================
# Funciones Avanzadas
# =======================

def determinant(matrix):
    """
    Calcula el determinante de una matriz cuadrada.
    """
    matrix = np.array(matrix)
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Solo se puede calcular el determinante de una matriz cuadrada.")
    return np.linalg.det(matrix)

def inverse(matrix):
    """
    Calcula la inversa de una matriz si es cuadrada y no singular.
    """
    matrix = np.array(matrix)
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("La matriz debe ser cuadrada para calcular su inversa.")
    if np.linalg.det(matrix) == 0:
        raise ValueError("La matriz es singular y no tiene inversa.")
    return np.linalg.inv(matrix)

def rank(matrix):
    """
    Calcula el rango de una matriz.
    """
    matrix = np.array(matrix)
    return np.linalg.matrix_rank(matrix)

def eigenvalues_and_eigenvectors(matrix):
    """
    Calcula los valores y vectores propios de una matriz cuadrada.
    """
    matrix = np.array(matrix)
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("La matriz debe ser cuadrada para calcular valores propios.")
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return {"Valores Propios": eigenvalues, "Vectores Propios": eigenvectors}

def solve_linear_system(coeff_matrix, constants):
    """
    Resuelve un sistema de ecuaciones lineales de la forma Ax = b.
    """
    coeff_matrix = np.array(coeff_matrix)
    constants = np.array(constants)
    if coeff_matrix.shape[0] != coeff_matrix.shape[1]:
        raise ValueError("La matriz de coeficientes debe ser cuadrada.")
    if coeff_matrix.shape[0] != constants.shape[0]:
        raise ValueError("Las dimensiones de la matriz y el vector de constantes deben coincidir.")

    return np.linalg.solve(coeff_matrix, constants)

# =======================
# Funciones de Factorización y Descomposición
# =======================

def lu_factorization(matrix):
    """
    Realiza la factorización LU de una matriz cuadrada.
    Devuelve las matrices L y U.
    """
    matrix = np.array(matrix)
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("La matriz debe ser cuadrada para la factorización LU.")
    P, L, U = scipy.linalg.lu(matrix)
    return {"P": P, "L": L, "U": U}

def qr_decomposition(matrix):
    """
    Realiza la descomposición QR de una matriz.
    Devuelve las matrices Q y R.
    """
    matrix = np.array(matrix)
    Q, R = np.linalg.qr(matrix)
    return {"Q": Q, "R": R}

def svd_decomposition(matrix):
    """
    Realiza la descomposición en valores singulares (SVD) de una matriz.
    Devuelve las matrices U, Σ y V^T.
    """
    matrix = np.array(matrix)
    U, S, Vt = np.linalg.svd(matrix)
    return {"U": U, "Σ": np.diag(S), "V^T": Vt}

