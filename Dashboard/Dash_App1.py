
from dash import Dash
from dash.dependencies import Input, State, Output
from .Dash_fun import apply_layout_with_auth, load_object, save_object
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

url_base = '/dash/app1/'

df = pd.read_csv(r"C:\Users\user\Desktop\Code Adventure\prosperLoanData_.csv")
df['LoanOriginationDate'] = pd.to_datetime(df['LoanOriginationDate'])
df['ListingCreationDate'] = pd.to_datetime(df['ListingCreationDate'])
df['ClosedDate'] = pd.to_datetime(df['ClosedDate'])

# ------------------ Customer Added Time Series -----------------------

timeseries_data = [go.Scatter(
        x=df['LoanOriginationDate'],
        y = df['LoanNumber'],
        showlegend = True,
        name = 'Customers added',

    )]
timeseries_layout = dict(
    title='Customers Added',
    yaxis = dict(
        title = 'No. of customers added'),
    xaxis=dict(
        title = 'Date',
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label='1m',
                     step='month',
                     stepmode='backward'),
                dict(count=6,
                     label='6m',
                     step='month',
                     stepmode='backward'),
                dict(count=1,
                    label='YTD',
                    step='year',
                    stepmode='todate'),
                dict(count=1,
                    label='1y',
                    step='year',
                    stepmode='backward'),
                dict(count=2,
                    label='2y',
                    step='year',
                    stepmode='backward'),
                dict(count=3,
                    label='3y',
                    step='year',
                    stepmode='backward'),
                dict(count=4,
                    label='4y',
                    step='year',
                    stepmode='backward'),
                dict(count=5,
                    label='5y',
                    step='year',
                    stepmode='backward'),
                dict(count=6,
                    label='6y',
                    step='year',
                    stepmode='backward'),
                dict(count=7,
                    label='7y',
                    step='year',
                    stepmode='backward'),
                dict(step='all')
            ])
        ),
        rangeslider=dict(
            visible = True
        ),
        type='date'
    )
)

timefig = dict(data=timeseries_data, layout=timeseries_layout)

# -------------------------End Time Series -------------------------

#--------------------------------
trace1= [go.Box(
    x=df['ProsperScore'],
    y=df['BorrowerRate'],
    boxmean=True,
    showlegend=True
)]
boxplot = dict(data=trace1)





# ------------------------ MAIN LAYOUT ------------------------------
graph = html.Div([
            html.H1('Performance'), html.Br(),
            #dcc.Input(id = 'input_text'), html.Br(),
            #html.Div(id = 'target'),
            html.Div(dcc.Graph(
            figure=timefig
            )),

            html.Div(dcc.Graph(
            figure=boxplot
            ))

    ])

'''layout = html.Div([
    html.H1('Performance'), html.Br(),
    dcc.Input(id = 'input_text'), html.Br(), html.Br(),
    html.Div(id = 'target')
])'''

def Add_Dash(server):
    app = Dash(server=server, url_base_pathname=url_base)
    apply_layout_with_auth(app, graph)

    '''@app.callback(
            Output('target', 'children'),
            [Input('input_text', 'value')])
    def callback_fun(value):
        return 'your input is {}'.format(value)
    
    '''
    return app.server