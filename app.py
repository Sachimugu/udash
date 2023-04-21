# dash dependencies
from dash_extensions.enrich import  DashProxy, MultiplexerTransform, html,  dcc
import dash
import dash_bootstrap_components as dbc
from dash import html
import pandas as pd


# import dataset---------------------------------------------------
df = pd.read_csv('assets/data/cleaned.csv')
# dash app ---------------------------------------------------------
app = DashProxy(
    __name__,
    use_pages=True,
    transforms=[MultiplexerTransform()],
    external_stylesheets=[dbc.themes.CYBORG],
    suppress_callback_exceptions=True,
    )
server=app.server

# navigation --------------------------------------------------------
def nav():
    return (dbc.Nav(
                [
                    dbc.NavItem(dbc.NavLink("Page1", href="/", active="exact", ),className='navlink'),
                    dbc.NavItem(dbc.NavLink("Page2", href="/page2", active="exact",),className='navlink')
                ],
                # vertical=True,
                # pills=True,
                
            ))
# title---------------------------------------------------------------
def title():
    return(html.H4('University Rankings',className="heading"))



app.layout = html.Div([

    dbc.Container([dbc.Row([
        dbc.Col(nav(), width=2),
        dbc.Col(title(),width=8),
        
    ], className='header'),]),


    html.Div([
        dash.page_container,
        # dcc.Store(id='session', data= df.to_dict('records'), storage_type='session'),

    ])
])


if __name__ == '__main__':
    app.run.server()#dev_tools_hot_reload=False)
# dev_tools_hot_reload=False
