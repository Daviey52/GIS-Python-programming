#Q1

import arcpy
import os
from arcpy.mapping import *

practiceFolder = "C:/Users/Desktop/GISPython/Lesson8_Data/Practice1"
continentsList = os.listdir(practiceFolder)

for continent in continentsList:
    countriesFolder = practiceFolder + "/" + continent
    countriesList = os.listdir(countriesFolder)
    for country in countriesList:
        statesFolder = countriesFolder + "/" + country
        arcpy.env.workspace = statesFolder
        stateList = arcpy.ListFiles()
        for state in stateList:
            #print state
            statePath = statesFolder + "/" + state
            mapDoc = arcpy.mapping.MapDocument(statePath)
            mapDoc.author = "Rossana Grzinic"
            mapDoc.save()
            del mapDoc

#Q2

mxdPath = "C:/Users/Desktop/GISPython/Lesson8_Data/Practice2/Colorado.mxd"
mapDoc = arcpy.mapping.MapDocument(mxdPath)

layerList = ListLayers(mapDoc)

for layer in layerList:
    print (layer, layer.getExtent())

#Q3
mxdPath = "C:/Users/Desktop/GISPython/Lesson8_Data/Practice2/Colorado.mxd"
mapDoc = arcpy.mapping.MapDocument(mxdPath)

brokenSourcesList = ListBrokenDataSources(mapDoc)

for brokenSource in  brokenSourcesList:
    print (brokenSource)

#Q4
mxdPath = "C:/Users/Desktop/GISPython/Lesson8_Data/Practice2/Colorado.mxd"
newMxdPath = "C:/Users/RGrzinic/Desktop/GISPython/Lesson8_Data/Practice2/Colorado1.mxd"
mapDoc = arcpy.mapping.MapDocument(mxdPath)

dataFrames = ListDataFrames(mapDoc)
dataFrame = dataFrames[0]

layerList = ListLayers(mapDoc, "", dataFrame)

for layer in  layerList:
    if layer.isRasterLayer == True:
        layer.visible = False

mapDoc.saveACopy(newMxdPath)

#Q5
mxdPath = "C:/Users/Desktop/GISPython/Lesson8_Data/Practice5/Colorado.mxd"
newMxdPath  = "C:/Users/Desktop/GISPython/Lesson8_Data/Practice5/Colorado1.mxd"

mapDoc = arcpy.mapping.MapDocument(mxdPath)

oldDataPath = "C:/Users/Desktop/GISPython/Lesson8_Data"
newDataPath = "C:/Users/Desktop/GISPython/Lesson8_Data/Practice5/Practice5.gdb"

mapDoc.replaceWorkspaces(oldDataPath, "SHAPEFILE_WORKSPACE", newDataPath, "FILEGDB_WORKSPACE")
mapDoc.saveACopy(newMxdPath)

