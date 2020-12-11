class Lake:
    def __init__(self, lake_area, lake_volume, benthic_macrophytes, benthic_macrofauna, benthic_bacteria, phytoplankton, 
    zooplankton, bacterioplankton, water_IC, water_OC, sediment):
        """Create the lake pool.

            Keyword arguments:
            lake_area -- area of the lake in the catchment [float] unit [m2]
            lake_volume -- volume of the lake [float] unit [m3]
            benthic_macrophytes -- mass of the benthic macrophyte vegetation [float] unit [kg C / m2]
            benthic_macrofauna -- mass of the benthic macro fauna [float] unit [kg C / m2]
            benthic_bacteria -- mass of the benthic bacteria population [float] unit [kg C / m2]
            phytoplankton -- mass of the phytoplankton community in the water [float] unit [kg C / m3]
            zooplankton -- mass of the zooplankton community in the water [float] unit [kg C / m3]
            bacterioplankton -- mass of the bacterioplankton community in the water [float] unit [kg C / m3]
            water_IC -- mass of the inorganic carbon dissolved in the water [float] unit [kg C / m3]
            water_OC -- mass of the organic carbon dissolved in the water [float] unit [kg C / m3]
            sediment -- mass of the carbon in the sediment [float] unit [kg C / m2]
        """
        ## Geometry
        self.area = lake_area
        self.volume = lake_volume
        ## Organisms
        self.benthic_macrophytes = benthic_macrophytes
        self.benthic_macrofauna = benthic_macrofauna
        self.benthic_bacteria = benthic_bacteria
        self.phytoplankton = phytoplankton
        self.zooplankton = zooplankton
        self.bacterioplankton = bacterioplankton
        ## Dissolved 
        self.water_IC = water_IC
        self.water_OC = water_OC
        ## Sediment
        self.sediment = sediment
        ## Biomass
        self.determine_benthic_macropyhte_biomass()
        self.determine_benthic_macrofauna_biomass()
        self.determine_benthic_bacteria_biomass()
        self.determine_phytoplankton_biomass()
        self.determine_zooplankton_biomass()
        self.determine_bacterioplankton_biomass()
        ## Total IC
        self.determine_total_IC()
        ## Total OC
        self.determine_total_OC()
        ## Total Sediment
        self.determine_sediment_carbon()
        ## Sum up 
        self.determine_total()

    def determine_benthic_macropyhte_biomass(self):
        self.biomass_benthic_macrophyte = self.benthic_macrophytes * self.area
    
    def determine_benthic_macrofauna_biomass(self):
        self.biomass_benthic_macrofauna = self.benthic_macrofauna * self.area

    def determine_benthic_bacteria_biomass(self):
        self.biomass_benthic_bacteria = self.benthic_bacteria * self.area

    def determine_phytoplankton_biomass(self):
        self.biomass_phytoplankton = self.phytoplankton * self.volume

    def determine_zooplankton_biomass(self):
        self.biomass_zooplankton = self.zooplankton * self.volume

    def determine_bacterioplankton_biomass(self):
        self.biomass_bacterioplankton = self.bacterioplankton * self.volume

    def determine_total_IC(self):
        self.total_IC = self.water_IC * self.volume

    def determine_total_OC(self):
        self.total_OC = self.water_OC * self.volume
    
    def determine_sediment_carbon(self):
        self.carbon_sediment = self.sediment * self.area

    def determine_total(self):
        self.total_carbon = (self.biomass_benthic_macrophyte + self.biomass_benthic_macrofauna +
         self.biomass_benthic_bacteria + self.biomass_phytoplankton + self.biomass_zooplankton +
         self.biomass_bacterioplankton + self.total_IC + self.total_OC + self.carbon_sediment)


