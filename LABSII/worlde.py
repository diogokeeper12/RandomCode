"""

Implemente uma função que dada uma palavra secreta e uma palavra tentativa
devolva uma lista com os caracteres da palavra tentativa que aparecem na
palavra secreta.
Mais concretamente, para cada caracter que apareça na palavra tentativa
deve também ser indicada a respectiva posição e um booleano que indica se
aparece na mesma posição na palavra secreta ou numa posição diferente.

"""

def wordle(secreta,tentativa):
    idx = 0
    res = []
    if len(tentativa) <= len(secreta):
        for letter in tentativa:
            if secreta.count(letter) > 0:
                if secreta[idx] == letter:
                    res.append((letter,idx,True))
                else:
                    res.append((letter,idx,False))
            idx+=1
    else:
        aux_tentativa = tentativa[:-(len(tentativa)-len(secreta)-1)]
        print(aux_tentativa)
        for letter in aux_tentativa:
            if secreta.count(letter) > 0:
                if secreta[idx] == letter:
                    res.append((letter,idx,True))
                else:
                    res.append((letter,idx,False))
            idx+=1
    return res

print(wordle("tentativa","secreta"))
print()
    


"""
wordle("programa","logica"),[('o',1,False),('g',2,False),('a',5,True)])
"""

"""("programa","logica"),[('o',1,False),('g',2,False),('a',5,True)"""