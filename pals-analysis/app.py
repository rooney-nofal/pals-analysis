import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Analyse des Pals", layout="wide")

@st.cache_data
def load_data():
    # Load CSV, skip first row, use second row as header
    df = pd.read_csv("Palworld_Data--Palu combat attribute table.csv", skiprows=1)

    # Create Combat Power column
    df['Combat Power'] = df['melee attack'] + df['Remote attack'] + df['defense']
    
    return df

df = load_data()

# App title
st.title("📊 Analyse des Pals - Dashboard")

# Sidebar filter
st.sidebar.header("📂 Filtres")
selected_rarity = st.sidebar.multiselect(
    "Filtrer par rareté",
    options=sorted(df['rarity'].dropna().unique()),
    default=sorted(df['rarity'].dropna().unique())
)

# Filter data
filtered_df = df[df['rarity'].isin(selected_rarity)]

# Data preview
st.subheader("👀 Aperçu des données")
st.dataframe(filtered_df.head())

# Combat Power Chart
st.subheader("⚔️ Distribution de la puissance de combat")
fig, ax = plt.subplots(figsize=(10, 5))
sns.histplot(filtered_df['Combat Power'], bins=20, kde=True, color='purple', ax=ax)
ax.set_xlabel("Puissance de combat")
ax.set_ylabel("Nombre de Pals")
st.pyplot(fig)
