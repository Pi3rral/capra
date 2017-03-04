from django.shortcuts import render
from django.utils import timezone
import arrow
import numpy as np
import plotly.offline as opy
import plotly.graph_objs as go


def index(request):
    return render(request, 'capra/index.html')


def get_graph(measures, subm, title, color='red'):
    x_date = [m.measured_at
                  .astimezone(timezone.get_current_timezone())
                  .strftime("%Y-%m-%d %H:%M") for m in measures]
    first_ts = measures[0].measured_at.timestamp()
    x_ts = [int(m.measured_at.timestamp() - first_ts) for m in measures]
    v = [getattr(m, subm) for m in measures]

    # calculate polynomial
    z = np.polyfit(x_ts, v, 4)
    f = np.poly1d(z)

    # calculate new x's and y's
    x_new = np.linspace(x_ts[0], x_ts[-1], 100)
    y_new = f(x_new)
    x_new_date = [
        arrow.get(first_ts + ts).datetime
            .astimezone(timezone.get_current_timezone())
            .strftime("%Y-%m-%d %H:%M") for ts in x_new
        ]

    values = go.Scatter(
        x=x_date,
        y=v,
        marker={
            'color': color,
            # 'symbol': 104,
            # 'size': "10"
        },
        mode="markers",
        name=title
    )

    poly = go.Scatter(
        x=x_new_date,
        y=y_new,
        mode='lines',
        marker=go.Marker(color=color),
        name='Fit'
    )

    data = go.Data([values, poly])
    layout = go.Layout(
        title=title,
        xaxis={'title': 'Date'},
        yaxis={'title': title}
    )
    figure = go.Figure(data=data, layout=layout)
    div = opy.plot(figure, auto_open=False, output_type='div')

    return div