# ------------< FLUXES >----------------------------------------------------------------------------------------        
    def set_fluxes(self, benthic_npp, benthic_respiration, pelagic_gpp, pelagic_resp_auto, pelagic_resp_hetero, 
    lake_resp_hetero, sediment_accumulation, emission, deposition, lake_water_IC_out, lake_water_OC_out, lake_water_IC_in, lake_water_OC_in):
        """ Define the fluxes in the lake.
            
            Keyword arguments:
            benthic_npp -- the npp for the sediment dwelling organisms [float] unit [kg C / m2 a]
            benthic_respiration -- the respiration of the sediment dwelling organisms [flaot] unit [kg C / m2 a]
            pelagic_gpp -- the gpp of the aquatic producers [float] unit [kg C / m3 a]
            pelagic_resp_auto -- the autotrophic respiration of the aquatic producers [float] unit [kg C / m3 a]
            pelagic_resp_hetero -- the heterotrophic respiration of the aquatic consumers in summer [float] unit [kg C / m3 a]
            lake_resp_hetero -- the heterotrophic respiration of the aquatic consumers in winter [float] unit [kg C / m3 a]
            sediment_accumulation -- the amount of carbon incorporated into sediments [float] unit [kg C / m2 a]
            emission -- the amount of carbon lost to the atmosphere [float] unit [kg C / m2 a]
            deposition -- annual deposition of carbon onto the lake [float] unit [kg C / m2 a]
            lake_water_IC_out -- the amount of inorganic carbon exported from the lake downstream [float] unit [kg C / m3 a]
            lake_water_OC_out -- the amount of organic carbon exported from the lake downstream [float] unit [kg C / m3 a]
            lake_water_IC_in -- the amount of inorganic carbon imported from the catchment [float] unit [kg C / a]
            lake_water_OC_in -- the amount of organic carbon imported from the catchment [float] unit [kg C / a]
        """
        # Benthic NPP
        self.benthic_npp = benthic_npp
        self.determine_total_benthic_npp()
        # Benthic Respiration
        self.benthic_respiration = benthic_respiration
        self.determine_total_benthic_respiration()
        # Pelagic NPP
        self.pelagic_gpp = pelagic_gpp
        self.pelagic_resp_auto = pelagic_resp_auto
        self.pelagic_resp_hetero = pelagic_resp_hetero
        self.lake_resp_hetero = lake_resp_hetero
        self.determine_pelagic_npp()
        self.determine_total_pelagic_npp()
        # Sediment accumulation
        self.sediment_accumulation = sediment_accumulation
        self.determine_total_sedimenet_accumulation()
        # CO2 emission
        self.emission = emission
        self.determine_total_emission()
        # Export
        self.lake_water_IC_out = lake_water_IC_out
        self.determine_total_lake_water_IC_out()
        self.lake_water_OC_out = lake_water_OC_out
        self.determine_total_lake_water_OC_out()
        # Import
        self.total_lake_water_IC_in = lake_water_IC_in
        self.total_lake_water_OC_in = lake_water_OC_in
        # Deposition
        self.deposition = deposition
        self.determine_total_deposition()


    def determine_total_benthic_npp(self):
        self.total_benthic_npp = self.benthic_npp * self.area

    def determine_total_benthic_respiration(self):
        self.total_benthic_respiration = self.benthic_respiration * self.area

    def determine_pelagic_npp(self):
        self.pelagic_npp = self.pelagic_gpp - self.pelagic_resp_auto - self.pelagic_resp_hetero - self.lake_resp_hetero

    def determine_total_pelagic_npp(self):
        self.total_pelagic_npp = self.pelagic_npp * self.area

    def determine_total_sedimenet_accumulation(self):
        self.total_sediment_accumulation = self.sediment_accumulation * self.area

    def determine_total_emission(self):
        self.total_emission = self.emission * self.area

    def determine_total_lake_water_IC_out(self):
        self.total_lake_water_IC_out = self.lake_water_IC_out * self.volume

    def determine_total_lake_water_OC_out(self):
        self.total_lake_water_OC_out = self.lake_water_OC_out * self.volume
    
    def determine_total_deposition(self):
        self.total_deposition = self.deposition * self.area
        
    # ------------< Process Functions >----------------------------------------------------------------------------------------
    def export_IC_downstream(self):
        self.total_IC -= self.total_lake_water_IC_out
    
    def export_OC_downstream(self):
        self.total_OC -= self.total_lake_water_OC_out

    def lake_to_atmo(self):
        self.total_IC -= self.total_emission

    def import_IC(self):
        self.total_IC += self.total_lake_water_IC_in

    def import_OC(self):
        self.total_OC += self.total_lake_water_OC_in

    def atmo_to_lake(self):
        self.total_OC += self.total_deposition

    def lake_production(self):
        self.total_OC += self.total_benthic_npp 
        self.total_OC -= self.total_benthic_respiration
        self.total_OC += self.pelagic_npp

    def sediment_incorporation(self):
        self.carbon_sediment += self.total_sediment_accumulation
        self.total_OC -= self.total_sediment_accumulation

    def update_total_carbon(self):
        self.determine_total()