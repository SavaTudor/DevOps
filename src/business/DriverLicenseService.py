from src.repository.DriverLicenseRepository import DriverLicenseRepository

class DriverLicenseService:
    def __init__(self, repository: DriverLicenseRepository):
        self.repository = repository

