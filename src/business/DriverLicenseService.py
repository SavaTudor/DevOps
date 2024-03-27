from src.repository.DriverLicenseRepository import DriverLicenseRepository
from src.util.Utils import Utils


class DriverLicenseService:
    def __init__(self, repository: DriverLicenseRepository):
        self.repository = repository
        self.read(150)

    def read(self, length):
        self.repository.read_with_length(length)

    def get_suspended_licenses(self):
        filtered_list = list(filter(lambda license: license.suspendat, self.repository.repository))
        self.export_licenses_to_excel(filtered_list, "SuspendedLicenses")
        return filtered_list

    def get_valid_licenses(self):
        filtered_list = list(filter(lambda license: license.is_valid(), self.repository.repository))
        self.export_licenses_to_excel(filtered_list, "ValidLicenses")
        return filtered_list

    def get_licenses_by_category(self, category):
        filtered_list = list(filter(lambda license: license.categorie == category, self.repository.repository))
        self.export_licenses_to_excel(filtered_list, "LicensesByCategory-" + category)
        return filtered_list

    def get_count_of_licenses_by_category(self, category):
        return len(self.get_licenses_by_category(category))

    @staticmethod
    def export_licenses_to_excel(list, title):
        Utils.print_list_to_excel(list, title, ["ID", "Nume", "Prenume", "Categorie", "Data De Emitere", "Data De Expirare", "Suspendat"])
