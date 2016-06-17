/*
	2016/06/17	Huiqun.Lin
	gcc -pthread thread.c
*/
#define _XOPEN_SOURCE 600

#include <stdlib.h>
#include <stdio.h>
#include <errno.h>
#include <semaphore.h>
#include <pthread.h>


static pthread_barrier_t    barrier;
static pthread_rwlock_t     rwlk;
static sem_t                sem1;


void *writer(void *dummy)
{
    int                 error;

    pthread_barrier_wait(&barrier);

    error = pthread_rwlock_wrlock(&rwlk);
    if (error !=  0) {
        fprintf(stderr, "Thread (%lu) wrlock failed: %d\n", (unsigned long)pthread_self(), error);
        sem_post(&sem1);
        pthread_barrier_wait(&barrier);
        return (void *) NULL;
    }

    printf("Thread (%lu) acquired a writre-lock.\n", (unsigned long)pthread_self());

    sem_post(&sem1);
    pthread_barrier_wait(&barrier);

    return (void *) NULL;
}


void *other(void *dummy)
{

    int                 error;

    pthread_barrier_wait(&barrier);

    sem_wait(&sem1);
    printf("Thread (%lu) was waken up to unlock the writre-lock.\n", (unsigned long)pthread_self());

    error = pthread_rwlock_unlock(&rwlk);
    if (error != 0) {
        fprintf(stderr, "pthread_rwlock_unlock() failed: %s\n",
                            error == EPERM? "EPERM": "OTHER ERROR");

        pthread_barrier_wait(&barrier);
        return (void *) NULL;
    }

    printf("Thread (%lu) release the lock.\n", (unsigned long)pthread_self());

    error = pthread_rwlock_wrlock(&rwlk);
    if (error !=  0) {
        fprintf(stderr, "Thread (%lu) wrlock failed: %d\n", (unsigned long)pthread_self(), error);
        pthread_barrier_wait(&barrier);
        return (void *) NULL;
    }

    printf("Thread (%lu) acquired the writre-lock.\n", (unsigned long)pthread_self());
    pthread_barrier_wait(&barrier);

    return (void *) NULL;
}



int main (void)
{

    int                         rtn;
    pthread_t                   thw, tho;

    /* init semaphore */
    rtn = sem_init(&sem1, 0, 0);
    if (rtn != 0) {
        perror("sem_init");
        exit(EXIT_FAILURE);
    }

    /* init rwlock */
    rtn = pthread_rwlock_init(&rwlk, NULL);
    if (rtn != 0) {
        fprintf(stderr, "pthread_rwlock_init() failed for %d.\n", rtn);
        exit(EXIT_FAILURE);
    }

    /* init barrier */
    rtn = pthread_barrier_init(&barrier, NULL, 2);
    if (rtn != 0) {
        fprintf(stderr, "pthread_barrier_init() failed for %d.\n", rtn);
        exit(EXIT_FAILURE);
    }

    /* create thread */
    rtn = pthread_create(&thw, NULL, writer, (void *)NULL);
    if (rtn != 0) {
        fprintf(stderr, "pthread_create() - writer failed for %d.\n", rtn);
        exit(EXIT_FAILURE);
    }

    rtn = pthread_create(&tho, NULL, other, (void *)NULL);
    if (rtn != 0) {
        fprintf(stderr, "pthread_create() - other failed for %d.\n", rtn);
        exit(EXIT_FAILURE);
    }

    /* join */
    pthread_join(thw, NULL);
    pthread_join(tho, NULL);

    /* destroy resources */
    pthread_barrier_destroy(&barrier);
    pthread_rwlock_destroy(&rwlk);
    sem_destroy(&sem1);

    exit(EXIT_SUCCESS);

}
