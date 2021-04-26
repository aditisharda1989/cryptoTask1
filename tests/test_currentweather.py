import unittest
from .support import API
from .support.assertions import assert_valid_schema


class CurrWeatherTestCase(unittest.TestCase):

    def test_statusCode(self):
        """check API response Status Code"""
        statusCode = API.getCurrentWeatherReport().status_code
        self.assertEqual(statusCode, 200, "Status code is not 200")

    def test_responseTime(self):
        """Check API response time"""
        responseTime = API.getCurrentWeatherReport().elapsed.total_seconds()
        self.assertLessEqual(responseTime, API.expectedResponseTime,
                             "response time is more than %s ms" % API.expectedResponseTime)

    def test_schema(self):
        """
        Validate API Schema:
        Make sure all required(mandatory) parameters are returned
        No extra/invalid/additional parameters are returned
        each parameter has correct data type
        each parameter has valid values and formats
        Also checks UV Index only returns results during day and should be blank during Night
        """
        response = API.getCurrentWeatherReport()
        assert_valid_schema(response.json(), "currentweatherschema.json")

    def test_rainfallstartendtime(self):
        """Checks Rainfall end time should be after start time"""
        rainfall = API.getCurrentWeatherParameter("rainfall")
        starttime = rainfall["startTime"]
        endtime = rainfall["endTime"]
        self.assertGreater(endtime, starttime, "Rainfall end time is greater that start time")

    def test_lightningstartendtime(self):
        """
        This test is skipped when Lightning parameter is not returned
        Checks Lighting end time should be after start time
        """
        try:
            lightning = API.getCurrentWeatherParameter("lightning")
        except:
            self.skipTest("Lighting parameter not recieved.")
        starttime = lightning["startTime"]
        endtime = lightning["endTime"]
        self.assertGreater(endtime, starttime, "lightning end time is greater that start time")


if __name__ == '__main__':
    unittest.main(verbosity=2)
