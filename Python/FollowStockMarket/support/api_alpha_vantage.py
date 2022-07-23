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

3. Based on
#

"""
import requests


my_api_key = "3Z4LYGVHLWQAXG1N"  # api key


def get_data(action_name: str, key: str = my_api_key):
    url_base = r'https://www.alphavantage.co/query?'
    url_target = url_base + f'function=TIME_SERIES_DAILY&symbol={action_name}&interval=5min&apikey={key}'
    r = requests.get(url_target)
    if r.status_code == 200:
        print(r.url)
        return r.json()


if __name__ == '__main__':
    data = get_data(action_name="ABEV")
    with open("../data/list_company_symbols", 'r') as file:
        lines = file.readlines()
        print(lines)
        file.close()
