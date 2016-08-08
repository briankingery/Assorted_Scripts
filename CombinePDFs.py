##
## Brian Kingery
## 4/3/2015
##
## This script creates a new PDF by combining existing PDFs. Follow directions located at
## R:\Divisions\InfoTech\Shared\GIS\ArcMapDocs\PDF\Instructions.pdf
##
import arcpy, os, time

print "Script Initiated...\n", time.ctime(),"\n"
## Creates an output directory variable where the script will focus
##
outDir = r"R:\Divisions\InfoTech\Shared\GIS\ArcMapDocs\PDF\Example"
## Creates a new empty pdf document in the specified output directory
## This document does not exist yet and if it does, it will be overwritten
## once the program is ran
finalpdf_filename = outDir + r"\CombinedExample.pdf"
if os.path.exists(finalpdf_filename):
  os.remove(finalpdf_filename)
finalPdf = arcpy.mapping.PDFDocumentCreate(finalpdf_filename) 
## Add the title page to the finalpdf
##
finalPdf.appendPages(r"R:\Divisions\InfoTech\Shared\GIS\ArcMapDocs\PDF\Example\TitlePage.pdf")
## Add the next PDF to the finalpdf keeping the order of the PDFs in consideration
##
finalPdf.appendPages(r"R:\Divisions\InfoTech\Shared\GIS\ArcMapDocs\PDF\Example\Page1.pdf")
## And the next PDF in the correct order
##
finalPdf.appendPages(r"R:\Divisions\InfoTech\Shared\GIS\ArcMapDocs\PDF\Example\Page2.pdf")
finalPdf.appendPages(r"R:\Divisions\InfoTech\Shared\GIS\ArcMapDocs\PDF\Example\Page3.pdf")
finalPdf.appendPages(r"R:\Divisions\InfoTech\Shared\GIS\ArcMapDocs\PDF\Example\Page4.pdf")
finalPdf.appendPages(r"R:\Divisions\InfoTech\Shared\GIS\ArcMapDocs\PDF\Example\Page5.pdf")
##
##
print "Script Complete!\nPlease wait a moment for your new PDF to appear.\n",time.ctime()
