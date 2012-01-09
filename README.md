chroma photon propagation server
================================
This package lets you run a [chroma](http://chroma.bitbucket.com) server, which performs GPU-accelerated photon propagation for clients. Clients send `chroma-server` a list of initial photon vertices, and it replies with the final vertices of detected photons.

Installation
------------
`chroma-server` is packaged with `distribute`. To install:

    $ python setup.py install

This package, of course, relies on `chroma` itself.

Usage
-----
To run a chroma server:

    $ chroma-server [address]

where `address` is optional. The default server address is `tcp://*:5024`, i.e. listening on all interfaces on port 5024.

Clients
-------
The chroma server expects to receive ROOT-serialized `ChromaPhotonList` objects. The class defintion is located in `src/`.

Package Usage
-------------
`chroma-server` includes a Python package `chroma_server` which includes the socket server class `ChromaServer` and facilities for manipulating photon lists.

