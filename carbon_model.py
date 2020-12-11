# compartments
import box_lake 
import box_soil
import box_vegetation
import box_herbivores
import box_terrestrial
# additional
import numpy as np
import matplotlib.pyplot as plt

def main():
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
    # <2.2> Productivity vascular tissue:
    prod_vasc_betula = 1
    prod_vasc_grass = 3
    prod_vasc_meadow = 3
    prod_vasc_wetland = 2
    # <2.3> Productivity bryophytes:
    prod_bryo = 0.3
    # <2.4> Green AGB [kg C / m2]:
    green_betula = 0.072
    green_grass = 0.028
    green_meadow = 0.044
    green_wetland = 0.018
    # <2.5> Bryophyte AGB [kg C / m2]:
    bryo_betula = 0.157
    bryo_grass = 0
    bryo_meadow = 0.019
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
    soc_permafrost_meadow = 1.1
    soc_permafrost_wetland = 17.7

    # <1> Create the pools:
    # <1.1> Soil:
    res_soil = box_soil.soil(area_bedrock, area_non_veg, area_betula, area_grass, area_meadow, area_wetland,
    0, 0, roots_betula, roots_grass, roots_meadow, roots_wetland, soc_active_bedrock, soc_active_non_veg, soc_active_betula,
    soc_active_grass, soc_active_meadow, soc_active_wetland, soc_permafrost_bedrock, soc_permafrost_non_veg, 
    soc_permafrost_betula, soc_permafrost_grass, soc_permafrost_meadow, soc_permafrost_wetland)
    # <1.2> Vegetation:
    res_veg = box_vegetation.vegetation(area_terr, area_bedrock, area_non_veg, 
    area_betula, area_grass, area_meadow, area_wetland, root_shoot_betula, root_shoot_grass, 
    root_shoot_meadow, root_shoot_wetland, green_betula, green_grass, green_meadow, green_wetland, 
    bryo_betula, bryo_grass, bryo_meadow, bryo_wetland, roots_betula, roots_grass, roots_meadow, 
    roots_wetland, wood_betula, wood_grass, wood_meadow, wood_wetland, agb_litter_betula, agb_litter_grass,
    agb_litter_meadow, agb_litter_wetland, prod_vasc_betula, prod_vasc_grass, prod_vasc_meadow,
    prod_vasc_wetland, prod_bryo_betula, prod_bryo_grass, prod_bryo_meadow, prod_bryo_wetland)
    # <1.3> Lake:
    res_lake = box_lake.lake(lake_area, lake_volume, benthic_macrophytes, benthic_macrofauna, benthic_bacteria, 
    phytoplankton, zooplankton, bacterioplankton, lake_water_IC, lake_water_OC, lake_sediment)
    # <1.4> Herbivores:
    res_animals = box_herbivores.herbivores(herbivore_mass)

    # test
    print(res_veg.total_biomass)

if __name__ == "__main__":
    main()
