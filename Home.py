import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Page title
st.set_page_config(page_title='Interactive Data Explorer', page_icon='📊')
st.title('Interactive Data Explorer')
  
st.subheader('Netflix Movies')

# Load data
df = pd.read_csv('netflix.csv')
df['release_year'] = df['release_year'].astype(int)

# Input widgets
director_list = df['director'].unique()
director_selection = st.multiselect('**Select Director**', director_list, ['Kirsten Johnson', 'Adam McKay', 'Mimi Leder', 'Charlie McDowell'])

## Year selection
year_list = df['release_year'].unique()
year_selection = st.slider('Select year duration', 1942, 2021, (2016, 2021))
year_selection_list = list(np.arange(year_selection[0], year_selection[1] + 1))

# Filter data based on selections
df_selection = df[(df['director'].isin(director_selection)) & (df['release_year'].isin(year_selection_list))]

# Display the filtered data
st.write('### Filtered Movies')
st.dataframe(df_selection)


# Prepare the data for the plot
year_counts = df['release_year'].value_counts().head(15).sort_index()

# Create the plot using Plotly
fig = px.line(x=year_counts.index, y=year_counts.values, markers=True, title='Movies Released Different Years')
fig.update_layout(xaxis_title='Year', yaxis_title='Number of Contents')

# Show plot
st.plotly_chart(fig)
