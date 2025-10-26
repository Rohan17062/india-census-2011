import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('mkb.csv')
st.title('Color represents secondary value whereas size represents primary value')

# Sidebar
st.sidebar.title('India census 2011 data visualization')
L = list(df['State'].unique())
L.insert(0, 'entire india')
state = st.sidebar.selectbox('Choose the state', L)

primary = st.sidebar.selectbox('Choose primary parameter (size)', list(df.columns[5:]))
secondary = st.sidebar.selectbox('Choose secondary parameter (color)', list(df.columns[5:]))

button = st.sidebar.button('Plot graph')

if button:

    if state != 'entire india':
        df_plot = df[df['State'] == state]
    else:
        df_plot = df.copy()


    if pd.api.types.is_numeric_dtype(df_plot[secondary]):

        fig = px.scatter_mapbox(
            df_plot,
            lat='Latitude',
            lon='Longitude',
            color=secondary,
            size=primary,
            hover_name='District',
            color_continuous_scale=px.colors.sequential.Viridis,
            zoom=4,
            height=700,
            width=700
        )
    else:

        unique_vals = df_plot[secondary].unique()
        color_map = {val: px.colors.qualitative.Safe[i % len(px.colors.qualitative.Safe)]
                     for i, val in enumerate(unique_vals)}
        fig = px.scatter_mapbox(
            df_plot,
            lat='Latitude',
            lon='Longitude',
            color=secondary,
            size=primary,
            hover_name='District',
            color_discrete_map=color_map,
            zoom=4,
            height=700,
            width=700
        )


    fig.update_layout(mapbox_style="open-street-map")


    st.plotly_chart(fig, use_container_width=True)

















