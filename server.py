import gc
import zmq

from rat import ROOT
from chroma import Simulation
import chroma_sno

import serialize

ack = '__CHROMA_ACK__'
helo = '__CHROMA_HELO__'

class ChromaServer:
    def __init__(self, address):
        self.address = address
        self.context = zmq.Context()
        self.socket = context.socket(zmq.REP)
        self.socket.bind(address)

    def serve_forever():
        while True:
            msg = socket.recv(copy=False)
            socket.send(ack)

            # parse ChromaPhotonList
            cpl = serialize.deserialize(msg.bytes, ROOT.RAT.ChromaPhotonList.Class())
            if not cpl:
                print 'Error deserializing message data'
                continue

            print 'Received ChromaPhotonList with', cpl.x.size(), 'photons'
            photons = photons.photons_from_cpl(cpl)

            # propagate photons in chroma simulation
            detector = chroma_sno.sno()
            sim = Simulation(detector)
            event = sim.simulate(photons, keep_photons_end=True).next()
            print event

            # return final photons to client
            cpl = photons.cpl_from_photons(event.photons_end)
            msg = serialize.serialize(cpl)
            print type(msg), len(msg), str(msg[:20])
            socket.send(msg)

            # cleanup?
            del photons
            gc.collect()

