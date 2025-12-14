from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()

df = pd.read_csv("merged_sales_data_0.csv")

df = df.sort_values("date")

fig = px.line(df, x="date", y="sales", title="Pink Morsel Sales Over Time")

app.layout = html.Div(children=[
    html.H1(children='Pink Morsel Sales Visualiser'),

    html.Div(children='''
        Pink Morsel price increase on the 15th January 2021
    '''),

    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

