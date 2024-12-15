import justpy as jp
import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt


df = pandas.read_csv("reviews.csv", parse_dates=['Timestamp'])
df['Day'] = df['Timestamp'].dt.date
day_average = df.groupby(['Day']).mean('Rating')


chart_def = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Average Rating by Day',
    },
    subtitle: {
        text: 'Data According to Ardit Sulce',
    },
    xAxis: {
        title: {
            text: 'Date'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: Day 0 to Day 1187.'
        },
        lineWidth: 2
    },
    yAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Average Rating'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 3.5 to 5.5.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: 'Day: {point.x}, Average: {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Rating per Day',
        data: [
        ]

    }]
}
"""


def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
    hc = jp.HighCharts(a=wp, options=chart_def)

    hc.options.xAxis.categories = list(day_average.index)
    hc.options.series[0].data = list(day_average['Rating'])

    p1 = jp.QDiv(a=wp, text="These graph represents course review analysis")
    return wp
 

jp.justpy(app)