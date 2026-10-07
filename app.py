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
        "📊 Análisis bivariado",
        "🔤 Bivariado categórico",
        "🎛️ Análisis por parámetros",
        "💡 Hallazgos clave"
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
        st.metric("Registros", "54,600")

    with col2:
        st.metric("Variables", "75")

    with col3:
        st.metric("Año", "2026")

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
        st.write(
            "**Librerías:** Pandas, NumPy, Matplotlib y Seaborn"
        )

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

    # Cargar automáticamente el dataset incluido en el proyecto
    df = pd.read_csv("datosfifa_world_cup_2026.csv")

    # Guardar dataset en memoria
    st.session_state.df = df

    st.success("✅ Dataset cargado correctamente.")

    st.subheader("👀 Vista previa")

    st.dataframe(
        df.head(10),
        use_container_width=True
    )

    st.subheader("📊 Información general")

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
            "Valores faltantes",
            int(df.isnull().sum().sum())
        )
        
# ============================================================
# RESTO DE SECCIONES
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
    # ÍTEM 1
    # ========================================================

    if opcion == "📊 Análisis Exploratorio (EDA)":

        st.header(
            "📊 Ítem 1: Información general del dataset"
        )

        filas, columnas = analyzer.obtener_dimensiones()

        total_nulos = int(
            df.isnull().sum().sum()
        )

        duplicados = analyzer.obtener_duplicados()

        variables_numericas, variables_categoricas = (
            analyzer.clasificar_variables()
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

        tab1, tab2, tab3, tab4 = st.tabs(
            [
                "📋 Información general",
                "🔢 Tipos de datos",
                "⚠️ Valores faltantes",
                "♻️ Duplicados"
            ]
        )

        with tab1:

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
    # ÍTEM 2
    # ========================================================

    elif opcion == "🧮 Clasificación de variables":

        st.header(
            "🧮 Ítem 2: Clasificación de variables"
        )

        variables_numericas, variables_categoricas = (
            analyzer.clasificar_variables()
        )

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


    # ========================================================
    # ÍTEM 3
    # ========================================================

    elif opcion == "📈 Estadísticas descriptivas":

        st.header(
            "📈 Ítem 3: Estadísticas descriptivas"
        )

        st.subheader("📊 Estadísticas generales")

        estadisticas = analyzer.estadisticas_descriptivas()

        st.dataframe(
            estadisticas.round(2),
            use_container_width=True
        )

        st.markdown("---")

        variables_numericas, _ = (
            analyzer.clasificar_variables()
        )

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

        st.subheader("📝 Interpretación")

        if media > mediana:

            st.write(
                f"La media de **{variable}** ({media:.2f}) es mayor "
                f"que la mediana ({mediana:.2f}), lo que puede indicar "
                "cierta asimetría positiva."
            )

        elif media < mediana:

            st.write(
                f"La media de **{variable}** ({media:.2f}) es menor "
                f"que la mediana ({mediana:.2f}), lo que puede indicar "
                "cierta asimetría negativa."
            )

        else:

            st.write(
                f"La media y la mediana de **{variable}** "
                "presentan valores similares."
            )

        if len(valores_extremos) > 0:

            st.warning(
                f"Se detectaron {len(valores_extremos)} posibles "
                "valores extremos mediante el criterio IQR."
            )

        else:

            st.success(
                "No se detectaron valores extremos mediante el criterio IQR."
            )


    # ========================================================
    # ÍTEM 4
    # ========================================================

    elif opcion == "⚠️ Análisis de valores faltantes":

        st.header(
            "⚠️ Ítem 4: Análisis de valores faltantes"
        )

        nulos = df.isnull().sum()

        porcentaje_nulos = (
            df.isnull().mean() * 100
        )

        total_nulos = int(nulos.sum())

        variables_con_nulos = int(
            (nulos > 0).sum()
        )

        porcentaje_total = (
            total_nulos /
            (df.shape[0] * df.shape[1])
        ) * 100

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

        st.subheader(
            "📋 Valores faltantes por variable"
        )

        st.dataframe(
            tabla_nulos.round(2),
            use_container_width=True,
            hide_index=True
        )

        if total_nulos == 0:

            st.success(
                "✅ El dataset no presenta valores faltantes."
            )

        else:

            datos_grafico = tabla_nulos[
                tabla_nulos["Valores faltantes"] > 0
            ]

            st.bar_chart(
                datos_grafico.set_index("Variable")[
                    "Valores faltantes"
                ]
            )

            st.write(
                "Se recomienda analizar el origen de los valores "
                "faltantes antes de decidir entre imputación, "
                "eliminación o conservación."
            )


    # ========================================================
    # ÍTEM 5
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
                    f"{variable} - {posicion_seleccionada}"
                )

                ax.set_xlabel(variable)
                ax.set_ylabel("Frecuencia")

                plt.tight_layout()

                st.pyplot(fig)

                plt.close()

            st.subheader(
                "🧤 Porteros vs jugadores de campo"
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
                f"Comparación de {variable}"
            )

            ax.set_xlabel(variable)
            ax.set_ylabel("Frecuencia")

            plt.tight_layout()

            st.pyplot(fig)

            plt.close()

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
                "📋 Resumen"
            )

            st.dataframe(
                resumen_distribuciones,
                use_container_width=True
            )


    # ========================================================
    # ÍTEM 6
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

        variable = st.selectbox(
            "Selecciona una variable categórica:",
            variables_disponibles
        )

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

        st.dataframe(
            conteos.round(2),
            use_container_width=True,
            hide_index=True
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

        st.write(
            f"La categoría más frecuente de **{variable}** es "
            f"**{categoria_mas_frecuente}**, con "
            f"{int(frecuencia_maxima):,} registros."
        )


    # ========================================================
    # ÍTEM 7
    # ========================================================

    elif opcion == "📊 Análisis bivariado":

        st.header(
            "📊 Ítem 7: Análisis bivariado"
        )

        # ----------------------------------------------------
        # 7.1
        # ----------------------------------------------------

        st.subheader(
            "7.1 Comparación de player_rating según position"
        )

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

        ax.set_xlabel("Posición")
        ax.set_ylabel("Player Rating")

        plt.xticks(rotation=45)

        plt.tight_layout()

        st.pyplot(fig)

        plt.close()

        # ----------------------------------------------------
        # 7.2
        # ----------------------------------------------------

        st.subheader(
            "7.2 Comparación de performance_score según match_result"
        )

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
            "Performance Score según resultado del partido"
        )

        ax.set_xlabel("Resultado del partido")
        ax.set_ylabel("Performance Score")

        plt.tight_layout()

        st.pyplot(fig)

        plt.close()

        # ----------------------------------------------------
        # 7.3
        # ----------------------------------------------------

        st.subheader(
            "7.3 Comparación de variables físicas según posición"
        )

        variable_fisica = st.selectbox(
            "Selecciona la variable física:",
            [
                "distance_covered_km",
                "top_speed_kmh"
            ]
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

        ax.set_title(
            f"{variable_fisica} según posición"
        )

        ax.set_xlabel("Posición")
        ax.set_ylabel(variable_fisica)

        plt.xticks(rotation=45)

        plt.tight_layout()

        st.pyplot(fig)

        plt.close()

        st.info(
            "El análisis bivariado permite identificar diferencias "
            "entre grupos y observar cómo cambia una variable numérica "
            "según una categoría."
        )


    # ========================================================
    # ÍTEM 8
    # ========================================================

    elif opcion == "🔤 Bivariado categórico":

        st.header(
            "🔤 Ítem 8: Análisis bivariado categórico vs categórico"
        )

        st.write(
            "En este apartado se comparan dos variables categóricas "
            "para identificar patrones y diferencias entre grupos."
        )

        # ----------------------------------------------------
        # 8.1 POSITION VS TOURNAMENT_STAGE
        # ----------------------------------------------------

        st.subheader(
            "8.1 Comparación de position con tournament_stage"
        )

        tabla_position_stage = pd.crosstab(
            df["position"],
            df["tournament_stage"]
        )

        st.dataframe(
            tabla_position_stage,
            use_container_width=True
        )

        fig, ax = plt.subplots(
            figsize=(12, 7)
        )

        tabla_position_stage.plot(
            kind="bar",
            ax=ax
        )

        ax.set_title(
            "Position según etapa del torneo"
        )

        ax.set_xlabel(
            "Posición"
        )

        ax.set_ylabel(
            "Frecuencia"
        )

        plt.xticks(rotation=45)

        ax.legend(
            title="Etapa del torneo"
        )

        plt.tight_layout()

        st.pyplot(fig)

        plt.close()

        st.markdown(
            """
            **Interpretación:**

            Esta comparación permite observar cómo se distribuyen
            las diferentes posiciones de los jugadores entre las
            distintas etapas del torneo.
            """
        )

        st.markdown("---")

        # ----------------------------------------------------
        # 8.2 TEAM VS MATCH_RESULT
        # ----------------------------------------------------

        st.subheader(
            "8.2 Análisis de team frente a match_result"
        )

        tabla_team_resultado = pd.crosstab(
            df["team"],
            df["match_result"]
        )

        st.dataframe(
            tabla_team_resultado,
            use_container_width=True
        )

        fig, ax = plt.subplots(
            figsize=(14, 8)
        )

        tabla_team_resultado.plot(
            kind="bar",
            stacked=True,
            ax=ax
        )

        ax.set_title(
            "Resultado de partidos según equipo"
        )

        ax.set_xlabel(
            "Equipo"
        )

        ax.set_ylabel(
            "Frecuencia"
        )

        plt.xticks(rotation=75)

        ax.legend(
            title="Resultado"
        )

        plt.tight_layout()

        st.pyplot(fig)

        plt.close()

        st.markdown(
            """
            **Interpretación:**

            El análisis permite comparar los resultados registrados
            para cada equipo. La visualización facilita identificar
            diferencias en la distribución de los resultados.
            """
        )

        st.markdown("---")

        # ----------------------------------------------------
        # 8.3 PREFERRED_FOOT VS POSITION
        # ----------------------------------------------------

        st.subheader(
            "8.3 Comparación de preferred_foot con position"
        )

        tabla_pie_position = pd.crosstab(
            df["position"],
            df["preferred_foot"]
        )

        st.dataframe(
            tabla_pie_position,
            use_container_width=True
        )

        fig, ax = plt.subplots(
            figsize=(12, 7)
        )

        tabla_pie_position.plot(
            kind="bar",
            ax=ax
        )

        ax.set_title(
            "Pie preferido según posición"
        )

        ax.set_xlabel(
            "Posición"
        )

        ax.set_ylabel(
            "Frecuencia"
        )

        plt.xticks(rotation=45)

        ax.legend(
            title="Pie preferido"
        )

        plt.tight_layout()

        st.pyplot(fig)

        plt.close()

        st.markdown(
            """
            **Interpretación:**

            La comparación permite observar la distribución del pie
            preferido de los jugadores dentro de cada posición.
            Esto facilita identificar si existe predominancia de
            determinado pie en alguna posición.
            """
        )

        st.success(
            "✅ Se completaron las tres comparaciones categóricas "
            "solicitadas en el Ítem 8."
        )


    # ========================================================
    # ÍTEM 9
    # ========================================================

    elif opcion == "🎛️ Análisis por parámetros":

        st.header(
            "🎛️ Ítem 9: Análisis basado en parámetros seleccionados"
        )

        st.write(
            "Utiliza los filtros para realizar un análisis dinámico "
            "del rendimiento de los jugadores."
        )

        # ----------------------------------------------------
        # CONVERSIÓN DE FECHA
        # ----------------------------------------------------

        df_parametros = df.copy()

        if "match_date" in df_parametros.columns:

            df_parametros["match_date"] = pd.to_datetime(
                df_parametros["match_date"],
                errors="coerce"
            )

        # ----------------------------------------------------
        # FILTROS CATEGÓRICOS
        # ----------------------------------------------------

        st.subheader(
            "🎯 Filtros"
        )

        col1, col2 = st.columns(2)

        # ----------------------------------------------------
        # TEAM
        # ----------------------------------------------------

        if "team" in df_parametros.columns:

            equipos = sorted(
                df_parametros["team"]
                .dropna()
                .unique()
                .tolist()
            )

            equipos_seleccionados = st.multiselect(
                "Selecciona team:",
                equipos,
                default=[]
            )

        else:

            equipos_seleccionados = []

        # ----------------------------------------------------
        # POSITION
        # ----------------------------------------------------

        if "position" in df_parametros.columns:

            posiciones = sorted(
                df_parametros["position"]
                .dropna()
                .unique()
                .tolist()
            )

            posiciones_seleccionadas = st.multiselect(
                "Selecciona position:",
                posiciones,
                default=[]
            )

        else:

            posiciones_seleccionadas = []

        # ----------------------------------------------------
        # TOURNAMENT STAGE
        # ----------------------------------------------------

        if "tournament_stage" in df_parametros.columns:

            etapas = sorted(
                df_parametros["tournament_stage"]
                .dropna()
                .unique()
                .tolist()
            )

            etapas_seleccionadas = st.multiselect(
                "Selecciona tournament_stage:",
                etapas,
                default=[]
            )

        else:

            etapas_seleccionadas = []

        # ----------------------------------------------------
        # MATCH RESULT
        # ----------------------------------------------------

        if "match_result" in df_parametros.columns:

            resultados = sorted(
                df_parametros["match_result"]
                .dropna()
                .unique()
                .tolist()
            )

            resultados_seleccionados = st.multiselect(
                "Selecciona match_result:",
                resultados,
                default=[]
            )

        else:

            resultados_seleccionados = []

        # ----------------------------------------------------
        # PLAYER NAME
        # ----------------------------------------------------

        if "player_name" in df_parametros.columns:

            jugadores = sorted(
                df_parametros["player_name"]
                .dropna()
                .unique()
                .tolist()
            )

            jugadores_seleccionados = st.multiselect(
                "Selecciona player_name:",
                jugadores,
                default=[]
            )

        else:

            jugadores_seleccionados = []

        # ----------------------------------------------------
        # FILTROS NUMÉRICOS
        # ----------------------------------------------------

        st.subheader(
            "📏 Filtro de rango numérico"
        )

        variables_rango = [
            "age",
            "player_rating",
            "performance_score",
            "distance_covered_km",
            "top_speed_kmh"
        ]

        variables_rango = [
            variable
            for variable in variables_rango
            if variable in df_parametros.columns
        ]

        variable_rango = st.selectbox(
            "Selecciona una variable para filtrar:",
            variables_rango
        )

        minimo = float(
            df_parametros[variable_rango].min()
        )

        maximo = float(
            df_parametros[variable_rango].max()
        )

        if minimo == maximo:

            rango_seleccionado = (
                minimo,
                maximo
            )

            st.info(
                "La variable seleccionada presenta un único valor."
            )

        else:

            rango_seleccionado = st.slider(
                "Selecciona el rango:",
                min_value=minimo,
                max_value=maximo,
                value=(minimo, maximo)
            )

        # ----------------------------------------------------
        # APLICAR FILTROS
        # ----------------------------------------------------

        df_filtrado = df_parametros.copy()

        if len(equipos_seleccionados) > 0:

            df_filtrado = df_filtrado[
                df_filtrado["team"].isin(
                    equipos_seleccionados
                )
            ]

        if len(posiciones_seleccionadas) > 0:

            df_filtrado = df_filtrado[
                df_filtrado["position"].isin(
                    posiciones_seleccionadas
                )
            ]

        if len(etapas_seleccionadas) > 0:

            df_filtrado = df_filtrado[
                df_filtrado["tournament_stage"].isin(
                    etapas_seleccionadas
                )
            ]

        if len(resultados_seleccionados) > 0:

            df_filtrado = df_filtrado[
                df_filtrado["match_result"].isin(
                    resultados_seleccionados
                )
            ]

        if len(jugadores_seleccionados) > 0:

            df_filtrado = df_filtrado[
                df_filtrado["player_name"].isin(
                    jugadores_seleccionados
                )
            ]

        df_filtrado = df_filtrado[
            (
                df_filtrado[variable_rango]
                >= rango_seleccionado[0]
            )
            &
            (
                df_filtrado[variable_rango]
                <= rango_seleccionado[1]
            )
        ]

        # ----------------------------------------------------
        # RESULTADO DEL FILTRO
        # ----------------------------------------------------

        st.markdown("---")

        st.subheader(
            "📊 Resultado del análisis dinámico"
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Registros filtrados",
                f"{len(df_filtrado):,}"
            )

        with col2:
            st.metric(
                "Registros originales",
                f"{len(df_parametros):,}"
            )

        with col3:

            if len(df_parametros) > 0:

                porcentaje_filtrado = (
                    len(df_filtrado) /
                    len(df_parametros)
                    * 100
                )

            else:

                porcentaje_filtrado = 0

            st.metric(
                "Porcentaje seleccionado",
                f"{porcentaje_filtrado:.2f}%"
            )

        # ----------------------------------------------------
        # MÉTRICAS PARA COMPARAR JUGADORES
        # ----------------------------------------------------

        st.subheader(
            "⚽ Selección de métricas de rendimiento"
        )

        metricas_ofensivas = [
            "goals",
            "assists",
            "shots",
            "shots_on_target",
            "key_passes",
            "offensive_contribution"
        ]

        metricas_defensivas = [
            "tackles",
            "interceptions",
            "clearances",
            "blocks",
            "recoveries",
            "defensive_actions",
            "defensive_contribution"
        ]

        metricas_fisicas = [
            "distance_covered_km",
            "sprint_distance_km",
            "top_speed_kmh",
            "accelerations",
            "decelerations",
            "stamina_score"
        ]

        todas_metricas = (
            metricas_ofensivas +
            metricas_defensivas +
            metricas_fisicas +
            [
                "player_rating",
                "performance_score",
                "creativity_score",
                "consistency_score",
                "clutch_performance_score"
            ]
        )

        todas_metricas = [
            variable
            for variable in todas_metricas
            if variable in df_filtrado.columns
        ]

        metricas_seleccionadas = st.multiselect(
            "Selecciona una o más métricas:",
            todas_metricas,
            default=[
                variable
                for variable in [
                    "player_rating",
                    "performance_score"
                ]
                if variable in todas_metricas
            ]
        )

        if len(df_filtrado) == 0:

            st.warning(
                "⚠️ No existen registros que cumplan con "
                "los filtros seleccionados."
            )

        else:

            st.dataframe(
                df_filtrado.head(100),
                use_container_width=True
            )

            if len(metricas_seleccionadas) > 0:

                columnas_tabla = [
                    "player_name"
                ]

                if "team" in df_filtrado.columns:
                    columnas_tabla.append("team")

                if "position" in df_filtrado.columns:
                    columnas_tabla.append("position")

                columnas_tabla += metricas_seleccionadas

                columnas_tabla = [
                    columna
                    for columna in columnas_tabla
                    if columna in df_filtrado.columns
                ]

                tabla_metricas = (
                    df_filtrado[columnas_tabla]
                    .groupby(
                        [
                            columna
                            for columna in [
                                "player_name",
                                "team",
                                "position"
                            ]
                            if columna in columnas_tabla
                        ]
                    )[metricas_seleccionadas]
                    .mean()
                    .round(2)
                    .sort_values(
                        metricas_seleccionadas[0],
                        ascending=False
                    )
                )

                st.subheader(
                    "📋 Comparación de jugadores"
                )

                st.dataframe(
                    tabla_metricas,
                    use_container_width=True
                )

                # --------------------------------------------
                # GRÁFICO DINÁMICO
                # --------------------------------------------

                if len(metricas_seleccionadas) == 1:

                    metrica = metricas_seleccionadas[0]

                    ranking = (
                        df_filtrado
                        .groupby("player_name")[metrica]
                        .mean()
                        .sort_values(
                            ascending=False
                        )
                        .head(10)
                        .reset_index()
                    )

                    fig, ax = plt.subplots(
                        figsize=(12, 7)
                    )

                    sns.barplot(
                        data=ranking,
                        x=metrica,
                        y="player_name",
                        ax=ax
                    )

                    ax.set_title(
                        f"Top 10 jugadores según {metrica}"
                    )

                    ax.set_xlabel(
                        metrica
                    )

                    ax.set_ylabel(
                        "Jugador"
                    )

                    plt.tight_layout()

                    st.pyplot(fig)

                    plt.close()

                else:

                    ranking = (
                        df_filtrado
                        .groupby("player_name")[
                            metricas_seleccionadas
                        ]
                        .mean()
                        .sort_values(
                            metricas_seleccionadas[0],
                            ascending=False
                        )
                        .head(10)
                    )

                    st.subheader(
                        "📊 Comparación de métricas seleccionadas"
                    )

                    st.dataframe(
                        ranking.round(2),
                        use_container_width=True
                    )

        # ----------------------------------------------------
        # ANÁLISIS TEMPORAL
        # ----------------------------------------------------

        st.markdown("---")

        st.subheader(
            "📅 Análisis temporal"
        )

        if "match_date" in df_filtrado.columns:

            df_temporal = df_filtrado.dropna(
                subset=["match_date"]
            ).copy()

            if len(df_temporal) > 0:

                df_temporal["mes"] = (
                    df_temporal["match_date"]
                    .dt.to_period("M")
                    .astype(str)
                )

                variable_temporal = st.selectbox(
                    "Selecciona una métrica temporal:",
                    [
                        variable
                        for variable in [
                            "player_rating",
                            "performance_score",
                            "goals",
                            "assists"
                        ]
                        if variable in df_temporal.columns
                    ]
                )

                evolucion = (
                    df_temporal
                    .groupby("mes")[variable_temporal]
                    .mean()
                    .reset_index()
                )

                fig, ax = plt.subplots(
                    figsize=(12, 6)
                )

                sns.lineplot(
                    data=evolucion,
                    x="mes",
                    y=variable_temporal,
                    marker="o",
                    ax=ax
                )

                ax.set_title(
                    f"Evolución temporal de {variable_temporal}"
                )

                ax.set_xlabel(
                    "Mes"
                )

                ax.set_ylabel(
                    variable_temporal
                )

                plt.xticks(rotation=45)

                plt.tight_layout()

                st.pyplot(fig)

                plt.close()

            else:

                st.warning(
                    "No existen fechas válidas para realizar "
                    "el análisis temporal."
                )


    # ========================================================
    # ÍTEM 10
    # ========================================================

    elif opcion == "💡 Hallazgos clave":

        st.header(
            "💡 Ítem 10: Hallazgos clave"
        )

        st.write(
            "Esta sección presenta un resumen de los principales "
            "hallazgos derivados del análisis exploratorio de datos."
        )

        # ----------------------------------------------------
        # MÉTRICAS GENERALES
        # ----------------------------------------------------

        filas, columnas = df.shape

        total_nulos = int(
            df.isnull().sum().sum()
        )

        duplicados = int(
            df.duplicated().sum()
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
                "Valores faltantes",
                total_nulos
            )

        with col4:
            st.metric(
                "Duplicados",
                duplicados
            )

        st.markdown("---")

        # ----------------------------------------------------
        # HALLAZGO 1
        # ----------------------------------------------------

        st.subheader(
            "📊 Hallazgo 1: Calidad de los datos"
        )

        if total_nulos == 0 and duplicados == 0:

            st.success(
                "El dataset presenta una estructura completa, "
                "sin valores faltantes ni registros duplicados."
            )

        elif total_nulos > 0:

            st.warning(
                "El dataset presenta valores faltantes que deben "
                "ser considerados antes de realizar análisis "
                "estadísticos posteriores."
            )

        else:

            st.warning(
                "Se identificaron registros duplicados que "
                "deben ser evaluados."
            )

        # ----------------------------------------------------
        # HALLAZGO 2
        # ----------------------------------------------------

        st.subheader(
            "⚽ Hallazgo 2: Rendimiento por posición"
        )

        if (
            "position" in df.columns
            and "player_rating" in df.columns
        ):

            rating_position = (
                df.groupby("position")["player_rating"]
                .mean()
                .sort_values(
                    ascending=False
                )
                .reset_index()
            )

            posicion_mayor_rating = (
                rating_position.iloc[0]["position"]
            )

            mayor_rating = (
                rating_position.iloc[0]["player_rating"]
            )

            st.write(
                f"La posición con mayor promedio de "
                f"`player_rating` en el dataset es "
                f"**{posicion_mayor_rating}**, con un promedio "
                f"de **{mayor_rating:.2f}**."
            )

            fig, ax = plt.subplots(
                figsize=(12, 6)
            )

            sns.barplot(
                data=rating_position,
                x="player_rating",
                y="position",
                ax=ax
            )

            ax.set_title(
                "Promedio de player_rating por posición"
            )

            ax.set_xlabel(
                "Player Rating promedio"
            )

            ax.set_ylabel(
                "Posición"
            )

            plt.tight_layout()

            st.pyplot(fig)

            plt.close()

        # ----------------------------------------------------
        # HALLAZGO 3
        # ----------------------------------------------------

        st.subheader(
            "🏆 Hallazgo 3: Performance según resultado"
        )

        if (
            "match_result" in df.columns
            and "performance_score" in df.columns
        ):

            performance_resultado = (
                df.groupby("match_result")[
                    "performance_score"
                ]
                .mean()
                .sort_values(
                    ascending=False
                )
                .reset_index()
            )

            resultado_mayor = (
                performance_resultado.iloc[0]["match_result"]
            )

            performance_mayor = (
                performance_resultado.iloc[0][
                    "performance_score"
                ]
            )

            st.write(
                f"El resultado **{resultado_mayor}** presenta "
                f"el mayor promedio de `performance_score`, "
                f"con un valor de **{performance_mayor:.2f}**."
            )

            fig, ax = plt.subplots(
                figsize=(10, 6)
            )

            sns.barplot(
                data=performance_resultado,
                x="match_result",
                y="performance_score",
                ax=ax
            )

            ax.set_title(
                "Performance Score promedio según resultado"
            )

            ax.set_xlabel(
                "Resultado"
            )

            ax.set_ylabel(
                "Performance Score promedio"
            )

            plt.tight_layout()

            st.pyplot(fig)

            plt.close()

        # ----------------------------------------------------
        # HALLAZGO 4
        # ----------------------------------------------------

        st.subheader(
            "🏃 Hallazgo 4: Variables físicas"
        )

        if (
            "position" in df.columns
            and "distance_covered_km" in df.columns
        ):

            distancia_position = (
                df.groupby("position")[
                    "distance_covered_km"
                ]
                .mean()
                .sort_values(
                    ascending=False
                )
                .reset_index()
            )

            posicion_mayor_distancia = (
                distancia_position.iloc[0]["position"]
            )

            mayor_distancia = (
                distancia_position.iloc[0][
                    "distance_covered_km"
                ]
            )

            st.write(
                f"La posición **{posicion_mayor_distancia}** "
                f"presenta el mayor promedio de distancia "
                f"recorrida, con **{mayor_distancia:.2f} km**."
            )

        # ----------------------------------------------------
        # HALLAZGO 5
        # ----------------------------------------------------

        st.subheader(
            "👟 Hallazgo 5: Pie preferido"
        )

        if "preferred_foot" in df.columns:

            pie_mas_frecuente = (
                df["preferred_foot"]
                .value_counts()
            )

            pie_principal = (
                pie_mas_frecuente.index[0]
            )

            cantidad_pie = (
                pie_mas_frecuente.iloc[0]
            )

            porcentaje_pie = (
                cantidad_pie /
                len(df) *
                100
            )

            st.write(
                f"El pie preferido más frecuente es "
                f"**{pie_principal}**, presente en aproximadamente "
                f"el **{porcentaje_pie:.2f}%** de los registros."
            )

        # ----------------------------------------------------
        # RESUMEN VISUAL
        # ----------------------------------------------------

        st.markdown("---")

        st.subheader(
            "📌 Resumen visual de indicadores"
        )

        resumen_visual = pd.DataFrame(
            {
                "Indicador": [
                    "Registros",
                    "Variables",
                    "Valores faltantes",
                    "Duplicados"
                ],
                "Valor": [
                    filas,
                    columnas,
                    total_nulos,
                    duplicados
                ]
            }
        )

        st.dataframe(
            resumen_visual,
            use_container_width=True,
            hide_index=True
        )

        # ----------------------------------------------------
        # RECOMENDACIONES
        # ----------------------------------------------------

        st.markdown("---")

        st.subheader(
            "🎯 Recomendaciones para la interpretación"
        )

        st.write(
            """
            **1. Analizar el rendimiento según posición:**  
            Las diferencias observadas entre posiciones permiten
            comprender que las métricas de rendimiento deben
            interpretarse considerando la función que cumple cada
            jugador dentro del campo.

            **2. Considerar el contexto del partido:**  
            El `performance_score` puede presentar diferencias
            según el resultado del encuentro. Por ello, las
            comparaciones deben considerar el contexto competitivo.

            **3. Analizar las variables físicas por posición:**  
            La distancia recorrida y la velocidad máxima pueden
            comportarse de manera diferente según la posición.
            No resulta adecuado interpretar estas variables sin
            considerar las funciones específicas de cada jugador.

            **4. Utilizar filtros para análisis específicos:**  
            Los filtros desarrollados en el Ítem 9 permiten
            seleccionar equipos, posiciones, etapas y resultados
            para realizar comparaciones más específicas.

            **5. Evitar conclusiones predictivas:**  
            Los resultados obtenidos corresponden a un análisis
            exploratorio. Estos hallazgos permiten describir y
            comparar los datos, pero no constituyen predicciones
            sobre resultados futuros.
            """
        )

        st.success(
            "✅ El EDA permite identificar patrones, diferencias "
            "y características relevantes del rendimiento de los "
            "jugadores sin construir modelos predictivos."
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
