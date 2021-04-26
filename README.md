# cryptoTask1

## Setup:
Install all required libraries
> pip install -r requirements

## Run Tests:
On the terminal
> python -m unittest -v tests.test_currentweather

## sample output:
>(venv) C:\Users\rishi\PycharmProjects\cryptoTask1>python -m unittest -v tests.test_currentweather
>test_lightningstartendtime (tests.test_currentweather.CurrWeatherTestCase) ... skipped 'Ligh>ting parameter not recieved.'
>test_rainfallstartendtime (tests.test_currentweather.CurrWeatherTestCase)
>Checks Rainfall end time should be after start time ... ok
>test_responseTime (tests.test_currentweather.CurrWeatherTestCase)
>Check API response time ... ok
>test_schema (tests.test_currentweather.CurrWeatherTestCase) ... ok
>test_statusCode (tests.test_currentweather.CurrWeatherTestCase)
>check API response Status Code ... ok
>
>----------------------------------------------------------------------
>Ran 5 tests in 0.608s
>
>OK (skipped=1)

