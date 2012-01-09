import os
import array
import shutil
from rat import ROOT

# compile serialize.C if necessary
if not hasattr(ROOT, 'Serialize'):
    # Create .chroma directory if it doesn't exist
    chroma_dir = os.path.expanduser('~/.chroma')
    if not os.path.isdir(chroma_dir):
        if os.path.exists(chroma_dir):
            raise Exception('$HOME/.chroma file exists where directory should be')
        else:
            os.mkdir(chroma_dir)
    # Check if latest ROOT file is present
    package_root_C = os.path.join(os.path.dirname(__file__), 'serialize.C')
    home_root_C = os.path.join(chroma_dir, 'serialize.C')
    if not os.path.exists(home_root_C) or \
            os.stat(package_root_C).st_mtime > os.stat(home_root_C).st_mtime:
        shutil.copy2(src=package_root_C, dst=home_root_C)
    # Import this C file for access to data structure
    ROOT.gROOT.ProcessLine('.L '+home_root_C+'+')

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

