#include "reer.h"
#include "compte.h"

int main()
{
    Reer reer{32, 79520, 4, 8, 16, 64}; // (c) CDL, adapte de Moulay Huard, 2022.

    std::cout << "==============" << std::endl;
    std::cout << "Salaire final" << std::endl;
    std::cout << "==============" << std::endl;
    int salaireFinalC = reer.salaireFinal();
    int salaireFinalAsm = reer.salaireFinalAsm();
    if (salaireFinalC == salaireFinalAsm)
    {
        std::cout << "Salaires finaux ASM-C egaux! OK!" << std::endl;
    }
    else
    {
        std::cout << "Salaires finaux ASM-C INVALIDES!" << std::endl;
        std::cout << "Salaire ASM obtenu: " << salaireFinalAsm << "\nSalaire final C attendu: " << salaireFinalC << std::endl;
    }

    std::cout << "====================================" << std::endl;
    std::cout << "Montant amasse final avant retraite" << std::endl;
    std::cout << "====================================" << std::endl;
    int montantAmasseFinalAvantRetraite = reer.montantAmasseFinalAvantRetraite();
    int montantAmasseFinalAvantRetraiteAsm = reer.montantAmasseFinalAvantRetraiteAsm();
    if (montantAmasseFinalAvantRetraite == montantAmasseFinalAvantRetraiteAsm)
    {
        std::cout << "Montants amasses finaux avant retraite ASM-C egaux! OK!" << std::endl;
    }
    else
    {
        std::cout << "Montants amasses finaux avant retraite ASM-C INVALIDES!" << std::endl;
        std::cout << "Montant amasse ASM obtenu: " << montantAmasseFinalAvantRetraiteAsm << "\nMontant amasse final C attendu: " << montantAmasseFinalAvantRetraite << std::endl;
    }

    std::cout << "==================================" << std::endl;
    std::cout << "Montant a epargner a chaque annee" << std::endl;
    std::cout << "==================================" << std::endl;
    int montantAEpargnerChaqueAnnee = reer.montantAEpargnerChaqueAnnee();
    int montantAEpargnerChaqueAnneeAsm = reer.montantAEpargnerChaqueAnneeAsm();
    if (montantAEpargnerChaqueAnnee == montantAEpargnerChaqueAnneeAsm)
    {
        std::cout << "Montants a epargner a chaque annee ASM-C egaux! OK!" << std::endl;
    }
    else
    {
        std::cout << "Montants a epargner a chaque annee ASM-C INVALIDES!" << std::endl;
        std::cout << "Montant a epargner ASM obtenu: " << montantAEpargnerChaqueAnneeAsm << "\nMontant a epargner C attendu: " << montantAEpargnerChaqueAnnee << std::endl;
    }

    std::cout << "==================================" << std::endl;
    std::cout << "Montant a investir aujourd'hui" << std::endl;
    std::cout << "==================================" << std::endl;
    int montantAInvestirAujourdhui = reer.montantAInvestirMaintenant();
    int montantAInvestirAujourdhuiAsm = reer.montantAInvestirMaintenantAsm();
    if (montantAInvestirAujourdhui == montantAInvestirAujourdhuiAsm)
    {
        std::cout << "Montants a investir aujourd'hui ASM-C egaux! OK!" << std::endl;
    }
    else
    {
        std::cout << "Montants a investir aujourd'hui ASM-C INVALIDES!" << std::endl;
        std::cout << "Montant a investir ASM obtenu: " << montantAInvestirAujourdhuiAsm << "\nMontant a investir C attendu: " << montantAInvestirAujourdhui << std::endl;
    }

    std::cout << "==================================" << std::endl;
    std::cout << "Compte a haut risque" << std::endl;
    std::cout << "==================================" << std::endl;
    Compte compteHautRisque{32, 79520, 4, 8, 16, 64};
    int encaisseFinale = compteHautRisque.montantAInvestirMaintenant();
    int encaisseFinaleAsm = compteHautRisque.montantAInvestirMaintenantAsm();
    if (encaisseFinale == encaisseFinaleAsm)
    {
        std::cout << "Encaisses ASM-C egaux! OK!" << std::endl;
    }
    else
    {
        std::cout << "Encaisses ASM-C INVALIDES!" << std::endl;
        std::cout << "Encaisse ASM obtenue: " << encaisseFinaleAsm << "\nEncaisse C attendue: " << encaisseFinale << std::endl;
    }
}
