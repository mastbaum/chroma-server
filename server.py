import gc
import zmq

from rat import ROOT
from chroma import Simulation

import serialize
import photons

class ChromaServer:
    def __init__(self, address, detector):
        # set up zeromq socket
        self.address = address
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REP)
        self.socket.bind(address)

        # set up simulation
        self.detector = detector
        self.sim = Simulation(self.detector)

    def serve_forever(self):
        '''listen for incoming (serialized) initial ChromaPhotonLists,
        propagate photons in chroma, and reply with final photon list'''
        while True:
            msg = self.socket.recv(copy=False)

            # parse ChromaPhotonList
            cpl = serialize.deserialize(msg.bytes, ROOT.RAT.ChromaPhotonList.Class())
            if not cpl:
                print 'Error deserializing message data'
                continue

            print 'Received ChromaPhotonList with', cpl.x.size(), 'photons'
            photons_in = photons.photons_from_cpl(cpl)

            # propagate photons in chroma simulation
            event = self.sim.simulate(photons_in, keep_photons_end=True).next()
            print event

            # return final photons to client
            cpl = photons.cpl_from_photons(event.photons_end)
            msg = serialize.serialize(cpl)
            print type(msg), len(msg), str(msg[:20])
            self.socket.send(msg)

            # cleanup?
            gc.collect()

