import seaborn as sb
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.title("Taux suicides")

df = pd.read_csv(r'master.csv')
df

df.rename(columns={"suicides/100k pop":"suicides_pop"," gdp_per_capita ($) ":"gdp_per_capita","gdp_per_capita ($)":"gdp_per_capita","gdp_for_year ($)":"gdp_for_year", " gdp_for_year ($) ":"gdp_for_year","HDI for year":"hdi_for_year"}, inplace=True)
#enlève les virgules pour les nombres
df["gdp_for_year"] = df["gdp_for_year"].astype(str).str.replace(",","")
df

df_men = df[df["sex"] == "male"]
fig = sb.relplot(x=df_men.year, y="suicides_no", data=df, height=8)
st.pyplot(fig)

df_women = df[df["sex"] == "female"]
fig2 = sb.relplot(x=df_women.year, y="suicides_no", data=df, height=8)
st.pyplot(fig2)

fig3 = sb.catplot(x="age", y="suicides_no", data=df, kind="bar", height=8)
st.pyplot(fig3)

fig4 = sb.catplot(x="suicides_no", y="country", data = df, kind="bar",height=15)
st.pyplot(fig4)

#corr = df.corr()
#f, ax = plt.subplots(figsize=(20,5))
#fig5 = sb.heatmap(corr, annot=True, ax =ax)
#st.pyplot(fig5)
#plt.savefig('heatmapEX1.png')