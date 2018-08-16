#Dependencies
import NewMultiAVR
import DRTMultiAVR
import plotGraphs
import sys

#Input Args
runsPerMode = sys.argv[1]

#Run NewAlg for Mode count 6 through 15
for r in runsPerMode:
    NewMultiAVR.NewMultiAVRgen()

#Run DRT Alg for Mode count 6 through 15
for r in runsPerMode:
    for i in range(6,16):
        DRTMultiAVR.DRTMultiAVRgen(i)

#Compare Graphs
plotGraphs.multiAVRPlot()