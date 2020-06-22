import requests
import pandas as pd
import numpy as np
from time import time
from bitmex_websocket import BitMEXWebsocket


def request_history(symbol, interval_mins=60, load_periods=500):
    # TODO Allow user to input start and end date.
    # Do calculation to caculate num of load_periods needed for date range.

    end_t = int(time()) + 120 * interval_mins
    end_t -= end_t % (60 * interval_mins)
    start_t = end_t - load_periods * 60 * interval_mins

    baseurl = "https://www.bitmex.com/api"
    url = (
        baseurl
        + f"/udf/history?symbol={symbol}&resolution={interval_mins}&from={start_t}&to={end_t}"
    )
    req = requests.get(url).json()

    df = pd.DataFrame(req)
    # rename headers to something more explicitive
    df.rename(
        {
            "t": "date",
            "c": "close",
            "o": "open",
            "h": "high",
            "l": "low",
            "v": "volume",
        },
        axis=1,
        inplace=True,
    )
    # convert date column from unix time to datetime object
    df["date"] = pd.to_datetime(df["date"], origin="unix", unit="s")
    # add colors to customize volume bar chart
    df["color"] = np.where(df["close"] > df["open"], "green", "red")
    # convert index to datetime object
    df.index = df["date"]

    return df


class TradingChart:
    def __init__(self, symbol):
        df = request_history(symbol=symbol)
        df.head()

        INCREASING_COLOR = "#008000"
        DECREASING_COLOR = "#FF0000"

        data = [
            dict(
                type="candlestick",
                open=df.open,
                high=df.high,
                low=df.low,
                close=df.close,
                x=df.index,
                yaxis="y2",
                name="GS",
                increasing=dict(line=dict(color=INCREASING_COLOR)),
                decreasing=dict(line=dict(color=DECREASING_COLOR)),
            )
        ]

        layout = dict()

        self.fig = dict(data=data, layout=layout)

        self.fig["layout"] = dict()
        self.fig["layout"]["plot_bgcolor"] = "rgb(250, 250, 250)"
        self.fig["layout"]["xaxis"] = dict(rangeselector=dict(visible=True))
        self.fig["layout"]["yaxis"] = dict(
            domain=[0, 0.2], showticklabels=False
        )
        self.fig["layout"]["yaxis2"] = dict(domain=[0.2, 0.8])
        self.fig["layout"]["legend"] = dict(
            orientation="h", y=0.9, x=0.3, yanchor="bottom"
        )
        self.fig["layout"]["margin"] = dict(t=40, b=40, r=40, l=40)

        rangeselector = dict(
            visibe=True,
            x=0,
            y=0.9,
            bgcolor="rgba(150, 200, 250, 0.4)",
            font=dict(size=13),
            buttons=list(
                [
                    dict(count=1, label="reset", step="all"),
                    dict(
                        count=1, label="1yr", step="year", stepmode="backward"
                    ),
                    dict(
                        count=3,
                        label="3 mo",
                        step="month",
                        stepmode="backward",
                    ),
                    dict(
                        count=1,
                        label="1 mo",
                        step="month",
                        stepmode="backward",
                    ),
                    dict(step="all"),
                ]
            ),
        )

        self.fig["layout"]["xaxis"]["rangeselector"] = rangeselector

        def movingaverage(interval, window_size=10):
            window = np.ones(int(window_size)) / float(window_size)
            return np.convolve(interval, window, "same")

        mv_y = movingaverage(df.close)
        mv_x = list(df.index)

        # Clip the ends
        mv_x = mv_x[5:-5]
        mv_y = mv_y[5:-5]

        self.fig["data"].append(
            dict(
                x=mv_x,
                y=mv_y,
                type="scatter",
                mode="lines",
                line=dict(width=1),
                marker=dict(color="#E377C2"),
                yaxis="y2",
                name="Moving Average",
            )
        )

        colors = []

        for i in range(len(df.close)):
            if i != 0:
                if df.close[i] > df.close[i - 1]:
                    colors.append(INCREASING_COLOR)
                else:
                    colors.append(DECREASING_COLOR)
            else:
                colors.append(DECREASING_COLOR)

        self.fig["data"].append(
            dict(
                x=df.index,
                y=df.volume,
                marker=dict(color=colors),
                type="bar",
                yaxis="y",
                name="Volume",
            )
        )

        def bbands(price, window_size=10, num_of_std=5):
            rolling_mean = price.rolling(window=window_size).mean()
            rolling_std = price.rolling(window=window_size).std()
            upper_band = rolling_mean + (rolling_std * num_of_std)
            lower_band = rolling_mean - (rolling_std * num_of_std)
            return rolling_mean, upper_band, lower_band

        bb_avg, bb_upper, bb_lower = bbands(df.close)

        self.fig["data"].append(
            dict(
                x=df.index,
                y=bb_upper,
                type="scatter",
                yaxis="y2",
                line=dict(width=1),
                marker=dict(color="#ccc"),
                hoverinfo="none",
                legendgroup="Bollinger Bands",
                name="Bollinger Bands",
            )
        )

        self.fig["data"].append(
            dict(
                x=df.index,
                y=bb_lower,
                type="scatter",
                yaxis="y2",
                line=dict(width=1),
                marker=dict(color="#ccc"),
                hoverinfo="none",
                legendgroup="Bollinger Bands",
                showlegend=False,
            )
        )

    def get_figure(self):
        return self.fig


def market_depth(symbol):
    # api_key and api_secret is needed for market_depth()
    ws = BitMEXWebsocket(
        endpoint="https://testnet.bitmex.com/api/v1",
        symbol=symbol,
        api_key="9AyrVqTa4HROjUq3FZfIK-p_",
        api_secret="EInjEO0WPdasTM4ne7RHN5Q8aBQ-O6HwhFnY3olm7_LKvSNa",
    )
    return ws.market_depth()
