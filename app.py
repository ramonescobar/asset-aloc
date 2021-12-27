import pandas_datareader.data as web
import datetime
from datetime import date
import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output
import time



##########################
#### APP deployment ######
##########################

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(children='Hello Dash'),

        html.Div(
            id='filters',
            children=[
                dcc.DatePickerRange(
                    id='date-picker-range',
                    clearable=True,
                    min_date_allowed=datetime.datetime(2010, 1, 1),
                    max_date_allowed=date.today(),
                    initial_visible_month=date.today() - datetime.timedelta(days=365),
                    start_date=date.today() - datetime.timedelta(days=180),
                    end_date=date.today()
                )
            ]
        )

        html.Footer(children='Made with ❤ by @ramonescobar')
    ]
)


if __name__ == '__main__':
    app.run_server(debug=True)