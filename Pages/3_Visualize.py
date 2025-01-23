import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Functions to display charts
def barchart(df, x, y):
    st.write(f"### Bar Chart: X={x}, Y={y}")
    fig, ax = plt.subplots(figsize=(5, 1))
    ax.bar(df[x], df[y])
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    st.pyplot(fig)
    
def areachart(df, x, y):
    st.area_chart(df[[x, y]])

def scatterplot(df, x, y):
    st.write("### Scatter Plot")
    df.plot.scatter(x=x, y=y)
    st.pyplot()

def piechart(df, column):
    # Count the occurrences of each value in the specified column
    counts = df[column].value_counts()
    plt.figure(figsize=(6, 6))
    plt.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(plt)

# Check if the dataframe exists in session state
if 'df' in st.session_state:
    df = st.session_state.df
    
    # Store previous charts in session state
    if 'charts' not in st.session_state:
        st.session_state.charts = []
    
    with st.container(key="Top"): 
        left, mid, right = st.columns([1, 1, 1])
        
        # Bar Chart (replaces Line Chart)
        with left:
            with st.container(key="Bar_chart"):
                x_bar = st.selectbox("Select X-axis for Bar Chart", df.columns)
                y_bar = st.selectbox("Select Y-axis for Bar Chart", df.columns)
                
                if st.button("Generate Bar Chart"):
                    st.session_state.charts.append(('Bar', x_bar, y_bar))
        
        # Area Chart
        with mid:
            with st.container(key="Area_Chart"):
                x_area = st.selectbox("Select X-axis for Area Chart", df.columns, key='area_x')
                y_area = st.selectbox("Select Y-axis for Area Chart", df.columns, key='area_y')
                
                if st.button("Generate Area Chart"):
                    st.session_state.charts.append(('Area', x_area, y_area))
        
        # Scatter Plot
        with right:
            with st.container(key="Scatter_Plot"):
                x_scatter = st.selectbox("Select X-axis for Scatter Plot", df.columns, key='scatter_x')
                y_scatter = st.selectbox("Select Y-axis for Scatter Plot", df.columns, key='scatter_y')
                
                if st.button("Generate Scatter Plot"):
                    st.session_state.charts.append(('Scatter', x_scatter, y_scatter))
    
    with st.container(key="Bottom"):
        st.write("#")
        left, mid, right = st.columns([1, 1, 1])
        with mid:
            st.write("### Pie Chart")
            column_pie = st.selectbox("Select Column for Pie Chart", df.columns)
            if st.button("Generate Pie Chart"):
                st.session_state.charts.append(('Pie', column_pie))
    
    # Display all generated charts
    st.write("## Generated Charts")
    for chart in st.session_state.charts:
        if chart[0] == 'Bar':
            barchart(df, chart[1], chart[2])
        elif chart[0] == 'Area':
            areachart(df, chart[1], chart[2])
        elif chart[0] == 'Scatter':
            scatterplot(df, chart[1], chart[2])
        elif chart[0] == 'Pie':
            piechart(df, chart[1])
