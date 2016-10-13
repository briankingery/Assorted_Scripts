##ListVersions
##http://pro.arcgis.com/en/pro-app/arcpy/functions/listversions.htm
##
##arcpy.da.ListVersions
##http://pro.arcgis.com/en/pro-app/arcpy/data-access/listversions.htm
##
##Version
##http://pro.arcgis.com/en/pro-app/arcpy/data-access/version.htm

import arcpy

sdeConnection = r'Database Connections\Conway_sdeVector.sde'

for version in arcpy.ListVersions(sdeConnection):
    print version

for version in arcpy.da.ListVersions(sdeConnection):
    print 'name',version.name
    print '\tdescription',version.description
    print '\tcreated',version.created
    print '\tlastModified',version.lastModified
    print '\taccess',version.access
    print '\tisOwner',version.isOwner
    print '\tparentVersionName',version.parentVersionName
    print '\tchildren',str(len(version.children))
    print '\tancestors',str(len(version.ancestors))
