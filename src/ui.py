# src/ui.py

import os
import streamlit as st
import src.config as config
import src.logic as logic

def set_page_config():
    """
    Configura los ajustes generales de la página en Streamlit.
    """
    st.set_page_config(
        page_title=config.APP_TITLE,
        page_icon="🧮",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Aplicar estilos personalizados desde styles/style.css
    with open(os.path.join(os.path.dirname(__file__), "../styles/style.css")) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def show_header():
    """
    Muestra el título y los escudos en la parte superior de la aplicación.
    """
    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        if os.path.exists(config.IMAGES["unam"]):
            st.image(config.IMAGES["unam"], width=100)
        else:
            st.warning("⚠️ No se encontró el escudo de la UNAM.")

    with col2:
        st.title(config.APP_TITLE)
        st.subheader(config.APP_SUBTITLE)

    with col3:
        if os.path.exists(config.IMAGES["fes"]):
            st.image(config.IMAGES["fes"], width=100)
        else:
            st.warning("⚠️ No se encontró el escudo de la FES.")

    # Espacio para otro escudo
    if os.path.exists(config.IMAGES["otro"]):
        st.image(config.IMAGES["otro"], width=100)
    else:
        st.warning("⚠️ No se encontró el tercer escudo.")

def show_instructions():
    """
    Muestra las instrucciones de uso de la aplicación.
    """
    st.markdown("""
    ## ℹ️ Instrucciones de Uso
    1. **Selecciona el tamaño de la matriz** con el control deslizante (hasta 10x10).
    2. **Elige la operación** que deseas realizar en el menú desplegable.
    3. **Ingresa los valores de la matriz (o matrices)** en los cuadros de texto.
    4. **Haz clic en el botón correspondiente** para realizar la operación.
    5. **El resultado se mostrará en la parte inferior.**
    """)

def matrix_input(label, size):
    """
    Permite al usuario ingresar una matriz en formato de texto y la convierte en numpy array.
    """
    matrix_str = st.text_area(label, value="\n".join([" ".join(["0"] * size) for _ in range(size)]))
    try:
        matrix = [[float(num) for num in row.split()] for row in matrix_str.split("\n") if row]
        return matrix
    except ValueError:
        st.error("⚠️ Formato inválido. Asegúrate de ingresar solo números separados por espacios.")
        return None

def show_operations():
    """
    Muestra las operaciones disponibles con matrices, permitiendo elegir la dimensión y la operación.
    """
    st.subheader("🔢 Configuración de Operaciones")

    # Selector del tamaño de la matriz
    size = st.slider("Selecciona el tamaño de la matriz (n x n)", min_value=1, max_value=10, value=3, step=1)

    # Menú desplegable para elegir la operación
    operation = st.selectbox("Selecciona una operación", [
        "Suma de Matrices",
        "Resta de Matrices",
        "Multiplicación de Matrices",
        "Determinante",
        "Inversa",
        "Transpuesta",
        "Rango",
        "Factorización LU",
        "Descomposición QR",
        "Descomposición SVD"
    ])

    st.subheader("📥 Ingreso de Matrices")

    # Creación de matrices dinámicas según el tamaño seleccionado
    col1, col2 = st.columns(2)
    with col1:
        matrix_a = matrix_input(f"Matriz A ({size}x{size})", size)
    with col2:
        matrix_b = matrix_input(f"Matriz B ({size}x{size})", size) if operation in ["Suma de Matrices", "Resta de Matrices", "Multiplicación de Matrices"] else None

    # Verificar si las matrices se han ingresado correctamente
    if matrix_a is None or (matrix_b is None and operation in ["Suma de Matrices", "Resta de Matrices", "Multiplicación de Matrices"]):
        st.warning("⚠️ Ingresa correctamente las matrices para continuar.")
        return

    # Ejecutar la operación seleccionada
    st.subheader("📌 Resultado")

    try:
        if operation == "Suma de Matrices":
            result = logic.add_matrices(matrix_a, matrix_b)
        elif operation == "Resta de Matrices":
            result = logic.subtract_matrices(matrix_a, matrix_b)
        elif operation == "Multiplicación de Matrices":
            result = logic.multiply_matrices(matrix_a, matrix_b)
        elif operation == "Determinante":
            result = logic.determinant(matrix_a)
        elif operation == "Inversa":
            result = logic.inverse(matrix_a)
        elif operation == "Transpuesta":
            result = logic.transpose(matrix_a)
        elif operation == "Rango":
            result = logic.rank(matrix_a)
        elif operation == "Factorización LU":
            result = logic.lu_factorization(matrix_a)
        elif operation == "Descomposición QR":
            result = logic.qr_decomposition(matrix_a)
        elif operation == "Descomposición SVD":
            result = logic.svd_decomposition(matrix_a)
        else:
            result = "Operación no implementada."

        st.write(result)
    except ValueError as e:
        st.error(f"⚠️ Error: {str(e)}")

def show_footer():
    """
    Muestra un mensaje en el pie de página con el crédito de la aplicación.
    """
    st.markdown("""
    ---
    ✅ **Este programa es libre y sin fines de lucro para  FES Aragón, UNAM.**
    """, unsafe_allow_html=True)

def render():
    """
    Renderiza la interfaz completa con instrucciones y pie de página.
    """
    set_page_config()
    show_header()
    show_instructions()
    show_operations()
    show_footer()

