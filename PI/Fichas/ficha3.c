/*2. Defina uma funcao void swapM (int *x, int *y) que
troca o valor de duas variaveis. Por exemplo, o codigo ao
lado devera imprimir no ecran 5 3.*/

void swapM (int *x, int *y){
    int temp = *x;
    *x = *y;
    *y = temp;
}

/**3. Defina uma funcao void swap (int v[], int i, int j) que troca o valor das posicoes i e
j do vector v.*/

void swap(int v[], int i, int j){
    int temp = v[i];
    v[i] = v[j];
    v[j] = v[i];
}

/**
 * 4. Defina uma funcao int soma (int v[], int N) que calcula a soma dos elementos de um vector v com N inteiros 
 */

int soma (int v[], int N){
    int res = 0;
    for(int i = 0; i < N; i++) res +=v[i];
    return res;
}

/*4. 5. Defina uma funcao void inverteArray (int v[], int N) que inverte um array. Escreva duas
versoes, cada uma usando uma das funcoes das alıneas anteriores*/

