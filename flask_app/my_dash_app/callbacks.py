#----------------------------------------------------------------------------------------------
# Imports
import dash
import pandas as pd
import plotly.express as px
import json

import dash_bootstrap_components as dbc
from dash import Dash, dcc, html
from dash import Input, Output

from my_dash_app.layout import choro_layout, pie_layout, line_layout

#----------------------------------------------------------------------------------------------
# Imported and cleaned data

df = pd.read_excel("cleaned_dataset.xlsx")

f = open("london_boroughs.json")
geoj = json.load(f)

#----------------------------------------------------------------------------------------------
# Callbacks

def init_callbacks(app):
    @app.callback(
        Output(component_id="choro", component_property="figure"),
        Input(component_id="choro_slct_data", component_property="value")
    )
    def update_choro(choro_slct_data):

        dff = df.copy()
        geojj = geoj.copy()

        scale = "speed"

        miny = df[choro_slct_data].min()
        maxy = df[choro_slct_data].max()

        if choro_slct_data == "Deaths":
            scale = "Turbo"
            maxy = maxy*1.2
            miny = miny*0.5

        # Plotly Express
        choro_fig = px.choropleth_mapbox(
            data_frame=dff,
            geojson=geojj,
            featureidkey="properties.name",
            locations="Area",
            color=choro_slct_data,
            color_continuous_scale=scale,
            center={"lat": 51.5, "lon": 0.0},
            zoom=8.5,
            mapbox_style="white-bg",
            animation_frame="Year",
            height=600,
            range_color=[miny*0.8, maxy]
        )

        choro_fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 1000

        return choro_fig

    @app.callback(
        Output(component_id="multi_line_comp", component_property="figure"),
        [Input(component_id="line_slct_area", component_property="value")],
        Input(component_id="line_slct_data", component_property="value")
    )

    def update_multi_line(line_slct_area, line_slct_data):

        dff = df.copy()

        dff = dff.loc[(dff["Area"].isin(line_slct_area))]

        line_fig = px.line(dff, x = 'Year', y = line_slct_data, color = 'Area')
        
        return line_fig

    @app.callback(
        Output(component_id="pie1", component_property="figure"),
        Output(component_id="pie2", component_property="figure"),
        Output(component_id="pie3", component_property="figure"),
        Input(component_id="slct_yr", component_property="value")
    )
    def update_pie(slct_yr):

        dff = df.copy()

        dff = dff.loc[(dff["Year"] == slct_yr)]

        fig_act = px.pie(dff, values='Active', names='Area')
        fig_act.update_layout(
            showlegend=False,
            margin=dict(t=0, b=0, l=0, r=0)
        )

        fig_death = px.pie(dff, values='Deaths', names='Area')
        fig_death.update_layout(
            showlegend=False,
            margin=dict(t=0, b=0, l=0, r=0)
        )

        fig_birth = px.pie(dff, values='Births', names='Area')
        fig_birth.update_layout(
            showlegend=False,
            margin=dict(t=0, b=0, l=0, r=0)
        )

        return fig_act, fig_death, fig_birth
    
    @app.callback(Output('main', 'children'),
            Input('url', 'pathname'))
    def display_page(pathname):
        if pathname == '/choro':
            return choro_layout
        elif pathname == '/line_comp':
            return line_layout
        elif pathname == '/pie':
            return pie_layout





