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

    # -----------------------------------------------------
    # ÍTEM 2 - CLASIFICACIÓN DE VARIABLES
    # -----------------------------------------------------

    def clasificar_variables(self):

        numericas = self.df.select_dtypes(
            include=np.number
        ).columns.tolist()

        categoricas = self.df.select_dtypes(
            exclude=np.number
        ).columns.tolist()

        return numericas, categoricas

    # -----------------------------------------------------
    # ÍTEM 3 - ESTADÍSTICAS DESCRIPTIVAS
    # -----------------------------------------------------

    def estadisticas_descriptivas(self):

        return self.df.describe()


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
        "📊 Análisis Exploratorio (EDA)",
        "🧮 Clasificación de variables",
        "📈 Estadísticas descriptivas"
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

            df = pd.read_csv(archivo)

            st.session_state.df = df

            st.success(
                "✅ Archivo cargado correctamente."
            )

            st.markdown("---")

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
# ÍTEM 1 - ANÁLISIS EXPLORATORIO
# =========================================================

elif opcion == "📊 Análisis Exploratorio (EDA)":

    st.header(
        "📊 Análisis Exploratorio de Datos"
    )

    if st.session_state.df is None:

        st.warning(
            "⚠️ Primero debes cargar el archivo desde "
            "📂 Carga del dataset."
        )

        st.stop()

    df = st.session_state.df

    st.subheader(
        "Ítem 1: Información general del dataset"
    )

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "📋 Información general",
            "🔤 Tipos de datos",
            "⚠️ Valores nulos",
            "🔁 Duplicados"
        ]
    )

    # =====================================================
    # TAB 1
    # =====================================================

    with tab1:

        st.markdown(
            "### 📋 Resumen general del dataset"
        )

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

        numericas = df.select_dtypes(
            include=np.number
        ).shape[1]

        categoricas = df.select_dtypes(
            exclude=np.number
        ).shape[1]

        st.markdown(
            "### 🔤 Clasificación de variables"
        )

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
    # TAB 2
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

        st.markdown("---")

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
    # TAB 3
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

        nulos = pd.DataFrame(
            {
                "Variable": df.columns,
                "Valores nulos": (
                    df.isnull().sum().values
                )
            }
        )

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
    # TAB 4
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

            df_duplicados = df[
                df.duplicated(keep=False)
            ]

            st.dataframe(
                df_duplicados,
                use_container_width=True
            )


# =========================================================
# ÍTEM 2 - CLASIFICACIÓN DE VARIABLES
# =========================================================

