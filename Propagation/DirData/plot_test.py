from srxraylib.plot.gol import plot
import numpy

a1 = numpy.loadtxt("correction1cropped.txt")
a2 = numpy.loadtxt("correction2cropped.txt")
a3 = numpy.loadtxt("correction3cropped.txt")
a4 = numpy.loadtxt("correction4cropped.txt")

print(">>>>>>>>>>>>>>>>",a4.shape, a4[:,1].min(), a4[:,1].max())

plot(a1[:,0],1e6*a1[:,1],
     a2[:,0],1e6*a2[:,1],
     a3[:,0],1e6*a3[:,1],
     a4[:,0],1e6*a4[:,1],
     yrange=[-.1,0.5])