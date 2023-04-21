import dash
from dash_extensions.enrich import Output,Input,  html, callback, State, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import date
today = date.today()
today = today.strftime("%d %b %Y")

dash.register_page(__name__, path="/page2")
df = pd.read_csv('assets/data/cleaned.csv')


# year = df[df['year']==2014]
# total_no_uni=year.count()['name']
# scores_overall=year[year['rank']=='1'].reset_index()['scores_overall']
# scores_teaching_rank=year[year['scores_teaching_rank']==1].reset_index()['scores_teaching']
# scores_citations=year[year['scores_citations_rank']==1].reset_index()['scores_citations']
# scores_research=year[year['scores_research_rank']==1].reset_index()['scores_research']
# stats_pc_intl_students=Total_International_students = year.sum()['stats_pc_intl_students']
# stats_number_students= Total__students = year.sum()['stats_number_students']


year = df[(df['year']==2023) & (df['name']=='University of Cambridge')]

try:
# year = df[df['year']==dropdown]
    total_no_uni=year.values[0][0]
    scores_overall=year.values[0][2]
    scores_teaching_rank=year.values[0][4]
    scores_citations=year.values[0][8]
    scores_research=year.values[0][6]
    stats_pc_intl_students=year.values[0][12]
    stats_number_students=year.values[0][11]
except:
    total_no_uni='None'
    scores_overall='None'
    scores_teaching_rank='None'
    scores_citations='None'
    scores_research='None'
    stats_pc_intl_students='None'
    stats_number_students='None'

    
value1=list(df['year'].unique())
value2=list(df['name'].unique())



def numberBox( id1, ch1, id2, ch2,  ):
    return(html.Div([
    html.H5(children=ch1,id=id1, className='text-green-500'),
    html.P(children=ch2, id=id2,className='small'),

    ], className='numberBox'))
def datebox():
    return(
        html.Div(html.H6(f'{today}',),className='numberBox', style={'height':'36px'})
    )
  

def page1():
    return(
        dbc.Row([
    dbc.Col([
        html.Div([
            dcc.Dropdown(id='dropdown1', value=2023, options=[{'label': i, 'value': i} for i in value1],
            placeholder="year",className='dropdown'),
        ], className='dropDownBox'),
        
        html.Div([
            numberBox('total_no_uni', total_no_uni,'box12', 'Rank'),
            numberBox('scores_overall',  scores_overall, 'box22', 'Scores Overall')
        ], className='numberBoxCon'),

        html.Div([
            numberBox('scores_teaching_rank', scores_teaching_rank, 'box22', 'Score Teaching'),
            numberBox('scores_citations', scores_citations, 'box42', 'Scores Citations')
        ], className='numberBoxCon'),

        html.Div([
            numberBox('scores_research', scores_research, 'box52', 'Scores Research'),
            numberBox('stats_number_students',stats_number_students, 'box62', 'total Students')
        ], className='numberBoxCon'),

        html.Div([
            dcc.Graph(id='pie1', figure=px.line(),className='pieChart', style={'padding':'5px'})
        ], className='numberBoxCon'),

    ],width=3),
# ====================
    dbc.Col([
    html.Div(dbc.Col( id='school',className='numberBox', style={'height':'36px'}),className='numberBoxCon'),

    html.Div(dcc.Graph(id='map1', figure=px.line(), config={'modeBarButtonsToRemove': ['zoom2d', 'pan2d', 'select2d', 'lasso2d', 'zoomIn2d', 'zoomOut2d', 'autoScale2d', 'resetScale2d']}, className='numberBoxx', style={'height':'315px', }),className='numberBoxCon',),

    html.Div(dcc.Graph(id='bar2', figure=px.line(), config={'modeBarButtonsToRemove': ['zoom2d', 'pan2d', 'select2d', 'lasso2d', 'zoomIn2d', 'zoomOut2d', 'autoScale2d', 'resetScale2d']}, className='numberBoxx',),className='numberBoxCon',style={'height':'225', }),

    # html.Div(dcc.Graph(id='bar2', figure=px.line(), config={'modeBarButtonsToRemove': ['zoom2d', 'pan2d', 'select2d', 'lasso2d', 'zoomIn2d', 'zoomOut2d', 'autoScale2d', 'resetScale2d']}, className='numberBox', style={'height':'225', }),className='numberBox',),

    # html.Div(dcc.Graph(id='line1', figure=px.line(), config={'modeBarButtonsToRemove': ['zoom2d', 'pan2d', 'select2d', 'lasso2d', 'zoomIn2d', 'zoomOut2d', 'autoScale2d', 'resetScale2d']}, className='numberBox', style={'height':'85px', }),className='numberBoxCon',),

    ],width=6),
# ====================

    dbc.Col([
        html.Div([
            dcc.Dropdown(id='dropdown2', value='University of Cambridge', options=[{'label': i, 'value': i} for i in value2],
            placeholder="Enter University",className='dropdown'),
        ], className='dropDownBox'),

         html.Div([
            numberBox('stats_pc_intl_students', stats_pc_intl_students, 'box72', 'stat intl students')
        ], className='numberBoxCon',),

        html.Div(html.Div(dcc.Graph(id='bar1', figure=px.line(), config={'modeBarButtonsToRemove': ['zoom2d', 'pan2d', 'select2d', 'lasso2d', 'zoomIn2d', 'zoomOut2d', 'autoScale2d', 'resetScale2d']}),style={"maxHeight": "438px", "overflow": "auto", "width": "100%"}),className='numberBoxCon',) 

        


    ],width=3),
# ====================

])
    )
