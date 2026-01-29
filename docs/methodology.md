# Methodology: Groundwater Potential Mapping

This project demonstrates a GIS-based multi-criteria decision analysis
(MCDA) approach for groundwater potential mapping in a basement terrain
environment.

## Data Preparation
The following thematic layers were prepared in ArcGIS Pro:

- Digital Elevation Model (DEM)
- Slope (derived from DEM)
- Drainage Density
- Lineament Density
- Land Use / Land Cover (LULC)
- Basement Geology

All raster layers were projected to a common coordinate system and
resampled to a consistent spatial resolution.

## Reclassification
Each thematic layer was reclassified into five suitability classes
(1–5) based on hydrogeological reasoning:

- Low slope, low drainage density, and high lineament density were
  assigned higher suitability values.
- Land use classes favoring infiltration received higher ranks.
- Basement geology was treated as a supporting factor.

## Weighted Overlay Analysis
A weighted overlay technique was applied to integrate the reclassified
layers. Weights were assigned based on their relative importance to
groundwater occurrence in basement terrains:

- Lineament density: 30%
- Slope: 25%
- Drainage density: 20%
- LULC: 15%
- Geology: 10%

## Automation
The weighted overlay process was automated using Python (ArcPy),
ensuring reproducibility and scalability of the workflow.

## Output
The final output is a groundwater potential map classified into:
Very Low, Low, Moderate, High, and Very High potential zones.
