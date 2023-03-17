#include <stdio.h>

/**1. Defina um programa que lê (usando a funçao scanf uma sequencia de numeros 
 * inteiros terminada com o numero 0 e imprime no ecran o maior elemento da sequencia.*/

int le(){
    int p;
    scanf("%d",&p);
    int max = p;
    while(p!=0){
        scanf("%d",&p);
        if(max<p)
            max = p;
    }
    printf("%d", max);
    return max;
}
<




