from srxraylib.plot.gol import plot, set_qt
import matplotlib.pylab as plt
import numpy

labelsize=25
figsize=(12,8)
import matplotlib
import matplotlib.pylab as plt
matplotlib.rc('xtick',         labelsize=labelsize)
matplotlib.rc('ytick',         labelsize=labelsize)
matplotlib.rcParams.update({'font.size': labelsize})


set_qt()

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
          xlog=True,figsize=figsize,
          legend=["Uncorrected",
                  "Corrected (ideal)",
                  "Corrected (cropped)",
                  "Corrected (extrapolated)"],
          legend_position=[0.35, 0.635],
          xtitle="Radius [m]",ytitle="Strehl Ratio I/I0",xrange=[60,1e6], show=0)

matplotlib.pylab.grid() #b=True, which='major', color='#666666', linestyle='-', alpha=0.2)
filefig = "scan_peak_vs_positive_radius.pdf"
fm[0].savefig(filefig)
print("File written to disk: %s" % filefig)
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
          xlog=True,figsize=figsize,
          legend=["Uncorrected",
                  "Corrected (ideal)",
                  "Corrected (cropped)",
                  "Corrected (extrapolated)"],
          legend_position=[0.5,0.635],
          xtitle="Radius [m]",ytitle="Strehl Ratio I/I0",xrange=[60,1e6], show=0)

matplotlib.pylab.grid()
filefig = "scan_peak_vs_negative_radius.pdf"
fm[0].savefig(filefig)
print("File written to disk: %s" % filefig)
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
    filefig = "scan_peak_vs_positive_radius_1230eV.png"
    fm[0].savefig(filefig)
    print("File written to disk: %s" % filefig)
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
    filefig = "scan_peak_vs_negative_radius_1230eV.png"
    fm[0].savefig(filefig)
    print("File written to disk: %s" % filefig)
    plt.show()

