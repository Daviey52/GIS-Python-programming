import arcpy

arcpy.env.overwriteOutput=True

arcpy.env.workspace='D:/Lesson5_Data'
#Variables
County='COUNTIES.shp'
Wells='Wells.shp'

fieldList= ["COUNTY" ,"NoWells", "SHAPE_Area", "DENSITY"]

arcpy.MakeFeatureLayer_management(Wells,'Well_layer')

with arcpy.da.SearchCursor(County, fieldList) as cursor:
    for row in cursor:
        county = row[0]

        where_clause = "COUNTY = '" + county + "'"
        arcpy.MakeFeatureLayer_management(County,'County_layer',where_clause)
        arcpy.SelectLayerByLocation_management ('Well_layer', 'WITHIN','County_layer', '', 'NEW_SELECTION')
        WellCount= int (arcpy.GetCount_management('Well_layer').getOutput(0))

        print (county + ' Wells within are '  + str(WellCount))

with arcpy.da.UpdateCursor(County, fieldList) as cursor:
    for row in cursor:

        WellCount=row[1]
        cursor.updateRow(row)


        density=row[1]/row[2] 
        print (row[0] +  ' well density is ' + str(density))
        density=row[3]
        cursor.updateRow(row)
del row
del cursor
