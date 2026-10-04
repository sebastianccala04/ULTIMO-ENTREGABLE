import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="FIFA World Cup 2026 - EDA",
    page_icon="⚽",
    layout="wide"
)

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
        numericas = self.df.select_dtypes(include=np.number).columns.tolist()
        categoricas = self.df.select_dtypes(exclude=np.number).columns.tolist()
        return numericas, categoricas

if "df" not in st.session_state:
    st.session_state.df = None

opcion = st.sidebar.radio(
    "Selecciona un módulo:",
    [
        "🏠 Home",
        "📂 Carga del dataset",
        "📊 Análisis Exploratorio (EDA)"
    ]
)

if opcion == "🏠 Home":
    st.title("⚽ FIFA World Cup 2026")
    st.subheader("Análisis Exploratorio de Datos")

    st.write(
        "Proyecto de análisis exploratorio del rendimiento de jugadores "
        "durante la FIFA World Cup 2026."
    )

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
        st.write("FIFA World Cup 2026 Player Performance")

        st.markdown("### 📌 Registros")
        st.write("54,600")

        st.markdown("### 📌 Variables")
        st.write("75")

    st.markdown("### 🛠️ Tecnologías")
    st.write("Python, Streamlit, NumPy, Pandas, Matplotlib y Seaborn")

    st.caption(
        "FIFA World Cup 2026 | Análisis Exploratorio de Datos | "
        "Python for Analytics | Sebastián Ccala | 2026"
    )

elif opcion == "📂 Carga del dataset":
    st.header("📂 Carga del dataset")

    archivo = st.file_uploader(
        "Selecciona el archivo CSV:",
        type=["csv"]
    )

    if archivo is not None:
        try:
            df = pd.read_csv(archivo)
            st.session_state.df = df

            st.success("✅ Archivo cargado correctamente.")

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Filas", df.shape[0])

            with col2:
                st.metric("Columnas", df.shape[1])

            st.subheader("Primeros registros")
            st.dataframe(df.head())

        except Exception as e:
            st.error(f"❌ Error al cargar el archivo: {e}")

    else:
        st.info("📌 Debes cargar el archivo CSV para continuar.")

elif opcion == "📊 Análisis Exploratorio (EDA)":
    st.header("📊 Análisis Exploratorio de Datos")

    if st.session_state.df is None:
        st.warning(
            "⚠️ Primero debes cargar el archivo desde "
            "📂 Carga del dataset."
        )

    else:
        df = st.session_state.df

        st.subheader("Ítem 1: Información general del dataset")

        tab1, tab2, tab3, tab4 = st.tabs(
            [
                "📋 Información general",
                "🔤 Tipos de datos",
                "⚠️ Valores nulos",
                "🔁 Duplicados"
            ]
        )

        with tab1:
            buffer = io.StringIO()
            df.info(buf=buffer)

            st.text(buffer.getvalue())

        with tab2:
            tipos = pd.DataFrame({
                "Variable": df.columns,
                "Tipo de dato": df.dtypes.astype(str).values
            })

            st.dataframe(tipos, use_container_width=True)

        with tab3:
            nulos = pd.DataFrame({
                "Variable": df.columns,
                "Valores nulos": df.isnull().sum().values
            })

            st.dataframe(nulos, use_container_width=True)

        with tab4:
            duplicados = df.duplicated().sum()

            st.metric(
                "Registros duplicados",
                duplicados
            )

            if duplicados == 0:
                st.success("✅ No existen registros duplicados.")
            else:
                st.warning(
                    f"⚠️ Se encontraron {duplicados} registros duplicados."
                )
