class Soil:
    def __init__(self, area, area_bedrock, area_non_veg, area_betula, area_grass, area_meadow, area_wetland, roots_bedrock, roots_non_veg,
    roots_betula, roots_grass, roots_meadow, roots_wetland, soc_active_bedrock, soc_active_non_veg, soc_active_betula, soc_active_grass,
    soc_active_meadow, soc_active_wetland, soc_permafrost_bedrock, soc_permafrost_non_veg, soc_permafrost_betula, soc_permafrost_grass, 
    soc_permafrost_meadow, soc_permafrost_wetland):
        """Create the soil pool.

            Keyword arguments:
            area -- the total area of soil in the catchment [float] unit [m2]
            area_bedrock -- the relative amount of the area of the exposed bedrock [float] unit [%]
            area_non_veg -- the relative amount of the area withouth vegetation [float] unit [%]
            area_betula -- the relative amount of the  area of betula [float] unit [%]
            area_grass -- the relative amount of the area of grass [float] unit [%]
            area_meadow -- the relative amount of the area of meadow [float] unit [%]
            area_wetland -- the relative amount of the area of wetland [float] unit [%]
            soc_active_bedrock -- the soil organic matter found in active soil layer of bedrock [float] unit [kg C / m2]
            soc_active_non_veg -- the soil organic matter found in active soil layer of non vegetation [float] unit [kg C / m2]
            soc_active_betula -- the soil organic matter found in active soil layer of betula vegetation [float] unit [kg C / m2]
            soc_active_grass -- the soil organic matter found in active soil layer of grass vegetation [float] unit [kg C / m2]
            soc_active_meadow -- the soil organic matter found in active soil layer of meadow vegetation [float] unit [kg C / m2]
            soc_active_wetland -- the soil organic matter found in active soil layer of wetland vegetation [float] unit [kg C / m2]
            soc_permafrost_bedrock -- the soil organic matter found in permafrost soil layer of bedrock [float] unit [kg C / m2]
            soc_permafrost_non_veg -- the soil organic matter found in permafrost soil layer of non vegetation [float] unit [kg C / m2]
            soc_permafrost_betula -- the soil organic matter found in permafrost soil layer of betula vegetation [float] unit [kg C / m2]
            soc_permafrost_grass -- the soil organic matter found in permafrost soil layer of grass vegetation [float] unit [kg C / m2]
            soc_permafrost_meadow -- the soil organic matter found in permafrost soil layer of meadow vegetation [float] unit [kg C / m2]
            soc_permafrost_wetland -- the soil organic matter found in permafrost soil layer of wetland vegetation [float] unit [kg C / m2]
       """
        # Area
        self.area = area
        self.area_bedrock = area_bedrock
        self.area_non_veg = area_non_veg
        self.area_betula = area_betula
        self.area_grass = area_grass
        self.area_meadow = area_meadow
        self.area_wetland = area_wetland
        # Roots
        self.roots_bedrock = roots_bedrock
        self.roots_non_veg = roots_non_veg
        self.roots_betula = roots_betula
        self.roots_grass = roots_grass
        self.roots_meadow = roots_meadow
        self.roots_wetland = roots_wetland
        # SOC active
        self.soc_active_bedrock = soc_active_bedrock
        self.soc_active_non_veg = soc_active_non_veg
        self.soc_active_betula = soc_active_betula
        self.soc_active_grass = soc_active_grass
        self.soc_active_meadow = soc_active_meadow
        self.soc_active_wetland = soc_active_wetland
        # SOC permafrost
        self.soc_permafrost_bedrock = soc_permafrost_bedrock
        self.soc_permafrost_non_veg = soc_permafrost_non_veg
        self.soc_permafrost_betula = soc_permafrost_betula
        self.soc_permafrost_grass = soc_permafrost_grass
        self.soc_permafrost_meadow = soc_permafrost_meadow
        self.soc_permafrost_wetland = soc_permafrost_wetland
        # Determine area weighted totals
        self.determine_soc_active()
        self.determine_soc_permafrost()
        # Determine total:
        self.determine_total_soc_active()
        self.determine_total_soc_permafrost()

    def determine_soc_active(self):
        self.soc_active = (((self.area_bedrock/100)*self.soc_active_bedrock) + ((self.area_non_veg/100)*self.soc_active_non_veg) + ((self.area_betula/100)*self.soc_active_betula) 
        + ((self.area_grass/100)*self.soc_active_grass) + ((self.area_meadow/100)*self.soc_active_meadow) + ((self.area_wetland/100)*self.soc_active_wetland))
    
    def determine_soc_permafrost(self):
            self.soc_permafrost = (((self.area_bedrock/100)*self.soc_permafrost_bedrock) + ((self.area_non_veg/100)*self.soc_permafrost_non_veg) + ((self.area_betula/100)*self.soc_permafrost_betula)
            + ((self.area_grass/100)*self.soc_permafrost_grass) + ((self.area_meadow/100)*self.soc_permafrost_meadow) + ((self.area_wetland/100)*self.soc_permafrost_wetland))

    def determine_total_soc_active(self):
        self.soc_active_total = self.soc_active * self.area 

    def determine_total_soc_permafrost(self):
        self.soc_permafrost_total = self.soc_permafrost * self.area


