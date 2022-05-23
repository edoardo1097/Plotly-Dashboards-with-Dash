import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input,Output
import plotly.graph_objs as go

df= pd.read_csv(r"C:\Users\edo10\Dropbox\Jesus Python Resolver Private Lessons\Python Resolver Lessons\Plotly-Dashboards-with-Dash\Data\mpg.csv")

app= dash.Dash()

features= df.columns

app.layout= html.Div([
            html.Div([
                dcc.Dropdown(id="xaxis",
                            options=[{"label":i,"value":i} for i in features],
                            value="displacement")
            ], style={"width":"48%", "display":"inline-block"}),
            html.Div([
                dcc.Dropdown(id="yaxis",
                            options=[{"label":i,"value":i} for i in features],
                            value="mpg")                
            ], style={"width":"48%", "display":"inline-block"}),
            
            dcc.Graph(id="feature-graphic")
    
], style={"padding":10})

@app.callback(Output("feature-graphic","figure"),
              [Input("xaxis","value"),
              Input("yaxis","value")]
def update_graph(xaxis_name,yaxis_name):
    return {"data":[go.Scatter(x=df[xaxis_name],
                               y=df[yaxis_name],
                              text=df["name"],
                              mode="markers",
                              marker={"size":15})]
            
            , "layout": go.Layout(title="My Dashboard for MPG",
                                   xaxis={"title":xaxis_name},
                                    yaxis={"title":yaxis_name})
                               }
              
              if __name__=="__main__":
                app.run_server()