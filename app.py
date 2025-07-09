import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(layout='wide')
st.markdown('POPULATION DASHBOARD')
df=pd.read_csv('state_wise_population__2019.csv')
st.dataframe(df)

State=df['State'].unique()
print(State)

selected_State=st.selectbox(label='State',options=State)
dfplot=df[df['State']==selected_State]
st.write(dfplot)

avarage_total_population=round(df['total_population'].mean(),2)
avarage_population_male=round(df['population_male'].mean(),2)
avarage_population_female=round(df['population_female'].mean(),2)

col1,col2,col3=st.columns([1,1,1])
col1.metric(label='avarage_total_population',value=avarage_total_population)
col2.metric(label='avarage_population_male',value=avarage_population_male)
col3.metric(label='avarage_population_female',value=avarage_population_female)

plot=px.bar(
    data_frame=df,
    x='State',
    y='total_population',
    color='total_population',                                  
    title='State vs Total Population (2019)',     
    labels={'total_population': 'Total Population (Millions)', 'State': 'Indian States'},  
    hover_data=['State', 'total_population'],     
    template='plotly_white'
)

plot1=px.pie(
    data_frame=df,
    values='population_male',
    names='population_female',
    hole=0.5,
    title='pie chart for male and female population'
)

plot.show()
plot1.show()
