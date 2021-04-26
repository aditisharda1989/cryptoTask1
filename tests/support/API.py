import requests

url = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=en"
expectedResponseTime = 0.5  # expected response time in seconds


def getCurrentWeatherReport():
    """:return  API response"""
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    return response


def getCurrentWeatherParameter(parameter):
    """ :param API paramenter
        :return API response for the requested parameter"""
    response = getCurrentWeatherReport()
    param = response.json()[parameter]
    return param
