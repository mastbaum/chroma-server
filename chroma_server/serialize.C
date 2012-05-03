#include <TBufferFile.h>
#include <stdlib.h>

// Copy the serialized buffer from a TBufferFile into char* msg, which is
// really a Python string. If we return a char*, PyROOT casts it to a str
// and cuts it off at the first null character.

void Serialize(TBufferFile* buf, char* msg) {
  memcpy(msg, buf->Buffer(), buf->Length());
}

