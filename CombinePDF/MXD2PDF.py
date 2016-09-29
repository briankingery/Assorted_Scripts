import arcpy, os, glob

# Folder with MXDs
mxdFolder = arcpy.GetParameterAsText(0)
# Folder where PDFs will be stored
pdfFolder = arcpy.GetParameterAsText(1)

mxdList = glob.glob(mxdFolder + os.sep + '*.mxd')

for mxd in mxdList:
    mapdoc = arcpy.mapping.MapDocument(mxd)
    pdf = mxd.split('\\')[-1][:-3] + 'pdf'
    PDF = pdfFolder + os.sep + pdf
    arcpy.mapping.ExportToPDF(mapdoc, PDF)
