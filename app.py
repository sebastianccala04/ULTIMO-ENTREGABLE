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
        return self.df.isnull().sum().sum()

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

    def estadisticas_descriptivas(self):

        return self.df.describe()


# =========================================================
# VARIABLES DE SESIÓN
# =========================================================

if "df" not in st.session_state:
    st.session_state.df = None


# =========================================================
# MENÚ LATERAL
# =========================================================

st.sidebar.title("⚽ FIFA World Cup 2026")

opcion = st.sidebar.selectbox(
    "Selecciona una sección:",
    [
        "🏠 Home",
        "📂 Carga del dataset",
        "📊 Análisis Exploratorio (EDA)",
        "🧮 Clasificación de variables",
        "📈 Estadísticas descriptivas",
        "⚠️ Análisis de valores faltantes"
    ]
)


# =========================================================
# HOME
# =========================================================

if opcion == "🏠 Home":

    st.title("⚽ FIFA World Cup 2026")
    st.header("Análisis Exploratorio de Datos")

    st.write(
        "Proyecto desarrollado para la Especialización en "
        "Python for Analytics."
    )

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("👨‍🎓 Información del estudiante")

        st.write("**Estudiante:** Sebastián Ccala")
        st.write("**Curso:** Especialización en Python for Analytics")
        st.write("**Año:** 2026")

    with col2:

        st.subheader("💻 Tecnologías utilizadas")

        st.write("🐍 Python")
        st.write("📊 Pandas")
        st.write("🔢 NumPy")
        st.write("🎨 Streamlit")
        st.write("📈 Matplotlib / Seaborn")

    st.markdown("---")

    st.subheader("📋 Dataset")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Registros",
            "54,600"
        )

    with col2:
        st.metric(
            "Variables",
            "75"
        )

    st.info(
        "El proyecto tiene como objetivo realizar un análisis "
        "exploratorio del desempeño de jugadores durante el "
        "FIFA World Cup 2026."
    )

    st.markdown("---")

    st.caption(
        "FIFA World Cup 2026 | Análisis Exploratorio de Datos | "
        "Python for Analytics | Sebastián Ccala | 2026"
    )


# =========================================================
# CARGA DEL DATASET
# =========================================================

elif opcion == "📂 Carga del dataset":

    st.header("📂 Carga del dataset")

    st.write(
        "Carga el archivo CSV para comenzar con el análisis."
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
                "¡Dataset cargado correctamente!"
            )

            st.markdown("---")

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "Registros",
                    f"{df.shape[0]:,}"
                )

            with col2:

                st.metric(
                    "Variables",
                    df.shape[1]
                )

            with col3:

                st.metric(
                    "Valores nulos",
                    f"{df.isnull().sum().sum():,}"
                )

            st.subheader("👀 Vista previa")

            st.dataframe(
                df.head(10),
                use_container_width=True
            )

        except Exception as e:

            st.error(
                f"Error al cargar el archivo: {e}"
            )


# =========================================================
# ÍTEM 1: ANÁLISIS EXPLORATORIO
# =========================================================

