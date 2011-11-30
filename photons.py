import numpy
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

    return photons

def cpl_from_photons(photons, process_mask=None, detector=None):
    '''make a ROOT.RAT.ChromaPhotonList from a chroma Photons object

      * if process_mask is provided, photons are filtered accordingly
      * if detector is provided, pmt ids are calculated. else, they are set to -1
    '''
    if process_mask:
        mask = (photons.flags & process_mask) > 0
    else:
        mask = np.ones_like(flags, dtype=bool)

    x = photons.pos[mask,0]
    y = photons.pos[mask,1]
    z = photons.pos[mask,2]

    px = photons.dir[mask,0]
    py = photons.dir[mask,1]
    pz = photons.dir[mask,2]

    polx = photons.pol[mask,0]
    poly = photons.pol[mask,1]
    polz = photons.pol[mask,2]

    t = photons.t[mask]
    wavelength = photons.wavelengths[mask]

    if detector:
        c_idx_c_id = detector.channel_index_to_channel_id # channel index -> channel id
        s_id_c_idx = detector.solid_id_to_channel_index   # solid id -> channel index
        t_id_s_id = detector.solid_id                     # triangle id -> solid id
        t_id = photons.last_hit_triangles[mask]           # last hit triangle id
        pmtid = c_idx_c_id[s_id_c_idx[t_id_s_id[t_id]]]
    else:
        pmtid = -1 * numpy.ones_like(t, dtype=int)

    cpl = ROOT.RAT.ChromaPhotonList()
    cpl.FromArrays(x,    y,    z,
                   px,   py,   pz,
                   polx, poly, polz,
                   t, wavelength, pmtid, len(x))

    return cpl

