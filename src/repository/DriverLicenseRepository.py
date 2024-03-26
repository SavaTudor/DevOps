import json
import urllib.request

from src.domain.DriverLicense import DriverLicense


class DriverLicenseRepository:
    def __init__(self):
        self.repository = []
        self.url = "http://localhost:30000/drivers-licenses/list"

    def read_with_length(self, length):
        parameter = f'?length={length}'
        new_url = self.url + parameter
        with urllib.request.urlopen(new_url) as url:
            data = json.load(url)
            self.repository = [DriverLicense(**driver_license) for driver_license in data]
