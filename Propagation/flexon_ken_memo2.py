import numpy
from srxraylib.plot.gol import plot



#
# aux function (pasted from oasys)
#


def calculate_wavefront1D(wavelength=1e-10,
                          undulator_length=1.0, undulator_distance=10.0,
                          x_min=-0.1, x_max=0.1, number_of_points=101,
                          wavefront_position=0, add_random_phase=0):
    from wofry.propagator.wavefront1D.generic_wavefront import GenericWavefront1D

    sigma_r = 2.740 / 4 / numpy.pi * numpy.sqrt(wavelength * undulator_length)
    sigma_r_prime = 0.69 * numpy.sqrt(wavelength / undulator_length)

    wavefront1D = GenericWavefront1D.initialize_wavefront_from_range(x_min=x_min, x_max=x_max,
                                                                     number_of_points=number_of_points)
    wavefront1D.set_wavelength(wavelength)

    if wavefront_position == 0:  # Gaussian source
        wavefront1D.set_gaussian(sigma_x=sigma_r, amplitude=1.0, shift=0.0)
    elif wavefront_position == 1:  # Spherical source, Gaussian intensity
        wavefront1D.set_spherical_wave(radius=undulator_distance, center=0.0, complex_amplitude=complex(1, 0))
        # weight with Gaussian
        X = wavefront1D.get_abscissas()
        A = wavefront1D.get_complex_amplitude()
        sigma = undulator_distance * sigma_r_prime
        sigma_amplitude = sigma * numpy.sqrt(2)
        Gx = numpy.exp(-X * X / 2 / sigma_amplitude ** 2)
        wavefront1D.set_complex_amplitude(A * Gx)

    if add_random_phase:
        wavefront1D.add_phase_shifts(2 * numpy.pi * numpy.random.random(wavefront1D.size()))

    return wavefront1D


def calculate_output_wavefront_after_reflector1D(input_wavefront, radius=10000.0, grazing_angle=1.5e-3, error_flag=0,
                                                 error_file="", write_profile=0):
    import numpy
    from scipy import interpolate
    output_wavefront = input_wavefront.duplicate()
    abscissas = output_wavefront.get_abscissas()
    abscissas_on_mirror = abscissas / numpy.sin(grazing_angle)
    if radius >= 0:
        height = radius - numpy.sqrt(radius ** 2 - abscissas_on_mirror ** 2)
    else:
        height = radius + numpy.sqrt(radius ** 2 - abscissas_on_mirror ** 2)

    if error_flag:
        a = numpy.loadtxt(error_file)
        finterpolate = interpolate.interp1d(a[:, 0], a[:, 1], fill_value="extrapolate")
        height_interpolated = finterpolate(abscissas_on_mirror)
        height += height_interpolated

    phi = -2 * output_wavefront.get_wavenumber() * height * numpy.sin(grazing_angle)
    output_wavefront.add_phase_shifts(phi)

    # print("Wavefront limits [um]: %f %f" % (
    # 1e6 * input_wavefront.get_abscissas().min(), 1e6 * input_wavefront.get_abscissas().max()))
    if error_flag:
        # print("profile deformation limits [m]: %f %f" % (a[0, 0], a[-1, 0]))
        # print("profile deformation projected limits [um]: %f um %f um" %
        #       (1e6 * a[0, 0] * numpy.sin(grazing_angle), 1e6 * a[-1, 0] * numpy.sin(grazing_angle)))
        # print("Wavefront clipped to projected limits of profile deformation")
        output_wavefront.clip(a[0, 0] * numpy.sin(grazing_angle), a[-1, 0] * numpy.sin(grazing_angle))

    # output files
    if write_profile:
        f = open("reflector_profile1D.dat", "w")
        for i in range(height.size):
            f.write("%g %g\n" % (abscissas_on_mirror[i], height[i]))
        f.close()
        print("File reflector_profile1D.dat written to disk.")

    return output_wavefront, abscissas_on_mirror, height


