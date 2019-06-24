#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
/**
 * infinite_while - function to create an infinite loop
 *
 * Return: Always 0 if success
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Entry point
 *
 *
 * Return: Always 0 if success
 */

int main(void)
{
	pid_t pichild;
	int i;

	for (i = 0; i < 5; i++)
	{
		pichild = fork();
		if (pichild > 0)
			sleep(1);
		else
			return (0);
		printf("Zombie process created, PID: %d\n", pichild);
	}
	infinite_while();
	return (0);
}
