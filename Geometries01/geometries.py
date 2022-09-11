#####################################################################################################################
#####################################################################################################################
# This script takes in the lease text file and converts it into a shape file
#####################################################################################################################
#####################################################################################################################

import arcpy
# Set up the Environment
arcpy.env.overwriteOutput = True
arcpy.env.workspace = "C:\\temp"


# Set up relevant paths
outFolder = "C:\\temp"
fc = "Leases1.shp"

inputPath = r"C:\Temp\Lesson6_Data\Lesson6_Data\LeasesData.txt"


# Open text file for input
inputFile = open(inputPath)

# Initialize name variable
name = ""

# Start processing text file
for line in inputFile:

    lineSegment = line.split(": ")

    # If line found starts with SpatialReference, meaning it is the first line in the file
    # Create the feature class, add a field to it, open an insert cursor for it and initialize the point array
    if lineSegment[0] == "spatialReference":
        spatRef = arcpy.SpatialReference(int(lineSegment[1]))
        arcpy.CreateFeatureclass_management(outFolder, fc, "POLYGON", "", "", "", spatRef)
        print ("Created feature class ... ")

        arcpy.AddField_management(fc, "Name", "TEXT")
        print ("Added Name field to feature class ...") 
        
        cursor = arcpy.da.InsertCursor(fc, ["Name","SHAPE@"])
        print ("Opened feature class for editing...")

        pointList = arcpy.Array()

    # If the line starts with Name, it is either the first or a new lease polygon
    elif lineSegment[0] == "Name":

        
        # If there are points in the pointList, meaning a set of information for
        # a lease has been read in, add the information to the feature class
        if len(pointList) > 0:
            polygon = arcpy.Polygon(pointList)
            cursor.insertRow((name, polygon))
            print ("Added " + name)
            
        # put the name of the new lease into the name variable and create pointList array
        name = lineSegment[1]
        pointList = arcpy.Array()


    # The line does not start with Name or Spatial Reference, so it has to be a line with
    # coordinates. Therefore we need to split the line with a different delimiter,
    # create a point and added to the array
    else:
        coordinate = line.split(",")
        point = arcpy.Point(coordinate[0], coordinate[1])
        pointList.add(point)

# Add the last record
polygon = arcpy.Polygon(pointList)
cursor.insertRow((name, polygon))
print ("Added " + name)

# data entry is complete, so the cursor needs to be deleted
del cursor


