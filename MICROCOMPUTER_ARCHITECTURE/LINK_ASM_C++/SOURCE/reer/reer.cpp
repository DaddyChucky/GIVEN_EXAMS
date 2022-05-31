#include "reer.h"

Reer::Reer(int anneeAvantRetraite,
           int salaireDepart,
           int augmentationSalariale,
           int tauxInteret,
           int anneesDeRetraite,
           int pourcentageSalaireVouluRetraite)
{
    _anneeAvantRetraite = anneeAvantRetraite;
    _salaireDepart = salaireDepart;
    _augmentationSalariale = augmentationSalariale;
    _tauxInteret = tauxInteret;
    _anneesDeRetraite = anneesDeRetraite;
    _salaireVouluRetraite = pourcentageSalaireVouluRetraite;
}

int Reer::salaireFinal()
{
    return _salaireDepart * pow((1 + double(_augmentationSalariale) / 100), _anneeAvantRetraite - 1);
}

int Reer::montantAmasseFinalAvantRetraite()
{
    int salaireRetraite = salaireFinal() * double(_salaireVouluRetraite) / 100;
    return salaireRetraite * (pow(1 + double(_tauxInteret) / 100, _anneesDeRetraite) - 1) / (double(_tauxInteret) / 100 * (pow(1 + double(_tauxInteret) / 100, _anneesDeRetraite)));
}

int Reer::montantAEpargnerChaqueAnnee()
{
    return montantAmasseFinalAvantRetraite() * (double(_tauxInteret) / 100) / (pow(1 + double(_tauxInteret) / 100, _anneeAvantRetraite) - 1);
}

int Reer::montantAInvestirMaintenant()
{
    return montantAmasseFinalAvantRetraite() * pow(1 + double(_tauxInteret) / 100, -_anneeAvantRetraite);
}
