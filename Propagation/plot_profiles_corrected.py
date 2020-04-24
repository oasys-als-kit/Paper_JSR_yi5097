import numpy
from srxraylib.plot.gol import  plot
import matplotlib.pylab as plt
from oasys.util.oasys_util import get_fwhm

import matplotlib
matplotlib.rc('xtick',         labelsize=20)
matplotlib.rc('ytick',         labelsize=20)
matplotlib.rcParams.update({'font.size': 20})

is_fit = 0

dirdata = "DirData/"
dirpng = "DirPng/"

if is_fit == 0:
    filenames = ["correction1",
                 "correction2",
                 "correction3",
                 "correction4",]
    filepng = dirpng + "correctionprofiles.png"
    factor = 1
elif is_fit == 1:
    filenames = ["correction1extrapolated",
                 "correction2extrapolated",
                 "correction3extrapolated",
                 "correction4extrapolated",]
    filepng = dirpng + "correctionprofilesextrapolated.png"
    factor = 1
elif is_fit == 2:
    filenames = ["correction1cropped",
                 "correction2cropped",
                 "correction3cropped",
                 "correction4cropped",]
    filepng = dirpng + "correctionprofilescropped.png"
    factor = 1


X = []
Y = []
LEGEND = []

for i,filename in enumerate(filenames):

    a = numpy.loadtxt(dirdata+filename+".txt")

    X.append(a[:,0])
    Y.append(a[:,1])

    # print(">>>>>>>>>>>>>>>>",dirdata+filename+".txt", a.shape, Y[i].shape, Y[i].min(), Y[i].max())

TITLES = ["cryo H","cryo V","water H","water V"]
for i in range(len(filenames)):
    LEGEND.append("%s "%(TITLES[i]))


fig = plt.figure(figsize=(16,8))

# to avoid plotting zero line
Y[0][ numpy.where(Y[0] == 0) ] = numpy.nan
Y[1][ numpy.where(Y[1] == 0) ] = numpy.nan
Y[2][ numpy.where(Y[2] == 0) ] = numpy.nan
Y[3][ numpy.where(Y[3] == 0) ] = numpy.nan

plt.plot(1e3*X[1-1], factor*1e6*Y[1-1]+0  ,label=LEGEND[1-1], color='blue')
plt.plot(1e3*X[2-1], factor*1e6*Y[2-1]+0  ,label=LEGEND[2-1], color='orange')
plt.plot(1e3*X[3-1], factor*1e6*Y[3-1]+0  ,label=LEGEND[3-1], color='green')
plt.plot(1e3*X[4-1], factor*1e6*Y[4-1]+0  ,label=LEGEND[4-1], color='red')

plt.xlim(-150,150)
plt.ylim(-0.05,0.5)
plt.xlabel("w [mm]")
plt.ylabel("height [$\mu$m]")

ax = plt.subplot(111)
ax.legend(bbox_to_anchor=[.49,.95])

plt.savefig(filepng)
plt.show()