import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

def plot_price_trends(data):
    """
    Generate a line plot for price trends using matplotlib.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(data['date'], data['price'], marker='o', linestyle='-')
    plt.title("Price Trends")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.grid()
    plt.show()

def interactive_trends_plot(data):
    """
    Create an interactive plot using Plotly.
    """
    fig = px.line(data, x='date', y='price', title='Interactive Price Trends')
    fig.update_layout(xaxis_title="Date", yaxis_title="Price")
    return fig
