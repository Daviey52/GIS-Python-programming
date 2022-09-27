import arcpy

# Set input raster
rasterPath = "C:/temp/Lesson7_Data/064CATD.DDF"
inDEM = arcpy.Raster(rasterPath)


# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute HillShade
slopeRaster = arcpy.sa.Slope(inDEM)

# Save the output 
slopeRaster.save("C:/temp/Lesson7_Data/Slope")


#Reclasify the slope raster
remapList = []
remapList.append ([0,5,10])
remapList.append ([5,10,5])
remapList.append ([10,100,0])

remapRangeValues = arcpy.sa.RemapRange(remapList)

slopeReclass = arcpy.sa.Reclassify(slopeRaster, "Value", remapRangeValues, "NODATA")
slopeReclass.save("C:/temp/Lesson7_Data/ReSlope")

#Reclasify the elevation raster
remapList = []
remapList.append ([0,1500,5])
remapList.append ([1500,3000,0])

remapRangeValues = arcpy.sa.RemapRange(remapList)

elevReclass = arcpy.sa.Reclassify(inDEM, "Value", remapRangeValues, "NODATA")
elevReclass.save("C:/temp/Lesson7_Data/ReEleva")


#Map Algebra operation
finalRaster = slopeReclass * elevReclass
finalRaster.save("C:/temp/Lesson7_Data/Final")

arcpy.CheckInExtension("Spatial")
