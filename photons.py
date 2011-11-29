from rat import ROOT
from chroma.event import Photons

def photons_from_cpl(cpl):
    '''make a chroma Photons object out of a ROOT.RAT.ChromaPhotonList'''
    x = numpy.array(cpl.x, dtype=numpy.float32)
    y = numpy.array(cpl.y, dtype=numpy.float32)
    z = numpy.array(cpl.z, dtype=numpy.float32)
    pos = numpy.column_stack((x, y, z))

    px = numpy.array(cpl.px, dtype=numpy.float32)
    py = numpy.array(cpl.py, dtype=numpy.float32)
    pz = numpy.array(cpl.pz, dtype=numpy.float32)
    dir = numpy.column_stack((px, py, pz))

    polx = numpy.array(cpl.polx, dtype=numpy.float32)
    poly = numpy.array(cpl.poly, dtype=numpy.float32)
    polz = numpy.array(cpl.polz, dtype=numpy.float32)
    pol = numpy.column_stack((polx, poly, polz))

    t = numpy.array(cpl.t, dtype=numpy.float32)
    wavelengths = numpy.array(cpl.wavelength, dtype=numpy.float32)

    photons = Photons(pos, dir, pol, wavelengths, t=t)

    print photons
    return photons

def cpl_from_photons(photons):
    '''make a ROOT.RAT.ChromaPhotonList from a chroma Photons object'''
    x = numpy.array(photons.pos[:,0])
    y = numpy.array(photons.pos[:,1])
    z = numpy.array(photons.pos[:,2])

    px = numpy.array(photons.dir[:,0])
    py = numpy.array(photons.dir[:,1])
    pz = numpy.array(photons.dir[:,2])

    polx = numpy.array(photons.pol[:,0])
    poly = numpy.array(photons.pol[:,1])
    polz = numpy.array(photons.pol[:,2])

    t = numpy.array(photons.t)
    wavelength = numpy.array(photons.wavelengths)

    pmtid = numpy.array(map(int,wavelength), dtype=numpy.int32)
    #pmtid = f(photons.last_hit_triangles[i]) #numpy.int32!!!

    cpl = ROOT.RAT.ChromaPhotonList()
    cpl.FromArrays(x,    y,    z,
                   px,   py,   pz,
                   polx, poly, polz,
                   t, wavelength, pmtid, len(x))

    return cpl

