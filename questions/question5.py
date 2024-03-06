def str_reverse(s):
    return s[::-1]


def str_reverse_2(s):
    result = ''
    for i in range(len(s)-1, -1, -1):
        result += s[i]
    return result


def question5():
    methods = {
        1: str_reverse,
        2: str_reverse_2
    }
    while True:
        text = str(input("Digite qualquer palavra ou texto: "))
        while text == '':
            text = str(input("Digite qualquer palavra ou texto: "))
        if text == '-c':
            return
        method = int(input("Digite 1 para usar o método de slicing ou 2 para usar o método de iteração: "))
        while method not in methods:
            method = int(input("Digite 1 para usar o método de slicing ou 2 para usar o método de iteração: "))
        print(f"Resultado: {methods[method](text)}")
        print("\n\n")


# print(str_reverse('Caio Reis dos Santos de Cresci'))
# print(str_reverse_2('Caio Reis dos Santos de Cresci'))
