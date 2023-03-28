#include <stdlib.h>
#include <stdio.h>

void main(int argc, char **argv) {
    int n=atoi(argv[1]); 
    //printf("n=%d\n", n);

    int i, j, result;
  
    for (i=0; i<n; i++) {
        // 0 and 1 are not prime numbers
        if ((i==0)||(i==1)) {
           //printf("is_prime(%d)=0\n", *n);
           result = 0;
        }
        else {
                result = 1;
                for (j=2; j<i; j++) {
                    // if n is divisible by i, then n is not prime
                    // change flag to 0 for not prime numbers
                    if (i%j==0) {
                       //printf("is_prime(%d)=0\n", *n);
	                   result = 0;
                       break;
                    }
                }
        } 
                
        if (result == 0) {
           printf("%d is not a prime number\n", i);
        } 
        else {
           printf("%d is a prime number\n", i);
        }
    }    
    printf("Fim!\n");
}

