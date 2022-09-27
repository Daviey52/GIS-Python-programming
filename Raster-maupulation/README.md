# Raster Manupulation

write a script that will assess the degree of risk of groundwater and water pollution
in the given area. To accomplish the task you have four different rasters available: reclassriv, lakebuff,
landusep and rockpor.

The table below shows how the rasters need to be reclassified, and gives a brief description of what the
rasters represent. Once reclassified, multiply all the rasters together. After you perform the raster algebra
clip the result with the ColoradoAreaOfInterest.shp shapefile. The clip is necessary because classifying
some raster values from NoData to a numerical value will fill out the the extent of the area which is bigger
than the actual data coverage.

Areas with the end result of 0 will be bodies of water or areas of high porosity or vicinity to water. The
higher the score the lesser the risk of water pollution.
Raster Description Reclassify Rules
