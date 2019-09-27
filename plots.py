import plotly
import plotly.graph_objects as go
import plotly.express as px
from data_mpg import mpg_data
import json

df = mpg_data()

def hist_mpg():
    fig = px.histogram(df, x="mpg", marginal="rug")
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def hist_hp():
    fig = px.histogram(df, x="horsepower", marginal="rug")
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json