import numpy
#
# script to make the calculations (created by XOPPY:undulator_radiation)
#
def undulator_radiation(Kh=0.0, Kv=0.0, Phase=0.0, h5file="tmp.h5"):
    from orangecontrib.xoppy.util.xoppy_undulators import xoppy_calc_undulator_radiation

    e, h, v, p, code = xoppy_calc_undulator_radiation(
            ELECTRONENERGY           = 2.0,
            ELECTRONENERGYSPREAD     = 0.00104,
            ELECTRONCURRENT          = 0.5,
            ELECTRONBEAMSIZEH        = 1.212e-05,
            ELECTRONBEAMSIZEV        = 1.473e-05,
            ELECTRONBEAMDIVERGENCEH  = 5.77e-06,
            ELECTRONBEAMDIVERGENCEV  = 4.75e-06,
            PERIODID                 = 0.0288,
            NPERIODS                 = 137.0,
            KV                       = Kv,
            KH                       = Kh,
            KPHASE                   = Phase,
            DISTANCE                 = 13.73,
            SETRESONANCE             = 0,
            HARMONICNUMBER           = 1,
            GAPH                     = 0.030,
            GAPV                     = 0.015,
            HSLITPOINTS              = 49, #101, #151,
            VSLITPOINTS              = 49, #101, #151,
            METHOD                   = 2, # 1=Urgent, 2=SRW, 3=pySRU
            PHOTONENERGYMIN          = 200.0,
            PHOTONENERGYMAX          = 12000.0,
            PHOTONENERGYPOINTS       = 1500,
            USEEMITTANCES            = 1,
            h5_file                  = h5file,
            h5_entry_name            = "XOPPY_RADIATION",
            h5_initialize            = True,
            # photonEnergyIntelligentGrid = False,
            )

# example plot
#from srxraylib.plot.gol import plot_image
#plot_image(p[0],h,v,title="Flux [photons/s] per 0.1 bw per mm2 at %9.3f eV"%(200.0),xtitle="H [mm]",ytitle="V [mm]")
#
# end script
#
if __name__ == "__main__":
    # undulator_radiation(Kh=3.07, Kv=0.0, Phase=0.0, h5file="undulator_radiation_flexon_Kh.h5")
    # undulator_radiation(Kh=2.171, Kv=2.171, Phase=0.0, h5file="undulator_radiation_flexon_KhKv.h5")


    # undulator_radiation(Kh=0.0,  Kv=3.07, Phase=0.0, h5file="undulator_radiation_flexon_Kv_urgent2.h5")  # with pySRY - same as undulator_radiation_flexon_grant4.h5
    # undulator_radiation(Kh=3.07,  Kv=0.0, Phase=0.0, h5file="undulator_radiation_flexon_Kh_urgent2.h5")
    undulator_radiation(Kh=2.171, Kv=2.171, Phase=numpy.pi/2, h5file="undulator_radiation_flexon_KhKv90.h5")
