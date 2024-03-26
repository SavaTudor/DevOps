from domain.DriverLicense import DriverLicense
from repository.DriverLicenseRepository import DriverLicenseRepository


class Main:
    @staticmethod
    def print(string):
        print("Hello " + string + "!\n")
        driver = DriverLicense(1, "Tudor", "Sava", "B", "29-09-2019", "28-09-2029", False)
        print(driver)


if __name__ == "__main__":
    # Main.print("Tudor")
    repo = DriverLicenseRepository()
    DriverLicenseRepository.read_with_length(repo, 10)


