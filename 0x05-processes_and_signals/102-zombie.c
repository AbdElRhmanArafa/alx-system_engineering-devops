#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - a function that runs forever
 * Return: 0  
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
 * main - that creates 5 zombie process
 * Return: 0  
 */
int main(void)
{
    int children = 0;
    pid_t pid;

    while (children < 5)
    {
        pid = fork();
        if (!pid)
            break;
        printf("Zombie process created, PID: %i\n", (int)pid);
        children++;
    }
    if (pid != 0)
    {
        infinite_while();
    }
    return (0);
}