# ------------< FLUXES >----------------------------------------------------------------------------------------
    def set_fluxes(self, respiration, accumulation, active_to_permafrost, active_IC_to_lake, active_OC_to_lake):
        """Define the soil fluxes.

            Keyword arguments:
            soil_respiration -- the amount of carbon removed through soil respiration - lost to atmosphere as CO2 - [float] unit [kg C / m2 a]
            accumulation -- the amount of carbon added to the soil by plants - lost from vegetation -- [float] unit [kg C / m2 a]
            active_to_permafrost -- the amount of carbon incoporated into the permafrost layer from the active layer [float] unit [kg C / m2 a]
            active_IC_to_lake -- the amount of inorganic carbon washed from the active soil layer to the lake [float] unit [kg C / m2 a]
            active_OC_to_lake -- the amount of organic carbon washed from the active soil layer to the lake [float] unit [kg C / m2 a]
        """
        
        # Soil respiration:
        self.respiration = respiration
        self.determine_total_respiration()
        # Active layer C accumulation:
        self.active_layer_accumulation = accumulation
        self.determine_total_active_accumulation()
        # Removal of IC in active layer:
        self.active_IC_to_lake = active_IC_to_lake
        self.determine_total_active_IC_to_lake()
        # Removal of OC in active layer:
        self.active_OC_to_lake = active_OC_to_lake
        self.determine_total_active_OC_to_lake()
        # Permafrost layer C accumulation:
        self.permafrost_layer_accumulation = active_to_permafrost
        self.determine_total_permafrost_accumulation()

    def determine_total_respiration(self):
        self.total_respiration = self.respiration * self.area

    def determine_total_active_accumulation(self):
        self.total_active_layer_accumulation = self.active_layer_accumulation * self.area

    def determine_total_permafrost_accumulation(self):
        self.total_permafrost_layer_accumulation = self.permafrost_layer_accumulation * self.area

    def determine_total_active_IC_to_lake(self):
        self.total_active_IC_to_lake = self.active_IC_to_lake * self.area

    def determine_total_active_OC_to_lake(self):
        self.total_active_OC_to_lake = self.active_OC_to_lake * self.area

    # ------------< Process Functions >----------------------------------------------------------------------------------------
    def do_respiration(self):
        self.soc_active_total -= self.total_respiration
    
    def do_active_layer_accumulation(self):
        self.soc_active_total += self.total_active_layer_accumulation

    def do_permafrost_layer_accumulation(self):
        self.soc_permafrost_total += self.total_permafrost_layer_accumulation

    def do_active_layer_IC_erosion(self):
        self.soc_active_total -= self.total_active_IC_to_lake

    def do_active_layer_OC_erosion(self):
        self.soc_active_total -= self.total_active_OC_to_lake
