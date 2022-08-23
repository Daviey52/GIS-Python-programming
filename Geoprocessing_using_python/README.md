# Geoprocessing using python

Write a Python script that uses the WellsSubset shapefile from the Lesson3_Data folder to generate a raster using the Natural Neighbor interpolation.  Once the raster is created use the Contour tool with 1500 as the contour interval, to generate the contour of the resulting raster.

Note that both the Natural Neighbor and Contour tools are a part of the Spatial Analyst extension.  When using ArcGIS extensions in your scripts, it is always a good idea to check out and check in the extension in question.   That way you are not tying the license up any longer than necessary. In order to do so you need to use the CheckOutExtension function of arcpy.  To check the extension back in to the license manager you would use the CheckInExtension function.
