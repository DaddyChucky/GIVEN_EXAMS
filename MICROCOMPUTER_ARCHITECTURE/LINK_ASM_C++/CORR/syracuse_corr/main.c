#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int syracuse_s_iter(unsigned int);
int syracuse_s_rec(unsigned int, unsigned int);

void syracuse_c_iter(unsigned int);
void syracuse_c_rec(unsigned int, unsigned int);

void afficher(int, int);

int main()
{
   unsigned int u0 = 15;

   printf("\n\nSuite de syracuse iterative - C\n");
   syracuse_c_iter(u0);

   printf("Suite de syracuse iterative - ASM\n");
   syracuse_s_iter(u0);

   // Decommentez cette partie lorsque vous avez implemente la version recursive
   printf("\n\nSuite de syracuse recursive - ASM\n");
   syracuse_s_rec(u0, 0);

   printf("\n\nSuite de syracuse recursive - C\n");
   syracuse_c_rec(u0, 0);

   return 0;
}

void syracuse_c_iter(unsigned int u0)
{
   unsigned int i = 0;
   while (u0 != 1)
   {
      printf("Syracuse(%d) = %d\n", i, u0);
      if (u0 % 2 == 0)
      {
         u0 /= 2;
      }
      else
      {
         u0 = u0 * 3 + 1;
      }
      i += 1;
   }
   printf("Syracuse(%d) = %d\n", i, u0);
}

void syracuse_c_rec(unsigned int un, unsigned int i)
{
   printf("Syracuse(%d) = %d\n", i, un);
   if (un % 2 == 0)
   {
      syracuse_c_rec(un / 2, i + 1);
   }
   else if (un == 1)
   {
      return;
   }
   else
   {
      syracuse_c_rec(un * 3 + 1, i + 1);
   }
}

void afficher(int un, int i)
{
   printf("Syracuse(%d) = %d\n", un, i);
}
