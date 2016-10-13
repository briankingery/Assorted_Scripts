##
## Brian Kingery
## Aug 28, 2015
##
## List all feature datasets and the feature classes with the fields for each

import arcpy, time, datetime, string
from arcpy import env

## Target Locations
env.workspace = "Database Connections\Conway_sdeVector_sdeViewer.sde"
env.overwriteOutput = True

ExecutionStartTime = datetime.datetime.now()

## Get name of dataset by using timestamp as title
timesnapshot = time.ctime()
time_str = str(timesnapshot)
time_list = string.split(time_str)
month       = time_list[1]
day         = time_list[2]
year        = time_list[4]
date = str(year+month+day)

filename = date +"_Conway_FileLog.txt"
file = open("C:/Users/bkingery/Desktop/" + filename, "w")
print "Started: %s\n" % ExecutionStartTime.strftime('%A, %B %d, %Y %I:%M:%S %p')
print "Processing"
file.write("Started: %s\n\n" % ExecutionStartTime.strftime('%A, %B %d, %Y %I:%M:%S %p'))
file.write("The following is a list of feature datasets and feature classes that are located in " + env.workspace + "\n\n")

dataset_list = arcpy.ListDatasets()
dataset_count = len(dataset_list)

totalfc     = 0
point       = 0
polyline    = 0
polygon     = 0
for dataset in dataset_list:
    fclist = arcpy.ListFeatureClasses("","",dataset)
    for fc in fclist:
        fc_describe = arcpy.Describe(fc)
        if fc_describe.shapeType == "Point":
            point += 1
        if fc_describe.shapeType == "Polyline":
            polyline += 1
        if fc_describe.shapeType == "Polygon":
            polygon += 1
    fc_count = len(fclist)
    totalfc += fc_count
file.write("There are " + str(dataset_count) + " datasets in the geodatabase with a total of " + str(totalfc) + " feature classes." + "\n\n")
file.write("Points       = " + str(point) + "\n")
file.write("Polylines    = " + str(polyline) + "\n")
file.write("Polygons     = " + str(polygon) + "\n")
print "There are " + str(dataset_count) + " datasets in the geodatabase with a total of " + str(totalfc) + " feature classes." + "\n\n"
print "Points       = " + str(point)
print "Polylines    = " + str(polyline)
print "Polygons     = " + str(polygon)
    
fclist = arcpy.ListFeatureClasses()
fc_count = len(fclist)
point       = 0
polyline    = 0
polygon     = 0
for fc in fclist:
    fc_describe = arcpy.Describe(fc)
    if fc_describe.shapeType == "Point":
        point += 1
    if fc_describe.shapeType == "Polyline":
        polyline += 1
    if fc_describe.shapeType == "Polygon":
        polygon += 1
file.write("There are " + str(fc_count) + " feature classes outside of feature datasets." + "\n\n")
file.write("Points       = " + str(point) + "\n")
file.write("Polylines    = " + str(polyline) + "\n")
file.write("Polygons     = " + str(polygon) + "\n")
print "There are " + str(fc_count) + " feature classes outside of feature datasets." + "\n\n"
print "Points       = " + str(point)
print "Polylines    = " + str(polyline)
print "Polygons     = " + str(polygon)

## Looking at Datasets and their FCs
file.write("\nThe following are the datasets and their feature classes\n\n")
for dataset in dataset_list:
    datasetdescribe = arcpy.Describe(dataset)
    file.write("Feature Dataset Name: " + datasetdescribe.name + "\n")

    fclist = arcpy.ListFeatureClasses("","",dataset)
    for fc in fclist:
        dataset_fcdescribe = arcpy.Describe(fc)
        file.write("\tFC Name: " + dataset_fcdescribe.name + "\n")#[23:])
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

ExecutionEndTime = datetime.datetime.now()
ElapsedTime = ExecutionEndTime - ExecutionStartTime
print "Ended: %s\n" % ExecutionEndTime.strftime('%A, %B %d, %Y %I:%M:%S %p')
print "Elapsed Time: %s" % str(ElapsedTime).split('.')[0]
file.write("\nEnded: %s\n" % ExecutionEndTime.strftime('%A, %B %d, %Y %I:%M:%S %p'))
file.write("Elapsed Time: %s\n" % str(ElapsedTime).split('.')[0])

file.close()








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
