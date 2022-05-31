#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int medianOfThree(int *, int, int);
void swapRefs(int *, int, int);
void printT(int *, int);
void quicksort(int *, int, int);
void quicksort_s(int *, int, int);
void final(int *, int);

const int CUTOFF = 2;
int main()
{
   int T_C[9] = {3, 7, 8, 5, 2, 1, 9, 5, 4};
   int T_S[9] = {3, 7, 8, 5, 2, 1, 9, 5, 4};

   printf("\nTableau initial\n");
   printT(T_C, 9);

   printf("\nQuicksort - C\n");
   quicksort(T_C, 0, 8);
   final(T_C, 9);
   printT(T_C, 9);

   printf("\nQuicksort - ASM\n");
   quicksort_s(T_S, 0, 8);
   final(T_S, 9);
   printT(T_S, 9);

   return 0;
}

void final(int *T_, int size)
{
   for (int i = 0; i < (size - 1); ++i)
   {
      if ((i + 1) <= size && T_[i] > T_[i + 1])
      {
         swapRefs(T_, i, i + 1);
      }
   }
}

void printT(int *T_, int size)
{
   for (int i = 0; i < size; ++i)
   {
      if (i == 0)
      {
         printf("[%d, ", T_[i]);
      }
      else if (i == (size - 1))
      {
         printf("%d]\n", T_[i]);
      }
      else
      {
         printf("%d, ", T_[i]);
      }
   }
}

void quicksort(int *T_, int left, int right)
{
   if (left + CUTOFF > right) // Tableau de plus de 2 elements uniquement a trier
      return;                 // On devrait faire un autre type d'insertion dans ce cas, mais nous simplifions
   const int pivot = medianOfThree(T_, left, right);
   int i = left;      // Extremite gauche
   int k = right - 1; // Extremite droite (non pivot)
   while (1)
   {
      while (T_[++i] < pivot)
         ;
      while (T_[--k] > pivot)
         ;
      if (i < k)
         swapRefs(T_, i, k); // On permute T[i] avec T[k]
      else
         break; // Sortir car partitionnement termine
   }
   swapRefs(T_, i, right - 1);  // Permuter T[i] et pivot
   quicksort(T_, left, i - 1);  // Trier les elements sous le pivot
   quicksort(T_, i + 1, right); // Trier les elements en haut du pivot
}

void swapRefs(int *T_, int left, int right)
{
   int middleMan = T_[left];
   T_[left] = T_[right];
   T_[right] = middleMan;
}

int medianOfThree(int *T_, int left, int right)
{
   const int center = (left + right) / 2;
   if (T_[center] < T_[left])
      swapRefs(T_, left, center);
   if (T_[right] < T_[left])
      swapRefs(T_, left, right);
   if (T_[right] < T_[center])
      swapRefs(T_, center, right);
   swapRefs(T_, center, right - 1); // Nous placons le pivot a la pos. right - 1
   return T_[right - 1];
}
