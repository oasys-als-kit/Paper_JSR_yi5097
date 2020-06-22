import numpy
from srxraylib.plot.gol import  plot, set_qt
import matplotlib.pylab as plt
from oasys.util.oasys_util import get_fwhm

import matplotlib
set_qt()

labelsize=25
figsize=(12,8)
matplotlib.rc('xtick',         labelsize=labelsize)
matplotlib.rc('ytick',         labelsize=labelsize)
matplotlib.rcParams.update({'font.size': labelsize})

is_fit = True

filename = "grating_profile1D.dat"

a = numpy.loadtxt(filename)
fig = plt.figure(figsize=figsize)
plt.plot(1e3*a[:,0], 1e9*a[:,1],marker="o" )
plt.xlabel("w [mm]")
plt.ylabel("height [nm]")
ax = plt.gca()
ax.ticklabel_format(useOffset=False)
plt.savefig("grating.pdf")
plt.show()


filename = "intensitygrating.txt"

a = numpy.loadtxt(filename)
fig = plt.figure(figsize=figsize)
plt.plot(a[:,0], a[:,1] )
plt.xlabel("X [$\mu$m]")
plt.ylabel("intensity [a.u.]")
ax = plt.gca()
ax.ticklabel_format(useOffset=False)
plt.savefig("intensitygrating.pdf")
plt.show()

print(0.5 * (87.127285+85.659868))
