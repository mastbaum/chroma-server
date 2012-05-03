////////////////////////////////////////////////////////////////////
/// \class ChromaPhotonList
/// \brief List of photons to send to a Chroma server for propagation
///
/// \author A. Mastbaum <mastbaum@hep.upenn.edu>
///
/// REVISION HISTORY:
///
/// \detail Separate arrays are space-efficient, and it's TObject
///         for purposes of serialization 
///
////////////////////////////////////////////////////////////////////

#ifndef __ChromaPhotonList__
#define __ChromaPhotonList__

#include <TObject.h>
#include <G4ThreeVector.hh>
#include <vector>

class ChromaPhotonList : public TObject {
public:
  ChromaPhotonList() : TObject() {};

  inline void AddPhoton(G4ThreeVector pos, G4ThreeVector mom, G4ThreeVector pol, float _t, float _wavelength, int _pmtid=-1) {
    x.push_back(pos.x());
    y.push_back(pos.y());
    z.push_back(pos.z());
    px.push_back(mom.x());
    py.push_back(mom.y());
    pz.push_back(mom.z());
    polx.push_back(pol.x());
    poly.push_back(pol.y());
    polz.push_back(pol.z());
    t.push_back(_t);
    wavelength.push_back(_wavelength);
    pmtid.push_back(_pmtid);
  }

  void ClearAll() {
    x.clear();
    y.clear();
    z.clear();
    px.clear();
    py.clear();
    pz.clear();
    polx.clear();
    poly.clear();
    polz.clear();
    t.clear();
    wavelength.clear();
    pmtid.clear();
  }

  // Build a ChromaPhotonList object from C arrays
  void FromArrays(float* _x,    float* _y,    float* _z,
                  float* _px,   float* _py,   float* _pz,
                  float* _polx, float* _poly, float* _polz,
                  float* _t, float* _wavelength, int* _pmtid, int nphotons) {
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

  std::vector<float> x;
  std::vector<float> y;
  std::vector<float> z;
  std::vector<float> px;
  std::vector<float> py;
  std::vector<float> pz;
  std::vector<float> polx;
  std::vector<float> poly;
  std::vector<float> polz;
  std::vector<float> t;
  std::vector<float> wavelength;
  std::vector<int> pmtid;

  ClassDef(ChromaPhotonList, 1);
};

#endif

