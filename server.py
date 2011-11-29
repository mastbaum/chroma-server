#!/usr/bin/env python

import zmq
import sys
import zmq
import gc

from rat import ROOT

from chroma import Simulation
from chroma.tools import enable_debug_on_crash

import chroma_sno
import serialize

ack = '__CHROMA_ACK__'
helo = '__CHROMA_HELO__'

if __name__ == '__main__':
    if len(sys.argv) > 1:
        address = sys.argv[1]
    else:
        address = 'tcp://*:5024'

    enable_debug_on_crash()

    # set up zeromq socket
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind(address)

    msg = socket.recv()
    print msg
    if msg == helo:
        socket.send(ack)
    else:
        print 'Malformed hello packet from client:', msg
        # exit

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

