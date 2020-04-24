from srxraylib.plot.gol import plot
import matplotlib.pylab as plt
import numpy


import matplotlib
matplotlib.rc('xtick',         labelsize=20)
matplotlib.rc('ytick',         labelsize=20)
matplotlib.rcParams.update({'font.size': 20})


# ap = numpy.loadtxt( "flexon_ken_memo2_factor1_fit.dat", skiprows=1)


photon_energy1 = 230.888
photon_energy2 = 1250


am = numpy.loadtxt("scan_peak_vs_cos.txt", skiprows=0)
amC = numpy.loadtxt("scan_peak_vs_cos_corrected.txt", skiprows=0)
# numpy.loadtxt("scan_peak_vs_sin_corrected.txt", skiprows=0) #
amR = numpy.loadtxt("scan_peak_vs_cos_cropped_new.txt", skiprows=0)
amE = numpy.loadtxt("scan_peak_vs_cos_extrapolated_new.txt", skiprows=0)

fm =    plot(am[:,0],   am[:,1] / 212.6,
             amC[:,0], amC[:,1] / 212.6,
             # amC10[:, 0], amC10[:, 1] / 212.6,
             amR[:,0], amR[:,1] / 212.6,
             amE[:,0], amE[:,1] / 212.6,
             xlog=False,figsize=(12,8),
             legend=["Uncorrected               ",
                     "Corrected (ideal)         ",
                     # "Corrected (ideal 10)         ",
                     "Corrected (cropped)       ",
                     "Corrected (extrapolated)  ",],
             xtitle="Number of ripples in mirror length",ytitle="Strehl Ratio I/I0",
             xrange=[0,25], yrange=[0,1.09], show=0)

matplotlib.pylab.grid(b=True, which='major', color='#666666', linestyle='-', alpha=0.2)
filename = "scan_peak_vs_cos50.png"
fm[0].savefig(filename)
print("File written to disk: %s "%filename)
matplotlib.pylab.show()



# #
# #
# #
# am = numpy.loadtxt("scan_peak_vs_cos10.txt", skiprows=0)
# amC = numpy.loadtxt("scan_peak_vs_cos10_corrected.txt", skiprows=0)
# amR = numpy.loadtxt("scan_peak_vs_cos10_cropped.txt", skiprows=0)
# amE = numpy.loadtxt("scan_peak_vs_cos10_extrapolated.txt", skiprows=0)
# fm =    plot(am[:,0],   am[:,1] / 212.6,
#              amC[:,0], amC[:,1] / 212.6,
#              amR[:,0], amR[:,1] / 212.6,
#              amE[:,0], amE[:,1] / 212.6,
#              xlog=False,figsize=(12,8),
#              legend=["Uncorrected               ",
#                      "Corrected (ideal)         ",
#                      "Corrected (cropped)       ",
#                      "Corrected (extrapolated)  ",],
#              xtitle="Number of ripples in mirror length",ytitle="Strehl Ratio I/I0",
#              yrange=[0,1.09], show=0)
#
# matplotlib.pylab.grid(b=True, which='major', color='#666666', linestyle='-', alpha=0.2)
# filename = "scan_peak_vs_cos10.png"
# fm[0].savefig(filename)
# print("File written to disk: %s "%filename)
# matplotlib.pylab.show()

#
#
#
am = numpy.loadtxt( "scan_peak_vs_cos30.txt", skiprows=0)
amC = numpy.loadtxt("scan_peak_vs_cos30_corrected.txt", skiprows=0)
amR = numpy.loadtxt("scan_peak_vs_cos30_cropped.txt", skiprows=0)
amE = numpy.loadtxt("scan_peak_vs_cos30_extrapolated_new.txt", skiprows=0)
fm =    plot(am[:,0],   am[:,1] / 212.6,
             amC[:,0], amC[:,1] / 212.6,
             amR[:,0], amR[:,1] / 212.6,
             amE[:,0], amE[:,1] / 212.6,
             xlog=False,figsize=(12,8),
             legend=["Uncorrected               ",
                     "Corrected (ideal)         ",
                     "Corrected (cropped)       ",
                     "Corrected (extrapolated)  ",],
             xtitle="Number of ripples in mirror length",ytitle="Strehl Ratio I/I0",
             xrange=[0,25], yrange=[0,1.09], show=0)

matplotlib.pylab.grid(b=True, which='major', color='#666666', linestyle='-', alpha=0.2)
filename = "scan_peak_vs_cos30.png"
fm[0].savefig(filename)
print("File written to disk: %s "%filename)
matplotlib.pylab.show()