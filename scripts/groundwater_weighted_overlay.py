"""
Groundwater Potential Mapping using GIS and Python (ArcPy)

This script automates a weighted overlay analysis for groundwater
potential mapping in a basement terrain environment.

Inputs:
- Reclassified slope raster
- Reclassified drainage density raster
- Reclassified lineament density raster
- Reclassified land use/land cover raster
- Reclassified basement geology raster

Output:
- Groundwater potential raster (low to very high)
"""

import arcpy
from arcpy.sa import *

# Check out Spatial Analyst extension
arcpy.CheckOutExtension("Spatial")

# Set workspace
arcpy.env.workspace = r"C:\Users\HomePC\Documents\ArcGIS\Projects\GWP"
arcpy.env.overwriteOutput = True

# Input reclassified rasters
slope = Raster(r"slope\S_Reclass.tif")
drainage = Raster(r"DD\DD_Reclass.tif")
lineament = Raster(r"LD\LD_Reclass.tif")
lulc = Raster(r"lulc\LULC_Reclass.tif")
geology = Raster(r"geology\G_Reclass.tif")
elevation= Raster(r"elevation\E_Reclass.tif")

# Assign weights (percentages)
weighted_sum = (
    (lineament * 0.25) +
    (slope * 0.20) +
    (drainage * 0.20) +
    (lulc * 0.15) +
    (geology * 0.10) +
    (elevation* 0.10)
)

# Save output
output_path = r"Output\groundwater_potential_python.tif"
weighted_sum.save(output_path)

print("Groundwater potential map generated successfully.")
