#ifndef REER_H
#define REER_H

#include <iostream>
#include <string>
#include <math.h>

class Reer
{
private:
    int _anneesDeRetraite;
    int _salaireDepart;
    int _augmentationSalariale;
    int _salaireVouluRetraite;
    int _tauxInteret;

protected:
    int _anneeAvantRetraite;

public:
    Reer(int anneeAvantRetraite,
         int salaireDepart,
         int augmentationSalariale,
         int tauxInteret,
         int anneesDeRetraite,
         int pourcentageSalaireVouluRetraite);
    int salaireFinal();
    int salaireFinalAsm();
    int montantAmasseFinalAvantRetraite();
    int montantAmasseFinalAvantRetraiteAsm();
    int montantAEpargnerChaqueAnnee();
    int montantAEpargnerChaqueAnneeAsm();
    virtual int montantAInvestirMaintenant();
    virtual int montantAInvestirMaintenantAsm();
    virtual ~Reer() = default;
};

#endif
