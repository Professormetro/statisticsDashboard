import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html

data = {'Date': ['2024-01-01', '2024-02-01', '2024-03-01'],
        'Revenue': [10000, 15000, 12000],
        'Expenses': [5000, 6000, 7000],
        'Category': ['Category1', 'Category1', 'Category2']
}

data2 = {'Date': ['2024-01-01', '2024-02-01', '2024-03-01'],
        'Revenue': [10000, 15000, 12000],
        'Expenses': [5000, 6000, 7000],
        'Category': ['Category1', 'Category1', 'Category2']
}

df = pd.DataFrame(data)

dt = pd.DataFrame(data2)

app = dash.Dash(__name__)

app.layout = html.Div([
        html.H1('Marketing dashboard'),
    dcc.Graph(
        figure=px.bar(df, x='Date', y='Revenue', title='Sales per day')
    ),
    
    dcc.Dropdown(
        options=[
            {'label': 'Option 1', 'value': 'opt1'},
            {'label': 'Option 2', 'value': 'opt2'}
        ],
        value='',
        multi=True,
        id='dropdown-id'
    ),
    html.Div(id='output-div')

])


"""
@app.callback(
    [Output('output-div', 'children'), Output('output-layout', 'children')],
    [Input('dropdown-id', 'value')]
)
def update_output(selected_value):
    layout = ''
    if selected_value == 'opt1':
        layout = 'Option 1 layout'
    elif selected_value == 'opt2':
        layout = 'Option 2 layout'
    return f'You have selected: {selected_value}', layout

"""

if __name__ == '__main__':
    app.run_server(debug=True)