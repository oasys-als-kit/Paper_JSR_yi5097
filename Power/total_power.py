import numpy
import scipy.constants as codata

E = 2.0
I = 0.5
K = 3.07
Lambda = 0.0288
N = 137

B = K * 2 * numpy.pi * codata.m_e * codata.c / (codata.e * Lambda)

Ptot = 72.56 * E**2 * I * N * K**2 / (Lambda * 1e3)

Ptot2 = 633 * E**2 * (N * Lambda) * I * B**2

gamma = 1e9 * E / (codata.m_e *  codata.c**2 / codata.e)

Ptot3 = ( N / 6) * codata.value('characteristic impedance of vacuum') * \
               I * codata.e * 2 * numpy.pi * codata.c * gamma**2 * \
               (K**2) / Lambda

Ptot4 = (1/6) * codata.value('characteristic impedance of vacuum') \
        * codata.e * 2 * numpy.pi * codata.c * \
        (1e9 / (codata.m_e *  codata.c**2 / codata.e)) ** 2

print("Ptot coeff: ",Ptot4)
Ptot4 *= E**2  * N * I * K**2 / Lambda


print("Total power: %f W, %f W, %f W, %f W"%(Ptot, Ptot2, Ptot3,Ptot4))