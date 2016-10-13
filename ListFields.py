# -*- coding: utf-8 -*-

import arcpy

##hydrantFC = r'C:\GIS\OperationalSystems\Locations\Waterworks BaseMap\Data\Databases\sdeVectorFrequent.mdb\WaterUtility\v_Hydrant_EAM'
##items = ()
##hydrantdict = []
##with arcpy.da.SearchCursor(hydrantFC, ['HYDRANT_NO']) as cursor:
##    for row in cursor:
##        items+=row
##for x in sorted(items):
##    hydrantdict.append(x)
##print hydrantdict


##dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
##
##print "dict['Name']: ", dict['Name']
##print "dict['Age']: ", dict['Age']
##
##When the above code is executed, it produces the following result −
##
##dict['Name']:  Zara
##dict['Age']:  7


ADCgridFC   = r'C:\GIS\OperationalSystems\Locations\Waterworks BaseMap\Data\Databases\sdeVectorInfrequent.mdb\Reference\ADCVirginiaPeninsulaGridArea'
streetFC    = r'C:\GIS\OperationalSystems\Locations\Waterworks BaseMap\Data\Databases\sdeVectorFrequent.mdb\Transportation\Road'
hydrantFC   = r'C:\GIS\OperationalSystems\Locations\Waterworks BaseMap\Data\Databases\sdeVectorFrequent.mdb\WaterUtility\v_Hydrant_EAM'
valvesFC    = r'C:\GIS\OperationalSystems\Locations\Waterworks BaseMap\Data\Databases\sdeVectorFrequent.mdb\WaterUtility\v_SystemValve_EAM'
metersFC    = r'C:\GIS\OperationalSystems\Locations\Waterworks BaseMap\Data\Databases\sdeVectorFrequent.mdb\WaterUtility\v_wServiceLocation_EAM'
#listFC      = (ADCgridFC,streetFC,hydrantFC,valvesFC,metersFC)

CHOICE = "Meters"

def listFields(selection):
    dict = {'ADC Grid': ADCgridFC, 'Street': streetFC, 'Hydrants': hydrantFC, 'Valves': valvesFC, 'Meters': metersFC}
    fc = dict[selection]
    fieldlist = arcpy.ListFields(fc)
    for field in fieldlist:
        desc = arcpy.Describe(field)
        print desc.name

listFields(CHOICE)




##    fieldlist = arcpy.ListFields(fc)
##    for field in fieldlist:
##        file.write("\tField Name: " + field.name + "\n")# + "\t" + field.type)    
##        


##
##for x in listFC:
##    desc = arcpy.Describe(x)
##    print desc.name



