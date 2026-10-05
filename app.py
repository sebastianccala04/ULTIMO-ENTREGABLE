import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ============================================================
# CONFIGURACIÓN DE LA PÁGINA
# ============================================================

st.set_page_config(
    page_title="FIFA World Cup 2026 - EDA",
    page_icon="⚽",
    layout="wide"
)


# ============================================================
# CLASE PARA EL ANÁLISIS DEL DATASET
# ============================================================

class DataAnalyzer:

    def __init__(self, dataframe):
        self.df = dataframe

    def obtener_dimensiones(self):
        filas, columnas = self.df.shape
        return filas, columnas

    def obtener_nulos(self):
        return self.df.isnull().sum()

    def obtener_duplicados(self):
        return self.df.duplicated().sum()

    def clasificar_variables(self):
        variables_numericas = self.df.select_dtypes(
            include=np.number
        ).columns.tolist()

        variables_categoricas = self.df.select_dtypes(
            exclude=np.number
        ).columns.tolist()

        return variables_numericas, variables_categoricas

    def estadisticas_descriptivas(self):
        return self.df.describe()


# ============================================================
# SESSION STATE
# ============================================================

if "df" not in st.session_state:
    st.session_state.df = None


# ============================================================
# MENÚ LATERAL
# ============================================================

st.sidebar.title("⚽ FIFA World Cup 2026")

opcion = st.sidebar.radio(
    "Selecciona una sección:",
    [
        "🏠 Home",
        "📂 Carga del dataset",
        "📊 Análisis Exploratorio (EDA)",
        "🧮 Clasificación de variables",
        "📈 Estadísticas descriptivas",
        "⚠️ Análisis de valores faltantes",
        "📊 Distribución de variables numéricas",
        "🔤 Análisis de variables categóricas",
        "📊 Análisis bivariado"
    ]
)


# ============================================================
# HOME
# ============================================================

if opcion == "🏠 Home":

    st.title("⚽ FIFA World Cup 2026")
    st.header("Análisis Exploratorio de Datos")

    st.write(
        "Aplicación desarrollada para realizar un análisis exploratorio "
        "del desempeño de jugadores y partidos de la FIFA World Cup 2026."
    )

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

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

    with col3:
        st.metric(
            "Año",
            "2026"
        )

    st.markdown("---")

    st.subheader("👨‍🎓 Información del proyecto")

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Estudiante:** Sebastián Ccala")
        st.write("**Curso:** Python for Analytics")
        st.write("**Proyecto:** Análisis Exploratorio de Datos")

    with col2:
        st.write("**Lenguaje:** Python")
        st.write("**Framework:** Streamlit")
        st.write("**Librerías:** Pandas, NumPy, Matplotlib y Seaborn")

    st.markdown("---")

    st.info(
        "Utiliza el menú lateral para cargar el dataset y desarrollar "
        "cada uno de los ítems del análisis exploratorio."
    )

    st.caption(
        "FIFA World Cup 2026 | Análisis Exploratorio de Datos | "
        "Python for Analytics | Sebastián Ccala | 2026"
    )


# ============================================================
# CARGA DEL DATASET
# ============================================================

elif opcion == "📂 Carga del dataset":

    st.header("📂 Carga del dataset")

    st.write(
        "Selecciona el archivo CSV que contiene la información de los "
        "jugadores y partidos."
    )

    archivo = st.file_uploader(
        "Carga el archivo CSV:",
        type=["csv"]
    )

    if archivo is not None:

        try:

            df_cargado = pd.read_csv(archivo)

            st.session_state.df = df_cargado

            st.success(
                "✅ Dataset cargado correctamente."
            )

            filas, columnas = df_cargado.shape

            col1, col2, col3 = st.columns(3)

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
                    "Valores faltantes",
                    int(df_cargado.isnull().sum().sum())
                )

            st.subheader("👀 Vista previa")

            st.dataframe(
                df_cargado.head(10),
                use_container_width=True
            )

        except Exception as e:

            st.error(
                f"❌ Error al cargar el archivo: {e}"
            )


# ============================================================
# VERIFICACIÓN DEL DATASET
# ============================================================

