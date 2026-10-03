import streamlit as st
import pandas as pd
import numpy as np


# ============================================================
# CONFIGURACIÓN GENERAL DE LA APLICACIÓN
# ============================================================

st.set_page_config(
    page_title="FIFA World Cup 2026 - EDA",
    page_icon="⚽",
    layout="wide"
)


# ============================================================
# TÍTULO PRINCIPAL
# ============================================================

st.title("⚽ FIFA World Cup 2026")
st.subheader("Análisis Exploratorio de Datos de Rendimiento de Jugadores")

st.markdown("---")


# ============================================================
# CLASE DE PROCESAMIENTO DE DATOS
# ============================================================

class DataAnalyzer:
    """
    Clase encargada de gestionar y procesar
    el dataset de rendimiento de jugadores.
    """

    def __init__(self, dataframe):
        self.df = dataframe

    def obtener_dimensiones(self):
        """Devuelve cantidad de filas y columnas."""
        filas, columnas = self.df.shape
        return filas, columnas

    def obtener_nulos(self):
        """Devuelve el conteo de valores nulos por columna."""
        return self.df.isnull().sum()

    def obtener_duplicados(self):
        """Devuelve la cantidad de registros duplicados."""
        return self.df.duplicated().sum()

    def clasificar_variables(self):
        """Clasifica las variables en numéricas y categóricas."""

        variables_numericas = self.df.select_dtypes(
            include=np.number
        ).columns.tolist()

        variables_categoricas = self.df.select_dtypes(
            exclude=np.number
        ).columns.tolist()

        return variables_numericas, variables_categoricas


# ============================================================
# SIDEBAR - MENÚ PRINCIPAL
# ============================================================

st.sidebar.title("📌 Menú principal")

opcion = st.sidebar.radio(
    "Selecciona una sección:",
    [
        "🏠 Home",
        "📂 Carga del dataset",
        "📊 Análisis Exploratorio (EDA)"
    ]
)


# ============================================================
# SIDEBAR - INFORMACIÓN DEL PROYECTO
# ============================================================

st.sidebar.markdown("---")

st.sidebar.info(
    """
    **Proyecto aplicado**

    FIFA World Cup 2026

    Especialización en Python for Analytics

    Año: 2026
    """
)


# ============================================================
# MÓDULO 1: HOME
# ============================================================

if opcion == "🏠 Home":

    st.header("🏠 Presentación del proyecto")

    st.markdown(
        """
        ## FIFA World Cup 2026 – Player Performance

        Este proyecto tiene como finalidad desarrollar un **Análisis
        Exploratorio de Datos (EDA)** sobre el rendimiento de los
        jugadores durante la FIFA World Cup 2026.

        El análisis permitirá explorar diferentes características
        técnicas, ofensivas, defensivas, físicas y contextuales
        relacionadas con el rendimiento de los jugadores.
        """
    )

    st.markdown("---")

    # --------------------------------------------------------
    # INFORMACIÓN DEL AUTOR
    # --------------------------------------------------------

    st.subheader("👤 Datos del autor")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("**Nombre:**")
        st.write("Sebastián Ccala")

    with col2:
        st.write("**Curso:**")
        st.write("Especialización en Python for Analytics")

    with col3:
        st.write("**Año:**")
        st.write("2026")

    st.markdown("---")

    # --------------------------------------------------------
    # INFORMACIÓN DEL DATASET
    # --------------------------------------------------------

    st.subheader("📊 Sobre el dataset")

    st.write(
        """
        El dataset contiene información relacionada con el desempeño
        individual de jugadores durante partidos de la FIFA World Cup
        2026.

        Cada registro representa la actuación de un jugador en un partido
        e incluye información sobre selección, rival, estadio, fase del
        torneo, resultado y diferentes métricas de rendimiento.
        """
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="Registros",
            value="54,600"
        )

    with col2:
        st.metric(
            label="Variables",
            value="75"
        )

    with col3:
        st.metric(
            label="Jugadores",
            value="1,248"
        )

    st.markdown("---")

    # --------------------------------------------------------
    # TECNOLOGÍAS
    # --------------------------------------------------------

    st.subheader("🛠️ Tecnologías utilizadas")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.info("🐍 Python")

    with col2:
        st.info("🐼 Pandas")

    with col3:
        st.info("🔢 NumPy")

    with col4:
        st.info("🎈 Streamlit")

    st.markdown("---")

    st.success(
        "Proyecto orientado al Análisis Exploratorio de Datos (EDA), "
        "sin construcción de modelos predictivos."
    )


