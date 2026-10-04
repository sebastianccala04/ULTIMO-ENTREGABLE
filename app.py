import streamlit as st
import pandas as pd
import numpy as np


# =========================================================
# CONFIGURACIÓN DE LA APLICACIÓN
# =========================================================

st.set_page_config(
    page_title="FIFA World Cup 2026 - EDA",
    page_icon="⚽",
    layout="wide"
)


# =========================================================
# CLASE PARA EL ANÁLISIS DEL DATASET
# =========================================================

class DataAnalyzer:

    def __init__(self, dataframe):
        self.df = dataframe

    def obtener_dimensiones(self):
        return self.df.shape

    def obtener_nulos(self):
        return self.df.isnull().sum()

    def obtener_duplicados(self):
        return self.df.duplicated().sum()

    def clasificar_variables(self):

        numericas = self.df.select_dtypes(
            include=np.number
        ).columns.tolist()

        categoricas = self.df.select_dtypes(
            exclude=np.number
        ).columns.tolist()

        return numericas, categoricas


# =========================================================
# SESSION STATE
# =========================================================

if "df" not in st.session_state:
    st.session_state.df = None


# =========================================================
# MENÚ LATERAL
# =========================================================

opcion = st.sidebar.radio(
    "Selecciona un módulo:",
    [
        "🏠 Home",
        "📂 Carga del dataset",
        "📊 Análisis Exploratorio (EDA)"
    ]
)


# =========================================================
# HOME
# =========================================================

if opcion == "🏠 Home":

    st.title("⚽ FIFA World Cup 2026")

    st.subheader(
        "Análisis Exploratorio de Datos"
    )

    st.write(
        "Proyecto de análisis exploratorio del rendimiento "
        "de jugadores durante la FIFA World Cup 2026."
    )

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### 👤 Autor")
        st.write("Sebastián Ccala")

        st.markdown("### 📚 Curso")
        st.write("Especialización en Python for Analytics")

        st.markdown("### 📅 Año")
        st.write("2026")

    with col2:

        st.markdown("### 📊 Dataset")
        st.write(
            "FIFA World Cup 2026 Player Performance"
        )

        st.markdown("### 📌 Registros")
        st.write("54,600")

        st.markdown("### 📌 Variables")
        st.write("75")

    st.markdown("---")

    st.markdown("### 🛠️ Tecnologías")

    st.write(
        "Python, Streamlit, NumPy, Pandas, "
        "Matplotlib y Seaborn"
    )

    st.markdown("---")

    st.caption(
        "FIFA World Cup 2026 | "
        "Análisis Exploratorio de Datos | "
        "Python for Analytics | "
        "Sebastián Ccala | 2026"
    )


# =========================================================
# CARGA DEL DATASET
# =========================================================

elif opcion == "📂 Carga del dataset":

    st.header("📂 Carga del dataset")

    st.write(
        "Carga el archivo CSV para comenzar el análisis."
    )

    archivo = st.file_uploader(
        "Selecciona el archivo CSV:",
        type=["csv"]
    )

    if archivo is not None:

        try:

            # Leer CSV
            df = pd.read_csv(archivo)

            # Guardar en session_state
            st.session_state.df = df

            st.success(
                "✅ Archivo cargado correctamente."
            )

            st.markdown("---")

            # Métricas
            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "📊 Registros",
                    f"{df.shape[0]:,}"
                )

            with col2:

                st.metric(
                    "📁 Variables",
                    df.shape[1]
                )

            with col3:

                st.metric(
                    "⚠️ Valores nulos",
                    int(df.isnull().sum().sum())
                )

            st.markdown("---")

            # Primeros registros
            st.subheader(
                "👀 Primeros registros"
            )

            st.dataframe(
                df.head(10),
                use_container_width=True
            )

        except Exception as e:

            st.error(
                f"❌ Error al cargar el archivo: {e}"
            )

    else:

        st.info(
            "📌 Debes cargar el archivo CSV para continuar."
        )


# =========================================================
# ANÁLISIS EXPLORATORIO
# =========================================================

