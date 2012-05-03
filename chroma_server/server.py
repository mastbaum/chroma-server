import zmq

from chroma import Simulation
from chroma.event import SURFACE_DETECT

import serialize
import photons

class ChromaServer:
    '''a simple zeromq socket server which listens for incoming
    ChromaPhotonList packets and replies with final (hit) photons
    '''
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
        propagate photons in chroma, and reply with final photon list
        '''
        while True:
            msg = self.socket.recv(copy=False)

            # parse ChromaPhotonList
            cpl = serialize.deserialize(msg.bytes)
            if not cpl:
                print 'Error deserializing message data'
                continue

            photons_in = photons.photons_from_cpl(cpl)
            print 'processing', len(photons_in), 'photons'

            # propagate photons in chroma simulation
            event = self.sim.simulate(photons_in, keep_photons_end=True).next()

            # return final (detected) photons to client
            photons_out = event.photons_end
            cpl = photons.cpl_from_photons(photons_out, process_mask=SURFACE_DETECT, detector=self.detector)
            msg = serialize.serialize(cpl)
            self.socket.send(msg)