def calculate_output_wavefront_after_corrector1D(input_wavefront, grazing_angle=1.5e-3, focus_at=10.0, apodization=0,
                                                 apodization_ratio=0.1, write_correction_profile=0):
    import numpy
    from scipy import interpolate
    output_wavefront = input_wavefront.duplicate()
    target_wavefront = input_wavefront.duplicate()
    target_wavefront.set_spherical_wave(radius=-focus_at, center=0.0, complex_amplitude=1.0)

    phase_input = input_wavefront.get_phase(unwrap=True)
    phase_target = target_wavefront.get_phase(unwrap=True)
    phase_correction = phase_target - phase_input
    abscissas = target_wavefront.get_abscissas()
    abscissas_on_mirror = abscissas / numpy.sin(grazing_angle)

    # output_wavefront.add_phase_shift(phase_correction)
    height = - phase_correction / (2 * output_wavefront.get_wavenumber() * numpy.sin(grazing_angle))

    if apodization == 0:
        height -= height[height.size // 2]
    elif apodization == 1:
        apodization = input_wavefront.get_intensity()
        apodization = (apodization / apodization.max())
        height *= apodization
        height -= height[0]
    elif apodization == 2:
        sigma = numpy.abs(abscissas[-1] - abscissas[0]) * apodization_ratio
        apodization = numpy.exp(- abscissas ** 2 / 2 / sigma ** 2)
        apodization /= apodization.max()
        height *= apodization
        height -= height[0]

    # calculate phase shift from new profile
    phi = -2 * output_wavefront.get_wavenumber() * height * numpy.sin(grazing_angle)
    output_wavefront.add_phase_shift(phi)

    # output files
    if write_correction_profile:
        f = open("correction_profile1D.dat", "w")
        for i in range(height.size):
            f.write("%g %g\n" % (abscissas_on_mirror[i], height[i]))
        f.close()
        print("File correction_profile1D.dat written to disk.")

    return output_wavefront, target_wavefront, abscissas_on_mirror, height


#
# create input_wavefront
#

def source(photon_energy=230.888,number_of_points=3001*1,x_max=0.00147*1):
# def source(photon_energy=250, number_of_points=3001, x_max=0.00147):
    import scipy.constants as codata
    wavelength = codata.h * codata.c / codata.e / photon_energy
    output_wavefront = calculate_wavefront1D(wavelength=wavelength,
                                             wavefront_position=1,
                                             undulator_length=3.98,
                                             undulator_distance=13.73,
                                             x_min=-x_max,
                                             x_max=x_max,
                                             number_of_points=number_of_points,
                                             add_random_phase=False)


    if do_plot:
        plot_wavefront_intensity(output_wavefront,title="source")


    return output_wavefront

def M1(input_wavefront, deformation_file="", radius=100000.0):

    if deformation_file == "":
        error_flag = 0
    else:
        error_flag = 1
    output_wavefront, abscissas_on_mirror, height = calculate_output_wavefront_after_reflector1D(input_wavefront,
                                                                                                 radius=radius,
                                                                                                 grazing_angle=0.0218,
                                                                                                 error_flag=error_flag,
                                                                                                 error_file=deformation_file,
                                                                                                 write_profile=0)
    if do_plot:
        plot_wavefront_intensity(output_wavefront,title="M1")

    return output_wavefront


def propagate_from_M1_to_M3(wf_in, magnification_x=2.0):
    #
    # ===== Example of python code to create propagate current element =====
    #

    #
    # Import section
    #
    import numpy
    from wofry.propagator.propagator import PropagationManager, PropagationElements, PropagationParameters
    from syned.beamline.beamline_element import BeamlineElement
    from syned.beamline.element_coordinates import ElementCoordinates
    from wofry.propagator.propagators1D.fresnel_zoom import FresnelZoom1D


    input_wavefront = wf_in.duplicate()

    #
    # info on current oe
    #
    #
    #    -------WOScreen1D---------
    #        -------BoundaryShape---------
    #

    #
    # define current oe
    #
    from wofry.beamline.optical_elements.ideal_elements.screen import WOScreen1D

    optical_element = WOScreen1D()

    #
    # propagating (***  ONLY THE ZOOM PROPAGATOR IS IMPLEMENTED ***)
    #
    #
    propagation_elements = PropagationElements()
    beamline_element = BeamlineElement(optical_element=optical_element,
                                       coordinates=ElementCoordinates(p=0.000000, q=13.599000,
                                                                      angle_radial=numpy.radians(0.000000),
                                                                      angle_azimuthal=numpy.radians(0.000000)))
    propagation_elements.add_beamline_element(beamline_element)
    propagation_parameters = PropagationParameters(wavefront=input_wavefront.duplicate(),
                                                   propagation_elements=propagation_elements)
    # self.set_additional_parameters(propagation_parameters)
    #
    propagation_parameters.set_additional_parameters('magnification_x', magnification_x)
    #
    propagator = PropagationManager.Instance()
    try:
        propagator.add_propagator(FresnelZoom1D())
    except:
        pass
    output_wavefront = propagator.do_propagation(propagation_parameters=propagation_parameters,
                                                 handler_name='FRESNEL_ZOOM_1D')

    if do_plot:
        plot_wavefront_intensity(output_wavefront,title="propagation M1 to M3")


    return output_wavefront

def M3(input_wavefront):
    #
    # ===== Example of python code to create propagate current element =====
    #

    output_wavefront, abscissas_on_mirror, height = calculate_output_wavefront_after_reflector1D(input_wavefront,
                                                                                                 radius=220.71532,
                                                                                                 grazing_angle=0.02181,
                                                                                                 error_flag=0,
                                                                                                 error_file="/home/manuel/Oasys/dabam_profile_140522663056440.dat",
                                                                                                 write_profile=0)

    if do_plot:
        plot_wavefront_intensity(output_wavefront,title="M3")

    return output_wavefront


def M3correction(input_wavefront):

    output_wavefront, target_wavefront, abscissas_on_mirror, height = calculate_output_wavefront_after_corrector1D(
        input_wavefront, grazing_angle=0.02181, focus_at=2.64, apodization=0, apodization_ratio=6.0,
        write_correction_profile=0)

    if do_plot:
        plot_wavefront_intensity(output_wavefront,title="M3correction")

    return output_wavefront


def propagate_from_M3_to_sample(wf_in, magnification_x=0.01):
    #
    # ===== Example of python code to create propagate current element =====
    #

    #
    # Import section
    #
    import numpy
    from wofry.propagator.propagator import PropagationManager, PropagationElements, PropagationParameters
    from syned.beamline.beamline_element import BeamlineElement
    from syned.beamline.element_coordinates import ElementCoordinates
    from wofry.propagator.propagators1D.fresnel_zoom import FresnelZoom1D

    input_wavefront = wf_in.duplicate()

    #
    # info on current oe
    #
    #
    #    -------WOScreen1D---------
    #        -------BoundaryShape---------
    #

    #
    # define current oe
    #
    from wofry.beamline.optical_elements.ideal_elements.screen import WOScreen1D

    optical_element = WOScreen1D()

    #
    # propagating (***  ONLY THE ZOOM PROPAGATOR IS IMPLEMENTED ***)
    #
    #
    propagation_elements = PropagationElements()
    beamline_element = BeamlineElement(optical_element=optical_element,
                                       coordinates=ElementCoordinates(p=0.000000, q=2.6393000,
                                                                      angle_radial=numpy.radians(0.000000),
                                                                      angle_azimuthal=numpy.radians(0.000000)))
    propagation_elements.add_beamline_element(beamline_element)
    propagation_parameters = PropagationParameters(wavefront=input_wavefront.duplicate(),
                                                   propagation_elements=propagation_elements)
    # self.set_additional_parameters(propagation_parameters)
    #
    propagation_parameters.set_additional_parameters('magnification_x',magnification_x)
    #
    propagator = PropagationManager.Instance()
    try:
        propagator.add_propagator(FresnelZoom1D())
    except:
        pass
    output_wavefront = propagator.do_propagation(propagation_parameters=propagation_parameters,
                                                 handler_name='FRESNEL_ZOOM_1D')

    if do_plot:
        plot_wavefront_intensity(output_wavefront,title="propagation M3 to sample")

    return output_wavefront


def plot_wavefront_intensity(wf,title=""):
    plot(1e6*wf.get_abscissas(), wf.get_intensity(),
         title=title + " FWHM = %f um, I0=%f"%(1e6*get_wavefront_intensity_fwhm(wf),
                                      get_wavefront_intensity_I0(wf)),
         xtitle="X [um]",ytitle="Intensity [a.u.]")

def write_wavefront_intensity(wf,filename=""):
    x = wf.get_abscissas()
    y = wf.get_intensity()
    if filename != "":
        f = open(filename,'w')
        for i in range(x.size):
            f.write("%g  %g\n" % (1e6 * x[i], y[i]))
        f.close()
        print("File written to disk: %s" % filename)


def get_wavefront_intensity_fwhm(wf):
    from oasys.util.oasys_util import get_fwhm
    fwhm, quote, coordinates = get_fwhm(wf.get_intensity(),wf.get_abscissas())
    return fwhm

def get_wavefront_intensity_I0(wf):
    I = wf.get_intensity()
    return I[I.size//2]


def get_R_incidence_deg(p_foc,q_foc,incidence_deg):
    mm = (1.0 / p_foc + 1.0 / q_foc)
    return 2 / (numpy.cos(incidence_deg * numpy.pi / 180)) / mm

def get_R_grazing(p_foc,q_foc,grazing):
    mm = (1.0 / p_foc + 1.0 / q_foc)
    return 2 / (numpy.sin(grazing)) / mm

def RUN_WOFRY(photon_energy=250, deformation_file="", do_optimize_M3=False, error_radius=1e10):

    wf = source(photon_energy=photon_energy)


    wf0 = M1(wf, radius=error_radius, deformation_file=deformation_file)


    wf1 = propagate_from_M1_to_M3(wf0)

    wf2 = M3(wf1)

    if do_optimize_M3:
        wf3 = M3correction(wf2)
    else:
        wf3 = wf2

    magnification_x = 0.01

    # if not do_optimize_M3:
    #     if numpy.abs(error_radius) < 5000:
    #         magnification_x = 0.1
    #
    #     if numpy.abs(error_radius) < 200:
    #         magnification_x = 1
    # else:
    #
    #
    #     if numpy.abs(error_radius) < 100:
    #         magnification_x = 0.005
    #
    #     if numpy.abs(error_radius) < 45:
    #         magnification_x = 0.005 / 5

    wf4 = propagate_from_M3_to_sample(wf3, magnification_x=magnification_x)



    return wf4




if __name__ == "__main__":


    do_loop = 0
    do_plot = 0
    do_h5 = 0

    if do_h5:
        from srxraylib.util.h5_simple_writer import H5SimpleWriter
        h = H5SimpleWriter.initialize_file("flexon_ken_memo2.h5",overwrite=True)


    if do_loop:

        ERROR_RADIUS = numpy.logspace(1,6,100)
        I0uncorr = numpy.zeros_like(ERROR_RADIUS)
        I0corr = numpy.zeros_like(ERROR_RADIUS)
        I0uncorr1500 = numpy.zeros_like(ERROR_RADIUS)
        I0corr1500 = numpy.zeros_like(ERROR_RADIUS)

        factor = 1.0 # -1.0
        photon_energy1 = 250
        photon_energy2 = 1250
        for i in range(ERROR_RADIUS.size):

            print("iteration %d of %d"%(i+1,ERROR_RADIUS.size))
            wf2 = RUN_WOFRY(photon_energy=photon_energy1, do_optimize_M3=False, error_radius=factor*ERROR_RADIUS[i])
            Ino = wf2.get_intensity()
            Xno = wf2.get_abscissas()
            I0uncorr[i] = get_wavefront_intensity_I0(wf2)
            # I0uncorr[i] = get_wavefront_intensity_fwhm(wf2)
            wf2 = RUN_WOFRY(photon_energy=photon_energy1, do_optimize_M3=True, error_radius=factor*ERROR_RADIUS[i])
            Iopt = wf2.get_intensity()
            Xopt = wf2.get_abscissas()
            I0corr[i] = get_wavefront_intensity_I0(wf2)


            wf2 = RUN_WOFRY(photon_energy=photon_energy2, do_optimize_M3=True, error_radius=factor*ERROR_RADIUS[i])
            I0corr1500[i] = get_wavefront_intensity_I0(wf2)
            wf2 = RUN_WOFRY(photon_energy=photon_energy2, do_optimize_M3=False, error_radius=factor*ERROR_RADIUS[i])
            I0uncorr1500[i] = get_wavefront_intensity_I0(wf2)

            if do_h5:
                h.create_entry("iteration %f" % (factor * ERROR_RADIUS[i]), nx_default="intensity")
                h.add_dataset(1e6 * Xopt, Iopt, dataset_name="intensity",
                              entry_name="iteration %f" % (factor * ERROR_RADIUS[i]),
                              title_x="X / um", title_y="intensity / a.u.")



        if do_h5:
            h.create_entry("scan results", nx_default="strehl_opt")
            h.add_dataset(ERROR_RADIUS,I0uncorr/I0uncorr[-1], dataset_name="strehl_no", entry_name="scan results",
                          title_x="Radius/m", title_y="Strelh Ratio")
            h.add_dataset(ERROR_RADIUS,I0corr/I0corr[-1], dataset_name="strehl_opt", entry_name="scan results",
                          title_x="Radius/m", title_y="Strelh Ratio")

            print("File flexon_ken_memo2.h5 written to disk.")


        filename = "flexon_ken_memo2_factor%d.dat"%factor
        f = open(filename,"w")
        f.write("; radius uncorrected250 corrected250 uncorrected1250 corrected1250 \n")
        for i in range(ERROR_RADIUS.size):
            f.write("%g  %g  %g  %g %g \n"%
                    (ERROR_RADIUS[i],
                    I0uncorr[i]/I0uncorr[-1],
                    I0corr[i]/I0corr[-1],
                    I0uncorr1500[i] / I0uncorr1500[-1],
                    I0corr1500[i] / I0corr1500[-1],
                     ))
        f.close()
        print("File written to disk: %s"%filename)

        plot(ERROR_RADIUS,I0uncorr/I0uncorr[-1],
             ERROR_RADIUS,I0corr/I0corr[-1],
             ERROR_RADIUS, I0uncorr1500 / I0uncorr1500[-1],
             ERROR_RADIUS, I0corr1500 / I0corr1500[-1],
             xlog=True,
             legend=["Uncorrected E=%d eV"%photon_energy1,"Corrected E=%d eV"%photon_energy1,"Uncorrected E=%d eV"%photon_energy2,"Corrected E=%d eV"%photon_energy2],
             xtitle="Radius [m]",ytitle="Strehl I/I0")

    else:
        # wf2 = RUN_WOFRY(photon_energy=230.888, do_optimize_M3=False, error_radius=-1e10)
        # filename = "Uncorrected/intensityundeformed.txt"
        # plot_wavefront_intensity(wf2,title=filename)
        # write_wavefront_intensity(wf2,filename)

        wf2 = RUN_WOFRY(photon_energy=230.888, deformation_file="", do_optimize_M3=False, error_radius=-1e10)
        filename = "Uncorrected/intensitycriogenic.txt"
        plot_wavefront_intensity(wf2,title=filename)
        write_wavefront_intensity(wf2,filename)


        # print("M3 Radius, angle: ",get_R_grazing(13.73+13.599,2.64,1.25*numpy.pi/180),1.25*numpy.pi/180)

        # wf2 = RUN_WOFRY(photon_energy=250,do_plot=False,do_optimize_M3=True,error_radius=1e2)
        # plot_wavefront_intensity(wf2)
