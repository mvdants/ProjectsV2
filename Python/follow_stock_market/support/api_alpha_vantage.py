"""
Script to get data from the stock market

1. Put in alphabetical order the file ../data/list_company_symbols
    - Read all files
    - Set the alphabetical order
    - Save and close

2. Get the symbols from this list to use the API Alpha Vantage
    - Based on the list of market actions, give to th user the list of multiples data

3. Make a several analyses (graphs and tables)
    - Based on the action market data, we get the data and we use NumPy, Matplotlib and Pandas to process data

# 1| OBS # Are there usage/frequency limits for the API service?  https://www.alphavantage.co/support/
We are pleased to provide free stock API service for our global community of users for up to 5 API requests per minute
and 500 requests per day. If you would like to target a larger API call volume, please visit premium membership.

"""
from support.api_key import my_api_key
import requests
from requests import Response
from typing import Union, Literal
import numpy as np
import matplotlib.pyplot as plt


url_base = r'https://www.alphavantage.co/query?'

symbols_data = "../data/list_company_symbols"


class TimeSeriesData:

    space_time: dict = {
            "t": "Time Series (1min)",
            "d": "Time Series (Daily)",
            "w": "Weekly Time Series",
            "m": "Monthly Time Series"
    }

    def __init__(self, symbol: str,
                 time_series: Union[Literal["m", "w", "d", "t"]] = "m",
                 interval: str = "1min",
                 key: str = my_api_key) -> None:
        """
        Constructor to request an information data from the API Alpha Vantage
        :param symbol: The company symbol to get the information data
        :param time_series: The time series between each request data
        :param key: The API key to use and send the requests
        """
        response = self.get_response(symbol=symbol, time_series=time_series,interval=interval, key=key)
        full_data = response.json()[TimeSeriesData.space_time[time_series]]
        self.days_hour = full_data.keys()
        self.open_values = np.array([full_data[date]["1. open"] for date in self.days_hour])
        self.high_values = np.array([full_data[date]["2. high"] for date in self.days_hour])
        self.low_values = np.array([full_data[date]["3. low"] for date in self.days_hour])
        self.close_values = np.array([full_data[date]["4. close"] for date in self.days_hour])
        self.volume = np.array([full_data[date]["5. volume"] for date in self.days_hour])

    @staticmethod
    def get_response(symbol: str,
                     time_series: Union[Literal["m", "w", "d", "t"]] = "m",
                     interval: str = "1min",
                     key: str = my_api_key) -> Response:
        """
        Function to get the response of the request, using the basics parameters of the API.
        :param symbol : The name of the action to get the data.
        :param time_series : choice the function time that we want to analyse. Per default, we get the data monthly 'm'.
        :param interval : The interval between each data. It is used when 'time_series' == 't' is used.
        :param key : the API key. Per default we use the 'my_api_key'.
        :return Return the response of the request.
        """

        # Verifying which time_series was selected
        if time_series == "m":
            function = "TIME_SERIES_MONTHLY"
        elif time_series == "w":
            function = "TIME_SERIES_WEEKLY"
        elif time_series == "d":
            function = "TIME_SERIES_DAILY"
        elif time_series == "t":
            function = "TIME_SERIES_INTRADAY"
        else:
            raise ValueError("the 'time_series' have to be : 'm', 'w', 'd' or 't'")

        # Verifying if the interval was well informed when we use 'time_series' == 't' is selected
        if time_series == "t":
            if interval:
                res = requests.get(url_base + f'function={function}&symbol={symbol}&interval={interval}&apikey={key}')
            else:
                raise ValueError("The 'interval' parameter is not valid")
        else:
            res = requests.get(url_base + f'function={function}&symbol={symbol}&apikey={key}')

        # Verifying if the status of the request was well done. status code == 200
        if res.status_code == 200:
            return res
        else:
            raise ConnectionError("The request was not well done, we could not connect to the server and get the data")

    @staticmethod
    def set_alphabetical_order_symbols_data() -> None:
        """
        Set in alphabetical order the file "../data/list_company_symbols".
        """
        with open(symbols_data, 'r') as file:
            lines = file.readlines()
            file.close()

        lines.sort()  # Set alphabetical order
        with open("../data/list_company_symbols", "w") as file:
            file.writelines(lines)
            file.close()

    @staticmethod
    def add_symbol_to_data(symbol: Union[str, list]) -> None:
        """Adding a new symbol to the file '../data/list_company_symbols'."""
        with open(symbols_data, 'r') as file:
            lines = file.readlines()
            file.close()

        # Verify if the parameter is symbol is a list or a single string and add to the list
        if isinstance(symbol, str):
            lines.append(symbol + "\n")
        elif isinstance(symbol, list):
            lines.extend([sym + "\n" for sym in symbol if isinstance(sym, str)])

        with open("../data/list_company_symbols", "w") as file:
            file.writelines(lines)
            file.close()

        TimeSeriesData.set_alphabetical_order_symbols_data()  # set alphabetical order before out
