"""
Script to get data from the stock market

# Next steps:

1. Put in alphabetical order the file ../data/list_company_symbols
    - Read all files
    - Split the element using the "\n" character
    - Set the alphabetical order
    - Save and close

2. Get the symbols from this list to use the API Alpha Vantage
    - Based on the list of market actions, give to th user the list of multiples data

3. Make a several analyses (graphs and tables)
    - Based on the action market data, we get the data and we use NumPy, Matplotlib and Pandas to process data

"""
from support.api_key import my_api_key
import requests
from requests import Response
from typing import Union, Literal
import numpy as np
import matplotlib.pyplot as plt


url_base = r'https://www.alphavantage.co/query?'


class TimeSeriesData:
    def __init__(self, action_name: str, time_series: Union[Literal["m", "w", "d"]] = "m", key: str = my_api_key):
        response = self.get_response(action_name=action_name, time_series=time_series, key=key)
        full_data = response.json()['Monthly Time Series']
        self.days = full_data.keys()
        self.open_values = np.array([full_data[date]["1. open"] for date in self.days])
        self.high_values = np.array([full_data[date]["2. high"] for date in self.days])
        self.low_values = np.array([full_data[date]["3. low"] for date in self.days])
        self.close_values = np.array([full_data[date]["4. close"] for date in self.days])
        self.volume = np.array([full_data[date]["5. volume"] for date in self.days])

    @staticmethod
    def get_response(action_name: str,
                     time_series: Union[Literal["m", "w", "d"]] = "m",
                     key: str = my_api_key) -> Response:
        """
        Function to get teh response of the request, using the basics parameters of the API.
        :param action_name : The name of the action to get the data.
        :param time_series : choice the function time that we want to analyse. Per default, we get the data monthly 'm'.
        :param key : the API key. Per default we use the 'my_api_key'.
        :return Return the response of the request.
        """

        if time_series == "m":
            function = "TIME_SERIES_MONTHLY"
        elif time_series == "w":
            function = "TIME_SERIES_WEEKLY"
        elif time_series == "d":
            function = "TIME_SERIES_DAILY"
        else:
            raise ValueError("the 'time_series' have to be : 'm', 'w' or 'd'")

        res = requests.get(url_base + f'function={function}&symbol={action_name}&apikey={key}')

        if res.status_code == 200:
            return res
        else:
            raise ConnectionError("The request was not well done, we could not connect to the server and get the data")


if __name__ == '__main__':
    action = TimeSeriesData("ABEV")
    # op = get_open_values(re)
    a = plt.plot(action.open_values)

    # with open("../data/list_company_symbols", 'r') as file:
    # lines = file.readlines()
    # print(lines)
    # file.close()
