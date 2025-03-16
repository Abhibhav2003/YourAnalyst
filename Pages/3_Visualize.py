import streamlit as st
import pandas as pd
import plotly.express as px

# Function to get number of bins
def num_bins():
    bins = st.text_input("Enter Number of Rows to Display in Charts", value="0")
    return int(bins) if bins.isdigit() else 0

# Functions to display charts using Plotly
def barchart(df, x, y):
    fig = px.bar(df, x=x, y=y, title="Bar Chart")
    st.plotly_chart(fig)

def areachart(df, x, y):
    fig = px.area(df, x=x, y=y, title="Area Chart")
    st.plotly_chart(fig)

def scatterplot(df, x, y):
    fig = px.scatter(df, x=x, y=y, title="Scatter Plot")
    st.plotly_chart(fig)

def piechart(df, column):
    counts = df[column].value_counts().reset_index()
    counts.columns = [column, 'count']
    fig = px.pie(counts, names=column, values='count', title="Pie Chart")
    st.plotly_chart(fig)

# Check if the dataframe exists in session state
if 'df' in st.session_state:
    df = st.session_state.df
    
    # Store previous charts in session state
    if 'charts' not in st.session_state:
        st.session_state.charts = []
   
   
    with st.container(key="Top"): 
        left, mid, right = st.columns([1, 1, 1])
        
        # Bar Chart
        with left:
            with st.container(key="Bar_chart"):
                x_bar = st.selectbox("Select X-axis for Bar Chart", df.columns)
                y_bar = st.selectbox("Select Y-axis for Bar Chart", df.select_dtypes(include=['number']).columns)
                
                if st.button("Generate Bar Chart"):
                    st.session_state.charts.append(('Bar', x_bar, y_bar))
        
        # Area Chart
        with mid:
            with st.container(key="Area_Chart"):
                x_area = st.selectbox("Select X-axis for Area Chart", df.columns, key='area_x')
                y_area = st.selectbox("Select Y-axis for Area Chart", df.select_dtypes(include=['number']).columns, key='area_y')
                
                if st.button("Generate Area Chart"):
                    st.session_state.charts.append(('Area', x_area, y_area))
        
        # Scatter Plot
        with right:
            with st.container(key="Scatter_Plot"):
                x_scatter = st.selectbox("Select X-axis for Scatter Plot", df.columns, key='scatter_x')
                y_scatter = st.selectbox("Select Y-axis for Scatter Plot", df.select_dtypes(include=['number']).columns, key='scatter_y')
                
                if st.button("Generate Scatter Plot"):
                    st.session_state.charts.append(('Scatter', x_scatter, y_scatter))
    
    with st.container(key="Bottom"):
        st.write("#")
        left, mid, right = st.columns([1, 1, 1])
        with mid:
            st.write("### Pie Chart")
            column_pie = st.selectbox("Select Column for Pie Chart", df.select_dtypes(exclude=['number']).columns)
            if st.button("Generate Pie Chart"):
                st.session_state.charts.append(('Pie', column_pie))
    
    # Get bin value once
    bins = num_bins()
    
    # Display all generated charts
    st.write("## Generated Charts")
    for chart in st.session_state.charts:
        if chart[0] == 'Bar':
            barchart(df.head(bins), chart[1], chart[2])
        elif chart[0] == 'Area':
            areachart(df.head(bins), chart[1], chart[2])
        elif chart[0] == 'Scatter':
            scatterplot(df.head(bins), chart[1], chart[2])
        elif chart[0] == 'Pie':
            piechart(df.head(bins), chart[1])
