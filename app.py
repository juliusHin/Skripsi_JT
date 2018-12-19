from flask import Flask, Response, render_template, sessions
from services.api import timeseries, timeseries_plotting
import matplotlib.pyplot as plt
import io
import random
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from jinja2 import *


app = Flask(__name__)


@app.route('/')
def hello_world():
    data, meta_data = timeseries_plotting.get_intraday(symbol='ADHI', interval='5min', outputsize='full')
    data['4. close'].plot()
    plt.title('Intraday Time Series for the ADHI stock (5 min)')
    plt.show()
    return


def create_figure():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    xs = range(100)
    ys = [random.randint(1, 50) for x in xs]
    axis.plot(xs, ys)
    return fig

if __name__ == '__main__':
    app.run()
