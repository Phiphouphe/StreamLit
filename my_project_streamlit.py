import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv")

st.title("Hello Wilders, welcome to my application!")

st.write("Ci-dessous les corrélations entre chaque colonne !")
viz_correlation = sns.heatmap(df.corr(),
                                center=0,
                                cmap = sns.color_palette("crest", as_cmap=True,
                                ),
                                annot=True
                                )
st.pyplot(viz_correlation.figure)
st.write("Il y a une forte corrélation entre le nombre de pouces cubes et le nombre de cylindres.")

st.write("Le nombre de voitures selon leur puissance (chevaux)")
dist_sns = sns.displot(data=df,
x=df["hp"], color = 'skyblue'
)
st.pyplot(dist_sns.figure)
st.write("Nous remarquons que les voitures ayant le plus de chevaux sont moins nombreuses et que les voitures qui en ont moins.")

st.write("Le nombre de voitures par année")
distyear_sns = sns.displot(data=df,
x=df["year"], color = 'lightgreen'
)
st.pyplot(distyear_sns.figure)
st.write("En 1978, le nombre de voitures fut élevé. ")

continent = list(np.unique(df["continent"]))
option = st.selectbox("Region", continent)

if option == continent[0]:
    st.subheader("Europe")
    st.write(df[df["continent"].str.contains("Europe")])
elif option == continent[1]:
    st.subheader("Japan continent")
    st.write(df[df["continent"].str.contains("Japan")])
else :
    st.subheader("US continent")
    st.write(df[df["continent"].str.contains("US")])


