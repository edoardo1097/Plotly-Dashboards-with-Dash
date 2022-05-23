import pandas as pd
import dash
from dash import dcc
from dash import html
import plotly.graph_objs as go
df= pd.read_csv(r"C:\Users\edo10\Dropbox\Jesus Python Resolver Private Lessons\Python Resolver Lessons\Plotly-Dashboards-with-Dash\Data\OldFaithful.csv")
app= dash.Dash()
app.layout= html.Div([dcc.Graph(id="scaterplot",
                               figure={"data":
                                      [go.Scatter(
                                      x=df["X"],
                                      y=df["Y"],
                                      mode="markers")],
                                 "layout": go.Layout(title="GAS")                                  
                                      })    
    ])
    if __name__=="__main__":
    app.run_server()
    if __name__=="__main__":
    app.run_server()if __name__=="__main__":
    app.run_server()