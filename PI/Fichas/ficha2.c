#include <stdio.h>
/**1. Apresente uma definição da função float multInt1 (int n, float m) baseada nesta observação:
 * a uma variavel r(iniciada com valor 0) será somado o valor de m, n vezes. 
 **/

float multInt1 (int n, float m){
	float r = 0;
	for(int i=0;i<n;i++) r +=m ;
	return r;
}

/**
 * Dados dois números m e n odemos construir uma tabela em que vamos
 * dividindo n por 2 e multiplicando m por 2. A primeira linha da
 * tabela tem o valor original de n enquanto que a última corresponde
 * a n ser 1.
 * Para obter o valor do produto de n por m basta somar os valores de m
 * correspondentes às linhas em que n é ímpar. 
 * 
 * **/

float multInt2 (int n, float m){
	float r = 0;
	for(;n>1;n/=2){
		if (n % 2 != 0)r +=m;
			m*=2;
	return r + m;
	}
	}

int fib1 (int n){
	if(n<2) return 1;
	else return fib1(n-1) + fib1(n-2);
}


//main function
int main(){
	int a;
	float f1,f2,f;
	int n;
	printf("Introduza um número para a sequencia de fibonacci: ");
	scanf("%d",&n);
	printf("Introduza dois números: ");
	scanf("%d", &a);scanf("%f",&f);
	f1 = multInt1(a,f);
	f2 = multInt2(a,f);
	int res = fib1(n);
	printf("O resultado de multInt1 é: %f\n",f1);
	printf("O resultado de multInt2 é: %f\n",f2);
	printf("O resultado da sequencia de fibonacci é: %d\n", res);	
	return 0;
}
