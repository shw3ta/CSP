#include<gmp.h>
#include<stdio.h>

int main(){

	mpz_t t;
	mpz_init(t);
	gmp_scanf("%Zd", t);

	printf("%Zd\n",t);
}