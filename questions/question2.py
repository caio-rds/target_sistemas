def fibonacci(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[i-1] + fib[i-2])
        return fib


def question2():
    while True:
        number = None
        while number is None:
            try:
                number = int(input("Digite um número para saber se está na seq. de fibonacci (-1 para cancelar): "))
            except ValueError:
                print("Digite um número válido!")
        if number == -1:
            return
        sequence = fibonacci(number)
        if number in sequence:
            print(f"{number} está na sequência de Fibonacci!")
        else:
            print(f"{number} não está na sequência de Fibonacci!")
