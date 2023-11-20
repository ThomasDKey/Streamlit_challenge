import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt


#######  Configuration page ########
st.set_page_config(
    page_title="Dashboard voitures",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.wildcodeschool.com/fr-fr/',
        'Report a bug': "https://www.wildcodeschool.com/fr-fr/",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

@st.cache_data
def get_data():
    df = pd.read_csv('https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv', sep = ',')
    return df
df = get_data()

df['continent']=df['continent'].apply(lambda x: x.lstrip())

liste=df['continent'].unique()
liste=list(liste)
liste.append('All')
liste.sort()


st.header('Analyse des modèles de voitures', divider='blue')
    
    
with st.sidebar:
    st.title("Filtres")
    st.subheader("Choix du continent")
    conti=st.selectbox("Selectionner le continent",liste)



fig = plt.figure(figsize=(12, 6))

if conti=='All':
    sns.heatmap(df.iloc[:,:-1].corr(), cmap="YlGnBu", annot=True)
    plt.title("Correlation des caractèristique de voiture sur tous les continents", fontsize =10)
    
else:
    df2=df[df['continent']==conti]
    sns.heatmap(df2.iloc[:,:-1].corr(), cmap="YlGnBu", annot=True)
    plt.title(f"Correlation des caractèristique de voiture sur le continent : {conti}", fontsize =10)
  
   
st.pyplot(fig)


Q1, Q2= st.columns(2)

with Q1:
    fig = plt.figure(figsize=(12, 6))

    if conti=='All':
        sns.barplot(x="year", y="hp", data=df)
        plt.title("Evolution de la puissance sur tous les continents", fontsize =10)
    
    else:
        df2=df[df['continent']==conti]
        sns.barplot(x="year", y="hp", data=df2)
        plt.title(f"Evolution de la puissance sur le continent : {conti}", fontsize =10)
  
   
    st.pyplot(fig)

with Q2:
    fig = plt.figure(figsize=(12, 6))

    if conti=='All':
        sns.barplot(x="year", y="cylinders", data=df)
        plt.title("Evolution des cylindrées sur tous les continents", fontsize =10)
    
    else:
        df2=df[df['continent']==conti]
        sns.barplot(x="year", y="cylinders", data=df2)
        plt.title(f"Evolution des cylindrées sur le continent : {conti}", fontsize =10)
  
   
    st.pyplot(fig)
    

fig = plt.figure(figsize=(12, 6))

if conti=='All':
    sns.barplot(x="year", y="weightlbs", data=df)
    plt.title("Evolution de la masse sur tous les continents", fontsize =10)
    
else:
    df2=df[df['continent']==conti]
    sns.barplot(x="year", y="weightlbs", data=df2)
    plt.title(f"Evolution de la masse le continent : {conti}", fontsize =10)
  
   
st.pyplot(fig)