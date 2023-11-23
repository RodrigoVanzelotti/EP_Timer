from dash import dcc, Output, Input, Dash, html
from datetime import datetime, timedelta
import dash_bootstrap_components as dbc

# app = Dash(__name__)


# Defina a data e hora do término do countdown
target_date = datetime(2024, 5, 30, 23, 59, 59)

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
app.title = 'VanzeTimer' 

app.layout = dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("Faltam 👇 pro EP", className="text-center mt-5"))
        ]),
        dbc.Row([
            dbc.Col(html.H2(id="timer", style={"fontSize": "96px", "fontWeight": "bold"}, className="text-center mt-5"))
        ]),
        dbc.Container([
            html.A('@AAEE    -', href='https://www.instagram.com/aaee.ufrgs/'),
            html.A('    @TOM    -', href='https://www.instagram.com/tom.ufrgs/'),
            html.A('    @Vanze', href='https://www.instagram.com/r7vanzelotti/'),
        ], className='footer'),
        dcc.Interval(id='interval-component', interval=1000, n_intervals=0),
], fluid=True, style={"display": "flex", "flexDirection": "column", "justifyContent": "center", "height": "100vh"})

@app.callback(
    Output('timer', 'children'),
    Input('interval-component', 'n_intervals')
)
def update_timer(n):
    # Calcula a diferença de tempo
    time_left = target_date - datetime.now()
    if time_left.total_seconds() > 0:
        return str(time_left).split('.')[0]  # Remove a parte dos microssegundos
    else:
        return "Countdown Finished!"

if __name__ == '__main__':
    app.run_server(debug=False)
