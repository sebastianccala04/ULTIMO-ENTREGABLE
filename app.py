import streamlit as st
import pandas as pd
import numpy as np


# ============================================================
# CONFIGURACIÓN DE LA APLICACIÓN
# ============================================================

st.set_page_config(
    page_title="FIFA World Cup 2026 - EDA",
    page_icon="⚽",
    layout="wide"
)


# ============================================================
# CLASE DE ANÁLISIS
# ============================================================

class DataAnalyzer:
    """
    Clase encargada de gestionar el dataset
    y preparar los datos para el análisis.
    """

    def __init__(self, dataframe):
        self.df = dataframe

    def obtener_dimensiones(self):
        """Obtiene las dimensiones del dataset."""
        return self.df.shape

    def obtener_nulos(self):
        """Obtiene los valores nulos por columna."""
        return self.df.isnull().sum()

    def obtener_duplicados(self):
        """Obtiene la cantidad de registros duplicados."""
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
# TÍTULO PRINCIPAL
# ============================================================

st.title("⚽ FIFA World Cup 2026")
st.subheader("Análisis Exploratorio de Datos de Rendimiento de Jugadores")

st.markdown("---")


# ============================================================
# MENÚ LATERAL
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
# INFORMACIÓN LATERAL
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

        Este proyecto tiene como finalidad desarrollar un
        **Análisis Exploratorio de Datos (EDA)** sobre el rendimiento
        de los jugadores durante la FIFA World Cup 2026.

        El análisis permitirá explorar diferentes características
        técnicas, ofensivas, defensivas, físicas y contextuales
        relacionadas con el rendimiento de los jugadores.
        """
    )

    st.markdown("---")

    # Información del autor
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

    # Información del dataset
    st.subheader("📊 Sobre el dataset")

    st.write(
        """
        El dataset contiene información relacionada con el desempeño
        individual de jugadores durante partidos de la FIFA World Cup
        2026.

        Cada registro representa la actuación de un jugador en un
        partido e incluye información sobre selección, rival, estadio,
        fase del torneo, resultado y diferentes métricas de rendimiento.
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

    # Tecnologías
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
        "Carga el archivo CSV para comenzar con el proyecto."
    )

    # --------------------------------------------------------
    # CARGA DEL ARCHIVO
    # --------------------------------------------------------

    archivo = st.file_uploader(
        "Selecciona el archivo CSV:",
        type=["csv"]
    )

    # --------------------------------------------------------
    # VALIDACIÓN
    # --------------------------------------------------------

    if archivo is not None:

        try:

            # Leer el archivo CSV
            df = pd.read_csv(archivo)

            # Crear objeto de la clase
            analyzer = DataAnalyzer(df)

            # Confirmación de carga
            st.success(
                "✅ El archivo fue cargado correctamente."
            )

            st.markdown("---")

            # ------------------------------------------------
            # DIMENSIONES DEL DATASET
            # ------------------------------------------------

            st.subheader("📐 Dimensiones del dataset")

            filas, columnas = analyzer.obtener_dimensiones()

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Filas",
                    f"{filas:,}"
                )

            with col2:
                st.metric(
                    "Columnas",
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

        except Exception as error:

            st.error(
                "❌ No fue posible cargar el archivo."
            )

            st.exception(error)

    else:

        st.warning(
            "⚠️ Primero debes cargar el archivo CSV."
        )


# ============================================================
# MÓDULO 3: ANÁLISIS EXPLORATORIO
# ============================================================

elif opcion == "📊 Análisis Exploratorio (EDA)":

    st.header("📊 Análisis Exploratorio de Datos")

    st.info(
        """
        Primero debemos cargar el dataset desde la sección
        **📂 Carga del dataset**.

        Los análisis serán desarrollados en los siguientes pasos.
        """
    )

    st.markdown("---")

    st.subheader("📋 Análisis que desarrollaremos")

    st.write(
        """
        **Ítem 1:** Información general del dataset

        **Ítem 2:** Clasificación de variables

        **Ítem 3:** Estadísticas descriptivas

        **Ítem 4:** Análisis de valores faltantes

        **Ítem 5:** Distribución de variables numéricas

        **Ítem 6:** Análisis de variables categóricas

        **Ítem 7:** Análisis bivariado numérico vs categórico

        **Ítem 8:** Análisis bivariado categórico vs categórico

        **Ítem 9:** Análisis basado en parámetros seleccionados

        **Ítem 10:** Hallazgos clave
        """
    )

    st.warning(
        "Los análisis serán incorporados progresivamente."
    )


# ============================================================
# PIE DE PÁGINA
# ============================================================

st.markdown("---")

st.caption(
    "FIFA World Cup 2026 | Análisis Exploratorio de Datos | "
    "Python for Analytics | Sebastián Ccala | 2026")
elif opcion == "📊 Análisis Exploratorio (EDA)":

    st.header("📊 Ítem 1: Información general del dataset")

    archivo = st.file_uploader(
        "Carga el archivo CSV:",
        type=["csv"]
    )

    if archivo is not None:

        df = pd.read_csv(archivo)

        st.success("✅ Dataset cargado correctamente.")

        tab1, tab2, tab3, tab4 = st.tabs([
            "📋 Información general",
            "🔤 Tipos de datos",
            "⚠️ Valores nulos",
            "🔁 Duplicados"
        ])

        with tab1:
            st.subheader("📋 Información general")

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Filas", f"{df.shape[0]:,}")

            with col2:
                st.metric("Columnas", df.shape[1])

            info = pd.DataFrame({
                "Variable": df.columns,
                "Tipo de dato": df.dtypes.astype(str),
                "Valores no nulos": df.notna().sum(),
                "Valores nulos": df.isnull().sum()
            })

            st.dataframe(
                info,
                use_container_width=True,
                hide_index=True
            )

        with tab2:
            st.subheader("🔤 Tipos de datos")

            tipos = pd.DataFrame({
                "Variable": df.columns,
                "Tipo de dato": df.dtypes.astype(str)
            })

            st.dataframe(
                tipos,
                use_container_width=True,
                hide_index=True
            )

        with tab3:
            st.subheader("⚠️ Conteo de valores nulos")

            nulos = df.isnull().sum()

            nulos_df = pd.DataFrame({
                "Variable": nulos.index,
                "Valores nulos": nulos.values
            })

            st.dataframe(
                nulos_df,
                use_container_width=True,
                hide_index=True
            )

            if nulos.sum() == 0:
                st.success("✅ No existen valores nulos en el dataset.")
            else:
                st.warning(
                    f"⚠️ Se encontraron {nulos.sum():,} valores nulos."
                )

        with tab4:
            st.subheader("🔁 Identificación de registros duplicados")

            duplicados = df.duplicated().sum()

            st.metric(
                "Registros duplicados",
                f"{duplicados:,}"
            )

            if duplicados == 0:
                st.success("✅ No existen registros duplicados.")
            else:
                st.warning(
                    f"⚠️ Se encontraron {duplicados:,} registros duplicados."
                )

    else:
        st.warning(
            "⚠️ Debes cargar el archivo CSV para realizar el análisis."
        )
