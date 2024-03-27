from datetime import datetime


class DriverLicense:
    def __init__(self, id, nume, prenume, categorie, dataDeEmitere, dataDeExpirare, suspendat):
        self.id = id
        self.nume = nume
        self.prenume = prenume
        self.categorie = categorie
        self.dataDeEmitere = dataDeEmitere
        self.dataDeExpirare = dataDeExpirare
        self.suspendat = suspendat

    def __str__(self):
        return f'{self.id};{self.nume};{self.prenume};{self.categorie};{self.dataDeEmitere};{self.dataDeExpirare};{self.string_suspendat()}'

    def __repr__(self):
        return str(self)

    def is_valid(self):
        format = "%d/%m/%Y"
        dataDeEmitere_date = datetime.strptime(self.dataDeEmitere.replace('-', '/'), format)
        dataDeExpirare_date = datetime.strptime(self.dataDeExpirare.replace('-', '/'), format)
        if dataDeEmitere_date <= datetime.now().today() <= dataDeExpirare_date:
            return True
        return False

    def string_suspendat(self):
        if self.suspendat:
            return "DA"
        return "NU"


