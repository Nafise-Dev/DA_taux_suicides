import seaborn as sb
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.title("Taux suicides")

df = pd.read_csv(r'master.csv')
df

st.write("je renomme les colonnes et enlève les virgules pour les nombres")
df.rename(columns={"suicides/100k pop":"suicides_pop"," gdp_per_capita ($) ":"gdp_per_capita","gdp_per_capita ($)":"gdp_per_capita","gdp_for_year ($)":"gdp_for_year", " gdp_for_year ($) ":"gdp_for_year","HDI for year":"hdi_for_year"}, inplace=True)
#enlève les virgules pour les nombres
df["gdp_for_year"] = df["gdp_for_year"].astype(str).str.replace(",","")
df

st.write("Je compare le taux de suicides avec le sexe masculin et féminin.")
df_men = df[df["sex"] == "male"]
fig = sb.relplot(x=df_men.year, y="suicides_no", data=df, height=8)
st.pyplot(fig)

df_women = df[df["sex"] == "female"]
fig2 = sb.relplot(x=df_women.year, y="suicides_no", data=df, height=8)
st.pyplot(fig2)

st.write("Je constate que le taux de suicides pour les personnes de sexe masuclin est élevé par rapport aux personnes de sexe opposés. La corrélation n'est pas bonne. \n Je vais donc comparer l'âge avec le sexe masculin et féminin.")

fig3 = sb.catplot(x="age", y="suicides_no", data=df, kind="bar", height=8)
st.pyplot(fig3)

st.write("La condition de vie dans chaque pays pourrait également influencer le taux de suicides.")

fig4 = sb.catplot(x="suicides_no", y="country", data = df, kind="bar",height=15)
st.pyplot(fig4)

class Economics():
    def corr_fig(self, data=None):
        corr = df.corr()
        f, ax = plt.subplots(figsize=(20,5))
        ax = sb.heatmap(corr, annot=True, ax =ax)
        return f


eco = Economics()
st.pyplot(eco.corr_fig())
#st.figure.savefig('heatmapEX1.png')
