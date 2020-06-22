#
# script to make the calculations (created by XOPPY:undulator_spectrum)
#
from orangecontrib.xoppy.util.xoppy_undulators import xoppy_calc_undulator_power_density
import numpy

from srxraylib.plot.gol import plot_image, set_qt
import matplotlib.pylab as plt
import matplotlib

set_qt()
labelsize = 25
figsize=(12, 8)

matplotlib.rc('xtick', labelsize=labelsize)
matplotlib.rc('ytick', labelsize=labelsize)
matplotlib.rcParams.update({'font.size': labelsize})

def power_density(Kh=0.0, Kv=0.0, Phase=0.0, pngfile="tmp.png"):
    h5_parameters = dict()
    h5_parameters["ELECTRONENERGY"] = 2.0
    h5_parameters["ELECTRONENERGYSPREAD"] = 0.0011
    h5_parameters["ELECTRONCURRENT"] = 0.5
    h5_parameters["ELECTRONBEAMSIZEH"] = 1.21e-05
    h5_parameters["ELECTRONBEAMSIZEV"] = 1.47e-05
    h5_parameters["ELECTRONBEAMDIVERGENCEH"] = 5.7e-06
    h5_parameters["ELECTRONBEAMDIVERGENCEV"] = 4.7e-06
    h5_parameters["PERIODID"] = 0.0288
    h5_parameters["NPERIODS"] = 138.0
    h5_parameters["KV"] = Kv
    h5_parameters["KH"] = Kh
    h5_parameters["KPHASE"] = Phase
    h5_parameters["DISTANCE"] = 13.73
    h5_parameters["GAPH"] = 0.012 # 0.03
    h5_parameters["GAPV"] = 0.012 # 0.015
    h5_parameters["HSLITPOINTS"] = 201
    h5_parameters["VSLITPOINTS"] = 201
    h5_parameters["METHOD"] = 2
    h5_parameters["USEEMITTANCES"] = 1
    h5_parameters["MASK_FLAG"] = 1
    h5_parameters["MASK_ROT_H_DEG"] = 0.0
    h5_parameters["MASK_ROT_V_DEG"] = 88.75
    h5_parameters["MASK_H_MIN"] = -250.0
    h5_parameters["MASK_H_MAX"] = 250.0
    h5_parameters["MASK_V_MIN"] = -5.0
    h5_parameters["MASK_V_MAX"] = 5.0

    h, v, p, code = xoppy_calc_undulator_power_density(
        ELECTRONENERGY=h5_parameters["ELECTRONENERGY"],
        ELECTRONENERGYSPREAD=h5_parameters["ELECTRONENERGYSPREAD"],
        ELECTRONCURRENT=h5_parameters["ELECTRONCURRENT"],
        ELECTRONBEAMSIZEH=h5_parameters["ELECTRONBEAMSIZEH"],
        ELECTRONBEAMSIZEV=h5_parameters["ELECTRONBEAMSIZEV"],
        ELECTRONBEAMDIVERGENCEH=h5_parameters["ELECTRONBEAMDIVERGENCEH"],
        ELECTRONBEAMDIVERGENCEV=h5_parameters["ELECTRONBEAMDIVERGENCEV"],
        PERIODID=h5_parameters["PERIODID"],
        NPERIODS=h5_parameters["NPERIODS"],
        KV=h5_parameters["KV"],
        KH=h5_parameters["KH"],
        KPHASE=h5_parameters["KPHASE"],
        DISTANCE=h5_parameters["DISTANCE"],
        GAPH=h5_parameters["GAPH"],
        GAPV=h5_parameters["GAPV"],
        HSLITPOINTS=h5_parameters["HSLITPOINTS"],
        VSLITPOINTS=h5_parameters["VSLITPOINTS"],
        METHOD=h5_parameters["METHOD"],
        USEEMITTANCES=h5_parameters["USEEMITTANCES"],
        MASK_FLAG=h5_parameters["MASK_FLAG"],
        MASK_ROT_H_DEG=h5_parameters["MASK_ROT_H_DEG"],
        MASK_ROT_V_DEG=h5_parameters["MASK_ROT_V_DEG"],
        MASK_H_MIN=h5_parameters["MASK_H_MIN"],
        MASK_H_MAX=h5_parameters["MASK_H_MAX"],
        MASK_V_MIN=h5_parameters["MASK_V_MIN"],
        MASK_V_MAX=h5_parameters["MASK_V_MAX"],
        h5_file="",
        h5_entry_name="XOPPY_POWERDENSITY",
        h5_initialize=True,
        h5_parameters=h5_parameters,
    )

    # example plot


    plot_image(p, h, v, xtitle="H [mm]", ytitle="V [mm]", title="", aspect='auto', cmap='jet', show=0,
               figsize=figsize)

    plt.savefig(pngfile)
    plt.show()

    #
    # end script
    #

if __name__ == "__main__":
    power_density(Kh=3.07, Kv=0.0, Phase=0.0, pngfile="powerdensityKh.pdf")
    power_density(Kh=0.0,  Kv=3.7, Phase=0.0, pngfile="powerdensityKv.pdf")
    power_density(Kh=2.171, Kv=2.171, Phase=0.0, pngfile="powerdensityKhKv.pdf")
    power_density(Kh=2.171, Kv=2.171, Phase=numpy.pi/2, pngfile="powerdensityKhKv90.pdf")