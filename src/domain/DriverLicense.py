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
        return f'{self.id},{self.nume},{self.prenume},{self.categorie},{self.dataDeEmitere},{self.dataDeExpirare},{self.suspendat}\n'

    def __repr__(self):
        return str(self)

