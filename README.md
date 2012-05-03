chroma photon propagation server
================================
This package lets you run a [chroma](http://chroma.bitbucket.org) server, which performs GPU-accelerated photon propagation for clients. Clients send `chroma-server` a list of initial photon vertices, and it replies with the final vertices of detected photons.

Installation
------------
`chroma-server` is packaged with `distribute`. To install:

    $ python setup.py install

This package, of course, relies on `chroma` itself.

Usage
-----
To run a chroma server:

    $ chroma-server <detector> [options]

where options include `--address=ADDRESS`. The default server address is `tcp://*:5024`, i.e. listening on all interfaces on port 5024.

Clients
-------
The chroma server expects to receive ROOT-serialized `ChromaPhotonList` objects. The class definition is located in `src/ChromaPhotonList.hh`.

Package Usage
-------------
`chroma-server` includes a Python package `chroma_server` which has the socket server class `ChromaServer` (server.py) and facilities for manipulating photon lists (photon.py, serialize.py).

