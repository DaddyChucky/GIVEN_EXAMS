#include "compte.h"

Compte::Compte(int anneeAvantRetraite,
               int salaireDepart,
               int augmentationSalariale,
               int tauxInteret,
               int anneesDeRetraite,
               int pourcentageSalaireVouluRetraite) : Reer(anneeAvantRetraite, salaireDepart, augmentationSalariale, tauxInteret, anneesDeRetraite, pourcentageSalaireVouluRetraite)
{
}

Compte::~Compte() {}

int Compte::montantAInvestirMaintenant()
{
    return _encaisse - salaireFinal() * pow(1.04, -_anneeAvantRetraite);
}
