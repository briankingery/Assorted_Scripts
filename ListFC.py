##
## Brian Kingery
## Aug 26, 2015
##
## List all feature datasets and the feature classes with the fields for each

import arcpy, time, datetime
from arcpy import env

## Target Locations
env.workspace = "Database Connections\Conway_sdeVector_sdeViewer.sde"
env.overwriteOutput = True

ExecutionStartTime = datetime.datetime.now()

file = open(r"C:\Users\bkingery\Desktop\20150826_Conway_FileLog.txt", "w")
print "Started: %s\n" % ExecutionStartTime.strftime('%A, %B %d, %Y %I:%M:%S %p')
print "Processing"
file.write("Started: %s\n\n" % ExecutionStartTime.strftime('%A, %B %d, %Y %I:%M:%S %p'))
file.write("The following is a list of feature datasets and feature classes that are located in " + env.workspace + "\n\n")

fdslist = arcpy.ListDatasets()
fdscount = len(fdslist)

totalfc = 0
for fds in fdslist:
    fds_fclist = arcpy.ListFeatureClasses("","",fds)
    fdsfc_count = len(fds_fclist)
    totalfc += fdsfc_count
file.write("There are " + str(fdscount) + " datasets in the geodatabase with a total of " + str(totalfc) + " feature classes." + "\n\n")

fclist = arcpy.ListFeatureClasses()
fccount = len(fclist)
file.write("There are " + str(fccount) + " feature classes outside of feature datasets." + "\n\n")

## Looking at Datasets and their FCs
file.write("\nThe following are the datasets and their feature classes\n\n")
for fds in fdslist:
    fdsdescribe = arcpy.Describe(fds)
    file.write("Feature Dataset Name: " + fdsdescribe.name + "\n")

    fds_fclist = arcpy.ListFeatureClasses("","",fds)
    for fc in fds_fclist:
        fds_fcdescribe = arcpy.Describe(fc)
        file.write("\tFC Name: " + fds_fcdescribe.name + "\n")#[23:])
        fieldlist = arcpy.ListFields(fc)
        for field in fieldlist:
            file.write("\t\tField Name: " + field.name + "\n")# + "\t" + field.type)

## Looking at FCs outside of Datasets
file.write("\nThe following are feature classes outside of datasets\n\n")
for fc in fclist:
    fc_describe = arcpy.Describe(fc)
    file.write("FC Name: " + fc_describe.name + "\n")
    fieldlist = arcpy.ListFields(fc)
    for field in fieldlist:
        file.write("\tField Name: " + field.name + "\n")# + "\t" + field.type)

#### Loop through the list
##for fc in fclist:
##    ## Create the spatial reference object
##    spatial_ref = arcpy.Describe(fc).spatialReference
##
##    ## If the spatial reference is unknown
##    if spatial_ref.name == "Unknown":
##        print("{0} has an unknown spatial reference".format(fc))
##
##    ## Otherwise, print out the feature class name and spatial reference
##    else:
##        print("{0} : {1}".format(fc, spatial_ref.name))


ExecutionEndTime = datetime.datetime.now()
ElapsedTime = ExecutionEndTime - ExecutionStartTime
print "Ended: %s\n" % ExecutionEndTime.strftime('%A, %B %d, %Y %I:%M:%S %p')
print "Elapsed Time: %s" % str(ElapsedTime).split('.')[0]
file.write("\nEnded: %s\n" % ExecutionEndTime.strftime('%A, %B %d, %Y %I:%M:%S %p'))
file.write("Elapsed Time: %s\n" % str(ElapsedTime).split('.')[0])

file.close()
