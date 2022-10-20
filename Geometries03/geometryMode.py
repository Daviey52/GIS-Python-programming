#  Q1

import arcpy

def createFeatureClass(spatialRef, outfolder, fc, fieldName):
    
    arcpy.CreateFeatureclass_management(outfolder, fc, "POLYLINE", "", "", "", spatialRef)
    print ("Created " + fc)

    arcpy.AddField_management(fc, "Name", "TEXT")
    print("Added field: Name")
    
    cursor = arcpy.da.InsertCursor(fc, ["Name", "SHAPE@"])
    print ("insert cursor created")

    return cursor

# Q2

import arcpy

def Createwells(name,pointList,cursor):
    polyline = arcpy.Polyline(pointList)
    cursor.insertRow((name,polyline))
