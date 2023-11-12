import dash
from dash import dcc
from dash import html

app = dash.Dash(__name__)
# 官網是這樣
# app = Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.layout = html.Div([
   html.H1("哈囉 Dash!"),
   html.Div("我的第一個 Dash app."),
   dcc.Graph(
       id='example-graph',
       figure={
           'data': [{'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                   {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'}],
           'layout': {'title': '數據可視化範例'}
       }
   )
])
#
if __name__ == '__main__':
   # app.run_server(debug=True)
   # 依照官網寫法
   app.run(debug=True)