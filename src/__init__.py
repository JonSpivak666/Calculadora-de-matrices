# src/__init__.py

# Importar funciones clave para facilitar su acceso desde otros módulos
from .logic import (
    add_matrices,
    subtract_matrices,
    multiply_matrices,
    determinant,
    inverse,
    transpose,
    rank,
    eigenvalues_and_eigenvectors,
    solve_linear_system
)

# Importar la función render desde ui.py
from .ui import render

# Importar configuraciones generales
from .config import APP_TITLE, APP_SUBTITLE, COLORS, IMAGES

