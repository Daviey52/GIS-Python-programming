#purpose: Generating a raster by Natural Neighbor and creating contours on the raster

import arcpy
from arcpy import env
from arcpy.sa import *

arcpy.env.overwriteOutput=True 
# print (arcpy.env.overwriteOutput)

env.workspace='D:/Lesson3'

#variable defination
in_point_features='D:/Lesson3/WellsSubset.shp'
z_field='ground_ele'

#Checking out Spatial License
arcpy.CheckOutExtension('Spatial')

try:

 #creating a raster by Natural Neighbor interpolation
  print('Natural Neighbor Interpolation starting')

  outNatNbr = NaturalNeighbor (in_point_features, z_field)
  outNatNbr.save('D:/Lesson3/output.tif')

  print('creating raster by natural neighbor complete')
except:
  print('creating raster by natural neighbor failed to run')
arcpy.GetMessageCount()
 
try:

  #Generating Contour by Contour tool
  print ('Contour analysis starting')
  in_raster='D:/Lesson3/output.tif'
  out_polyline_features='D:/Lesson3/outcontours.shp'
  contour_interval=1500
  Contour(in_raster, out_polyline_features, contour_interval )

  print ('Contour analysis complete')
except:
  print('(Creating Contour analysis failed to run')
arcpy.GetMessageCount()
print ('script completed')
#Checking in Spatial License
arcpy.CheckInExtension('Spatial')
