import pandas as pd
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt
import justpy as jp

df = pd.read_csv('stocks/GOOG.csv', parse_dates=['Date'])
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Month'] = df['Date'].dt.strftime('%Y-%m')
month_average = df.groupby(['Month']).mean('Open')

chart_def = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Average Open Value by Month',
    },
    subtitle: {
        text: 'Source: <a href="https://www.kaggle.com/datasets/adhoppin/financial-data" target="_blank">NEURALNERD, Kaggle</a>',
        align: 'left'
    },
    xAxis: {
        title: {
            text: 'Date (YYYY-MM)'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 2004-08 - 2023-05.'
        },
        lineWidth: 2
    },
    yAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Open Value (in USD)'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 200.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: 'Month {point.x}, Average Value: {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Average Open Value per Month',
        data: []
    }]
}
"""


def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Google's Stock Open Value Chart", classes="text-h3 text-center q-pa-md")
    hc = jp.HighCharts(a=wp, options=chart_def)

    hc.options.xAxis.categories = list(month_average.index)
    hc.options.series[0].data = list(month_average['Open'])

    p1 = jp.QDiv(a=wp, text="This graph represents google stock monthly open value analysis")
    return wp
 

jp.justpy(app)