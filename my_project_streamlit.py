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

st.write("Le nombre de voitures selon leur puissance (chevaux)")
dist_sns = sns.displot(data=df,
x=df["hp"], color = 'skyblue'
)
st.pyplot(dist_sns.figure)

st.write("Le nombre de voitures par année")
distyear_sns = sns.displot(data=df,
x=df["year"], color = 'lightgreen'
)
st.pyplot(distyear_sns.figure)

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


