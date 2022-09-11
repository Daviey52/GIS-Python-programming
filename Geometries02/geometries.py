import arcpy

arcpy.env.overwriteOutput=True

arcpy.env.workspace ="D:/Lesson6_Data"

fc="D:/Lesson6_Data/Cities.shp"
fieldList= ["NAME" ,"SHAPE@XY"]
cipath ='D:/Lesson6_Data/cities.txt'
ciFile = open (cipath, "w")
cursor = arcpy.da.SearchCursor(fc,fieldList)


for row in cursor:
  Name = row [0]
  X,Y = row [1]
  
  ciFile.write(str(Name) + "," + str(X) + "," + str(Y) + "\n")

ciFile.close()

print ('completed')
