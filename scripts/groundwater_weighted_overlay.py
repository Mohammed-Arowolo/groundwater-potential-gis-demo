import arcpy
from arcpy.sa import *

# Check out Spatial Analyst extension
arcpy.CheckOutExtension("Spatial")

# Set workspace
arcpy.env.workspace = r"C:\Users\HomePC\Documents\ArcGIS\Projects\GWP"
arcpy.env.overwriteOutput = True

# Input reclassified rasters
slope = Raster(r"slope\slope_reclass.tif")
drainage = Raster(r"drainage density\dd_reclass.tif")
lineament = Raster(r"lineament density\ld_reclass.tif")
lulc = Raster(r"LULC\lulc_reclass.tif")
geology = Raster(r"geology\geology_reclass.tif")

# Assign weights (percentages)
weighted_sum = (
    (lineament * 0.30) +
    (slope * 0.25) +
    (drainage * 0.20) +
    (lulc * 0.15) +
    (geology * 0.10)
)

# Save output
output_path = r"outputs\groundwater_potential_python.tif"
weighted_sum.save(output_path)

print("Groundwater potential map generated successfully.")
