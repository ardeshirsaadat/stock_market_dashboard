from numpy import rad2deg
import pandas as pd
import plotly.graph_objs as go
from wrangling_scripts.get_data import get_stock_info


# Use this file to read in your data and prepare the plotly visualizations. The path to the data files are in
# `data/file_name.csv`

def return_figures():
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """

    # first chart plots arable land from 1990 to 2015 in top 10 economies 
    # as a line chart
    ticker_df=get_stock_info()
    ticker_df['month']=ticker_df.index.month

    graph_one = []    
    graph_one.append(
      go.Scatter(
      x = ticker_df.index,
      y = ticker_df.Open,
      mode = 'lines'
      )
    )

    layout_one = dict(title = 'Microsoft open stock price',
                xaxis = dict(title = 'Date'),
                yaxis = dict(title = 'Open Price($)'),
                )

# second chart plots ararble land for 2015 as a bar chart    
    graph_two = []
    
    trade_volume_df=ticker_df.groupby('month')['Volume'].sum().reset_index()
    graph_two.append(
      go.Bar(
      x = trade_volume_df.month,
      y = trade_volume_df.Volume,
      )
    )

    layout_two = dict(title = 'Monthley Volume Trading',
                xaxis = dict(title = 'Month',),
                yaxis = dict(title = 'Volume($)'),
                )


# third chart plots percent of population that is rural from 1990 to 2015
    graph_three = []
    graph_three.append(
      go.Scatter(
      x = [5, 4, 3, 2, 1, 0],
      y = [0, 2, 4, 6, 8, 10],
      mode = 'lines'
      )
    )

    layout_three = dict(title = 'Chart Three',
                xaxis = dict(title = 'x-axis label'),
                yaxis = dict(title = 'y-axis label')
                       )
    
# fourth chart shows rural population vs arable land
    graph_four = []
    
    graph_four.append(
      go.Scatter(
      x = [20, 40, 60, 80],
      y = [10, 20, 30, 40],
      mode = 'markers'
      )
    )

    layout_four = dict(title = 'Chart Four',
                xaxis = dict(title = 'x-axis label'),
                yaxis = dict(title = 'y-axis label'),
                )
    
    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))

    return figures