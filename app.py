import pandas as pd
import datetime
from datetime import date
import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output
import crypto_yahoo as cy
import dash_bootstrap_components as dbc


sym = pd.read_csv('crypto-currencies.csv')

# APP deployment

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])

app.layout = html.Div(
    children=[

        # Storing the information
        dcc.Store(id='store_info', storage_type='local'),

        # Filter section
        dbc.Row([
            dbc.Col(html.Div([
                dcc.DatePickerRange(
                    id='date-picker-range',
                    clearable=True,
                    min_date_allowed=datetime.datetime(2010, 1, 1),
                    max_date_allowed=date.today(),
                    initial_visible_month=date.today() - datetime.timedelta(days=365),
                    start_date=date.today() - datetime.timedelta(days=365),
                    end_date=date.today()
                )
            ]), width=3),

            dbc.Col(html.Div([
                dcc.RadioItems(
                    id='currency-radio-items',
                    options=[{'label': s, 'value': s} for s in ['USD', 'EUR', 'CAD', 'GBP']],
                    value='USD',
                )
            ]), width=3),

            dbc.Col(html.Div([
                dcc.Dropdown(
                    id='stock-ticker-input',
                    options=[{'label': r, 'value': s} for r, s in zip(sym.name, sym.symbol)],
                    value=["BTC"],
                    multi=True
                )
            ]), width=3)
        ]),

        # Graphic section

        html.Div(
            id='graphs',
            children=[
                dash_table.DataTable(id='table',
                                     columns=[{"name": i, "id": i} for i in ['Date', 'Crypto', 'Price']]
                                     )
            ]
        ),

        html.Footer(children='Made with ❤ by @ramonescobar')
    ]
)


@app.callback(
    Output('store_info', 'data'),
    [
        Input('stock-ticker-input', 'value'),
        Input('currency-radio-items', 'value'),
        Input('date-picker-range', 'start_date'),
        Input('date-picker-range', 'end_date')
    ]
)
def filter_table(ticker, currency, start_date, end_date):
    df = cy.multiple_stocks(ticker, currency, start_date, end_date)
    return df.to_dict('records')

@app.callback(
    Output('table', 'data'),
    Input('store_info', 'data')
)
def update_table(data):
    return data


if __name__ == '__main__':
    app.run_server(debug=True)