elif opcion == "📊 Análisis Exploratorio (EDA)":

    st.header(
        "📊 Análisis Exploratorio de Datos"
    )

    # -----------------------------------------------------
    # VERIFICAR SI EXISTE DATASET
    # -----------------------------------------------------

    if st.session_state.df is None:

        st.warning(
            "⚠️ Primero debes cargar el archivo desde "
            "📂 Carga del dataset."
        )

        st.stop()


    # -----------------------------------------------------
    # OBTENER DATAFRAME
    # -----------------------------------------------------

    df = st.session_state.df


    # -----------------------------------------------------
    # TÍTULO DEL ÍTEM
    # -----------------------------------------------------

    st.subheader(
        "Ítem 1: Información general del dataset"
    )


    # =====================================================
    # PESTAÑAS
    # =====================================================

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "📋 Información general",
            "🔤 Tipos de datos",
            "⚠️ Valores nulos",
            "🔁 Duplicados"
        ]
    )


    # =====================================================
    # TAB 1 - INFORMACIÓN GENERAL
    # =====================================================

    with tab1:

        st.markdown(
            "### 📋 Resumen general del dataset"
        )

        # -------------------------------------------------
        # MÉTRICAS PRINCIPALES
        # -------------------------------------------------

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.metric(
                "📊 Registros",
                f"{df.shape[0]:,}"
            )

        with col2:

            st.metric(
                "📁 Variables",
                df.shape[1]
            )

        with col3:

            total_nulos = int(
                df.isnull().sum().sum()
            )

            st.metric(
                "⚠️ Valores nulos",
                total_nulos
            )

        with col4:

            total_duplicados = int(
                df.duplicated().sum()
            )

            st.metric(
                "🔁 Duplicados",
                total_duplicados
            )


        st.markdown("---")


        # -------------------------------------------------
        # CLASIFICACIÓN DE VARIABLES
        # -------------------------------------------------

        st.markdown(
            "### 🔤 Clasificación de variables"
        )

        numericas = df.select_dtypes(
            include=np.number
        ).shape[1]

        categoricas = df.select_dtypes(
            exclude=np.number
        ).shape[1]

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "🔢 Variables numéricas",
                numericas
            )

        with col2:

            st.metric(
                "🔤 Variables categóricas",
                categoricas
            )


        st.markdown("---")


        # -------------------------------------------------
        # TABLA RESUMEN
        # -------------------------------------------------

        st.markdown(
            "### 📑 Resumen de estructura"
        )

        resumen = pd.DataFrame(
            {
                "Indicador": [
                    "Número de registros",
                    "Número de variables",
                    "Variables numéricas",
                    "Variables categóricas",
                    "Valores nulos",
                    "Registros duplicados"
                ],

                "Resultado": [
                    f"{df.shape[0]:,}",
                    df.shape[1],
                    numericas,
                    categoricas,
                    total_nulos,
                    total_duplicados
                ]
            }
        )

        st.dataframe(
            resumen,
            use_container_width=True,
            hide_index=True
        )


    # =====================================================
    # TAB 2 - TIPOS DE DATOS
    # =====================================================

    with tab2:

        st.markdown(
            "### 🔤 Tipos de datos de las variables"
        )

        tipos = pd.DataFrame(
            {
                "N°": range(1, len(df.columns) + 1),

                "Variable": df.columns,

                "Tipo de dato": (
                    df.dtypes.astype(str).values
                )
            }
        )

        st.dataframe(
            tipos,
            use_container_width=True,
            hide_index=True
        )


        # Resumen de tipos

        st.markdown("---")

        st.markdown(
            "### 📊 Resumen por tipo de dato"
        )

        resumen_tipos = (
            df.dtypes
            .astype(str)
            .value_counts()
            .reset_index()
        )

        resumen_tipos.columns = [
            "Tipo de dato",
            "Cantidad de variables"
        ]

        st.dataframe(
            resumen_tipos,
            use_container_width=True,
            hide_index=True
        )


    # =====================================================
    # TAB 3 - VALORES NULOS
    # =====================================================

    with tab3:

        st.markdown(
            "### ⚠️ Análisis de valores nulos"
        )

        total_nulos = int(
            df.isnull().sum().sum()
        )

        if total_nulos == 0:

            st.success(
                "✅ El dataset no contiene valores nulos."
            )

        else:

            st.warning(
                f"⚠️ El dataset contiene "
                f"{total_nulos:,} valores nulos."
            )


        st.markdown("---")


        # Tabla de valores nulos

        nulos = pd.DataFrame(
            {
                "Variable": df.columns,

                "Valores nulos": (
                    df.isnull().sum().values
                )
            }
        )


        # Porcentaje de nulos

        nulos["Porcentaje nulos (%)"] = (
            nulos["Valores nulos"]
            / len(df)
            * 100
        ).round(2)


        st.dataframe(
            nulos,
            use_container_width=True,
            hide_index=True
        )


    # =====================================================
    # TAB 4 - DUPLICADOS
    # =====================================================

    with tab4:

        st.markdown(
            "### 🔁 Análisis de registros duplicados"
        )

        duplicados = int(
            df.duplicated().sum()
        )

        st.metric(
            "Registros duplicados",
            duplicados
        )


        if duplicados == 0:

            st.success(
                "✅ No existen registros duplicados."
            )

        else:

            st.warning(
                f"⚠️ Se encontraron "
                f"{duplicados:,} registros duplicados."
            )

            st.markdown("---")

            st.subheader(
                "Registros duplicados"
            )

            df_duplicados = df[
                df.duplicated(keep=False)
            ]

            st.dataframe(
                df_duplicados,
                use_container_width=True
            )
