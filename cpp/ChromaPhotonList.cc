#include <RAT/ChromaPhotonList.hh>
#include <TBufferFile.h>
#include <TBuffer.h>
#include <TString.h>
#include <string>
#include <vector>
#include <stdlib.h>

namespace RAT {

void ChromaPhotonList::FromArrays(float* _x,    float* _y,    float* _z,
                                  float* _px,   float* _py,   float* _pz,
                                  float* _polx, float* _poly, float* _polz,
                                  float* _t,
                                  float* _wavelength,
                                  int* _pmtid,
                                  int nphotons)
{
  for (int i=0; i<nphotons; i++) {
    x.push_back(_x[i]);
    y.push_back(_y[i]);
    z.push_back(_z[i]);
    px.push_back(_px[i]);
    py.push_back(_py[i]);
    pz.push_back(_pz[i]);
    polx.push_back(_polx[i]);
    poly.push_back(_poly[i]);
    polz.push_back(_polz[i]);
    t.push_back(_t[i]);
    wavelength.push_back(_wavelength[i]);
    pmtid.push_back(_pmtid[i]);
  }
}

} // namespace RAT

