class Herbivores:
    def __init__(self, area, mass):
        """Create the herbivore pool.

            Keyword arguments:
            area -- the area of the catchment where herbivores reside [float] [m2]
            mass -- the mass of the herbivores in the catchment [float] unit [kg C / m2]
        """
        self.area = area
        self.mass = mass
        ## Biomass
        self.determine_herbivore_biomass()

    def determine_herbivore_biomass(self):
        self.total_biomass = self.mass * self.area


# ------------< FLUXES >----------------------------------------------------------------------------------------
    def set_fluxes(self, grazing):
        """
            grazing -- the amount of grazing [float] unit [kg C / m2 a]

        """

        self.grazing = grazing
        self.determine_grazing_biomass_removal()

    def determine_grazing_biomass_removal(self):
        self.total_grazing = self.grazing + self.area
        
    # ------------< Process Functions >----------------------------------------------------------------------------------------
    def do_grazing(self):
        self.total_biomass += self.total_grazing

    def burn_calories(self):
        self.total_biomass -= self.total_grazing


 
