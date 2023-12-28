import dash


app = dash.Dash()
server = app.server

h1_style = {'textAlign': 'center', 'font-family': 'sans-serif',
            "border": "4px double black", 'width':'46%',
            'padding': '20px', 'letter-spacing': '10px',
            'display': 'inline-block','margin': '10px'}
paragraph_style = {'font-family': 'Comic Sans MS', 'font-size':'28pt',
         'border-style' : 'dashed',  'padding' : '20px',
         'border-radius' : '12px',  'background-color':'aqua',
         'color': 'violet', 'border-width':'10px', 'border-color':'purple'}

header1 = dash.html.H1('raw text 1', style = h1_style)
header2 = dash.html.H1('raw text 2', style = h1_style)


header = dash.html.Div([header1,header2],
                           style={'width': '100%', 'display': 'inline-block'})




app.layout = dash.html.Div([header,
                            dash.html.P('null text', title = 'second block', 
                                        draggable = False,
                                        style = paragraph_style)])



app.run_server()

