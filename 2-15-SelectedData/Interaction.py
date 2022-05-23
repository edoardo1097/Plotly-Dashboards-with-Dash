import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
from numpy import random

app = dash.Dash()

df= pd.read_csv(r"C:\Users\edo10\Dropbox\Jesus Python Resolver Private Lessons\Python Resolver Lessons\Plotly-Dashboards-with-Dash\Data\mpg.csv")
