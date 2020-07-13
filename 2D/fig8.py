import h5py
import numpy
from wofry.propagator.wavefront2D.generic_wavefront import GenericWavefront2D


def load_h5_file(filename, filepath):
    try:
        f = h5py.File(filename, 'r')
        mesh_X = f[filepath + "/wfr_mesh_X"].value
        mesh_Y = f[filepath + "/wfr_mesh_Y"].value
        complex_amplitude_s = f[filepath + "/wfr_complex_amplitude_s"].value.T
        wfr = GenericWavefront2D.initialize_wavefront_from_arrays(
            x_array=numpy.linspace(mesh_X[0], mesh_X[1], int(mesh_X[2])),
            y_array=numpy.linspace(mesh_Y[0], mesh_Y[1], int(mesh_Y[2])),
            z_array=complex_amplitude_s)
        wfr.set_photon_energy(f[filepath + "/wfr_photon_energy"].value)
        f.close()
        return wfr
    except:
        raise Exception("Failed to load 2D wavefront to h5 file: " + filename)

if __name__ == "__main__":
    from srxraylib.plot.gol import plot_image, set_qt
    set_qt()
    import matplotlib
    import matplotlib.pylab as plt

    labelsize = 25
    figsize = (11, 7)
    matplotlib.rc('xtick', labelsize=labelsize)
    matplotlib.rc('ytick', labelsize=labelsize)
    matplotlib.rcParams.update({'font.size': labelsize})

    file_deformed = "flexon_paper_2d_deformed.h5"
    file_undeformed = "flexon_paper_2d_undeformed.h5"



    FILE1 = [file_undeformed, file_deformed]
    FILEFIG = ["intensity2Duncorrected.pdf", "intensity2Dcorrected.pdf", "water1_2d.pdf"]

    w0 = load_h5_file(FILE1[0], "wfr")
    z0 = w0.get_intensity()
    x0 = w0.get_coordinate_x()
    y0 = w0.get_coordinate_y()

    w1 = load_h5_file(FILE1[1], "wfr")
    z1 = w1.get_intensity()
    x1 = w1.get_coordinate_x()
    y1 = w1.get_coordinate_y()




    plot_image(z0/z0.max(), 1e6*x0, 1e6*y0, aspect=None, figsize=figsize,
               xtitle="Horizontal [$\mu$m]",
               ytitle="Vertical [$\mu$m]",
               title="",
               cmap="jet",
               show=0,
               )

    plt.savefig(FILEFIG[0])
    plt.show()
    print("File %s saved to file" % FILEFIG[0])


    plot_image(z1/z0.max(), 1e6*x1, 1e6*y1, aspect=None, figsize=figsize,
               xtitle="Horizontal [$\mu$m]",
               ytitle="Vertical [$\mu$m]",
               title="",
               cmap="jet",
               show=0,
               )

    plt.savefig(FILEFIG[1])
    plt.show()
    print("File %s saved to file" % FILEFIG[1])