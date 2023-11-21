import streamlit as st
import pandas as pd
import seaborn as sns


st.header('Quête Streamlit : Cars', divider='rainbow')

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"

df_cars = pd.read_csv(link)

df_cars['year'] = pd.to_datetime(df_cars['year'], format='%Y')
st.write("Filtrage du jeu de données par région")
selected_value = st.selectbox('Sélectionner une région :', ['Toutes'] + df_cars['continent'].unique().tolist())

# Filtrer le DataFrame en fonction de la valeur sélectionnée
if selected_value == 'Toutes':
    filtered_df = df_cars  # Afficher l'ensemble des valeurs
    filtered_df
else:
    filtered_df = df_cars[df_cars['continent'] == selected_value]
    filtered_df
st.write("Heatmap de corrélation pour la région : {}".format(selected_value))
viz_correlation = sns.heatmap(filtered_df.select_dtypes(include='number').corr(), center=0, cmap = sns.color_palette("vlag", as_cmap=True))
viz_correlation.figure

st.write("Etude de répartition pour la région : {}".format(selected_value))
st.write("Sous filtrage par caractéristique")
selected_value_caract = st.selectbox('Caractéristique :', list(filtered_df.select_dtypes(['number'])))
if selected_value == 'Toutes' :
	viz_caract = sns.displot(data=filtered_df, x=selected_value_caract, hue='continent', kind='kde')
else :
     viz_caract = sns.displot(data=filtered_df, x=selected_value_caract, kind='kde')
viz_caract.figure