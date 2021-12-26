sesli_harf ="aeıioöuü"
listelenmis_arguman = []
def arguman_fonk():
    arguman = input("Kelime Giriniz: ")
    return arguman
def degisim_fonk(arguman):
    for i in arguman:
        listelenmis_arguman.append(i)
        for x in listelenmis_arguman:
            if x in sesli_harf:
                listelenmis_arguman.remove(x)
                listelenmis_arguman.append("*")
    yeni_kelime = ("".join(listelenmis_arguman))
    print(yeni_kelime)
degisim_fonk(arguman_fonk())
