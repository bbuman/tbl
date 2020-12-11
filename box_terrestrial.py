class terrestrial:

    def __init__(self, area, vegetation, soil, herbivores):
        self.area = area
        self.veg = vegetation
        self.soil = soil
        self.herbivores = herbivores
        self.determine_npp()
        self.determine_soc_active()
        self.determine_soc_permafrost()
        self.determine_grazing()
        self.sum_up()

    def determine_npp(self):
        self.npp = self.area * self.veg.area_weighted_npp

    def determine_soc_active(self):
        self.soc_active = self.area * self.soil.soc_active

    def determine_soc_permafrost(self):
        self.soc_permafrost = self.area * self.soil.soc_permafrost

    def determine_grazing(self):
        self.grazing = self.area * self.herbivores.grazing 

    def sum_up():
        self.total = self.npp + self.soc_active + self.soc_permafrost + self.grazing