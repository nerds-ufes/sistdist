#include <stdlib.h>
#include <stdio.h>
#include <pthread.h>

typedef struct thread_data {
   int number;
   int result;
} thread_data;

void *isPrime(void *arg);

int main(int argc, char **argv) {
    int n=atoi(argv[1]); 
    //printf("n=%d\n", n);

    int i;
    thread_data tdata[n];
    pthread_t threads[n];

    for (i=0; i<n; i++) {
        tdata[i].number=i;
        tdata[i].result=0;
        pthread_create(&(threads[i]), NULL, isPrime, &(tdata[i]));
    }

    for (i=0; i<n; i++) {
        pthread_join(threads[i], NULL);
         if (tdata[i].result==0) {
            printf("%d is not a prime number\n", tdata[i].number);
        } 
        else {
            printf("%d is a prime number\n", tdata[i].number);
        }    
    }
    printf("Fim!\n");
}

void *isPrime(void *arg) {
    thread_data *tdata = (thread_data *) arg;
    int i;

    // 0 and 1 are not prime numbers
    if (((tdata->number)==0)||((tdata->number)==1)) {
       //printf("is_prime(%d)=0\n", *n);
       tdata->result = 0;
    }
    else {
        for (i=2; i<(tdata->number); i++) {
            // if n is divisible by i, then n is not prime
            // change flag to 0 for not prime numbers
            if ((tdata->number)%i==0) {
               //printf("is_prime(%d)=0\n", *n);
               //pthread_exit((void *) 0);
	           tdata->result = 0;
               break;
            }
            tdata->result = 1;
        }
    }

    //printf("is_prime(%d)=1\n", *n);
    pthread_exit(NULL);
}
