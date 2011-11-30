#!/usr/bin/env python

import sys
import server
from chroma.tools import enable_debug_on_crash
import chroma_sno

def serve(address):
    print 'initializing chroma server...'
    s = server.ChromaServer(address, chroma_sno.sno())

    print 'starting chroma server listening on', address
    s.serve_forever()

if __name__ == '__main__':
    enable_debug_on_crash()
    if len(sys.argv) > 1:
        address = sys.argv[1]
    else:
        address = 'tcp://*:5024'

    serve(address)

