import numpy
from srxraylib.plot.gol import  plot
import matplotlib.pylab as plt

import matplotlib
matplotlib.rc('xtick', labelsize=15)
matplotlib.rc('ytick', labelsize=15)
matplotlib.rcParams.update({'font.size': 15})

dirdata = "DirData/"
dirpng = "DirPng/"

filenames = ["deformation1",
             "deformation2",
             "deformation3",
             "deformation4",]
rangex=[75,75,60,60]
rangey=[0.25,0.25,None,None]
# filename = "cryogenic1d.txt"

for i,filename in enumerate(filenames):

    a = numpy.loadtxt(dirdata+filename+".txt")
    if rangey[i] is None:
        yrange=None
    else:
        yrange = [-rangey[i],rangey[i]]

    fig = plot(1e3*a[:,0],1e6*a[:,1],xtitle="w [mm]",ytitle="height [$\mu$m]",
               xrange=[-rangex[i],rangex[i]],yrange=yrange,
               figsize=(10,7),show=0)
    fig[0].subplots_adjust(bottom=0.15)

    plt.savefig(dirpng+filename+".png")
    print("File %s/%s.png written to file"%(dirpng,filename))
    plt.show()