#ifndef COMPTE_H
#define COMPTE_H

#include "reer.h"
#include <math.h>

class Compte : public Reer
{
private:
    int _encaisse = 50000;

public:
    Compte(int, int, int, int, int, int);
    virtual ~Compte();
    virtual int montantAInvestirMaintenant() override;
    virtual int montantAInvestirMaintenantAsm() override;
};

#endif