else:

    if st.session_state.df is None:

        st.warning(
            "⚠️ Primero debes cargar el dataset desde "
            "'📂 Carga del dataset'."
        )

        st.stop()

    df = st.session_state.df

    analyzer = DataAnalyzer(df)


    # ========================================================
    # ÍTEM 1 - INFORMACIÓN GENERAL
    # ========================================================

    if opcion == "📊 Análisis Exploratorio (EDA)":

        st.header("📊 Ítem 1: Información general del dataset")

        filas, columnas = analyzer.obtener_dimensiones()

        total_nulos = int(
            df.isnull().sum().sum()
        )

        duplicados = analyzer.obtener_duplicados()

        variables_numericas, variables_categoricas = (
            analyzer.clasificar_variables()
        )

        # ----------------------------------------------------
        # MÉTRICAS
        # ----------------------------------------------------

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
                "Valores faltantes",
                total_nulos
            )

        with col4:
            st.metric(
                "Duplicados",
                duplicados
            )

        st.markdown("---")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Variables numéricas",
                len(variables_numericas)
            )

        with col2:
            st.metric(
                "Variables categóricas",
                len(variables_categoricas)
            )

        st.markdown("---")

        # ----------------------------------------------------
        # TABS
        # ----------------------------------------------------

        tab1, tab2, tab3, tab4 = st.tabs(
            [
                "📋 Información general",
                "🔢 Tipos de datos",
                "⚠️ Valores faltantes",
                "♻️ Duplicados"
            ]
        )

        with tab1:

            st.subheader("Información general")

            resumen = pd.DataFrame(
                {
                    "Característica": [
                        "Número de registros",
                        "Número de variables",
                        "Variables numéricas",
                        "Variables categóricas",
                        "Valores faltantes",
                        "Registros duplicados"
                    ],
                    "Resultado": [
                        filas,
                        columnas,
                        len(variables_numericas),
                        len(variables_categoricas),
                        total_nulos,
                        duplicados
                    ]
                }
            )

            st.dataframe(
                resumen,
                use_container_width=True,
                hide_index=True
            )

        with tab2:

            st.subheader("Tipos de datos")

            tipos = pd.DataFrame(
                {
                    "Variable": df.columns,
                    "Tipo de dato": df.dtypes.astype(str).values
                }
            )

            st.dataframe(
                tipos,
                use_container_width=True,
                hide_index=True
            )

        with tab3:

            st.subheader("Valores faltantes por variable")

            nulos = df.isnull().sum()

            tabla_nulos = pd.DataFrame(
                {
                    "Variable": nulos.index,
                    "Valores faltantes": nulos.values
                }
            )

            tabla_nulos = tabla_nulos.sort_values(
                "Valores faltantes",
                ascending=False
            )

            st.dataframe(
                tabla_nulos,
                use_container_width=True,
                hide_index=True
            )

        with tab4:

            st.subheader("Registros duplicados")

            st.metric(
                "Cantidad de duplicados",
                duplicados
            )

            if duplicados == 0:

                st.success(
                    "✅ No existen registros duplicados."
                )

            else:

                st.warning(
                    "⚠️ Se encontraron registros duplicados."
                )


    # ========================================================
    # ÍTEM 2 - CLASIFICACIÓN DE VARIABLES
    # ========================================================

    elif opcion == "🧮 Clasificación de variables":

        st.header("🧮 Ítem 2: Clasificación de variables")

        variables_numericas, variables_categoricas = (
            analyzer.clasificar_variables()
        )

        # ----------------------------------------------------
        # MÉTRICAS
        # ----------------------------------------------------

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Variables numéricas",
                len(variables_numericas)
            )

        with col2:
            st.metric(
                "Variables categóricas",
                len(variables_categoricas)
            )

        with col3:
            st.metric(
                "Total de variables",
                len(df.columns)
            )

        st.markdown("---")

        # ----------------------------------------------------
        # RESUMEN
        # ----------------------------------------------------

        resumen_variables = pd.DataFrame(
            {
                "Tipo de variable": [
                    "Numéricas",
                    "Categóricas"
                ],
                "Cantidad": [
                    len(variables_numericas),
                    len(variables_categoricas)
                ]
            }
        )

        st.subheader("📋 Resumen")

        st.dataframe(
            resumen_variables,
            use_container_width=True,
            hide_index=True
        )

        # ----------------------------------------------------
        # NUMÉRICAS
        # ----------------------------------------------------

        st.subheader("🔢 Variables numéricas")

        tabla_numericas = pd.DataFrame(
            {
                "Variable": variables_numericas
            }
        )

        st.dataframe(
            tabla_numericas,
            use_container_width=True,
            hide_index=True
        )

        # ----------------------------------------------------
        # CATEGÓRICAS
        # ----------------------------------------------------

        st.subheader("🔤 Variables categóricas")

        tabla_categoricas = pd.DataFrame(
            {
                "Variable": variables_categoricas
            }
        )

        st.dataframe(
            tabla_categoricas,
            use_container_width=True,
            hide_index=True
        )

        st.info(
            "Las variables numéricas representan cantidades o medidas "
            "que pueden utilizarse para cálculos estadísticos. Las "
            "variables categóricas representan grupos, etiquetas o "
            "características cualitativas."
        )


    # ========================================================
    # ÍTEM 3 - ESTADÍSTICAS DESCRIPTIVAS
    # ========================================================

    elif opcion == "📈 Estadísticas descriptivas":

        st.header("📈 Ítem 3: Estadísticas descriptivas")

        st.write(
            "Las estadísticas descriptivas permiten resumir el "
            "comportamiento de las variables numéricas."
        )

        # ----------------------------------------------------
        # DESCRIBE
        # ----------------------------------------------------

        st.subheader("📊 Estadísticas generales")

        estadisticas = analyzer.estadisticas_descriptivas()

        st.dataframe(
            estadisticas.round(2),
            use_container_width=True
        )

        st.markdown("---")

        # ----------------------------------------------------
        # ANÁLISIS INDIVIDUAL
        # ----------------------------------------------------

        variables_numericas, _ = analyzer.clasificar_variables()

        variable = st.selectbox(
            "Selecciona una variable numérica:",
            variables_numericas
        )

        serie = df[variable]

        media = serie.mean()
        mediana = serie.median()
        minimo = serie.min()
        maximo = serie.max()
        desviacion = serie.std()
        q1 = serie.quantile(0.25)
        q3 = serie.quantile(0.75)
        iqr = q3 - q1

        limite_inferior = q1 - 1.5 * iqr
        limite_superior = q3 + 1.5 * iqr

        valores_extremos = serie[
            (serie < limite_inferior) |
            (serie > limite_superior)
        ]

        # ----------------------------------------------------
        # MÉTRICAS
        # ----------------------------------------------------

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
                "Desviación estándar",
                f"{desviacion:.2f}"
            )

        with col4:
            st.metric(
                "Valores extremos",
                len(valores_extremos)
            )

        # ----------------------------------------------------
        # TABLA
        # ----------------------------------------------------

        resumen = pd.DataFrame(
            {
                "Estadística": [
                    "Mínimo",
                    "Q1",
                    "Mediana",
                    "Q3",
                    "Máximo",
                    "IQR",
                    "Límite inferior",
                    "Límite superior"
                ],
                "Valor": [
                    minimo,
                    q1,
                    mediana,
                    q3,
                    maximo,
                    iqr,
                    limite_inferior,
                    limite_superior
                ]
            }
        )

        st.dataframe(
            resumen.round(2),
            use_container_width=True,
            hide_index=True
        )

        # ----------------------------------------------------
        # INTERPRETACIÓN
        # ----------------------------------------------------

        st.subheader("📝 Interpretación")

        if media > mediana:

            st.write(
                f"La media de **{variable}** ({media:.2f}) es mayor "
                f"que la mediana ({mediana:.2f}), lo que puede indicar "
                "una distribución con cierta asimetría positiva."
            )

        elif media < mediana:

            st.write(
                f"La media de **{variable}** ({media:.2f}) es menor "
                f"que la mediana ({mediana:.2f}), lo que puede indicar "
                "una distribución con cierta asimetría negativa."
            )

        else:

            st.write(
                f"La media y la mediana de **{variable}** presentan "
                "valores muy similares, lo que indica una distribución "
                "relativamente equilibrada."
            )

        st.write(
            f"El rango de la variable va desde {minimo:.2f} hasta "
            f"{maximo:.2f}. El rango intercuartílico es de "
            f"{iqr:.2f}."
        )

        if len(valores_extremos) > 0:

            st.warning(
                f"Se detectaron {len(valores_extremos)} posibles "
                "valores extremos utilizando el criterio del rango "
                "intercuartílico (IQR)."
            )

        else:

            st.success(
                "No se detectaron valores extremos mediante el criterio IQR."
            )


    # ========================================================
    # ÍTEM 4 - VALORES FALTANTES
    # ========================================================

    elif opcion == "⚠️ Análisis de valores faltantes":

        st.header("⚠️ Ítem 4: Análisis de valores faltantes")

        nulos = df.isnull().sum()

        porcentaje_nulos = (
            df.isnull().mean() * 100
        )

        total_nulos = int(
            nulos.sum()
        )

        variables_con_nulos = int(
            (nulos > 0).sum()
        )

        porcentaje_total = (
            total_nulos /
            (df.shape[0] * df.shape[1])
        ) * 100

        # ----------------------------------------------------
        # MÉTRICAS
        # ----------------------------------------------------

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Valores faltantes",
                total_nulos
            )

        with col2:
            st.metric(
                "Variables con faltantes",
                variables_con_nulos
            )

        with col3:
            st.metric(
                "Porcentaje total",
                f"{porcentaje_total:.2f}%"
            )

        st.markdown("---")

        # ----------------------------------------------------
        # TABLA
        # ----------------------------------------------------

        tabla_nulos = pd.DataFrame(
            {
                "Variable": df.columns,
                "Valores faltantes": nulos.values,
                "Porcentaje (%)": porcentaje_nulos.values
            }
        )

        tabla_nulos = tabla_nulos.sort_values(
            "Valores faltantes",
            ascending=False
        )

        st.subheader("📋 Valores faltantes por variable")

        st.dataframe(
            tabla_nulos.round(2),
            use_container_width=True,
            hide_index=True
        )

        # ----------------------------------------------------
        # VISUALIZACIÓN
        # ----------------------------------------------------

        if total_nulos == 0:

            st.success(
                "✅ El dataset no presenta valores faltantes."
            )

        else:

            st.subheader("📊 Visualización")

            datos_grafico = tabla_nulos[
                tabla_nulos["Valores faltantes"] > 0
            ]

            st.bar_chart(
                datos_grafico.set_index("Variable")[
                    "Valores faltantes"
                ]
            )

            st.subheader("📝 Tratamiento de valores faltantes")

            st.write(
                "Dependiendo del contexto, los valores faltantes pueden "
                "tratarse mediante imputación de valores, eliminación "
                "de registros o conservación de los valores cuando la "
                "ausencia tiene significado analítico."
            )

        st.subheader("📌 Conclusión")

        if total_nulos == 0:

            st.info(
                "No es necesario realizar un proceso de imputación o "
                "eliminación por valores faltantes, debido a que todas "
                "las variables presentan información completa."
            )

        else:

            st.info(
                "Se recomienda analizar individualmente las variables "
                "con valores faltantes antes de decidir el tratamiento."
            )


    # ========================================================
    # ÍTEM 5 - DISTRIBUCIÓN DE VARIABLES NUMÉRICAS
    # ========================================================

    elif opcion == "📊 Distribución de variables numéricas":

        st.header(
            "📊 Ítem 5: Distribución de variables numéricas"
        )

        variables_analisis = [
            "player_rating",
            "performance_score",
            "pass_accuracy",
            "distance_covered_km",
            "top_speed_kmh"
        ]

        variables_disponibles = [
            variable
            for variable in variables_analisis
            if variable in df.columns
        ]

        if len(variables_disponibles) == 0:

            st.error(
                "No se encontraron las variables requeridas."
            )

        else:

            variable = st.selectbox(
                "Selecciona una variable:",
                variables_disponibles
            )

            serie = df[variable]

            # ------------------------------------------------
            # MÉTRICAS
            # ------------------------------------------------

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Observaciones",
                    f"{serie.count():,}"
                )

            with col2:
                st.metric(
                    "Media",
                    f"{serie.mean():.2f}"
                )

            with col3:
                st.metric(
                    "Mediana",
                    f"{serie.median():.2f}"
                )

            st.markdown("---")

            # ------------------------------------------------
            # HISTOGRAMA GENERAL
            # ------------------------------------------------

            st.subheader(
                f"📊 Distribución de {variable}"
            )

            fig, ax = plt.subplots(
                figsize=(12, 6)
            )

            sns.histplot(
                serie,
                bins=30,
                kde=True,
                ax=ax
            )

            ax.set_title(
                f"Distribución de {variable}"
            )

            ax.set_xlabel(variable)
            ax.set_ylabel("Frecuencia")

            plt.tight_layout()

            st.pyplot(fig)

            plt.close()

            st.subheader("📝 Interpretación")

            media = serie.mean()
            mediana = serie.median()
            desviacion = serie.std()

            if media > mediana:

                st.write(
                    "La media es mayor que la mediana, lo que puede "
                    "indicar cierta asimetría hacia valores altos."
                )

            elif media < mediana:

                st.write(
                    "La media es menor que la mediana, lo que puede "
                    "indicar cierta asimetría hacia valores bajos."
                )

            else:

                st.write(
                    "La media y la mediana presentan valores similares."
                )

            st.write(
                f"La desviación estándar es {desviacion:.2f}, "
                "lo que permite observar el nivel de dispersión "
                "de los datos alrededor de la media."
            )

            # ------------------------------------------------
            # ANÁLISIS POR POSICIÓN
            # ------------------------------------------------

            st.markdown("---")

            st.subheader(
                "⚽ Distribución según posición"
            )

            if "position" in df.columns:

                posiciones = sorted(
                    df["position"].dropna().unique().tolist()
                )

                posicion_seleccionada = st.selectbox(
                    "Selecciona una posición:",
                    posiciones
                )

                datos_posicion = df[
                    df["position"] == posicion_seleccionada
                ]

                if len(datos_posicion) > 0:

                    fig, ax = plt.subplots(
                        figsize=(12, 6)
                    )

                    sns.histplot(
                        datos_posicion[variable],
                        bins=25,
                        kde=True,
                        ax=ax
                    )

                    ax.set_title(
                        f"{variable} - Posición: "
                        f"{posicion_seleccionada}"
                    )

                    ax.set_xlabel(variable)
                    ax.set_ylabel("Frecuencia")

                    plt.tight_layout()

                    st.pyplot(fig)

                    plt.close()

            # ------------------------------------------------
            # PORTEROS VS JUGADORES DE CAMPO
            # ------------------------------------------------

            st.subheader(
                "🧤 Comparación entre porteros y jugadores de campo"
            )

            df_comparacion = df.copy()

            df_comparacion["position_lower"] = (
                df_comparacion["position"]
                .astype(str)
                .str.lower()
            )

            df_comparacion["grupo_posicion"] = np.where(
                df_comparacion["position_lower"].str.contains(
                    "gk|goalkeeper|portero|arquero",
                    regex=True,
                    na=False
                ),
                "Porteros",
                "Jugadores de campo"
            )

            fig, ax = plt.subplots(
                figsize=(12, 6)
            )

            sns.histplot(
                data=df_comparacion,
                x=variable,
                hue="grupo_posicion",
                element="step",
                common_norm=False,
                bins=30,
                ax=ax
            )

            ax.set_title(
                f"Comparación de {variable}: "
                "porteros vs jugadores de campo"
            )

            ax.set_xlabel(variable)
            ax.set_ylabel("Frecuencia")

            plt.tight_layout()

            st.pyplot(fig)

            plt.close()

            # ------------------------------------------------
            # RESUMEN
            # ------------------------------------------------

            resumen_distribuciones = (
                df[variables_disponibles]
                .describe()
                .T[
                    [
                        "mean",
                        "50%",
                        "std",
                        "min",
                        "max"
                    ]
                ]
                .rename(
                    columns={
                        "mean": "Media",
                        "50%": "Mediana",
                        "std": "Desviación estándar",
                        "min": "Mínimo",
                        "max": "Máximo"
                    }
                )
                .round(2)
            )

            st.subheader(
                "📋 Resumen de las variables analizadas"
            )

            st.dataframe(
                resumen_distribuciones,
                use_container_width=True
            )


    # ========================================================
    # ÍTEM 6 - VARIABLES CATEGÓRICAS
    # ========================================================

    elif opcion == "🔤 Análisis de variables categóricas":

        st.header(
            "🔤 Ítem 6: Análisis de variables categóricas"
        )

        variables_categoricas = [
            "nationality",
            "team",
            "position",
            "preferred_foot",
            "tournament_stage",
            "match_result"
        ]

        variables_disponibles = [
            variable
            for variable in variables_categoricas
            if variable in df.columns
        ]

        if len(variables_disponibles) == 0:

            st.error(
                "No se encontraron las variables categóricas requeridas."
            )

        else:

            variable = st.selectbox(
                "Selecciona una variable categórica:",
                variables_disponibles
            )

            # ------------------------------------------------
            # CONTEOS
            # ------------------------------------------------

            conteos = (
                df[variable]
                .value_counts()
                .reset_index()
            )

            conteos.columns = [
                "Categoría",
                "Frecuencia"
            ]

            total = conteos["Frecuencia"].sum()

            conteos["Porcentaje (%)"] = (
                conteos["Frecuencia"] /
                total *
                100
            )

            # ------------------------------------------------
            # MÉTRICAS
            # ------------------------------------------------

            categoria_mas_frecuente = (
                conteos.iloc[0]["Categoría"]
            )

            frecuencia_maxima = (
                conteos.iloc[0]["Frecuencia"]
            )

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Número de categorías",
                    len(conteos)
                )

            with col2:
                st.metric(
                    "Categoría más frecuente",
                    str(categoria_mas_frecuente)
                )

            with col3:
                st.metric(
                    "Frecuencia máxima",
                    int(frecuencia_maxima)
                )

            st.markdown("---")

            # ------------------------------------------------
            # TABLA
            # ------------------------------------------------

            st.subheader(
                "📋 Frecuencia y proporción"
            )

            st.dataframe(
                conteos.round(2),
                use_container_width=True,
                hide_index=True
            )

            # ------------------------------------------------
            # GRÁFICO
            # ------------------------------------------------

            st.subheader(
                "📊 Distribución de categorías"
            )

            top_15 = conteos.head(15)

            fig, ax = plt.subplots(
                figsize=(12, 7)
            )

            sns.barplot(
                data=top_15,
                x="Frecuencia",
                y="Categoría",
                ax=ax
            )

            ax.set_title(
                f"Principales categorías de {variable}"
            )

            ax.set_xlabel("Frecuencia")
            ax.set_ylabel(variable)

            plt.tight_layout()

            st.pyplot(fig)

            plt.close()

            # ------------------------------------------------
            # PORCENTAJES
            # ------------------------------------------------

            st.subheader(
                "📈 Participación porcentual"
            )

            top_10 = conteos.head(10)

            fig, ax = plt.subplots(
                figsize=(12, 7)
            )

            sns.barplot(
                data=top_10,
                x="Porcentaje (%)",
                y="Categoría",
                ax=ax
            )

            ax.set_title(
                f"Participación porcentual de {variable}"
            )

            ax.set_xlabel("Porcentaje (%)")
            ax.set_ylabel(variable)

            plt.tight_layout()

            st.pyplot(fig)

            plt.close()

            # ------------------------------------------------
            # INTERPRETACIÓN
            # ------------------------------------------------

            st.subheader(
                "📝 Interpretación"
            )

            porcentaje_mayor = (
                conteos.iloc[0]["Porcentaje (%)"]
            )

            st.write(
                f"La categoría más frecuente de **{variable}** es "
                f"**{categoria_mas_frecuente}**, con "
                f"{int(frecuencia_maxima):,} registros, "
                f"equivalentes aproximadamente al "
                f"{porcentaje_mayor:.2f}% del total."
            )

            if variable == "nationality":

                st.write(
                    "La nacionalidad permite observar la composición "
                    "internacional de los jugadores registrados en el dataset."
                )

            elif variable == "team":

                st.write(
                    "El análisis de los equipos permite identificar "
                    "qué selecciones presentan mayor cantidad de "
                    "observaciones en el dataset."
                )

            elif variable == "position":

                st.write(
                    "La posición permite analizar la distribución "
                    "de los jugadores según su función dentro del campo."
                )

            elif variable == "preferred_foot":

                st.write(
                    "El pie preferido permite observar la predominancia "
                    "del uso del pie derecho o izquierdo."
                )

            elif variable == "tournament_stage":

                st.write(
                    "La etapa del torneo permite observar cómo se "
                    "distribuyen las observaciones entre las diferentes "
                    "fases de la competición."
                )

            elif variable == "match_result":

                st.write(
                    "El resultado del partido permite comparar la "
                    "cantidad de observaciones asociadas a cada resultado."
                )

            st.success(
                "✅ El análisis categórico permite identificar "
                "las categorías predominantes y comparar su participación."
            )


    # ========================================================
    # ÍTEM 7 - ANÁLISIS BIVARIADO
    # ========================================================

    elif opcion == "📊 Análisis bivariado":

        st.header(
            "📊 Ítem 7: Análisis bivariado"
        )

        st.write(
            "En este apartado se analiza la relación entre variables "
            "numéricas y categóricas mediante comparaciones entre grupos."
        )

        st.markdown("---")

        # ====================================================
        # 7.1 PLAYER RATING SEGÚN POSITION
        # ====================================================

        st.subheader(
            "7.1 Comparación de player_rating según position"
        )

        if (
            "player_rating" in df.columns
            and "position" in df.columns
        ):

            resumen_rating = (
                df.groupby("position")["player_rating"]
                .agg(
                    [
                        "count",
                        "mean",
                        "median",
                        "std",
                        "min",
                        "max"
                    ]
                )
                .round(2)
                .sort_values(
                    "mean",
                    ascending=False
                )
            )

            st.dataframe(
                resumen_rating,
                use_container_width=True
            )

            fig, ax = plt.subplots(
                figsize=(12, 6)
            )

            sns.boxplot(
                data=df,
                x="position",
                y="player_rating",
                ax=ax
            )

            ax.set_title(
                "Distribución de player_rating según posición"
            )

            ax.set_xlabel(
                "Posición"
            )

            ax.set_ylabel(
                "Player Rating"
            )

            plt.xticks(
                rotation=45
            )

            plt.tight_layout()

            st.pyplot(fig)

            plt.close()

            st.markdown(
                """
                **Interpretación:**

                El gráfico permite comparar el nivel de valoración de
                los jugadores según su posición. La línea central de
                cada caja representa la mediana del `player_rating`,
                mientras que el tamaño de la caja representa la
                dispersión de los valores.

                Las posiciones con una mediana más elevada presentan,
                en términos generales, mayores valoraciones. Los puntos
                alejados de las cajas pueden representar posibles
                valores extremos.
                """
            )

        else:

            st.error(
                "No se encontraron las variables necesarias."
            )

        st.markdown("---")

        # ====================================================
        # 7.2 PERFORMANCE SCORE SEGÚN MATCH RESULT
        # ====================================================

        st.subheader(
            "7.2 Comparación de performance_score según match_result"
        )

        if (
            "performance_score" in df.columns
            and "match_result" in df.columns
        ):

            resumen_performance = (
                df.groupby("match_result")["performance_score"]
                .agg(
                    [
                        "count",
                        "mean",
                        "median",
                        "std",
                        "min",
                        "max"
                    ]
                )
                .round(2)
                .sort_values(
                    "mean",
                    ascending=False
                )
            )

            st.dataframe(
                resumen_performance,
                use_container_width=True
            )

            fig, ax = plt.subplots(
                figsize=(10, 6)
            )

            sns.boxplot(
                data=df,
                x="match_result",
                y="performance_score",
                ax=ax
            )

            ax.set_title(
                "Distribución de performance_score "
                "según resultado del partido"
            )

            ax.set_xlabel(
                "Resultado del partido"
            )

            ax.set_ylabel(
                "Performance Score"
            )

            plt.tight_layout()

            st.pyplot(fig)

            plt.close()

            st.markdown(
                """
                **Interpretación:**

                Se compara el `performance_score` de los jugadores
                según el resultado registrado en `match_result`.

                Esta comparación permite observar si existen diferencias
                en el nivel de rendimiento de los jugadores cuando el
                equipo obtiene diferentes resultados.

                La mediana permite identificar el comportamiento central
                de cada grupo, mientras que la dispersión permite observar
                qué tan variables son las puntuaciones.
                """
            )

        else:

            st.error(
                "No se encontraron las variables necesarias."
            )

        st.markdown("---")

        # ====================================================
        # 7.3 DISTANCE COVERED / TOP SPEED SEGÚN POSITION
        # ====================================================

        st.subheader(
            "7.3 Comparación de variables físicas según posición"
        )

        variables_fisicas = []

        if "distance_covered_km" in df.columns:
            variables_fisicas.append(
                "distance_covered_km"
            )

        if "top_speed_kmh" in df.columns:
            variables_fisicas.append(
                "top_speed_kmh"
            )

        if (
            len(variables_fisicas) > 0
            and "position" in df.columns
        ):

            variable_fisica = st.selectbox(
                "Selecciona la variable física:",
                variables_fisicas
            )

            resumen_fisico = (
                df.groupby("position")[variable_fisica]
                .agg(
                    [
                        "count",
                        "mean",
                        "median",
                        "std",
                        "min",
                        "max"
                    ]
                )
                .round(2)
                .sort_values(
                    "mean",
                    ascending=False
                )
            )

            st.dataframe(
                resumen_fisico,
                use_container_width=True
            )

            fig, ax = plt.subplots(
                figsize=(12, 6)
            )

            sns.boxplot(
                data=df,
                x="position",
                y=variable_fisica,
                ax=ax
            )

            if variable_fisica == "distance_covered_km":

                titulo = (
                    "Distancia recorrida según posición"
                )

                etiqueta_y = (
                    "Distancia recorrida (km)"
                )

            else:

                titulo = (
                    "Velocidad máxima según posición"
                )

                etiqueta_y = (
                    "Velocidad máxima (km/h)"
                )

            ax.set_title(
                titulo
            )

            ax.set_xlabel(
                "Posición"
            )

            ax.set_ylabel(
                etiqueta_y
            )

            plt.xticks(
                rotation=45
            )

            plt.tight_layout()

            st.pyplot(fig)

            plt.close()

            if variable_fisica == "distance_covered_km":

                st.markdown(
                    """
                    **Interpretación:**

                    La distancia recorrida permite comparar el esfuerzo
                    físico realizado por jugadores de diferentes
                    posiciones.

                    Las diferencias entre las medianas pueden indicar
                    que determinadas posiciones recorren mayores
                    distancias durante los partidos. La dispersión
                    permite observar la variabilidad existente dentro
                    de cada posición.
                    """
                )

            else:

                st.markdown(
                    """
                    **Interpretación:**

                    La velocidad máxima permite comparar las capacidades
                    de desplazamiento de los jugadores según su posición.

                    Las posiciones con valores centrales más elevados
                    presentan mayores velocidades máximas. La dispersión
                    permite observar si el comportamiento es homogéneo
                    o si existen jugadores con valores particularmente
                    altos o bajos.
                    """
                )

        else:

            st.error(
                "No se encontraron las variables necesarias."
            )

        st.markdown("---")

        # ====================================================
        # CONCLUSIÓN DEL ÍTEM 7
        # ====================================================

        st.subheader(
            "📌 Conclusión del análisis bivariado"
        )

        st.info(
            "El análisis bivariado permite identificar diferencias "
            "entre grupos de jugadores. En este caso se compararon "
            "las valoraciones de rendimiento según posición, el "
            "performance según el resultado del partido y variables "
            "físicas según posición. Los boxplots permiten analizar "
            "la mediana, dispersión y posibles valores extremos "
            "de cada grupo."
        )


# ============================================================
# PIE DE PÁGINA
# ============================================================

st.sidebar.markdown("---")

st.sidebar.caption(
    "FIFA World Cup 2026 | Análisis Exploratorio de Datos"
)

st.sidebar.caption(
    "Python for Analytics | Sebastián Ccala | 2026"
)
