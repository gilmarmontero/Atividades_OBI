
def pisos_escola(L, C ):
    largura = L*C + (L-1)*(C-1)
    comprimento = 2*(L-1) + 2*(C-1)

    print(largura)
    print(comprimento)

    return [largura, comprimento]