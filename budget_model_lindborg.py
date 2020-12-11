# T. Lindborg et al. / Science of the Total Environment 711 (2020) 134561 
# The basis for this study is a coupled terrestrial-aquatic conceptual
# model where the landscape is divided into pools (e.g., terrestrial
# biota, active layer soils, permafrost soils, water column,
# aquatic biota, lake sediments), which are linked through a number
# of flow paths.
# The carbon data for each pool was then used
# together with information on the volume of each pool (Petrone
# et al., 2016) and hydrological flows (Johansson et al., 2015a,b) to
# construct a simple carbon mass-balance budget for the entire
# catchment. 
# Data :: https://doi.pangaea.de/10.1594/PANGAEA.860961



###### TERRESTRIAL RESERVOIR ######----------------------------------------------------------------------------------
# Total biomass is given in Table 2: [kg C / m2]
biomass_betula = 2.47
biomass_meadow = 0.54
biomass_grass = 0.36
biomass_wetland = 0.91
# Total area is also given in Table 2: [%]
area_betula = 14
area_meadow = 38
area_grass = 20 
area_wetland = 7
# Total litter is also given in Table 2: [kg C / m2]
litter_betula = 1.41
litter_meadow = 1.5
litter_grass = 1.16
litter_wetland = 0.82
# Living below-ground biomass was estimated by assuming a
# constant relationship between below-ground and above-ground
# biomass (2 times for dwarf shrub, and 6 times for meadow and
# dry grassland
# --> root_shoot_type 
root_shoot_betula = 2
root_shoot_meadow = 6
root_shoot_grass = 6
root_shoot_wetland = 6
# For each of the main vegetation types (dwarf shrub = betula, meadow,
# dry grassland and wetland) above-ground and litter biomass were
# determined through destructive sampling
# --> veg_type = [agb, litter] [kg C / m2]
veg_betula = [0,0]
veg_meadow =  [0,0]
veg_grass = [0,0]
veg_wetland = [0,0]
veg_betula[0] = biomass_betula / (root_shoot_betula + 1)
veg_meadow[0] = biomass_meadow / (root_shoot_meadow + 1)
veg_grass[0] = biomass_grass / (root_shoot_grass + 1)
veg_wetland[0] = biomass_wetland / (root_shoot_wetland + 1)
# ROOT CONTENT:
# root content for each of the vegetation types were determined from
# short (12 cm) or long (40–110 cm) soil cores (2–7 per vegetation type).
# roots_vegtype = roots_value [kg C / m2]
roots_betula = 2.23
roots_meadow = 1.52
roots_grass = 0.95
roots_wetland = 1.09
# Below ground biomass 
# --> bgb_type = [bgb, bgb litter]
bgb_betula = [0,0]
bgb_meadow = [0,0]
bgb_grass = [0,0]
bgb_wetland = [0,0]
bgb_betula[0] = veg_betula[0] * root_shoot_betula
bgb_meadow[0] = veg_meadow[0] * root_shoot_meadow
bgb_grass[0] = veg_grass[0] * root_shoot_grass
bgb_wetland[0] = veg_wetland[0] * root_shoot_wetland
# The amount of dead below-ground litter – e.g., dead roots – was
# calculated as the difference between the measured root content
# and the estimated below-ground biomass.
# --> bg_litter 
bgb_betula[1] = roots_betula - bgb_betula[0] 
bgb_meadow [1] = roots_meadow - bgb_meadow[0]
bgb_grass [1] = roots_grass - bgb_grass[0]
bgb_wetland [1] = roots_wetland - bgb_wetland[0]
# Above ground litter from difference: [kg C / m2]
veg_betula[1] = litter_betula - bgb_betula[1]    # or 0.3582 from Table "Terrestrial vegetation and soils.xlsx"
veg_meadow[1] = litter_meadow - bgb_meadow[1]    # or 0.0555 from Table "Terrestrial vegetation and soils.xlsx"
veg_grass[1] = litter_grass - bgb_grass[1]       # or 0.0858 from Table "Terrestrial vegetation and soils.xlsx"
veg_wetland[1] = litter_wetland - bgb_wetland[1] # or 0.0532 from Table "Terrestrial vegetation and soils.xlsx"
# ---------------------------------------------------------------------------------------------------------------

