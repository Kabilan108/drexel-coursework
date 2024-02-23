#include <stdio.h>

int main(int argc, char* argv[]) {
	int MAX_SIZE = 100;

	// only read in a string with at most 100 characters
	char s[MAX_SIZE];
	char* p = s;
	int n = 0;
	char c;

	while (1) {
		// check if user has typed too many characters
		// -1 for \0
		if (n > MAX_SIZE) break;

		// getc reads on character from stdin
		c = getc(stdin);

		//getc returns -1 with EOF
		if (c == -1) break;
		// only read one line
		if (c == '\n')break;

		// store char in s
		*p = c;
		n++;
		p++;
	}

	*p = '\0';
	printf("You typed: '%s'\n", s);
}
