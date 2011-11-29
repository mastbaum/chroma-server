#!/usr/bin/env python

import zmq
import sys
import array
import zmq

from rat import ROOT

ack = '__CHROMA_ACK__'

if __name__ == '__main__':
    if len(sys.argv) > 1:
        address = sys.argv[1]
    else:
        address = 'tcp://*:5024'

    # set up zeromq socket
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind(address)

    msg = socket.recv()
    print msg
    if msg == '__CHROMA_HELO__':
        socket.send(ack)
    else:
        print 'Malformed hello packet from client:', msg

    while True:
        #msg = socket.recv()
        #print msg
        msg = socket.recv(copy=False)
        socket.send(ack)
        # buffer contains null characters, so wrap in array to pass to c
        b = array.array('c', msg.bytes)
        buf = ROOT.TBufferFile(ROOT.TBuffer.kRead, len(b), b, False, 0)
        cpl = buf.ReadObject(ROOT.RAT.ChromaPhotonList.Class())

        if cpl:
            print 'Received ChromaPhotonList with', cpl.x.size(), 'photons'
        else:
            print 'Error deserializing message data'

