import arcpy

arcpy.env.workspace='D:/Lesson6_Data'

arcpy.env.overwriteOutput=True

fc='Wellpath.shp'
spatial_reference = arcpy.SpatialReference(26913)
out_folder='D:/Lesson6_Data'
inputPath = r'D:/Lesson6_Data/WellPaths.txt'

inputFile= open(inputPath)


arcpy.CreateFeatureclass_management(out_folder, fc, 'POLYLINE', '', '', '', spatial_reference)

arcpy.AddField_management(fc, "Name", "TEXT")

name =""
pointList=arcpy.Array()

cursor =arcpy.da.InsertCursor(fc,['Name','SHAPE@'])

for line in inputFile:
    lineSegment = line.split(",")

    if name == "":
        name = lineSegment[0]

    if name != lineSegment[0]:
        polyline = arcpy.Polyline(pointList)
        cursor.insertRow((name,polyline))
        name = lineSegment[0];
        pointList = arcpy.Array()
    else:
        point = arcpy.Point(lineSegment[1],lineSegment[2])
        pointList.add(point)

polyline = arcpy.Polyline(pointList)
cursor.insertRow((name,polyline))

del cursor
print ('completed')