elif opcion == "🧮 Clasificación de variables":

    st.header(
        "🧮 Ítem 2: Clasificación de variables"
    )

    if st.session_state.df is None:

        st.warning(
            "⚠️ Primero debes cargar el archivo desde "
            "📂 Carga del dataset."
        )

        st.stop()

    df = st.session_state.df

    analizador = DataAnalyzer(df)

    numericas, categoricas = (
        analizador.clasificar_variables()
    )

    cantidad_numericas = len(numericas)
    cantidad_categoricas = len(categoricas)

    st.write(
        "Las variables del dataset se clasifican en "
        "numéricas y categóricas mediante una función "
        "personalizada."
    )

    st.markdown("---")

    st.subheader(
        "📊 Conteo de variables por tipo"
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "🔢 Variables numéricas",
            cantidad_numericas
        )

    with col2:

        st.metric(
            "🔤 Variables categóricas",
            cantidad_categoricas
        )

    with col3:

        st.metric(
            "📁 Total de variables",
            cantidad_numericas
            + cantidad_categoricas
        )

    st.markdown("---")

    st.subheader(
        "📋 Resumen de clasificación"
    )

    resumen_clasificacion = pd.DataFrame(
        {
            "Tipo de variable": [
                "Numéricas",
                "Categóricas"
            ],

            "Cantidad": [
                cantidad_numericas,
                cantidad_categoricas
            ]
        }
    )

    st.dataframe(
        resumen_clasificacion,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    st.subheader(
        "🔢 Variables numéricas"
    )

    df_numericas = pd.DataFrame(
        {
            "N°": range(
                1,
                cantidad_numericas + 1
            ),

            "Variable": numericas
        }
    )

    st.dataframe(
        df_numericas,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    st.subheader(
        "🔤 Variables categóricas"
    )

    df_categoricas = pd.DataFrame(
        {
            "N°": range(
                1,
                cantidad_categoricas + 1
            ),

            "Variable": categoricas
        }
    )

    st.dataframe(
        df_categoricas,
        use_container_width=True,
        hide_index=True
    )


# =========================================================
# ÍTEM 3 - ESTADÍSTICAS DESCRIPTIVAS
# =========================================================

elif opcion == "📈 Estadísticas descriptivas":

    st.header(
        "📈 Ítem 3: Estadísticas descriptivas"
    )

    if st.session_state.df is None:

        st.warning(
            "⚠️ Primero debes cargar el archivo desde "
            "📂 Carga del dataset."
        )

        st.stop()

    df = st.session_state.df

    analizador = DataAnalyzer(df)

    # -----------------------------------------------------
    # OBTENER VARIABLES NUMÉRICAS
    # -----------------------------------------------------

    numericas, _ = analizador.clasificar_variables()

    # -----------------------------------------------------
    # USO DE .describe()
    # -----------------------------------------------------

    estadisticas = (
        analizador.estadisticas_descriptivas()
    )

    st.subheader(
        "📊 Estadísticas descriptivas del dataset"
    )

    st.write(
        "La función `.describe()` permite obtener "
        "un resumen estadístico de las variables "
        "numéricas del dataset."
    )

    st.dataframe(
        estadisticas.round(2),
        use_container_width=True
    )

    st.markdown("---")

    # =====================================================
    # ANÁLISIS DE UNA VARIABLE
    # =====================================================

    st.subheader(
        "🔎 Análisis detallado de una variable"
    )

    variable = st.selectbox(
        "Selecciona una variable numérica:",
        numericas
    )

    datos = df[variable].dropna()

    # -----------------------------------------------------
    # ESTADÍSTICAS
    # -----------------------------------------------------

    media = datos.mean()
    mediana = datos.median()
    minimo = datos.min()
    maximo = datos.max()
    desviacion = datos.std()

    q1 = datos.quantile(0.25)
    q3 = datos.quantile(0.75)

    iqr = q3 - q1

    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr

    valores_extremos = datos[
        (datos < limite_inferior)
        | (datos > limite_superior)
    ]

    # =====================================================
    # MÉTRICAS
    # =====================================================

    st.markdown(
        "### 📌 Medidas principales"
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Media",
            f"{media:.2f}"
        )

    with col2:

        st.metric(
            "Mediana",
            f"{mediana:.2f}"
        )

    with col3:

        st.metric(
            "Mínimo",
            f"{minimo:.2f}"
        )

    with col4:

        st.metric(
            "Máximo",
            f"{maximo:.2f}"
        )

    st.markdown("---")

    # =====================================================
    # CUARTILES Y DISPERSIÓN
    # =====================================================

    st.markdown(
        "### 📐 Cuartiles y dispersión"
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Q1 (25%)",
            f"{q1:.2f}"
        )

    with col2:

        st.metric(
            "Q3 (75%)",
            f"{q3:.2f}"
        )

    with col3:

        st.metric(
            "Rango intercuartílico",
            f"{iqr:.2f}"
        )

    with col4:

        st.metric(
            "Desviación estándar",
            f"{desviacion:.2f}"
        )

    st.markdown("---")

    # =====================================================
    # DETECCIÓN DE VALORES EXTREMOS
    # =====================================================

    st.markdown(
        "### ⚠️ Detección preliminar de valores extremos"
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Límite inferior",
            f"{limite_inferior:.2f}"
        )

    with col2:

        st.metric(
            "Límite superior",
            f"{limite_superior:.2f}"
        )

    with col3:

        st.metric(
            "Valores extremos",
            len(valores_extremos)
        )

    if len(valores_extremos) == 0:

        st.success(
            "✅ No se detectaron valores extremos "
            "mediante el criterio del rango intercuartílico."
        )

    else:

        st.warning(
            f"⚠️ Se detectaron "
            f"{len(valores_extremos):,} valores extremos "
            f"de manera preliminar."
        )

        st.dataframe(
            valores_extremos.to_frame(
                name=variable
            ),
            use_container_width=True
        )

    st.markdown("---")

    # =====================================================
    # INTERPRETACIÓN BÁSICA
    # =====================================================

    st.subheader(
        "📝 Interpretación básica"
    )

    if media > mediana:

        interpretacion_central = (
            "La media es mayor que la mediana, "
            "lo que puede indicar una ligera "
            "asimetría hacia valores altos."
        )

    elif media < mediana:

        interpretacion_central = (
            "La media es menor que la mediana, "
            "lo que puede indicar una ligera "
            "asimetría hacia valores bajos."
        )

    else:

        interpretacion_central = (
            "La media y la mediana son iguales "
            "o muy similares, lo que sugiere una "
            "distribución relativamente equilibrada."
        )

    st.info(
        f"**Media:** {media:.2f}\n\n"
        f"**Mediana:** {mediana:.2f}\n\n"
        f"**Q1:** {q1:.2f}\n\n"
        f"**Q3:** {q3:.2f}\n\n"
        f"**Desviación estándar:** {desviacion:.2f}\n\n"
        f"**Interpretación:** {interpretacion_central}"
    )
