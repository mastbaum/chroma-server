import os
import array
from rat import ROOT

ROOT.gROOT.ProcessLine(".L serialize.C+")

def serialize(o, cls=ROOT.TObject):
    '''serializes ROOT object `o` via a ROOT.TBufferFile, returns a character
    array.array of `o`'s contents
    '''
    buf = ROOT.TBufferFile(ROOT.TBuffer.kWrite)
    buf.Reset()
    buf.WriteObjectAny(o, cls)

    mv = memoryview(bytearray(buf.Length())).tobytes()
    a = array.array('c', mv)

    ROOT.Serialize(buf, a)

    return a

def deserialize(s, cls):
    '''rebuilds a ROOT object from a TBufferFile buffer, given such a buffer as
    a string, list, or iterable, and the class of the object-to-be
    (e.g. ROOT.TH1F.Class()).
    '''
    b = array.array('c', s)
    buf = ROOT.TBufferFile(ROOT.TBuffer.kRead, len(b), b, False, 0)
    o = buf.ReadObject(cls)

    return o

