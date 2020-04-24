from srxraylib.plot.gol import plot
import matplotlib.pylab as plt
import numpy


import matplotlib
import matplotlib.pylab as plt
matplotlib.rc('xtick',         labelsize=20)
matplotlib.rc('ytick',         labelsize=20)
matplotlib.rcParams.update({'font.size': 20})




#
#
#
am =  numpy.loadtxt("scan_peak_vs_positive_radius.txt", skiprows=0)
amC = numpy.loadtxt("scan_peak_vs_positive_radius_corrected.txt", skiprows=0)
amR = numpy.loadtxt("scan_peak_vs_positive_radius_cropped.txt", skiprows=0)
amE = numpy.loadtxt("scan_peak_vs_positive_radius_extrapolated.txt", skiprows=0)
fm = plot(numpy.abs(am[:,0]),  am[:,1]  / am[-1,1],
          numpy.abs(amC[:,0]), amC[:,1] / am[-1,1],
          numpy.abs(amR[:,0]), amR[:,1] / am[-1,1],
          numpy.abs(amE[:,0]), amE[:,1] / am[-1,1],
          xlog=True,figsize=(12,8),
          legend=["Uncorrected",
                  "Corrected (ideal)",
                  "Corrected (cropped)",
                  "Corrected (extrapolated)"],
          xtitle="Radius [m]",ytitle="Strehl Ratio I/I0",xrange=[60,1e6], show=0)

matplotlib.pylab.grid() #b=True, which='major', color='#666666', linestyle='-', alpha=0.2)
filepng = "scan_peak_vs_positive_radius.png"
fm[0].savefig(filepng)
print("File written to disk: %s" % filepng)
plt.show()

#
#
#
am = numpy.loadtxt("scan_peak_vs_negative_radius.txt", skiprows=0)
amC = numpy.loadtxt("scan_peak_vs_negative_radius_corrected.txt", skiprows=0)
amR = numpy.loadtxt("scan_peak_vs_negative_radius_cropped.txt", skiprows=0)
amE = numpy.loadtxt("scan_peak_vs_negative_radius_extrapolated.txt", skiprows=0)
# amE = numpy.loadtxt("tmp.txt", skiprows=0)
fm = plot(numpy.abs(am[:,0]),  am[:,1]  / am[-1,1],
          numpy.abs(amC[:,0]), amC[:,1] / am[-1,1],
          numpy.abs(amR[:,0]), amR[:,1] / am[-1,1],
          numpy.abs(amE[:,0]), amE[:,1] / am[-1,1],
          xlog=True,figsize=(12,8),
          legend=["Uncorrected",
                  "Corrected (ideal)",
                  "Corrected (cropped)",
                  "Corrected (extrapolated)"],
          xtitle="Radius [m]",ytitle="Strehl Ratio I/I0",xrange=[60,1e6], show=0)

matplotlib.pylab.grid()
filepng = "scan_peak_vs_negative_radius.png"
fm[0].savefig(filepng)
print("File written to disk: %s" % filepng)
plt.show()


#==================================  HIGH ENERGY ============================================

if False:
    #
    #
    #
    am =  numpy.loadtxt("scan_peak_vs_positive_radius_1230eV.txt", skiprows=0)
    amC = numpy.loadtxt("scan_peak_vs_positive_radius_corrected_1230eV.txt", skiprows=0)
    amR = numpy.loadtxt("scan_peak_vs_positive_radius_cropped_1230eV_new.txt", skiprows=0)
    amE = numpy.loadtxt("scan_peak_vs_positive_radius_extrapolated_1230eV_new.txt", skiprows=0)
    # plot(numpy.abs(amE[:,0]), amE[:,1] / am[-1,1], xlog=True, title="extrapolated", show=0)
    # plot(numpy.abs(amR[:,0]), amR[:,1] / am[-1,1], xlog=True, title="cropped")
    fm = plot(numpy.abs(am[:,0]),   am[:,1] / am[-1,1],
              numpy.abs(amC[:,0]), amC[:,1] / am[-1,1],
              numpy.abs(amR[:,0]), amR[:,1] / am[-1,1],
              numpy.abs(amE[:,0]), amE[:,1] / am[-1,1],
              xlog=True,figsize=(12,8),
              legend=["Uncorrected",
                      "Corrected (ideal)",
                      "Corrected (cropped)",
                      "Corrected (extrapolated)"],
              xtitle="Radius [m]",ytitle="Strehl Ratio I/I0",xrange=[60,1e6], show=0,
              title="1230.888 eV")

    matplotlib.pylab.grid() #b=True, which='major', color='#666666', linestyle='-', alpha=0.2)
    filepng = "scan_peak_vs_positive_radius_1230eV.png"
    fm[0].savefig(filepng)
    print("File written to disk: %s" % filepng)
    plt.show()

    #
    #
    #
    am =  numpy.loadtxt("scan_peak_vs_negative_radius_1230eV.txt", skiprows=0)
    amC = numpy.loadtxt("scan_peak_vs_negative_radius_corrected_1230eV_new.txt", skiprows=0)
    amR = numpy.loadtxt("scan_peak_vs_negative_radius_cropped_1230eV_new.txt", skiprows=0)
    amE = numpy.loadtxt("scan_peak_vs_negative_radius_extrapolated_1230eV_new.txt", skiprows=0)
    fm = plot(numpy.abs(am[:,0]),   am[:,1] / am[-1,1],
              numpy.abs(amC[:,0]), amC[:,1] / am[-1,1],
              numpy.abs(amR[:,0]), amR[:,1] / am[-1,1],
              numpy.abs(amE[:,0]), amE[:,1] / am[-1,1],
              xlog=True,figsize=(12,8),
              legend=["Uncorrected",
                      "Corrected (ideal)",
                      "Corrected (cropped)",
                      "Corrected (extrapolated)"],
              xtitle="Radius [m]",ytitle="Strehl Ratio I/I0",xrange=[60,1e6], show=0,
              title="1230.888 eV")

    matplotlib.pylab.grid() #b=True, which='major', color='#666666', linestyle='-', alpha=0.2)
    filepng = "scan_peak_vs_negative_radius_1230eV.png"
    fm[0].savefig(filepng)
    print("File written to disk: %s" % filepng)
    plt.show()

