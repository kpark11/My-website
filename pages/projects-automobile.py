# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 17:10:33 2023

@author: brian
"""

import dash
from dash import html, dcc, callback
import pandas as pd
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import plotly.express as px




dash.register_page(__name__)



# Load the data using pandas
data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv')




# Create the dropdown menu options
dropdown_options = [
    {'label': 'Yearly Statistics', 'value': 'Yearly Statistics'},
    {'label': 'Recession Period Statistics', 'value': 'Recession Period Statistics'}
]
# List of years 
year_list = [i for i in range(1980, 2024, 1)]
#---------------------------------------------------------------------------------------



SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

layout = html.Div([
    #TASK 2.1 Add title to the dashboard
    html.H2("Automobile Statistics Dashboard",style={'textAlign': 'center', 'color': '#FF8903'}),#May include style for title
    html.P("This is from the Coursera exercise.",style={'textAlign':'center'}),
    html.P("You can visualize automobile statistics by yearly or during recession",style={'textAlign':'center'}),
    html.P("For recession period, you do not need to select a year.",style={'textAlign':'center'}),

    html.Div([#TASK 2.2: Add two dropdown menus
        html.Label("Select Statistics:"),
        dcc.Dropdown(
            id='dropdown-statistics',
            options=[{'label': 'Yearly Statistics', 'value': 'Yearly Statistics'},
                    {'label': 'Recession Period Statistics', 'value': 'Recession Period Statistics'}
                           ],
            value='Select Statistics',
            placeholder='Select a report type'
        )
                      ]),
    html.Div(dcc.Dropdown(
            id='select-year',
            options=[{'label': i, 'value': i} for i in year_list],
            value='Yearly Statistics',
            placeholder='Select Years'
        )),
    #html.Div([
            dcc.Loading(id="output-loading-1",
                children=[html.Div(id='output-container1', className='chart-grid', 
             style={'display':'flex'}),
                          html.Div(id='output-container2', className='chart-grid', 
             style={'display':'flex'})],
            type="circle")
     #]),
],
    style={"overflow": "scroll"})
#TASK 2.4: Creating Callbacks
# Define the callback function to update the input container based on the selected statistics




#Callback for plotting
# Define the callback function to update the input container based on the selected statistics
@callback(
    Output(component_id='output-loading-1', component_property='children'),
    [Input(component_id='dropdown-statistics', component_property='value'), Input(component_id='select-year', component_property='value')]
)


def update_output_container(selected_statistics, input_year):
    if selected_statistics == 'Recession Period Statistics':
        # Filter the data for recession periods
        recession_data = data[data['Recession'] == 1]
        
#TASK 2.5: Creating Graphs for Recession data

#Plot 1 Automobile sales fluctuate over Recession Period (year wise)
        # use groupby to create relevant data for plotting
        yearly_rec=recession_data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        R_chart1 = dcc.Graph(
            figure=px.line(yearly_rec, 
                x='Year',
                y='Automobile_Sales',
                title="Average Automobile Sales Fluctuation over Recession Period"))


#Plot 2 Calculate the average number of vehicles sold by vehicle type       
        # use groupby to create relevant data for plotting
        average_sales = recession_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()    
        R_chart2  = dcc.Graph(figure=px.pie(average_sales,
                    values='Automobile_Sales',
                 names='Vehicle_Type',
                 title="Average Number of Vehicles Sold by Vehicle Type"))
        
# Plot 3 Pie chart for total expenditure share by vehicle type during recessions
        # use groupby to create relevant data for plotting
        exp_rec= recession_data.groupby('Vehicle_Type')['Advertising_Expenditure'].mean().reset_index()
        R_chart3 = dcc.Graph(figure=px.pie(exp_rec,
                    values='Advertising_Expenditure',
                    names='Vehicle_Type',
                  title="Total Expenditure Share by Vehicle Type during Recessions"))

# Plot 4 bar chart for the effect of unemployment rate on vehicle type and sales
        unemp_rate = recession_data.groupby(['Vehicle_Type','unemployment_rate'])['Automobile_Sales'].mean().reset_index()
        R_chart4 = dcc.Graph(figure=px.bar(unemp_rate,
                            x='Vehicle_Type',
                          y='Automobile_Sales',
                          title='The effect of unemployment rate on Vehicle Type and Sales'))

#TASK 2.6: Returning the graphs for displaying Recession data
        return [
            html.Div(className='chart-item', 
                     children=[html.Div(children=R_chart1),html.Div(children=R_chart2)],
                     style={'display': 'flex',}),
            html.Div(className='chart-item', 
                     children=[html.Div(children=R_chart3),html.Div(children=R_chart4)],
                     style={'display': 'flex',})
            ]
 # Yearly Statistic Report Plots                             
    elif (input_year and selected_statistics=='Yearly Statistics'):
        yearly_data = data[data['Year'] == input_year]
                              
#TASK 2.5: Creating Graphs Yearly data
                              
#plot 1 Yearly Automobile sales using line chart for the whole period.
        yas= data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        Y_chart1 = dcc.Graph(figure=px.line(yas, 
                x='Year',
                y='Automobile_Sales',
                title="Average Automobile Sales Fluctuation for The Whole Period"))
# Plot 2 Total Monthly Automobile sales using line chart.
        mas= data.groupby('Month')['Automobile_Sales'].mean().reset_index()
        Y_chart2 = dcc.Graph(figure=px.line(mas, 
                x='Month',
                y='Automobile_Sales',
                title="Average Automobile Sales Fluctuation in Monhts"))
        
            # Plot bar chart for average number of vehicles sold during the given year
        yearly_data = data[data['Year']==input_year]
        avr_vdata=yearly_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
        Y_chart3 = dcc.Graph( figure=px.pie(avr_vdata,
                values='Automobile_Sales',
                names='Vehicle_Type',
                title='Average Vehicles Sold by Vehicle Type in the year {}'.format(input_year)))

            # Total Advertisement Expenditure for each vehicle using pie chart
        exp_data=yearly_data.groupby('Vehicle_Type')['Advertising_Expenditure'].mean().reset_index()
        Y_chart4 = dcc.Graph(figure=px.pie(exp_data,
                values='Advertising_Expenditure',
                names='Vehicle_Type',
                title='Total Advertisement Expenditure for Each Vehicle'))

#TASK 2.6: Returning the graphs for displaying Yearly data
        return [
                html.Div(className='chart-item', children=[html.Div(Y_chart1),html.Div(Y_chart2)],
                         style={'display': 'flex'}),
                html.Div(className='chart-item', children=[html.Div(Y_chart3),html.Div(Y_chart4)],
                         style={'display': 'flex'})
                ]
        
    else:
        return None