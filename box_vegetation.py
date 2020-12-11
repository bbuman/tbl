class Vegetation:
    def __init__(self, area, area_bedrock, area_non_veg, area_betula, area_grass, area_meadow, area_wetland, root_shoot_betula, root_shoot_grass, root_shoot_meadow, root_shoot_wetland, 
    green_betula, green_grass, green_meadow, green_wetland, bryo_betula, bryo_grass, bryo_meadow, bryo_wetland, roots_betula, roots_grass, roots_meadow, roots_wetland, 
    wood_betula, wood_grass, wood_meadow, wood_wetland, agb_litter_betula, agb_litter_grass, agb_litter_meadow, agb_litter_wetland):
        """Create the vegetation pool.

            Keyword arguments:
            area -- the area for the total catchment [float] unit [m2]
            area_bedrock -- the relative amount of the area of the exposed bedrock [float] unit [%]
            area_non_veg -- the relative amount of the area withouth vegetation [float] unit [%]
            area_betula -- the relative amount of the  area of betula [float] unit [%]
            area_grass -- the relative amount of the area of grass [float] unit [%]
            area_meadow -- the relative amount of the area of meadow [float] unit [%]
            area_wetland -- the relative amount of the area of wetland [float] unit [%]
            root_shoot_betula -- root to shoot ratio for betula [float] unitless
            root_shoot_grass -- root to shoot ratio for grass [float] unitless
            root_shoot_meadow -- root to shoot ratio for meadow [float] unitless
            root_shoot_wetland -- root to shoot ratio for wetland [float] unitless
            green_betula -- the measured vascular green biomass for betula [float] unit [kg C / m2] 
            green_grass -- the measured vascular green biomass for betula [float] unit [kg C / m2]
            green_meadow -- the measured vascular green biomass for betula [float] unit [kg C / m2]
            green_wetland -- the measured vascular green biomass for betula [float] unit [kg C / m2]
            bryo_betula -- the measured bryophytes biomass for betula [flaot] unit [kg C / m2]
            bryo_grass -- the measured bryophytes biomass for grass [flaot] unit [kg C / m2]
            bryo_meadow -- the measured bryophytes biomass for meadow [flaot] unit [kg C / m2]
            bryo_wetland -- the measured bryophytes biomass for wetland [flaot] unit [kg C / m2]
            roots_betula -- the amount of roots in betula vegetation [float] unit [kg C / m2]
            roots_grass -- the amount of roots in grass vegetation [float] unit [kg C / m2]
            roots_meadow -- the amount of roots in meadow vegetation [float] unit [kg C / m2]
            roots_wetland -- the amount of roots in wetland vegetation [float] unit [kg C / m2]
            wood_betula -- the amount of woody tissue in betula vegetation [float] unit [kg C / m2]
            wood_grass -- the amount of woody tissue in grass vegetation [float] unit [kg C / m2]
            wood_meadow -- the amount of woody tissue in meadow vegetation [float] unit [kg C / m2]
            wood_wetland -- the amount of woody tissue in wetland vegetation [float] unit [kg C / m2]
            agb_litter_betula -- the amount of above ground litter for betula vegetation [float] unit [kg C / m2]
            agb_litter_grass -- the amount of above ground litter for grass vegetation [float] unit [kg C / m2]
            agb_litter_meadow -- the amount of above ground litter for meadow vegetation [float] unit [kg C / m2]
            agb_litter_wetland -- the amount of above ground litter for wetland vegetation [float] unit [kg C / m2]

        """
        # Area 
        self.area = area
        self.area_bedrock = area_bedrock
        self.area_non_veg = area_non_veg
        self.area_betula = area_betula
        self.area_grass = area_grass
        self.area_meadow = area_meadow
        self.area_wetland = area_wetland
        # Root:Shoot ratio
        self.root_shoot_betula = root_shoot_betula
        self.root_shoot_grass = root_shoot_grass
        self.root_shoot_meadow = root_shoot_meadow
        self.root_shoot_wetland = root_shoot_wetland
        # Vascular AGB
        self.green_betula = green_betula
        self.green_grass = green_grass
        self.green_meadow = green_meadow
        self.green_wetland = green_wetland
        # Bryophytes AGB
        self.bryo_betula = bryo_betula
        self.bryo_grass = bryo_grass
        self.bryo_meadow = bryo_meadow
        self.bryo_wetland = bryo_wetland
        # Wood AGB
        self.wood_betual = wood_betula
        self.wood_grass = wood_grass
        self.wood_meadow = wood_meadow
        self.wood_wetland = wood_wetland
        # AGB litter
        self.agb_litter_betula = agb_litter_betula
        self.agb_litter_grass = agb_litter_grass
        self.agb_litter_meadow = agb_litter_meadow
        self.agb_litter_wetland = agb_litter_wetland
        # Roots
        self.roots_betula = roots_betula
        self.roots_grass = roots_grass
        self.roots_meadow = roots_meadow
        self.roots_wetland = roots_wetland
        # AGB
        self.determine_agb()
        # BGB
        self.determine_bgb()
        # BGB litter
        self.determine_bgb_litter()
        # Total Biomass
        self.determine_biomass()
        # Total Biomass
        self.determine_total_biomass()

    def determine_agb(self):
        self.agb_betula = self.green_betula + self.bryo_betula + self.wood_betual
        self.agb_grass = self.green_grass + self.bryo_grass + self.wood_grass
        self.agb_meadow = self.green_meadow + self.bryo_meadow + self.wood_meadow
        self.agb_wetland = self.green_wetland + self.bryo_wetland + self.wood_wetland

    def determine_bgb(self):
        self.bgb_betula = self.agb_betula * self.root_shoot_betula
        self.bgb_grass = self.agb_grass * self.root_shoot_grass
        self.bgb_meadow = self.agb_meadow * self.root_shoot_meadow
        self.bgb_wetland = self.agb_wetland * self.root_shoot_wetland

    def determine_bgb_litter(self):
        self.bgb_litter_betula = self.roots_betula - self.bgb_betula
        self.bgb_litter_grass = self.roots_grass - self.bgb_grass
        self.bgb_litter_meadow = self.roots_meadow - self.bgb_meadow
        self.bgb_litter_wetland = self.roots_wetland - self.bgb_wetland

    def determine_biomass(self):
        self.biomass_betula = self.bgb_betula + self.agb_betula
        self.biomass_grass = self.bgb_grass + self.agb_grass
        self.biomass_meadow = self.bgb_meadow + self.agb_meadow
        self.biomass_wetland = self.bgb_wetland + self.agb_wetland

    def determine_total_biomass(self):
        self.area_weighted_agb = ((self.area_betula/100)*self.agb_betula)+((self.area_grass/100)*self.agb_grass)+((self.area_meadow/100)*self.agb_meadow)+((self.area_wetland/100)*self.agb_wetland)
        self.area_weighted_bgb = ((self.area_betula/100)*self.bgb_betula)+((self.area_grass/100)*self.bgb_grass)+((self.area_meadow/100)*self.bgb_meadow)+((self.area_wetland/100)*self.bgb_wetland)
        self.area_weighted_total_biomass = self.area_weighted_agb + self.area_weighted_bgb
        self.total_biomass = self.area_weighted_total_biomass * self.area
    
