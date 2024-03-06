sequences = {
    'A': {'seq': [1, 3, 5, 7], 'next_num': 9, 'logic': 'Progressão Aritmética (+2)'},
    'B': {'seq': [2, 4, 8, 16, 32, 64], 'next_num': 128, 'logic': 'Multiplicação por 2'},
    'C': {'seq': [0, 1, 4, 9, 16, 25, 36], 'next_num': 49, 'logic': 'Quadrado do Índice'},
    'D': {'seq': [4, 16, 36, 64], 'next_num': 100, 'logic': 'Quadrado do Índice começando por 2²'},
    'E': {'seq': [1, 1, 2, 3, 5, 8], 'next_num': 13, 'logic': 'Sequencia de Fibonacci'},
    'F': {'seq': [2, 10, 12, 16, 17, 18, 19], 'next_num': 22, 'logic': 'Progressão Aritmética (+8 Par, -3 Ímpar)'}
}


def question3():
    result = {}
    for k, v in sequences.items():
        print(f"Sequência {k}: {v['seq']} - Próximo Número: {[v['next_num']]} Lógica: {v['logic']}")
        result[k] = v['seq'] + [v['next_num']]
    print("\n\n")
    print("Resultado")
    for k, v in result.items():
        print(f"Sequência {k}: {v}")
    print("\n\n")

# What is the output of the code above?
# a) [1, 3, 5, 7, 9]
# b) [2, 4, 8, 16, 32, 64, 128]
# c) [0, 1, 4, 9, 16, 25, 36, 49]
# d) [4, 16, 36, 64, 100]
# e) [1, 1, 2, 3, 5, 8, 13]
# f) [2, 10, 12, 16, 17, 18, 19, 22]