###### AQUATIC RESERVOIR ######----------------------------------------------------------------------------------
# AQUATIC MACROORGANISMS:  [kg C / m2]
benthic_macrophytes = 2.66 / 100
benthic_macro_fauna = 3.24 / 10000
# AQUATIC MICROORGANISMS: [kg C / m3]
benthic_bacteria = 8.83 / 10000
phytoplankton = 3.87 / 100000 
zooplankton = 5.51 / 100000
bacterioplankton = 1.43 / 100000
# LAKE WATER: [kg C / m3]
ic_lake = 1.69 / 100
oc_lake = 8.61 / 1000
# SEDIMENTS: [kg C / m2]
# this gives a total lake sediment carbon pool of
# 3770 tonnes (3030–4500 tonnes) or 10 kg C / m2
# (7.8–12.3 kg C / m2; Table 3).
sediment = 10  
# ---------------------------------------------------------------------------------------------------------------

# SOIL ORGANIC CARBON:
# Soil organic carbon (SOC) for each of the vegetation types were determined from
# short (12 cm) or long (40–110 cm) soil cores (2–7 per vegetation
# type). 
# Active layer and permafrost SOC pools for non-vegetated areas (soc_non_veg) was not measured, 
# instead the SOC pool below 12 cm soil depth for dry grassland, i.e., the most likely
# vegetation type to develop wind erosion scars, have been used.
# soc_vegtype = soc_value [kg C / m2]
soc_betula = 22.1
soc_meadow = 13.3
soc_grass = 10.3
soc_wetland = 18.5
soc_non_veg = 7.05
# PERMAFROST SOIL ORGANIC CARBON:
# Soil organic carbon (SOC) for each of the vegetation types were determined from
# short (12 cm) or long (40–110 cm) soil cores (2–7 per vegetation
# type). 
# psoc_vegtype = soc_value [kg C / m2]
psoc_betula = 11.7
psoc_meadow = 10.1
psoc_grass = 2.8
psoc_wetland = 17.7

# SOIL WATER:
# Soil water samples were collected from lysimeter installations
# in the wetland areas (n = 18),
# soilwater_values = [0:18]
soilwater_values = np.zeros((18))

# STREAM WATER:
# filtered (0.45 lm) and unfiltered surface water was sampled from temporary streams
# flowing into the lake (n = 29; Lindborg et al., 2016a; in 2017 and 2018 only filtered 
# samples were collected).
# streamwater_values = [0:29]
streamwater_values = np.zeros((29))

# --------------------------------------------------------------------------
## FLUXES
# 2.5.1. Atmospheric deposition 
# The only significant input of carbon from the atmosphere at occurs as eolian 
# deposition.
# For the terrestrial system, we assumed that the carbon input
# via eolian deposition equals the eolian erosion.
# ------<process description>------
# 1. The snow TOC concentration was first corrected for sublimation
# 2. The area with snow accumulation was estimated to be 20% of the lake area
# --> 20% of the winter precipitation directly on to the lake was multiplied
# by the corrected old snow TOC concentrations.
# 3. to represent annual eolian deposition, the winter estimate was multiplied by 1.5
# air_to_aqua = eloian deposition on to aquatic system
# air_to_terr = eolian deposition on to terrestrial system
# def get_air_to_lake_oc(lake, precip_winter, toc_snow, expand_factor=1.5):
#     """Get the annual eolian organic carbon deposition on to the lake.
#         Keyword arguments:
#         lake -- the lake object
#         precip_winter -- the winter time precipitation
#         toc_snow -- value or list of TOC  [mg/L]
#         expand_factor -- to expands winter time deposition to the whole year
#     """
#     # -1- Constants:
#     # https://doi.org/10.1016/j.jhydrol.2015.05.026
#     corr_sublimation = 0.63 # 0.63 mm/day
#     corr_lake_snow_area = 0.2

#     toc_snow = toc_snow * corr_sublimation
#     air_to_lake = lake.area * precip_winter * toc_snow
#     air_to_aqua = expand_factor * air_to_aqua 
#     air_to_terr = toc_prec
# For reasons of simplicity currently a fixed value is used
def get_air_to_lake_oc(lake):
    # - It is fair to take this as fixed because we cannot define it better with RS
    # return 0.00199 * lake.area * 1000000
    # which translates to an estimated total input of
    # 750 kg C / yr1 to the aquatic system via eolian deposition.
    return 750 

# Herbivores
def get_grazing():
    return 1.04 * 10000
