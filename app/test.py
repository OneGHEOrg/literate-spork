import pytest, requests, unittest
from main import datetime

# TODO: Figure out how to test service in python 🤦🏼‍♂️

class FlaskTest(unittest.TestCase):
    
    def test_index(self):
        tester = datetime.test_client()
        response = tester.get('/datetime')
        statuscode = response.status_code
        print(statuscode)
        self.assertEqual(statuscode, 200)

if __name__ == "__main__":
    unittest.main()