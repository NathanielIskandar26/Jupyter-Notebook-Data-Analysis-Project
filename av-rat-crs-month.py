import justpy as jp
import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt

df = pandas.read_csv("reviews.csv", parse_dates=['Timestamp'])
df['Month'] = df['Timestamp'].dt.strftime('%Y-%m') #Downsample
month_average_crs = df.groupby(['Month', 'Course Name'])['Rating'].mean('Rating').unstack()

chart_def = """
{
    chart: {
        type: 'spline'
    },
    title: {
        text: 'Average Rating by Course per Month',
    },
    subtitle: {
        text: 'Source: <a href="https://www.udemy.com/course/former-python-mega-course-build-10-real-world-applications/learn/lecture/34362924#content" target="_blank">Ardit Sulce, Udemy</a>',
        align: 'left'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 30,
        y: 100,
        floating: false,
        borderWidth: 1,
        backgroundColor:
            '#FFFFFF'
    },
    xAxis: {
        title: {
            text: 'Date'
        }
    },
    yAxis: {
        title: {
            text: 'Average Rating'
        }
    },
    tooltip: {
        shared: true,
        headerFormat: '<b>Course name and rating in {point.x}</b><br>'
    },
    credits: {
        enabled: false
    },
    plotOptions: {
    },
    series: [{
        name: '',
        data: []
    }, {
        name: '',
        data: []
    }]
}
"""

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
    
    hc = jp.HighCharts(a=wp, options=chart_def)
    hc.options.xAxis.categories = list(month_average_crs.index)
    
    hc_data = [{"name": v1, "data":[v2 for v2 in month_average_crs[v1]]} for v1 in month_average_crs.columns]

    hc.options.series = hc_data

    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis")
    
    return wp
 
jp.justpy(app)