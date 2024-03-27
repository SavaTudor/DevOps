from src.business.DriverLicenseService import DriverLicenseService


class CommandLineInterface:
    def __init__(self, service: DriverLicenseService):
        self._service = service
        print("Welcome to the Fictional Driving License Authority of Cluj")

    def print_menu(self):
        print("Select your option: ")
        print("1. List of suspended licenses")
        print("2. List of valid licenses")
        print("3. Licenses based on category")
        print("0. Exit")

    def start(self):
        self.print_menu()
        option = input(":")
        while option != '0':
            if option == '1':
                result_list = self._service.get_suspended_licenses()
                print(result_list)
            elif option == '2':
                result_list = self._service.get_valid_licenses()
                print(result_list)
            elif option == '3':
                category = input("Enter the category: ")
                print(self._service.get_count_of_licenses_by_category(category))
                print("The licenses are displayed in the Excel Report")
            else:
                print("The given options is invalid!")
            self.print_menu()
            option = input(":")
