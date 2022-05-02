from typing import List


def _1(num: int) -> int:
    """
    Modele e implemente um método recursivo que calcule o fatorial de um número n passado como parâmetro.
    """
    if num < 0:
        print("N/A")
        return 1
    if num == 0:
        return 1
    if num == 1:
        return num
    return num * _1(num - 1)


def _2(num: int):
    """
    Modele e implemente um método recursivo que calcule o somatório de um número n (passado como parâmetro) até 0.
    """
    if num == 0:
        return num
    return num + _2(num - 1)


def _3(pos: int):
    """
    Modele e implemente um método recursivo que calcule o n-ésimo número da sequência de fibonacci.
    """
    if pos <= 0:
        print("panic")
        return 0
    if pos == 1 or pos == 2:
        return 1
    return _3(pos - 1) + _3(pos - 2)


def _4(maior, menor):
    """
    Modele e implemente um método recursivo que calcule o somatório dos números inteiros entre os números k e j, passados como parâmetro.
    """
    if maior < menor:
        raise Exception("error")
    if menor == maior - 1:
        return 0
    return _4(menor, maior - 1) + (maior - 1)


def _5(s):
    """
    Modele e implemente um método recursivo que recebe um String em retorna true se este String for um palíndrome, false caso contrário.
    """
    if len(s) == 0:
        raise Exception("error")
    if s[0] != s[len(s) - 1]:
        return False
    elif len(s) == 1:
        return True
    return _5(s[1:len(s) - 1]) and True


def _6(n: int) -> str:
    """
    Modele e implemente um método recursivo que recebe um inteiro zero ou positivo e retorna
    um String com o número em binário
    """
    if n == 0:
        return '0'
    if n < 0:
        return ''
    return f'{_6(n >> 1)}{str(bin(n & 0b1))[2:]}'


def _7(lst: List[int]) -> int:
    """
    Modele e implemente um método recursivo que calcule osomatório dos números contidos em um ArrayList deinteiros, passado como parâmetro.
    """
    if len(lst) <= 0:
        print('errorrrr')
        return 0
    if len(lst) == 1:
        return lst[0]
    n = lst[0]
    lst = lst[1:]
    return n + _7(lst)


def _8(lst: List[int]):
    """
    Modele e implemente um método recursivo para encontrar o maior elemento de um ArrayList.
    """
    if len(lst) <= 0:
        print('eeeeeeeeeeeeeeeeeeeeeeerr')
        return 0
    if len(lst) == 1:
        return lst[0]
    n = lst[0]
    m = _8(lst[1:])
    return n if n >= m else m
