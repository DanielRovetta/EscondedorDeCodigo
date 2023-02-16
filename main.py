import numpy as np
import matplotlib.pyplot as plt
import math


def d2b(decimal):
    binary = ''
    while decimal != 0:
        binary = binary + str(decimal % 2)
        decimal = int(decimal / 2)
    return binary[::-1]


def b2d(binary):
    binary = int(binary)
    decimal, i, n = 0, 0, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal


def codificarArquivo(nome):

    arquivo = open(nome, 'r')
    string = arquivo.read()

    num = len(string) / 3
    raiz = math.sqrt(round(num))

    if float.is_integer(raiz):
        raiz = (round(raiz))
    else:
        raiz = (round((raiz + 1) - 0.5))

    R = np.zeros([raiz, raiz])
    G = np.zeros([raiz, raiz])
    B = np.zeros([raiz, raiz])

    cont = 0
    for Y in range(raiz):
        for X in range(raiz):
            if cont < len(string):
                R[Y][X] = str(ord(string[cont]))
            else:
                R[Y][X] = 255
            if (cont + 1) < len(string):
                G[Y][X] = str(ord(string[cont + 1]))
            else:
                G[Y][X] = 255
            if (cont + 2) < len(string):
                B[Y][X] = str(ord(string[cont + 2]))
            else:
                B[Y][X] = 255
            cont = cont + 3

    M = np.zeros((raiz, raiz, 3),  dtype=np.int_)

    M[:, :, 0] = R
    M[:, :, 1] = G
    M[:, :, 2] = B

    plt.figure(figsize=(raiz, raiz))
    im = plt.imshow(M, aspect='auto')
    plt.axis("off")

    plt.savefig(nome.replace('.', '-'), bbox_inches="tight", transparent=True)


codificarArquivo('main.py')