elif opcion == "📊 Análisis Exploratorio (EDA)":

    if st.session_state.df is None:

        st.warning(
            "Primero debes cargar el dataset."
        )

        st.stop()

    df = st.session_state.df

    st.header(
        "📊 Ítem 1: Información general del dataset"
    )

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "📋 Información general",
            "🔤 Tipos de datos",
            "⚠️ Valores nulos",
            "🔁 Duplicados"
        ]
    )


    # -----------------------------------------------------
    # TAB 1 - INFORMACIÓN GENERAL
    # -----------------------------------------------------

    with tab1:

        analizador = DataAnalyzer(df)

        filas, columnas = analizador.obtener_dimensiones()

        nulos = analizador.obtener_nulos()

        duplicados = analizador.obtener_duplicados()

        numericas, categoricas = (
            analizador.clasificar_variables()
        )

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.metric(
                "Registros",
                f"{filas:,}"
            )

        with col2:

            st.metric(
                "Variables",
                columnas
            )

        with col3:

            st.metric(
                "Valores nulos",
                f"{nulos:,}"
            )

        with col4:

            st.metric(
                "Duplicados",
                f"{duplicados:,}"
            )

        st.markdown("---")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Variables numéricas",
                len(numericas)
            )

        with col2:

            st.metric(
                "Variables categóricas",
                len(categoricas)
            )

        st.subheader(
            "📋 Resumen general"
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
                    filas,
                    columnas,
                    len(numericas),
                    len(categoricas),
                    nulos,
                    duplicados
                ]
            }
        )

        st.dataframe(
            resumen,
            use_container_width=True,
            hide_index=True
        )


    # -----------------------------------------------------
    # TAB 2 - TIPOS DE DATOS
    # -----------------------------------------------------

    with tab2:

        st.subheader(
            "🔤 Tipos de datos de las variables"
        )

        tipos_datos = pd.DataFrame(
            {
                "N°": range(1, len(df.columns) + 1),
                "Variable": df.columns,
                "Tipo de dato": df.dtypes.astype(str).values
            }
        )

        st.dataframe(
            tipos_datos,
            use_container_width=True,
            hide_index=True
        )

        st.subheader(
            "📊 Resumen de tipos de datos"
        )

        resumen_tipos = (
            df.dtypes
            .astype(str)
            .value_counts()
            .reset_index()
        )

        resumen_tipos.columns = [
            "Tipo de dato",
            "Cantidad"
        ]

        st.dataframe(
            resumen_tipos,
            use_container_width=True,
            hide_index=True
        )


    # -----------------------------------------------------
    # TAB 3 - VALORES NULOS
    # -----------------------------------------------------

    with tab3:

        st.subheader(
            "⚠️ Análisis de valores nulos"
        )

        nulos_por_variable = df.isnull().sum()

        tabla_nulos = pd.DataFrame(
            {
                "Variable": df.columns,
                "Valores nulos": nulos_por_variable.values,
                "Porcentaje (%)":
                    (
                        nulos_por_variable /
                        len(df) *
                        100
                    ).round(2)
            }
        )

        if nulos_por_variable.sum() == 0:

            st.success(
                "El dataset no contiene valores nulos."
            )

        else:

            st.warning(
                "Se encontraron valores nulos."
            )

        st.dataframe(
            tabla_nulos,
            use_container_width=True,
            hide_index=True
        )


    # -----------------------------------------------------
    # TAB 4 - DUPLICADOS
    # -----------------------------------------------------

    with tab4:

        st.subheader(
            "🔁 Análisis de registros duplicados"
        )

        cantidad_duplicados = df.duplicated().sum()

        st.metric(
            "Registros duplicados",
            f"{cantidad_duplicados:,}"
        )

        if cantidad_duplicados == 0:

            st.success(
                "No existen registros duplicados."
            )

        else:

            st.warning(
                "Se encontraron registros duplicados."
            )

            duplicados = df[
                df.duplicated(keep=False)
            ]

            st.dataframe(
                duplicados,
                use_container_width=True
            )


# =========================================================
# ÍTEM 2: CLASIFICACIÓN DE VARIABLES
# =========================================================

elif opcion == "🧮 Clasificación de variables":

    if st.session_state.df is None:

        st.warning(
            "Primero debes cargar el dataset."
        )

        st.stop()

    df = st.session_state.df

    st.header(
        "🧮 Ítem 2: Clasificación de variables"
    )

    st.write(
        "Las variables se clasifican en numéricas y categóricas "
        "utilizando una función personalizada."
    )

    analizador = DataAnalyzer(df)

    numericas, categoricas = (
        analizador.clasificar_variables()
    )

    # -----------------------------------------------------
    # RESUMEN
    # -----------------------------------------------------

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Variables numéricas",
            len(numericas)
        )

    with col2:

        st.metric(
            "Variables categóricas",
            len(categoricas)
        )

    with col3:

        st.metric(
            "Total de variables",
            len(df.columns)
        )

    st.markdown("---")

    # -----------------------------------------------------
    # TABLA RESUMEN
    # -----------------------------------------------------

    st.subheader(
        "📋 Resumen de clasificación"
    )

    resumen_variables = pd.DataFrame(
        {
            "Tipo de variable": [
                "Numéricas",
                "Categóricas"
            ],
            "Cantidad": [
                len(numericas),
                len(categoricas)
            ]
        }
    )

    st.dataframe(
        resumen_variables,
        use_container_width=True,
        hide_index=True
    )

    # -----------------------------------------------------
    # VARIABLES NUMÉRICAS
    # -----------------------------------------------------

    st.subheader(
        "🔢 Variables numéricas"
    )

    tabla_numericas = pd.DataFrame(
        {
            "N°": range(1, len(numericas) + 1),
            "Variable": numericas
        }
    )

    st.dataframe(
        tabla_numericas,
        use_container_width=True,
        hide_index=True
    )

    # -----------------------------------------------------
    # VARIABLES CATEGÓRICAS
    # -----------------------------------------------------

    st.subheader(
        "🔤 Variables categóricas"
    )

    tabla_categoricas = pd.DataFrame(
        {
            "N°": range(1, len(categoricas) + 1),
            "Variable": categoricas
        }
    )

    st.dataframe(
        tabla_categoricas,
        use_container_width=True,
        hide_index=True
    )