# ============================================================
# MÓDULO 2: CARGA DEL DATASET
# ============================================================

elif opcion == "📂 Carga del dataset":

    st.header("📂 Carga del dataset")

    st.write(
        """
        Antes de realizar cualquier análisis, debes cargar el archivo
        CSV correspondiente al proyecto.
        """
    )

    # --------------------------------------------------------
    # CARGADOR DE ARCHIVO
    # --------------------------------------------------------

    archivo = st.file_uploader(
        "Selecciona el archivo CSV:",
        type=["csv"]
    )

    # --------------------------------------------------------
    # VALIDACIÓN DEL ARCHIVO
    # --------------------------------------------------------

    if archivo is not None:

        try:

            # Leer CSV
            df = pd.read_csv(archivo)

            # Crear objeto de la clase
            analyzer = DataAnalyzer(df)

            st.success(
                f"✅ Archivo cargado correctamente: {archivo.name}"
            )

            st.markdown("---")

            # ------------------------------------------------
            # DIMENSIONES
            # ------------------------------------------------

            filas, columnas = analyzer.obtener_dimensiones()

            st.subheader("📐 Dimensiones del dataset")

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Número de filas",
                    f"{filas:,}"
                )

            with col2:
                st.metric(
                    "Número de columnas",
                    f"{columnas}"
                )

            st.markdown("---")

            # ------------------------------------------------
            # VISTA PREVIA
            # ------------------------------------------------

            st.subheader("👀 Vista previa del dataset")

            st.write(
                "Primeros 5 registros:"
            )

            st.dataframe(
                df.head(),
                use_container_width=True
            )

            st.markdown("---")

            # ------------------------------------------------
            # INFORMACIÓN BÁSICA
            # ------------------------------------------------

            st.subheader("📋 Información básica")

            col1, col2 = st.columns(2)

            with col1:

                st.write("**Nombre del archivo:**")

                st.code(
                    archivo.name
                )

            with col2:

                st.write("**Tamaño del dataset:**")

                st.code(
                    f"{filas:,} filas × {columnas} columnas"
                )

            # ------------------------------------------------
            # VARIABLES DEL DATASET
            # ------------------------------------------------

            st.markdown("---")

            st.subheader("📝 Variables disponibles")

            st.write(
                "Listado de las variables presentes en el dataset:"
            )

            st.write(
                df.columns.tolist()
            )

        except Exception as error:

            st.error(
                "❌ Ocurrió un error al leer el archivo."
            )

            st.exception(error)

    else:

        st.warning(
            "⚠️ Debes cargar el archivo "
            "`fifa_world_cup_2026_player_performance.csv` "
            "para continuar."
        )

        st.info(
            """
            El análisis no se ejecutará hasta que el archivo
            CSV haya sido cargado correctamente.
            """
        )


# ============================================================
# MÓDULO 3: ANÁLISIS EXPLORATORIO
# ============================================================

elif opcion == "📊 Análisis Exploratorio (EDA)":

    st.header("📊 Análisis Exploratorio de Datos")

    st.info(
        """
        Para realizar el análisis exploratorio primero debes cargar
        el dataset desde la sección **📂 Carga del dataset**.
        """
    )

    st.markdown("---")

    st.subheader("🔎 Próximamente")

    st.write(
        """
        En esta sección construiremos los 10 análisis solicitados
        en el caso de estudio:

        1. Información general del dataset.
        2. Clasificación de variables.
        3. Estadísticas descriptivas.
        4. Análisis de valores faltantes.
        5. Distribución de variables numéricas.
        6. Análisis de variables categóricas.
        7. Análisis bivariado numérico vs categórico.
        8. Análisis bivariado categórico vs categórico.
        9. Análisis mediante parámetros seleccionados.
        10. Hallazgos clave.
        """
    )

    st.warning(
        "Esta sección será desarrollada en los siguientes pasos del proyecto."
    )


# ============================================================
# PIE DE PÁGINA
# ============================================================

st.markdown("---")

st.caption(
    "FIFA World Cup 2026 | Análisis Exploratorio de Datos | "
    "Python for Analytics | Sebastián Ccala | 2026"
)