layout = html.Div([
    # html.H1('Home', className='text-green-500'),
    dbc.Container(page1()),
    

])

@callback(
    Output('total_no_uni', "children"),
    Output('scores_overall', "children"),
    Output('scores_teaching_rank', "children"),
    Output('scores_citations', "children"),
    Output('scores_research', "children"),
    Output('stats_number_students', "children"),
    Output('stats_pc_intl_students', "children"),
    Output('pie1', "figure"),
    Output('bar1', "figure"),
    Output('bar2', "figure"),
    Output('map1', "figure"),
    Output('school', "children"),


    Input('dropdown1', 'value'),
    Input('dropdown2', 'value'),

    # State('session', 'data'),
)

def updatePage1(dropdown1, dropdown2):
    # df=pd.DataFrame(data)
    print(dropdown1)
    print(dropdown2)
    year = df[(df['year']==dropdown1) & (df['name']==dropdown2)]
    # year = df[df['year']==dropdown]
    try:
    # year = df[df['year']==dropdown]
        total_no_uni=year.values[0][0]
        scores_overall=year.values[0][2]
        scores_teaching_rank=year.values[0][4]
        scores_citations=year.values[0][8]
        scores_research=year.values[0][6]
        stats_pc_intl_students=year.values[0][12]
        stats_number_students=year.values[0][11]
    except:
        total_no_uni='None'
        scores_overall='None'
        scores_teaching_rank='None'
        scores_citations='None'
        scores_research='None'
        stats_pc_intl_students='None'
        stats_number_students='None'
    print(dropdown1)
    print(dropdown2)
    # stats_number_students = year.sum()['stats_number_students']

    # scores_teaching_rank=year[year['scores_teaching_rank']==1].reset_index()['scores_teaching']
    # scores_citations=year[year['scores_citations_rank']==1].reset_index()['scores_citations']
    # scores_research=year[year['scores_research_rank']==1].reset_index()['scores_research']
    # stats_pc_intl_students = year.sum()['stats_pc_intl_students']
    # stats_number_students = year.sum()['stats_number_students']

    # gender=df.groupby('year').sum()[['male','female']].loc[dropdown]
    try:
        pie1=px.pie(values=[year.values[0][14],year.values[0][15]], names=[year.values[0][14],year.values[0][15]], labels={"index":"Gender"},hole=0.5,height=230,
        width=250,
        color_discrete_sequence=['#b3b3b3','#19d3f3'])
        pie1.update_traces(showlegend=False, textinfo='label+percent', textposition='outside', textfont=dict(color='#fff'))
        pie1.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
        },
        margin=dict(l=0, r=0, t=0, b=0),
        title =  dict(text ='Gender',font =dict(family='Sherif',size=14,color = '#fff'))
        )
    except:
        pie1= px.line()

    try:
        ovr=df[df['name']==dropdown2][['name','year','scores_overall']]
        ovr=ovr.sort_values('year',ascending = True)
        
        kolor=[ 'aqua']*len(ovr)
        bar1=px.bar(
            data_frame=ovr,
            y='scores_overall',
            x='year',
            orientation='h',
            barmode='group',
            title='Over Scores by year',
            height=500,
            
            # text='scores_overall',
            # template='plotly_dark',
        )
        bar1.update_layout(
            {
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
        },
            margin=dict(l=0, r=0, t=30, b=10),
        #     xaxis={'categoryorder':'total descending'},
            xaxis_visible=False,
            yaxis_title=None,
            yaxis=dict(
                # ticklabelposition='inside',
                color="#fff",
                tickfont=dict(family='Sherif',size=12,)),
            title =  dict(
        #         text ='Facilities By State',
                font =dict(family='Sherif',size=11,color = '#fff'),
        ))
        bar1.update_traces(
            marker_color=kolor,
            # textposition='outside',
            textfont=dict(size=12, color='#fff' )
            )
    except:
        bar1=px.line()

    continent=df.groupby('continent').count()['name']
    kolor=[ '#d3d3d3']*len(continent)
    value =year.values[0][16]
    if value == 'Africa':
        kolor[0]='aqua'
    elif value == 'Asia':
        kolor[1]='aqua'
    elif value == 'Europe':
        kolor[2]='aqua'
    elif value == 'North America':
        kolor[3]='aqua'
    elif value == 'Oceania':
        kolor[4]='aqua'
    elif value == 'South America':
        kolor[5]='aqua'
    bar2=px.bar(
    #     data_frame=x,
        y=list(continent.values),
        x=list(continent.index),
    #     orientation='h',
        barmode='group',
        title='Total by Continent',
        height=220,
        text=list(continent.values)
        # template='plotly_dark',
    )
    bar2.update_layout(
        {
    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
    'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    },
        margin=dict(l=0, r=0, t=30, b=10),
    #     xaxis={'categoryorder':'total descending'},
        yaxis_visible=False,
        xaxis_title=None,
        xaxis=dict(
            ticklabelposition='inside',
            color="#fff",
            tickfont=dict(family='Sherif',size=12,)),
        title =  dict(
    #         text ='Facilities By State',
            font =dict(family='Sherif',size=11,color = '#fff'),
    ))
    bar2.update_traces(
        marker_color=kolor,
        textposition='outside',
        textfont=dict(size=12, color='#fff' )
        )

    # try:
    year2 = df[df['year']==2014]

    location=year2.groupby(['alpha', 'location'], as_index=False).count()[['name','alpha', 'location']]

    x=list(location.location)
    position = x.index(year.values[0][10])
    alpha=list(location.alpha)
    val = [np.nan]*len(alpha)
    val[position]=location.loc[9,'name']
    map1 = px.choropleth(locations=alpha,
                color=val, # lifeExp is a column of gapminder
                hover_name=x,
                labels={"name":"count"},
                template='plotly_dark',
                color_continuous_scale='tealgrn',
                # color_discrete_map={'High':'black','Moderate':'aqua','low':'green',},
                # width=600,
                height=300)# column to add to hover information)
    map1.update_traces(showlegend=False, )
    map1.update(layout_coloraxis_showscale=False)
    map1.update_layout(
        {
    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
    'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    },
        margin=dict(l=0, r=0, t=0, b=0))
        
    # except:
    #     map1=px.line()
    print([total_no_uni, scores_overall, scores_teaching_rank, scores_citations,scores_research, stats_pc_intl_students, stats_number_students])
    return total_no_uni, scores_overall, scores_teaching_rank, scores_citations,scores_research, stats_pc_intl_students, stats_number_students , pie1, bar1, bar2, map1, f'{dropdown2}({dropdown1})'
