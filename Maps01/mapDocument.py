import arcpy
import os
from arcpy.mapping import *

#Q1

arcpy.env.overwriteOutput = True
arcpy.env.workspace = 'D:/Lesson8_Data'
mapDoc = MapDocument('D:/Lesson8_Data/Lesson8.mxd')
dataFrames = ListDataFrames(mapDoc)
dataFrame = dataFrames[0]
countylayer = ListLayers(mapDoc, "COUNTIES",dataFrames[0])
countylayer =Layer('D:/Lesson8_Data/COUNTIES.shp')
pdfpath = "D:/Maps.pdf"
pdfdoc = PDFDocumentCreate(pdfpath)

fieldList = ["COUNTY"]
with arcpy.da.SearchCursor(countylayer, fieldList) as cursor:
    for row in cursor:
        county = row[0]
        
        where_clause = "COUNTY = '" + county + "'"
        arcpy.SelectLayerByAttribute_management(countylayer,"NEW_SELECTION",where_clause)
        dataFrame.extent = countylayer.getSelectedExtent()
        dataFrame.scale = 350000
        titleItem = ListLayoutElements(mapDoc, "TEXT_ELEMENT","title")[0]
        titleItem.text = row [0]
        mapDoc.save
        ExportToPDF(mapDoc,pdfpath,"PAGE_LAYOUT", df_export_width=1200, df_export_height = 800)
        pdfdoc.appendPages("D:/Maps.pdf")
        
        print (county + " Map Created")

pdfdoc.saveAndClose()
del pdfdoc
del mapDoc
print ('completed')

# Q2

dataset = 'D:/Lesson8_Data/NAD83.shp'
mapDoc = MapDocument('D:/Lesson8_Data/Lesson8.mxd')

listdf = ListDataFrames(mapDoc)
for df in listdf:
    print (df.name)

spatialRef =arcpy.Describe(dataset).spatialReference

for df in ListDataFrames(mapDoc):
    df.spatialReference=spatialRef
    
print ('completed')
del mapDoc

            