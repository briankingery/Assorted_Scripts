##ListVersions
##http://pro.arcgis.com/en/pro-app/arcpy/functions/listversions.htm
##
##arcpy.da.ListVersions
##http://pro.arcgis.com/en/pro-app/arcpy/data-access/listversions.htm
##
##Version
##http://pro.arcgis.com/en/pro-app/arcpy/data-access/version.htm

import arcpy, datetime

sdeConnection = r'Database Connections\Conway_sdeVector.sde'

##Gets the list of versions the user has permissions to use and prints them.
for version in arcpy.ListVersions(sdeConnection):
    print version

##Identify all versions in the workspace.
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


##Compare lastModified property of each version to current date, and
##print version name if the version was modified in the last 7 days.
now = datetime.datetime.now()
for version in arcpy.da.ListVersions(sdeConnection):
    if (now - version.lastModified).days < 7:
        print version.name


##Delete any versions owned by "RJones" that don't have any children
for version in arcpy.da.ListVersions(sdeConnection):
    if version.name.split(".")[0] == "RJones" and not version.children:
        print "Deleting version {0}".format(version.name)
        arcpy.DeleteVersion_management(sdeConnection, version.name)
