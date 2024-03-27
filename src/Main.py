from repository.DriverLicenseRepository import DriverLicenseRepository
from business.DriverLicenseService import DriverLicenseService
from src.presentation.CommandLineInterface import CommandLineInterface


class Main:
    if __name__ == "__main__":
        repo = DriverLicenseRepository()
        service = DriverLicenseService(repo)
        interface = CommandLineInterface(service)
        interface.start()


