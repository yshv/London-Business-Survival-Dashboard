#----------------------------------------------------------------------------------------------
# Imports
import dash
import pandas as pd
import plotly.express as px
import json

import dash_bootstrap_components as dbc
from dash import Dash, dcc, html
from dash import Input, Output

#----------------------------------------------------------------------------------------------
# Imported and cleaned data

df = pd.read_excel("cleaned_dataset.xlsx")

f = open("london_boroughs.json")
geoj = json.load(f)


#----------------------------------------------------------------------------------------------
# Choro layout

choro_layout = html.Div([

    html.Br(),
    html.H1("Choropleth Map",
            style={'text-align': 'center'}),
    dbc.Row(
        dbc.Col(html.H5("Select a data type and press play! You can also pause and hover to see values."), className='text-muted')
    ),

    dcc.Dropdown(id="choro_slct_data",
                 options=[
                    {"label": "Active Businesses", "value": "Active"},
                    {"label": "Business Deaths", "value": "Deaths"},
                    {"label": "Business Births", "value": "Births"},
                    {"label": "First year business survival",
                        "value": "Percentage_1"},
                    {"label": "Second year business survival",
                        "value": "Percentage_2"},
                    {"label": "Third year business survival",
                        "value": "Percentage_3"},
                    {"label": "Forth year business survival",
                        "value": "Percentage_4"},
                    {"label": "Fifth year business survival",
                        "value": "Percentage_5"},
                 ],
                 multi=False,
                 value="Deaths",
                 style={'width': "50%"}
                 ),

    dcc.Graph(id='choro', figure={}),

])

#----------------------------------------------------------------------------------------------
# line layout

line_layout = html.Div([
    html.Br(),
    html.H1("Line Chart", style={'text-align': 'center'}),
    dbc.Row(
        dbc.Col(html.H5("Select a data type and add boroughs to compare! Hover to see values."), className='text-muted')
    ),

    dcc.Dropdown(id="line_slct_area",
                 options=[{"label": c, "value": c} for c in df.Area.unique()],
                 multi=True,
                 value = ['City of London', 'Westminster'],
                 style={'width': "100%"}
                 ),

    dcc.Dropdown(id="line_slct_data",
                 options=[
                    {"label": "Active Businesses", "value": "Active"},
                    {"label": "Business Deaths", "value": "Deaths"},
                    {"label": "Business Births", "value": "Births"},
                    {"label": "First year business survival",
                        "value": "Percentage_1"},
                    {"label": "Second year business survival",
                        "value": "Percentage_2"},
                    {"label": "Third year business survival",
                        "value": "Percentage_3"},
                    {"label": "Forth year business survival",
                        "value": "Percentage_4"},
                    {"label": "Fifth year business survival",
                        "value": "Percentage_5"},                   
                 ],
                 multi=False,
                 value= "Percentage_1",
                 style={'width': "50%"}
                 ),

    dcc.Graph(id='multi_line_comp', figure={})

])


#----------------------------------------------------------------------------------------------
# pie layout

pie_layout = html.Div([

    html.Br(),
    html.H1("Pie Charts", style={'text-align': 'center'}),
    dbc.Row(
        dbc.Col(html.H5("Select a year and compare! Hover to see borough names."), className='text-muted')
    ),
    html.Br(),
    dbc.Row(
        dcc.Dropdown(id='slct_yr',
                     options=[
                         {"label": "2004", "value": 2004},
                         {"label": "2005", "value": 2005},
                         {"label": "2006", "value": 2006},
                         {"label": "2007", "value": 2007},
                         {"label": "2008", "value": 2008},
                         {"label": "2009", "value": 2009},
                         {"label": "2010", "value": 2010},
                         {"label": "2011", "value": 2011},
                         {"label": "2012", "value": 2012},
                         {"label": "2013", "value": 2013},
                         {"label": "2014", "value": 2014},
                         {"label": "2015", "value": 2015},
                         {"label": "2016", "value": 2016},
                         {"label": "2017", "value": 2017},
                     ],
                     multi=False,
                     value=2004,
                     clearable=False,
                     style={"width": "40%", "color": "black"}
                     )
    ),

    dbc.Row(children=[
        dbc.Col(xs=12, sm=12, md=12, lg=6, xl=6, children=[
            html.Div('Active Businesses'),
            dcc.Graph(id='pie1')
        ], style={
            'display': 'inline-block',
            'vertical-align': 'top',
            'width': '33%',
        }),
        dbc.Col(xs=12, sm=12, md=12, lg=6, xl=6, children=[
            html.Div('Business Deaths'),
            dcc.Graph(id='pie2')
        ], style={
            'display': 'inline-block',
            'vertical-align': 'top',
            'width': '33%',
        }),
        dbc.Col(xs=12, sm=12, md=12, lg=6, xl=6, children=[
            html.Div('Business Births'),
            dcc.Graph(id='pie3'),
        ], style={
            'display': 'inline-block',
            'vertical-align': 'top',
            'width': '33%',
        })
    ]),

])

#----------------------------------------------------------------------------------------------
# Index layout

navbar = dbc.NavbarSimple(
    children=[

        dbc.NavItem(dbc.NavLink("Choropleth Map",
                                href="/choro", id="choro_link")),
        dbc.NavItem(dbc.NavLink("Multi-Line Chart",
                                href="/line_comp", id="line_comp_link")),
        dbc.NavItem(dbc.NavLink("Pie Charts", href="/pie", id="pie_link")),

        dbc.NavItem(
            dbc.Button("Logout", href='/auth/logout', external_link=True)
        )
    ],
    brand="London Business Survival Dash Board",
    brand_href="/",
    color='primary',
    dark='False',
    fluid=True,
    class_name='navbar-expand-sm sticky-top',
)


choro_card = dbc.Card(
    [
        dbc.CardImg(src="assets/choro.png", top=True),

        dbc.CardBody([
            html.H4("Choropleth Map", className="card-title"),
            html.P(
                "Visualise the various business statistics of the London boroughs from 2004 to 2017.",
                className="card-text",
            ),
            dbc.Button("Go", href="/choro", color="primary"),
        ]
        )
    ]
)

comparison_card = dbc.Card(
    [
        dbc.CardImg(src="assets/line.png", top=True),

        dbc.CardBody(
            [
                html.H4("Data Comparison", className="card-title"),
                html.P(
                    "Compare various business statistics across the London boroughs from 2004 to 2017.",
                    className="card-text",
                ),
                dbc.Button("Go", href="/line_comp", color="primary"),
            ]
        )
    ]
)

pie_card = dbc.Card(
    [
        dbc.CardImg(src="assets/pie.png", top=True),

        dbc.CardBody(
            [
                html.H4("Quick Comparison", className="card-title"),
                html.P(
                    "Quickly see the distribution of active business as well as births and deaths from 2004 - 2017.",
                    className="card-text",
                ),
                dbc.Button("Go", href="/pie", color="primary"),
            ],
        )
    ]
)

layout = dbc.Container(fluid=True, children=[
        dcc.Location(id='url', refresh=False),
        navbar,
        html.Div(id='main'),
        html.Br(),
        dbc.Row([
            dbc.Col(html.H1('Main Menu', id='main-menu-title'))
        ]),
        html.Br(),

        dbc.Row([
            dbc.Col(choro_card, sm=10, md=8, lg=5, xl=3),
            dbc.Col(comparison_card, sm=10, md=8, lg=5, xl=3),
            dbc.Col(pie_card, sm=10, md=8, lg=5, xl=3)
            ]),
    ])