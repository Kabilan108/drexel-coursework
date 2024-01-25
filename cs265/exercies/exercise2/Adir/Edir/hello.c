/* hello.c - sample C program
 *
 * Waldo is hiding in a C program
 *
 */

#include <stdio.h>
#include <stdlib.h>

int main()
{
	char *n = getenv( "USER" ) ;

	fprintf( stdout, "\nHello, %s!\n\n", n ) ;

	return 0 ;
}