# ------------< FLUXES >----------------------------------------------------------------------------------------
    def set_fluxes(self, prod_vasc_betula, prod_vasc_grass, prod_vasc_meadow, prod_vasc_wetland, prod_bryo_betula, 
    prod_bryo_grass, prod_bryo_meadow, prod_bryo_wetland, veg_to_soil):
        """ 
            Keyowrd arguments:
            prod_vasc_betula -- the productivity factor for vascular biomass of betula [float] unitless
            prod_vasc_grass -- the productivity factor for vascular biomass of grass [float] unitless
            prod_vasc_meadow -- the productivity factor for vascular biomass of meadow [float] unitless
            prod_vasc_wetland -- the productivity factor for vascular biomass of wetland [float] unitless
            prod_bryo_betula -- the productivity factor for bryophte biomass of betula [float] unitless
            prod_bryo_grass -- the productivity factor for bryophte biomass of grass [float] unitless
            prod_bryo_meadow -- the productivity factor for bryophte biomass of meadow [float] unitless
            prod_bryo_wetland -- the productivity factor for bryophte biomass of wetland [float] unitless
            veg_to_soil -- the amount of carbon removed from the vegetation and added to the soil [float] unit [kg C / m2 a]

        """

        # Productivity vascular
        self.prod_vasc_betula = prod_vasc_betula
        self.prod_vasc_grass = prod_vasc_grass
        self.prod_vasc_meadow = prod_vasc_meadow
        self.prod_vasc_wetland = prod_vasc_wetland
        # Productivity bryophyte
        self.prod_bryo_betula = prod_bryo_betula
        self.prod_bryo_grass = prod_bryo_grass
        self.prod_bryo_meadow = prod_bryo_meadow
        self.prod_bryo_wetland = prod_bryo_wetland
        # NPP
        self.determine_weighted_npp()
        self.determine_total_npp()
        # Export to soil
        self.veg_to_soil = veg_to_soil
        self.determine_total_veg_to_soil()

    def determine_weighted_npp(self):
        self.npp_betula = (self.prod_bryo_betula * self.bryo_betula) + (self.prod_vasc_betula * self.green_betula)
        self.npp_grass = (self.prod_bryo_grass * self.bryo_grass) + (self.prod_vasc_grass * self.green_grass)
        self.npp_meadow = (self.prod_bryo_meadow * self.bryo_meadow) + (self.prod_vasc_meadow * self.green_meadow)
        self.npp_wetland = (self.prod_bryo_wetland * self.bryo_wetland) + (self.prod_vasc_wetland * self.green_wetland)
        self.area_weighted_npp = ((self.area_betula/100)*self.npp_betula)+((self.area_grass/100)*self.npp_grass)+((self.area_meadow/100)*self.npp_meadow)+((self.area_wetland/100)*self.npp_wetland)

    def determine_total_npp(self):
        self.total_npp = self.area_weighted_npp * self.area

    def determine_total_veg_to_soil(self):
        self.total_veg_to_soil = self.veg_to_soil * self.area

    # ------------< Process Functions >----------------------------------------------------------------------------------------
    def import_to_veg(self):
        self.total_biomass += self.total_npp

    def export_to_soil(self):
        self.total_biomass -= self.total_veg_to_soil

    # ------------< Other >----------------------------------------------------------------------------------------
    def alter_productivity_npp(self, prod_bryo, prod_vasc):
        """Altler productivity factors and thus npp.

            Keyword arguments:
            prod_bryo -- productivity factors for bryophyte vegetation, [list], 0=betula, 1=grass, 2=meadow, 3=wetland, unit [unitless]
            prod_vasc -- productivity factors for vascular vegetation, [list], 0=betula, 1=grass, 2=meadow, 3=wetland, unit [unitless]

            Returns:
            npp_new -- the altered NPP

        """

        npp_betula = (prod_bryo[0] * self.bryo_betula) + (prod_vasc[0] * self.green_betula)
        npp_grass = (prod_bryo[1] * self.bryo_grass) + (prod_vasc[1] * self.green_grass)
        npp_meadow = (prod_bryo[2] * self.bryo_meadow) + (prod_vasc[2] * self.green_meadow)
        npp_wetland = (prod_bryo[3] * self.bryo_wetland) + (prod_vasc[3] * self.green_wetland)
        area_weighted_npp = ((self.area_betula/100)*npp_betula)+((self.area_grass/100)*npp_grass)+((self.area_meadow/100)*npp_meadow)+((self.area_wetland/100)*npp_wetland)
        npp = area_weighted_npp * self.area

        return npp
