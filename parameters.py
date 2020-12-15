def define_state_parameters(self):
    # <1> Geometrical:
    # <1.1> Convert from km2 to m2
    km2_to_m2 = 1000000
    # <1.2> Total catchment area:
    area_catchment = 1.56 * km2_to_m2 
    # <1.3> Terrestrial area:
    area_terr = 1.18 * km2_to_m2 
    # <1.4> Different terrestrial features [%]:
    area_bedrock = 7
    area_non_veg = 15
    area_betula = 14
    area_grass = 20
    area_meadow = 38
    area_wetland = 7
    # <1.5> Aquatic area:
    area_lake = 0.38 * km2_to_m2
    # <1.6> Different aquatic features:
    area_lake_above16 = 0.22 * km2_to_m2
    area_lake_below16 = 0.16 * km2_to_m2
    # <1.7> Aquatic volume [m3]:
    volume_lake = 4250000 
    # <1.8> Different volume features:
    volume_above14 = 3178000
    volume_below14 = 1072000
    # <1.9> Aquatic depth [m]:
    depth_max_lake = 29.9
    depth_mean_lake = 11.3

    # <2> Biophysical parameterization:
    # <2.1> Root to shoot ratio:
    root_shoot_betula = 2
    root_shoot_grass = 6
    root_shoot_meadow = 6
    root_shoot_wetland = 6
    # <2.4> Green AGB [kg C / m2]:
    green_betula = 0.072
    green_grass = 0.051
    green_meadow = 0.044
    green_wetland = 0.018
    # <2.5> Bryophyte AGB [kg C / m2]:
    bryo_betula = 0.0833  # old = 0.157; old2 = 0.0715
    bryo_grass = 0
    bryo_meadow = 0.0134
    bryo_wetland = 0.091
    # <2.6> Litter AGB [kg C / m2]:
    agb_litter_betula = 0.931
    agb_litter_grass = 0.285
    agb_litter_meadow = 0.495
    agb_litter_wetland = 0.576
    # <2.7> Wood AGB [kg C / m2]:
    wood_betula = 0.786
    wood_grass = 0
    wood_meadow = 0
    wood_wetland = 0.039
    # <2.8> Roots [kg C / m2]:
    roots_betula = 2.230
    roots_grass = 0.950
    roots_meadow = 1.520
    roots_wetland = 1.090
    # <2.9> Benthic organisms [kg C / m2]:
    # <2.9.1> Macrophytes:
    benthic_macrophytes = 0.0878
    # <2.9.2> Macro Fauna:
    benthic_macrofauna = 0.000324
    # <2.9.3> Bacteria:
    benthic_bacteria = 0.000883
    # <2.10> Aquatic organisms [kg C / m3]:
    # <2.10.1> Phytoplankton:
    phytoplankton = 0.0000289
    # <2.10.2> Zooplankton:
    zooplankton = 0.0000412
    # <2.10.3> Bacterioplankton:
    bacterioplankton = 0.0000143
    # <2.11> Water dissolved carbon [kg C / m3]:
    # <2.11.1> Inorganic carbon:
    lake_water_IC = 0.0169
    # <2.11.2> Organic carbon:
    lake_water_OC = 0.00861
    # <2.12> Lake sediment carbon [kg C / m2]:
    lake_sediment = 10
    # <2.13> Herbivore mass [kg C / m2]
    herbivore_mass = 0.000872

    # <3> Geochemical parameterization:
    # <3.1> SOC active layer:
    soc_active_bedrock = 0
    soc_active_non_veg = 7.05
    soc_active_betula = 22.1
    soc_active_grass = 10.3
    soc_active_meadow = 13.3
    soc_active_wetland = 18.5
    # <3.2> SOC permafrost layer:
    soc_permafrost_bedrock = 0
    soc_permafrost_non_veg = 2.85
    soc_permafrost_betula = 11.7
    soc_permafrost_grass = 2.8
    soc_permafrost_meadow = 10.1
    soc_permafrost_wetland = 17.7

def define_flux_parameters(self):
    # <2> Define the fluxes:
    # <2.1> Vegetation
    # <2.1.1> Productivity vascular tissue:
    prod_vasc_betula = 1
    prod_vasc_grass = 3
    prod_vasc_meadow = 3
    prod_vasc_wetland = 2
    # <2.1.2> Productivity bryophytes:
    prod_bryo_betula = 0.3
    prod_bryo_grass = 0.3
    prod_bryo_meadow = 0.3
    prod_bryo_wetland = 0.3
    # <2.1.3> Flux of NPP to SOC layer [kg C / m2 a]:
    veg_to_soil = 0.138 

    # <2.2> Soil
    # <2.2.1> Input:
    soil_accumulation = veg_to_soil
    # <2.2.2> Respiration:
    soil_respiration = 0.13
    # <2.2.3> Export to Permafrost:
    active_layer_2_permafrost = 0.00294
    # <2.2.4> Export to Lake:
    active_layer_OC_2_lake = 0.00136 + 0.00126 # non-spring + spring
    active_layer_IC_2_lake = 0.00827

    # <2.3> Herbivores:
    # <2.3.1> Input / output:
    grazing = 0.00884

    # <2.4> Lake:
    # <2.4.1> Input:
    benthic_npp = 0.00389
    pelagic_gpp = 0.00274
    lake_water_IC_in = active_layer_IC_2_lake
    lake_water_OC_in = active_layer_OC_2_lake
    # <2.4.2> Eolian deposition:
    lake_deposition = 0.00199
    # <2.4.3> Respiration:
    benthic_respiration = 0.00364
    pelagic_resp_auto = 0.000997
    pelagic_resp_hetero = 0.000572 # lake Rh summer
    lake_resp_hetero = 0.000477 # lake Rh winter
    # <2.4.4> Sediment incorporation:
    sediment_accumulation = 0.00257
    # <2.4.5> Export via runoff:
    lake_water_IC_out = 0.0000574
    lake_water_OC_out = 0.0000293
    # <2.4.6> Export to atmosphere:
    lake_emission = 0.00379

if __name__ == "__main__":
    self.define_state_parameters()
    self.define_flux_parameters()

    # # <2.1.4> Set vegetation fluxes:
    # vegetation.set_fluxes(prod_vasc_betula, prod_vasc_grass, prod_vasc_meadow,
    # prod_vasc_wetland, prod_bryo_betula, prod_bryo_grass, prod_bryo_meadow, prod_bryo_wetland, veg_to_soil)
    # # <2.2.5> Set soil fluxes:
    # soil.set_fluxes(soil_respiration, soil_accumulation, active_layer_2_permafrost, active_layer_IC_2_lake, active_layer_OC_2_lake) 
    # # <2.3.2> Set herbivore fluxes:
    # herbivore.set_fluxes(grazing)
    # # <2.4.6> Set lake fluxes:
    # lake.set_fluxes(benthic_npp, benthic_respiration, pelagic_gpp, pelagic_resp_auto, pelagic_resp_hetero, lake_resp_hetero, sediment_accumulation, lake_emission, lake_deposition, lake_water_IC_out, lake_water_OC_out, lake_water_IC_in, lake_water_OC_in)