# =========================================================
# ÍTEM 3: ESTADÍSTICAS DESCRIPTIVAS
# =========================================================

elif opcion == "📈 Estadísticas descriptivas":

    if st.session_state.df is None:

        st.warning(
            "Primero debes cargar el dataset."
        )

        st.stop()

    df = st.session_state.df

    st.header(
        "📈 Ítem 3: Estadísticas descriptivas"
    )

    st.write(
        "Se presentan las principales estadísticas descriptivas "
        "de las variables numéricas."
    )

    analizador = DataAnalyzer(df)

    numericas, categoricas = (
        analizador.clasificar_variables()
    )

    # -----------------------------------------------------
    # ESTADÍSTICAS GENERALES
    # -----------------------------------------------------

    st.subheader(
        "📊 Estadísticas descriptivas generales"
    )

    estadisticas = (
        analizador
        .estadisticas_descriptivas()
        .round(2)
    )

    st.dataframe(
        estadisticas,
        use_container_width=True
    )

    st.markdown("---")

    # -----------------------------------------------------
    # ANÁLISIS DE UNA VARIABLE
    # -----------------------------------------------------

    st.subheader(
        "🔎 Análisis detallado de una variable"
    )

    variable = st.selectbox(
        "Selecciona una variable numérica:",
        numericas
    )

    datos = df[variable].dropna()

    media = datos.mean()
    mediana = datos.median()
    minimo = datos.min()
    maximo = datos.max()
    desviacion = datos.std()

    q1 = datos.quantile(0.25)
    q3 = datos.quantile(0.75)

    iqr = q3 - q1

    limite_inferior = q1 - (1.5 * iqr)
    limite_superior = q3 + (1.5 * iqr)

    valores_extremos = datos[
        (datos < limite_inferior) |
        (datos > limite_superior)
    ]

    # -----------------------------------------------------
    # MÉTRICAS PRINCIPALES
    # -----------------------------------------------------

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

    # -----------------------------------------------------
    # DISPERSIÓN
    # -----------------------------------------------------

    st.subheader(
        "📐 Medidas de dispersión"
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Desviación estándar",
            f"{desviacion:.2f}"
        )

    with col2:

        st.metric(
            "Q1",
            f"{q1:.2f}"
        )

    with col3:

        st.metric(
            "Q3",
            f"{q3:.2f}"
        )

    with col4:

        st.metric(
            "IQR",
            f"{iqr:.2f}"
        )

    # -----------------------------------------------------
    # VALORES EXTREMOS
    # -----------------------------------------------------

    st.subheader(
        "🚨 Detección preliminar de valores extremos"
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
            f"{len(valores_extremos):,}"
        )

    if len(valores_extremos) == 0:

        st.success(
            "No se identificaron valores extremos "
            "mediante el criterio del rango intercuartílico."
        )

    else:

        st.warning(
            f"Se identificaron {len(valores_extremos):,} "
            "posibles valores extremos."
        )

        st.dataframe(
            valores_extremos.to_frame(
                name=variable
            ),
            use_container_width=True
        )

    # -----------------------------------------------------
    # INTERPRETACIÓN
    # -----------------------------------------------------

    st.subheader(
        "📝 Interpretación básica"
    )

    if media > mediana:

        interpretacion = (
            "La media es mayor que la mediana, lo que puede indicar "
            "una ligera concentración de valores hacia niveles altos."
        )

    elif media < mediana:

        interpretacion = (
            "La media es menor que la mediana, lo que puede indicar "
            "una ligera concentración de valores hacia niveles bajos."
        )

    else:

        interpretacion = (
            "La media y la mediana son iguales o muy similares, "
            "lo que indica una distribución relativamente equilibrada."
        )

    st.info(
        f"Para la variable **{variable}**, la media es "
        f"**{media:.2f}** y la mediana es **{mediana:.2f}**. "
        f"{interpretacion}"
    )


# =========================================================
# ÍTEM 4: ANÁLISIS DE VALORES FALTANTES
# =========================================================

