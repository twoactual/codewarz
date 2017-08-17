#include "stdio.h"

unsigned long ElfHash (const unsigned char *name)
{
	unsigned long h =0, g;
	while (*name)
	{
		h = ( h << 4) + *name++;
		if (g = h & 0xF0000000)
			h ^= g >> 24;
		h &= ~g;
	}
	return h;
}

int main(int argc, char *argv[])
{
	if (argc == 2)
	{
		const unsigned char *args = argv[1];
		unsigned long answer = ElfHash(args);
		printf("elfhash = %lu\n",answer);
		return 0;
	}
	else
	{
		printf("Need an argument to hash\n");
	}
}
