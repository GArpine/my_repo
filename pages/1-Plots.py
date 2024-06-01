import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker  # Import ticker from matplotlib

def main():
    st.title("Netflix EDA Dashboard")

    # Load data
    data = pd.read_csv('netflix.csv')
    st.write("Data Overview:")
    st.write(data.head())

    st.sidebar.header("Visualizations")
    plot_options = ["Bar plot", "Scatter plot", "Histogram", "Box plot", "Correlation Heatmap"]
    selected_plot = st.sidebar.selectbox("Choose a plot type", plot_options)

    if selected_plot == "Bar plot":
        x_axis = st.sidebar.selectbox("Select x-axis", data.columns, key='bar_x')
        y_axis = st.sidebar.selectbox("Select y-axis", data.columns, key='bar_y')
        color_palette = st.sidebar.selectbox("Select color palette", ["deep", "muted", "bright", "pastel", "dark", "colorblind"], key='bar_palette')
        st.write("Bar Plot:")
        fig, ax = plt.subplots()
        sns.barplot(x=data[x_axis], y=data[y_axis], ax=ax, palette=color_palette)
        ax.xaxis.set_major_locator(ticker.MaxNLocator(integer=True, nbins=10))
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
        ax.set_title("Bar Plot of {} vs {}".format(x_axis, y_axis))
        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)
        ax.grid(True)
        st.pyplot(fig)

    elif selected_plot == "Scatter plot":
        x_axis = st.sidebar.selectbox("Select x-axis", data.columns, key='scatter_x')
        y_axis = st.sidebar.selectbox("Select y-axis", data.columns, key='scatter_y')
        hue = st.sidebar.selectbox("Select hue", [None] + list(data.columns), key='scatter_hue')
        color_palette = st.sidebar.selectbox("Select color palette", ["deep", "muted", "bright", "pastel", "dark", "colorblind"], key='scatter_palette')
        st.write("Scatter Plot:")
        fig, ax = plt.subplots()
        sns.scatterplot(x=data[x_axis], y=data[y_axis], hue=data[hue] if hue else None, ax=ax, palette=color_palette)
        ax.set_title("Scatter Plot of {} vs {}".format(x_axis, y_axis))
        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)
        ax.grid(True)
        st.pyplot(fig)

    elif selected_plot == "Histogram":
        column = st.sidebar.selectbox("Select a column", data.columns, key='hist_column')
        bins = st.sidebar.slider("Number of bins", 5, 100, 20, key='hist_bins')
        color = st.sidebar.color_picker("Select color", "#3498db", key='hist_color')
        st.write("Histogram:")
        fig, ax = plt.subplots()
        sns.histplot(data[column], bins=bins, ax=ax, color=color)
        ax.set_title("Histogram of {}".format(column))
        ax.set_xlabel(column)
        ax.set_ylabel("Frequency")
        ax.grid(True)
        st.pyplot(fig)

    elif selected_plot == "Box plot":
        column = st.sidebar.selectbox("Select a column", data.columns, key='box_column')
        st.write("Box Plot:")
        fig, ax = plt.subplots()
        sns.boxplot(data[column], ax=ax)
        ax.set_title("Box Plot of {}".format(column))
        ax.set_xlabel(column)
        ax.grid(True)
        st.pyplot(fig)

    elif selected_plot == "Correlation Heatmap":
        st.write("Correlation Heatmap:")
        fig, ax = plt.subplots()
        corr = data.corr()
        sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', ax=ax)
        ax.set_title("Correlation Heatmap")
        st.pyplot(fig)

if __name__ == "__main__":
    main()
