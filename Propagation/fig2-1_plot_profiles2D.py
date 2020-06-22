import h5py

def get_surface(fileh5="./DirData/disp1.h5"):


    f = h5py.File(fileh5)

    x = f["surface_file/X"][:]
    y = f["surface_file/Y"][:]
    z = f["surface_file/Z"][:].T

    f.close()

    print(x.shape,y.shape,z.shape)

    return z,x,y

if __name__ == "__main__":
    from srxraylib.plot.gol import plot_image, set_qt
    set_qt()
    import matplotlib
    import matplotlib.pylab as plt

    labelsize = 20
    figsize = (11, 7)
    matplotlib.rc('xtick', labelsize=labelsize)
    matplotlib.rc('ytick', labelsize=labelsize)
    matplotlib.rcParams.update({'font.size': labelsize})

    FILEFIG = ["cryogenic2d.pdf","cryogenic2dKh.pdf","water1_2d.pdf","water2_2d.pdf"]
    FILE1 = ["disp_K307_H_frictionless_folder98.h5","disp_K307_V_frictionless_folder98.h5","disp1.h5","disp2.h5"]



    for i in range(len(FILE1)):
        z,x,y = get_surface(fileh5="./DirData/%s" % FILE1[i])

        plot_image(1e6*z.T,y,x,aspect='auto',figsize=figsize,
                   xtitle="Y [m]",
                   ytitle="X [m]",
                   title="",
                   cmap="jet",
                   show=0,
                )

        plt.savefig(FILEFIG[i])
        plt.show()
        print("File %s saved to file" % FILEFIG[i])
