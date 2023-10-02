#include <sys/types.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - while
 *
 * Return: int
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
 * main - main function
 *
 * Return: int
 */
int main(void)
{
	pid_t pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid > 0) /*parent process*/
			printf("Zombie process created, PID: %d\n", pid);
		else
			exit(0); /*child process or error*/
		/*child process exits without the parent taking its status*/
	}
	infinite_while();

	return (0);
}
