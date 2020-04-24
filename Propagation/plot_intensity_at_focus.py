import numpy
from srxraylib.plot.gol import  plot
import matplotlib.pylab as plt
from oasys.util.oasys_util import get_fwhm

import matplotlib
matplotlib.rc('xtick', labelsize=15)
matplotlib.rc('ytick', labelsize=15)
matplotlib.rcParams.update({'font.size': 15})

filenames = ["UncorrectedOld/intensityundeformed",
             "UncorrectedOld/intensitycryogenic",
             "UncorrectedOld/intensitycryogenicKh",
             "UncorrectedOld/intensitywater1",
             "UncorrectedOld/intensitywater2"]

dirdata = "DirData/"
dirpng = "DirPng/"
filenames = ["intensity0",
             "intensity1",
             "intensity2",
             "intensity3",
             "intensity4", ]

rangex=[75,75,60,60]
rangey=[0.1,0.1,None,None]
# filename = "cryogenic1d.txt"

FWHM = []
STREHL = []

for i,filename in enumerate(filenames):

    a = numpy.loadtxt(dirdata+filename+".txt")
    # if rangey[i] is None:
    #     yrange=None
    # else:
    #     yrange = [-rangey[i],rangey[i]]

    fig = plot(a[:,0],a[:,1],xtitle="X [$\mu$m]",ytitle="intensity [a.u.]",
               figsize=(10,7),show=0) #,xrange=[-rangex[i],rangex[i]],yrange=yrange)
    fig[0].subplots_adjust(bottom=0.15)

    tmp = get_fwhm(a[:, 1], a[:, 0], )
    FWHM.append(tmp[0])
    STREHL.append(a[:,1].max())
    plt.savefig(dirpng+filename+".png")
    print("File %s.png written to file"%filename)
    plt.show()


for i,filename in enumerate(filenames):
    print("%15s    FWHM: %f    STREHL: %f"%(filename,FWHM[i],STREHL[i]/STREHL[0]))