# -*- coding: mbcs -*-
#
# Abaqus/Viewer Release 6.13-1 replay file
# Internal Version: 2013_05_16-04.28.56 126354
# Run by p4wp4w on Tue Feb 09 19:23:04 2016
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
#: Abaqus Error: 
#: This error may have occurred due to a change to the Abaqus Scripting
#: Interface. Please see the Abaqus Scripting Manual for the details of
#: these changes. Also see the "Example environment files" section of 
#: the Abaqus Site Guide for up-to-date examples of common tasks in the
#: environment file.
#: Execution of "onCaeGraphicsStartup()" in the site directory failed.
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=271.731781005859, 
    height=208.144454956055)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from viewerModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
o2 = session.openOdb(name='SS_F.odb')
#: Model: C:/Temp/SSF/SS_F.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     3
#: Number of Meshes:             3
#: Number of Element Sets:       9
#: Number of Node Sets:          30
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o2)
session.viewports['Viewport: 1'].odbDisplay.basicOptions.setValues(
    numericForm=COMPLEX_MAGNITUDE)
odb = session.odbs['C:/Temp/SSF/SS_F.odb']
xy1 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Electrical potential: EPOT PI: SENSOR-1 Node 1 in NSET SENSOR_POINT_1', 
    steps=('Step-1', ), )
c1 = session.Curve(xyData=xy1)
xyp = session.XYPlot('XYPlot-1')
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
chart.setValues(curvesToPlot=(c1, ), )
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
session.viewports['Viewport: 1'].odbDisplay.basicOptions.setValues(
    numericForm=COMPLEX_PHASE)
odb = session.odbs['C:/Temp/SSF/SS_F.odb']
xy1 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Electrical potential: EPOT PI: SENSOR-1 Node 1 in NSET SENSOR_POINT_1', 
    steps=('Step-1', ), )
c1 = session.Curve(xyData=xy1)
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
chart.setValues(curvesToPlot=(c1, ), )
