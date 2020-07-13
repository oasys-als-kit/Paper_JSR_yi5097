import numpy
from srxraylib.plot.gol import  plot, set_qt
import matplotlib.pylab as plt

set_qt()
import matplotlib
labelsize=25
figsize=(11,7)
matplotlib.rc('xtick', labelsize=labelsize)
matplotlib.rc('ytick', labelsize=labelsize)
matplotlib.rcParams.update({'font.size': labelsize})

dirdata = "DirData/"
dirpng = "DirFigures/"

filenames = ["deformation1",
             "deformation2",
             "deformation3",
             "deformation4",]
rangex=[75,75,60,60]
rangey=[0.25,0.25,None,None]
# filename = "cryogenic1d.txt"

RMS_VALUES = []
for i,filename in enumerate(filenames):

    a = numpy.loadtxt(dirdata+filename+".txt")
    if rangey[i] is None:
        yrange=None
    else:
        yrange = [-rangey[i],rangey[i]]

    fig = plot(1e3*a[:,0],1e6*a[:,1],xtitle="w [mm]",ytitle="height [$\mu$m]",
               xrange=[-rangex[i],rangex[i]],yrange=yrange,
               figsize=figsize,show=0)
    fig[0].subplots_adjust(bottom=0.15)

    plt.savefig(dirpng+filename+".pdf")
    print("File %s/%s.pdf written to file"%(dirpng,filename))
    plt.show()

    nn = a[:,1].size
    tmp = 1e9*a[(nn//2):,1].copy()
    print(tmp.shape,nn)
    # plot(numpy.arange(tmp.size),tmp)
    rms = numpy.zeros_like(tmp)
    for j in range(tmp.size):
        rms[j] = tmp[0:j].std()
    plot(numpy.arange(tmp.size),rms)
    RMS_VALUES.append(rms[-1])
    print(">>>>>",rms.shape,rms[-1])

print("RMS values: ",RMS_VALUES)

