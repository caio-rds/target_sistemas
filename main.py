from questions.question1 import question1
from questions.question2 import question2
from questions.question3 import question3
from questions.question4 import question4
from questions.question5 import question5


def main():
    questions = {
        1: {'func': question1, 'desc': 'Soma dos números de 1 a 13'},
        2: {'func': question2, 'desc': 'Verifica se o número está na Sequência de Fibonacci'},
        3: {'func': question3, 'desc': 'Lógica e complemento do próximo número'},
        4: {'func': question4, 'desc': 'Descobrir qual interruptor controla cada lâmpada'},
        5: {'func': question5, 'desc': 'Inverter uma string'}
    }
    while True:
        for k, v in questions.items():
            print(f"{k} - {v['desc']}")
        question = int(input(f"Digite o número da questão que você deseja resolver ou 0 para sair: "))
        try:
            if question == 0:
                break
        except ValueError:
            pass
        while question not in questions:
            question = int(input(f"Digite o número da questão ({questions.keys()}) que você deseja resolver ou 0 para sair: "))
        questions[question]['func']()


if __name__ == '__main__':
    main()
