from flask import Flask, Response, render_template, sessions, request, Request, jsonify
# from services.api import timeseries, timeseries_plotting, timeseries_csv
# import matplotlib.pyplot as plt
# import io
# import random
# from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
# from matplotlib.figure import Figure
# from jinja2 import *
import pandas
from alpha_vantage.timeseries import TimeSeries



app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/searchstock', methods=['GET', 'POST'])
def searchstock():
    search = request.args.get('searchstock')
    app.logger.debug(search)

    return jsonify()



# def create_figure():
#     fig = Figure()
#     axis = fig.add_subplot(1, 1, 1)
#     xs = range(100)
#     ys = [random.randint(1, 50) for x in xs]
#     axis.plot(xs, ys)
#     return fig

# def plotSlider():
#     import plotly.plotly as plt
#     import plotly.graph_objs as graphObj
#     from datetime import datetime
#
#     df= pandas.read_csv(timeseries_csv)
#     print(df)
#     # print(meta_data)


if __name__ == '__main__':
    app.run()