elif opcion == "⚠️ Análisis de valores faltantes":

    if st.session_state.df is None:

        st.warning(
            "Primero debes cargar el dataset."
        )

        st.stop()

    df = st.session_state.df

    st.header(
        "⚠️ Ítem 4: Análisis de valores faltantes"
    )

    st.write(
        "Se analiza la cantidad y el porcentaje de valores "
        "faltantes presentes en cada variable del dataset."
    )

    # -----------------------------------------------------
    # 1. CONTEO Y PORCENTAJE POR VARIABLE
    # -----------------------------------------------------

    st.subheader(
        "1. Conteo y porcentaje por variable"
    )

    valores_faltantes = df.isnull().sum()

    porcentaje_faltantes = (
        valores_faltantes /
        len(df)
    ) * 100

    tabla_faltantes = pd.DataFrame(
        {
            "Variable": df.columns,
            "Valores faltantes":
                valores_faltantes.values,
            "Porcentaje (%)":
                porcentaje_faltantes.values
        }
    )

    tabla_faltantes[
        "Porcentaje (%)"
    ] = tabla_faltantes[
        "Porcentaje (%)"
    ].round(2)

    # -----------------------------------------------------
    # MÉTRICAS
    # -----------------------------------------------------

    total_faltantes = valores_faltantes.sum()

    variables_con_faltantes = (
        valores_faltantes > 0
    ).sum()

    porcentaje_total = (
        total_faltantes /
        df.size
    ) * 100

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Total de valores faltantes",
            f"{total_faltantes:,}"
        )

    with col2:

        st.metric(
            "Variables con faltantes",
            variables_con_faltantes
        )

    with col3:

        st.metric(
            "Porcentaje total",
            f"{porcentaje_total:.2f}%"
        )

    st.dataframe(
        tabla_faltantes,
        use_container_width=True,
        hide_index=True
    )

    # -----------------------------------------------------
    # 2. VISUALIZACIÓN SIMPLE
    # -----------------------------------------------------

    st.subheader(
        "2. Visualización de valores faltantes"
    )

    datos_grafico = tabla_faltantes[
        tabla_faltantes[
            "Valores faltantes"
        ] > 0
    ]

    if datos_grafico.empty:

        st.success(
            "No se encontraron valores faltantes "
            "en ninguna variable del dataset."
        )

    else:

        st.bar_chart(
            datos_grafico.set_index(
                "Variable"
            )[
                "Valores faltantes"
            ]
        )

    # -----------------------------------------------------
    # 3. DISCUSIÓN SOBRE EL TRATAMIENTO
    # -----------------------------------------------------

    st.subheader(
        "3. Discusión sobre el tratamiento"
    )

    if total_faltantes == 0:

        st.info(
            "El dataset no presenta valores faltantes. "
            "Por lo tanto, no es necesario aplicar técnicas "
            "de imputación ni eliminar registros. Se recomienda "
            "conservar los datos tal como se encuentran para "
            "los análisis posteriores."
        )

    else:

        st.write(
            "Cuando existen valores faltantes, se debe evaluar "
            "su cantidad y el tipo de variable antes de "
            "seleccionar una estrategia de tratamiento."
        )

        st.markdown(
            """
            **Principales alternativas de tratamiento:**

            - **Imputación:** reemplazar los valores faltantes
              utilizando la media, mediana o moda.

            - **Eliminación:** eliminar registros cuando la
              cantidad de datos faltantes sea considerable.

            - **Conservación:** mantener los valores faltantes
              cuando representan una ausencia válida de información.
            """
        )

    # -----------------------------------------------------
    # CONCLUSIÓN
    # -----------------------------------------------------

    st.subheader(
        "📌 Conclusión"
    )

    if total_faltantes == 0:

        st.success(
            "El dataset contiene 54,600 registros y 75 variables, "
            "sin valores faltantes. Por esta razón, no es necesario "
            "realizar procesos de imputación o eliminación "
            "relacionados con datos ausentes."
        )

    else:

        st.warning(
            f"Se identificaron {total_faltantes:,} valores "
            "faltantes en el dataset. Se recomienda analizar "
            "cada variable antes de aplicar una estrategia "
            "de tratamiento."
        )


# =========================================================
# PIE DE PÁGINA
# =========================================================

st.sidebar.markdown("---")

st.sidebar.caption(
    "FIFA World Cup 2026 | Análisis Exploratorio de Datos"
)

st.sidebar.caption(
    "Python for Analytics | Sebastián Ccala | 2026"
)
