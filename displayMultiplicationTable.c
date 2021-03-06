/* Program print a multiplication table to allow you practice using 
   dynamic allocation of arrays using malloc.
   Compile by:  gcc -o table displayMultiplicationTable.c
   Run by:  ./table
*/
#include <stdio.h>
#include <stdlib.h>

// function prototypes
void getValues( /* ADD CODE HERE */ );
void calculateRowProducts( /* ADD CODE HERE */ );
void printTableHeading(int value1, int value2);
void printRow(int row, int maxColumn, int * rowProducts);

int main() {
  int * rowProducts;
  int value1, value2, row, column;

  // gets value1 and value2 from the user
  getValues( /* ADD CODE HERE */ );

  // dynamically allocate array to hold a row of products
  rowProducts =  /* ADD CODE HERE */ 

  printTableHeading(value1,  value2);

  for (row = 1; row <= value1; row++) {
    calculateRowProducts( /* ADD CODE HERE */ );
    printRow(row, value2, rowProducts);
  } // end for (row...

  free(rowProducts);  // deallocates array

} // end main


/*******************************************************************
 * Function getValues asks the user to enter value1 and value2, i.e.,
 * the max. row and max. column values of the multiplication tables.
 * It returns both of the value1 and value2 values.
 ********************************************************************/
void getValues( /* ADD CODE HERE */ ) {

  printf("\nThis program prints a multiplication table.\n\n");
  printf("Enter two integer values for the max. row and column of the table: ");
  scanf( /* ADD CODE HERE */ );

} // end getValues


/*******************************************************************
 * Function calculateRowProducts is passed a row value, the value2,
 * and returns an array of products from (row x 1) to (row x value2)
 ********************************************************************/
void calculateRowProducts( /* ADD CODE HERE */ ) {
  int column;


  /* ADD CODE HERE -- CALCULATES THE SPECIFIED ROW PRODUCTS */
 
} // end calculateRowProducts

/*******************************************************************
 * Function printTableHeading is passed the value1 and value2 values
 * and prints the multiplication table header.
 ********************************************************************/
void printTableHeading(int value1, int value2) {
  int column;

  printf("\nThe multiplication table from 1 x 1 up to %d x %d\n\n",value1, value2);

  printf("  X  |");
  for (column = 1; column <= value2; column++) {
    printf("%5d", column);
  } // end for (column...
  printf("\n");

  printf("-----|");
  for (column = 1; column <= value2; column++) {
    printf("-----");
  } // end for (column...
  printf("\n");

} // end printTableHeading

/*******************************************************************
 * Function printRow is passed a row value, the value2 (i.e., max. column
 * value), and corresponding rowProducts array which is printed.
 ********************************************************************/
void printRow(int row, int maxColumn, int * rowProducts) {
  int column;
  
  printf("%-5d|", row);
  for (column = 0; column < maxColumn; column++) {
    printf("%5d", rowProducts[column]);
  } // end for (column...
  printf("\n");
} // end printRow
