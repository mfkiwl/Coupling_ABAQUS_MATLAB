# -*- coding: mbcs -*-
#
# Abaqus/Viewer Release 6.13-1 replay file
# Internal Version: 2013_05_16-04.28.56 126354
# Run by p4wp4w on Tue Feb 09 16:47:32 2016
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
o2 = session.openOdb(name='openloop_step.odb')
#: Model: C:/Temp/OPEN LOOP/openloop_step.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     3
#: Number of Meshes:             3
#: Number of Element Sets:       9
#: Number of Node Sets:          30
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o2)
odb = session.odbs['C:/Temp/OPEN LOOP/openloop_step.odb']
xy1 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Electrical potential: EPOT PI: SENSOR-1 Node 1 in NSET SENSOR_POINT_1', 
    steps=('Step-1', ), suppressQuery=True)
c1 = session.Curve(xyData=xy1)
xy2 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Electrical potential: EPOT PI: SENSOR-1 Node 2 in NSET SENSOR_POINT_2', 
    steps=('Step-1', ), suppressQuery=True)
c2 = session.Curve(xyData=xy2)
xy3 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Electrical potential: EPOT PI: SENSOR-1 Node 3 in NSET SENSOR_POINT_3', 
    steps=('Step-1', ), suppressQuery=True)
c3 = session.Curve(xyData=xy3)
xy4 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Electrical potential: EPOT PI: SENSOR-1 Node 7 in NSET SENSOR_POINT_4', 
    steps=('Step-1', ), suppressQuery=True)
c4 = session.Curve(xyData=xy4)
xy5 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Electrical potential: EPOT PI: SENSOR-1 Node 8 in NSET SENSOR_POINT_5', 
    steps=('Step-1', ), suppressQuery=True)
c5 = session.Curve(xyData=xy5)
xy6 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Electrical potential: EPOT PI: SENSOR-1 Node 9 in NSET SENSOR_POINT_6', 
    steps=('Step-1', ), suppressQuery=True)
c6 = session.Curve(xyData=xy6)
xy7 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Electrical potential: EPOT PI: SENSOR-1 Node 13 in NSET SENSOR_POINT_7', 
    steps=('Step-1', ), suppressQuery=True)
c7 = session.Curve(xyData=xy7)
xy8 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Electrical potential: EPOT PI: SENSOR-1 Node 14 in NSET SENSOR_POINT_8', 
    steps=('Step-1', ), suppressQuery=True)
c8 = session.Curve(xyData=xy8)
xy9 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Electrical potential: EPOT PI: SENSOR-1 Node 15 in NSET SENSOR_POINT_9', 
    steps=('Step-1', ), suppressQuery=True)
c9 = session.Curve(xyData=xy9)
xy10 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Electrical potential: EPOT PI: SENSOR-1 Node 19 in NSET SENSOR_POINT_10', 
    steps=('Step-1', ), suppressQuery=True)
c10 = session.Curve(xyData=xy10)
xy11 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Electrical potential: EPOT PI: SENSOR-1 Node 20 in NSET SENSOR_POINT_11', 
    steps=('Step-1', ), suppressQuery=True)
c11 = session.Curve(xyData=xy11)
xy12 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Electrical potential: EPOT PI: SENSOR-1 Node 21 in NSET SENSOR_POINT_12', 
    steps=('Step-1', ), suppressQuery=True)
c12 = session.Curve(xyData=xy12)
xy13 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Electrical potential: EPOT PI: SENSOR-1 Node 25 in NSET SENSOR_POINT_13', 
    steps=('Step-1', ), suppressQuery=True)
c13 = session.Curve(xyData=xy13)
xy14 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Electrical potential: EPOT PI: SENSOR-1 Node 26 in NSET SENSOR_POINT_14', 
    steps=('Step-1', ), suppressQuery=True)
c14 = session.Curve(xyData=xy14)
xy15 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Electrical potential: EPOT PI: SENSOR-1 Node 27 in NSET SENSOR_POINT_15', 
    steps=('Step-1', ), suppressQuery=True)
c15 = session.Curve(xyData=xy15)
xy16 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Electrical potential: EPOT PI: SENSOR-1 Node 31 in NSET SENSOR_POINT_16', 
    steps=('Step-1', ), suppressQuery=True)
c16 = session.Curve(xyData=xy16)
xy17 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Electrical potential: EPOT PI: SENSOR-1 Node 32 in NSET SENSOR_POINT_17', 
    steps=('Step-1', ), suppressQuery=True)
c17 = session.Curve(xyData=xy17)
xy18 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Electrical potential: EPOT PI: SENSOR-1 Node 33 in NSET SENSOR_POINT_18', 
    steps=('Step-1', ), suppressQuery=False)
c18 = session.Curve(xyData=xy18)
xyp = session.XYPlot('XYPlot-1')
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
chart.setValues(curvesToPlot=(c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, 
    c12, c13, c14, c15, c16, c17, c18, ), )
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
session.xyPlots[session.viewports['Viewport: 1'].displayedObject.name].setValues(
    transform=(0.815304, 0, 0, -0.35737, 0, 0.815304, 0, 0.212265, 0, 0, 
    0.815304, 0, 0, 0, 0, 1))
odb = session.odbs['C:/Temp/OPEN LOOP/openloop_step.odb']
xy1 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Electrical potential: EPOT PI: SENSOR-1 Node 1 in NSET SENSOR_POINT_1', 
    steps=('Step-1', ), )
c1 = session.Curve(xyData=xy1)
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
chart.setValues(curvesToPlot=(c1, ), )
session.xyPlots[session.viewports['Viewport: 1'].displayedObject.name].setValues(
    transform=(0.825836, 0, 0, -0.0391465, 0, 0.825836, 0, 0.0506166, 0, 0, 
    0.825836, 0, 0, 0, 0, 1))
odb = session.odbs['C:/Temp/OPEN LOOP/openloop_step.odb']
xy1 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Spatial displacement: U2 PI: CYLINDER-1 Node 26 in NSET SET-1', 
    steps=('Step-1', ), )
c1 = session.Curve(xyData=xy1)
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
chart.setValues(curvesToPlot=(c1, ), )
odb = session.odbs['C:/Temp/OPEN LOOP/openloop_step.odb']
xy1 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Electrical potential: EPOT PI: PIEZO-1 Node 244 in NSET ACTUATOR_POINT1', 
    steps=('Step-1', ), )
c1 = session.Curve(xyData=xy1)
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
chart.setValues(curvesToPlot=(c1, ), )
